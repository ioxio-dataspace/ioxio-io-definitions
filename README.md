# IOXIO.IO Dataspace Definitions

This repository contains Data Product definitions for the
[IOXIO.io Dataspace](https://ioxio.io).

Specification for describing data product definitions can be found in
[./DataProducts/README.md](./DataProducts/README.md).

To view these definitions in a more human readable format instead of the raw technical
format in this repository, you can check these resources:

- [Definitions viewer](https://definitions.ioxio.io)
- [API docs](https://docs.ioxio.io)
- [Swagger UI](https://gateway.ioxio.io/docs)

# Repo structure

- [./src](./src) - Definition sources in python format
- [./DataProducts](./DataProducts) - Final Definitions as OpenAPI 3.x specs
- [.github/workflows](.github/workflows) - Pre-configured CI workflows for validating
  and converting definitions from sources

# Getting started

Press `Use this template` to create a new repo from this template and define your data
products there.

Please check the [Contribution guidelines](./CONTRIBUTING.md) to learn how to submit new
data product definitions in this repo.

## Python sources

Each python file located in the `src` folder is treated as a Data Product definition.

For example, `src/AirQuality/Current_v1.0.py` defines the `AirQuality/Current_v1.0` data
product.

These files are then converted to OpenAPI 3.x specs, which are final forms of
definitions. To make the converter work correctly, each file must follow the same
structure:

```python
from pydantic import Field

from definition_tooling.converter import CamelCaseModel, DataProductDefinition, ErrorResponse


class Request(CamelCaseModel):
    ...


class Response(CamelCaseModel):
    ...


@ErrorResponse(description="...")
class Error418(CamelCaseModel):
    ...


DEFINITION = DataProductDefinition(
    version="1.0.0",
    title="...",
    description="...",
    request=Request,
    response=Response,
    requires_authorization=False,
    requires_consent=False,
    error_responses={
        418: Error418,
    },
    deprecated=False,
    tags=["Foo"],
)

```

Considering `CamelCaseModel` is a subclass of `pydantic`'s `BaseModel`, it's better to
understand how to use this library. Please read
[pydantic](https://docs.pydantic.dev/1.10/)'s documentation if you're not familiar with
it yet.

Each data product definition represented as python file must define a `DEFINITION`
variable which is an instance of `DataProductDefinition` class.

DataProductDefinition is a structure consisting of:

- `version`

  Version is used in the info block of the OpenAPI spec. The data product definitions
  use [Semantic Versioning](https://semver.org/) of the form `MAJOR.MINOR.PATCH`, for
  example `1.0.0`. Definitions in the `test` and `draft` folders must have versions of
  the form `0.0.z` and the version number should not exist in the filename of the
  definition. In all other definitions the version number needs to be `>= 0.1.0` and the
  corresponding short version number needs to be included in the filename. For example
  the version `0.1.0` of the `Foo/Bar` definition would correspond to the file
  `src/Foo/Bar_v0.1.py`. For more details about versions and filenames see the
  [Versioning of definitions](CONTRIBUTING.md#versioning-of-definitions) section in the
  contribution guidelines.

- `title`

  Title used in the info block of OpenAPI spec and the summary for the POST route

- `description`

  Data product description, used in the top of OpenAPI spec and in the POST route

- `request`

  pydantic model describing body of POST request

- `response`

  pydantic model describing expected response from data source

- `requires_authorization`

  Marks the Authorization header as required

- `requires_consent`

  Marks the X-Consent-Token header as required

- `error_responses`

  A mapping from HTTP error status codes to pydantic models, wrapped in the
  `ErrorResponse` decorator, describing expected error responses from the data source

- `deprecated`

  Marks the route as deprecated

- `tags`

  A list (or other iterable) of strings to use as tags for the POST route. The tags
  should be in `Title Case`.

### Example

There's an example of Data Product Definition for current weather:

```python
from pydantic import Field

from definition_tooling.converter import CamelCaseModel, DataProductDefinition


class CurrentWeatherMetricRequest(CamelCaseModel):
    lat: float = Field(
        ...,
        title="Latitude",
        description="The latitude coordinate of the desired location",
        ge=-90.0,
        le=90.0,
        examples=[60.192059],
    )
    lon: float = Field(
        ...,
        title="Longitude",
        description="The longitude coordinate of the desired location",
        ge=-180.0,
        le=180.0,
        examples=[24.945831],
    )


class CurrentWeatherMetricResponse(CamelCaseModel):
    humidity: float = Field(..., title="Current relative air humidity in %", examples=[72])
    pressure: float = Field(..., title="Current air pressure in hPa", examples=[1007])
    rain: bool = Field(
        ..., title="Rain status", description="If it's currently raining or not."
    )
    temp: float = Field(
        ..., title="Current temperature in Celsius", examples=[17.3], ge=-273.15
    )
    wind_speed: float = Field(..., title="Current wind speed in m/s", examples=[2.1], ge=0)
    wind_direction: float = Field(
        ...,
        title="Current wind direction in meteorological wind direction degrees",
        ge=0,
        le=360,
        examples=[220.0],
    )


DEFINITION = DataProductDefinition(
    version="1.0.0",
    title="Current weather in a given location",
    description="Current weather in a given location with metric units",
    request=CurrentWeatherMetricRequest,
    response=CurrentWeatherMetricResponse,
    tags=["Weather"],
)
```

## Guides and help

[Written guide for how to create data definitions](https://ioxio.com/guides/how-to-create-data-definitions)

You can also check out our YouTube tutorial:

[![Defining Data Products for the IOXIO® Dataspace technology
](https://img.youtube.com/vi/yPzN04ICsbw/0.jpg)](http://www.youtube.com/watch?v=yPzN04ICsbw)

Also join our [IOXIO Community Slack](https://slack.ioxio.com/)
