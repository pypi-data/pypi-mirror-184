from typing import Type, Optional, Set, Union, Dict
from pathlib import Path
from openapi_schema_pydantic import (OpenAPI, Operation, PathItem, MediaType, RequestBody, Response, Parameter, Schema,
                                     Components, SecurityScheme)
from openapi_schema_pydantic.util import PydanticSchema, construct_open_api_with_schema_class, PydanticType
from pydantic.schema import field_schema
from pydantic.fields import ModelField
from pydantic import Field
from chalice import IAMAuthorizer, CognitoUserPoolAuthorizer
from .route import Route


class IAMSecurityScheme(SecurityScheme):
    x_amazon_apigateway_authtype: str = Field(alias="x-amazon-apigateway-authtype")


class OpenAPISchema(OpenAPI):
    _auth_scheme_ids: Set[int] = set()
    _oath_security_schemes: Optional[Dict[str, SecurityScheme]] = {}

    def register_oath_security_scheme(self, name: str, scheme: Union[SecurityScheme, dict]):
        if isinstance(scheme, SecurityScheme):
            self._oath_security_schemes[name] = scheme
        else:
            self._oath_security_schemes[name] = SecurityScheme.parse_obj(scheme)

    @staticmethod
    def _to_field_schema(model_field: ModelField, **kwargs) -> Schema:
        schema = field_schema(model_field, model_name_map={}, **kwargs)[0]
        return Schema.parse_obj(schema)

    def register_veneer_route(self, route: Type[Route],
                              authorizer: Optional[Union[IAMAuthorizer, CognitoUserPoolAuthorizer]] = None):
        op = Operation()

        authorizer = authorizer or route.Config.authorizer
        if authorizer:
            if not self.components:
                self.components = Components()
            if not self.components.securitySchemes:
                self.components.securitySchemes = {}
            authorizer_id = id(authorizer)
            if isinstance(authorizer, IAMAuthorizer):
                # Only allow 1 instance of IAM auth in components
                if authorizer_id not in self._auth_scheme_ids and "sigv4" not in self.components.securitySchemes:
                    self.components.securitySchemes["sigv4"] = IAMSecurityScheme(
                        type="apiKey",
                        name="Authorization",
                        security_scheme_in="header",
                        x_amazon_apigateway_authtype="awsSigv4",
                        description="AWS IAM STS Session Token"
                    )
                    self._auth_scheme_ids.add(authorizer_id)
                op.security = [{"sigv4": []}]
            elif isinstance(authorizer, CognitoUserPoolAuthorizer):
                if authorizer_id not in self._auth_scheme_ids:
                    if scheme := self._oath_security_schemes.get(authorizer.name):
                        self.components.securitySchemes[str(authorizer_id) + "z"] = scheme
                    else:
                        self.components.securitySchemes[str(authorizer_id) + "z"] = SecurityScheme(
                            type="oauth2",
                            description=authorizer.name,
                        )
                op.security = [{str(authorizer_id) + "z": authorizer.scopes}]

        if route.Config.open_api_tags:
            op.tags = route.Config.open_api_tags

        if route.Config.open_api_summary:
            op.summary = route.Config.open_api_summary

        if route.request.__doc__:
            op.description = route.request.__doc__

        if any((route.PathModel.__fields__, route.QueryModel.__fields__)):
            op.parameters = []
            for k, v in route.PathModel.__fields__.items():
                op.parameters.append(
                    Parameter(
                        name=k,
                        param_in="path",
                        required=v.required,
                        param_schema=self._to_field_schema(v)
                    )
                )
            for k, v in route.QueryModel.__fields__.items():
                op.parameters.append(
                    Parameter(
                        name=k,
                        param_in="query",
                        required=v.required,
                        param_schema=self._to_field_schema(v)
                    )
                )

        if route.BodyModel.__fields__:
            # Below is a work-around to rename the generated component schemas
            model_copy: Type[PydanticType] = type(f"{route.__name__}BodyModel", (route.BodyModel,), {})
            media_schema = MediaType(
                media_type_schema=PydanticSchema(
                    schema_class=model_copy
                )
            )
            if route.Config.open_api_body_example:
                media_schema.example = route.Config.open_api_body_example
            required = any((x.required for x in model_copy.__fields__.values()))
            op.requestBody = RequestBody(
                content={"application/json": media_schema},
                required=required,
                description=model_copy.__doc__ or "",
            )

        op.responses = {}
        if route.ResponseModel.__fields__:
            model_copy: Type[PydanticType] = type(f"{route.__name__}ResponseModel", (route.ResponseModel,), {})
            op.responses[str(route.Config.default_status_code)] = Response(
                content={
                    route.Config.response_content_type: MediaType(
                        media_type_schema=PydanticSchema(
                            schema_class=model_copy
                        )
                    )
                },
                description=model_copy.__doc__ or "",
            )
        route_methods = route.Config.methods
        path_item = PathItem()
        for method in route_methods:
            setattr(path_item, method.lower(), op)

        if not self.paths:
            self.paths = {}
        if route.Config.path not in self.paths:
            self.paths[route.Config.path] = path_item
        else:
            for set_method, value in path_item:
                if value:
                    setattr(self.paths[route.Config.path], set_method, value)

    def to_open_api_file(self, path: Path, **kwargs):
        path.write_text(
            construct_open_api_with_schema_class(self).json(
                by_alias=True,
                exclude_none=True,
                **kwargs
            )
        )

    def get_doc_html(
            self,
            *,
            openapi_url: str,
            allow_server_selection: Optional[bool] = False,
            logo_url: Optional[str] = None
    ):
        nav = "" if not logo_url else f"""<img
    slot="nav-logo"
    src="{logo_url}"
  />"""
        html = f"""<!doctype html> <!-- Important: must specify -->
<html>
<head>
  <meta charset="utf-8"> <!-- Important: rapi-doc uses utf8 characters -->
  <script type="module" src="https://unpkg.com/rapidoc/dist/rapidoc-min.js"></script>
  <link href="https://fonts.googleapis.com/css?family=Nunito" rel="stylesheet">
  <title>{self.info.title} - {self.info.version}</title>
</head>
<body>
  <rapi-doc
    spec-url={openapi_url}
    theme = "dark"
    regular-font = "Nunito"
    font-size = "large"
    allow-spec-url-load = false
    allow-spec-file-load = false
    allow-spec-file-download = true
    default-schema-tab = "schema"
    allow-server-selection = {str(allow_server_selection).lower()}
    render-style = "view"
    x-tag-expanded = true
    show-info = true
  >
    {nav}
  </rapi-doc>
</body>
</html>"""
        Path.cwd().joinpath("index.html").write_text(html)
        if self._oath_security_schemes:
            html = """<!doctype html>
<head>
  <script type="module" src="https://unpkg.com/rapidoc/dist/rapidoc-min.js"></script>
</head>

<body>
  <oauth-receiver>
  </oauth-receiver>
</body>"""
            Path.cwd().joinpath("oath-receiver.html").write_text(html)

