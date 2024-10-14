import datetime
from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class WeatherRequest(CamelCaseModel):
    lat: float = Field(
        ...,
        title="Latitude (°)",
        description="The latitude coordinate of the desired location in degrees",
        ge=-90.0,
        le=90.0,
        examples=[60.192059],
    )
    lon: float = Field(
        ...,
        title="Longitude (°)",
        description="The longitude coordinate of the desired location in degrees",
        ge=-180.0,
        le=180.0,
        examples=[24.945831],
    )
    when: Optional[datetime.datetime] = Field(
        None,
        title="Date and time",
        description="Date and time in RFC 3339 format. If not set, request the current weather",
        examples=[
            datetime.datetime(2023, 4, 12, 23, 20, 50, tzinfo=datetime.timezone.utc)
        ],
    )


class WeatherResponse(CamelCaseModel):
    temperature: float = Field(
        ...,
        title="Temperature (°C)",
        description="Current temperature in degrees Celsius",
        examples=[17.3],
        ge=-273.15,
    )
    humidity: Optional[float] = Field(
        None,
        title="Humidity (%)",
        description="Current relative air humidity percentage",
        ge=0.0,
        le=100.0,
        examples=[72],
    )
    pressure: Optional[float] = Field(
        None,
        title="Pressure (hPa)",
        description="Current air pressure in hectopascals",
        ge=0.0,
        examples=[1007],
    )
    wind_speed: Optional[float] = Field(
        None,
        title="Wind speed (m/s)",
        description="Current wind speed in meters per second",
        examples=[2.1],
        ge=0.0,
    )
    wind_direction: Optional[float] = Field(
        None,
        title="Wind direction (°)",
        description="Current wind direction in meteorological wind direction degrees",
        ge=0.0,
        le=360.0,
        examples=[220.0],
    )
    precipitation: Optional[float] = Field(
        None,
        title="Precipitation (mm/h)",
        description="Current precipitation in millimeters per hour",
        ge=0.0,
        le=1000.0,
        examples=[120.0],
    )
    visibility: Optional[float] = Field(
        None,
        title="Visibility (m)",
        description="Visibility in meters",
        ge=0.0,
        le=300000.0,
        examples=[320.0],
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Weather in metric units",
    description="Weather information for a given location, either current "
    "weather prediction or historical weather observations, using metric units.",
    request=WeatherRequest,
    response=WeatherResponse,
)
