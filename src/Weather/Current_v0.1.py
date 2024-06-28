from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class WeatherCurrentRequest(CamelCaseModel):
    latitude: float = Field(
        ...,
        title="Latitude",
        description="The latitude coordinate of the desired location",
        ge=-90.0,
        le=90.0,
        examples=[60.192059],
    )
    longitude: float = Field(
        ...,
        title="Longitude",
        description="The longitude coordinate of the desired location",
        ge=-180.0,
        le=180.0,
        examples=[24.945831],
    )


class WeatherCurrentResponse(CamelCaseModel):
    temperature: float = Field(
        ...,
        title="Temperature",
        description="Current temperature in Celsius (°C)",
        examples=[17.3],
        ge=-273.15,
    )
    humidity: float = Field(
        ...,
        title="Humidity",
        description="Current relative air humidity (%)",
        ge=0.0,
        le=100.0,
        examples=[72],
    )
    pressure: float = Field(
        ...,
        title="Pressure",
        description="Current air pressure (hPa)",
        ge=0.0,
        examples=[1007],
    )
    wind_speed: float = Field(
        ...,
        title="Wind speed",
        description="Current wind speed (m/s)",
        examples=[2.1],
        ge=0.0,
    )
    wind_direction: float = Field(
        ...,
        title="Wind direction",
        description="Current wind direction in meteorological wind direction degrees",
        ge=0.0,
        le=360.0,
        examples=[220.0],
    )
    rain: bool = Field(
        ...,
        title="Rain",
        description="Is it currently raining?",
        examples=[False],
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Current Weather",
    description="Common data points about the current weather with metric units in a "
    "given location",
    request=WeatherCurrentRequest,
    response=WeatherCurrentResponse,
)
