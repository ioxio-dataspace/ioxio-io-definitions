import datetime
from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class LocationCoordinates(CamelCaseModel):
    latitude: float = Field(
        ...,
        title="Latitude (°)",
        description="The latitude coordinate of the location in degrees",
        ge=-90.0,
        le=90.0,
        examples=[60.192059],
    )
    longitude: float = Field(
        ...,
        title="Longitude (°)",
        description="The longitude coordinate of the location in degrees",
        ge=-180.0,
        le=180.0,
        examples=[24.945831],
    )


class Sample(CamelCaseModel):
    time: datetime.datetime = Field(
        ...,
        title="Time",
        description="The time of the equipment's performance sample, in RFC 3339 format",
        examples=[
            datetime.datetime(2023, 4, 12, 23, 20, 50, tzinfo=datetime.timezone.utc),
        ],
    )

    speed: float = Field(
        ...,
        title="Speed (mm/s)",
        description="The instantaneous speed of the equipment on the ground in millimeters per second",
        examples=[3000],
    )
    load: float = Field(
        ...,
        title="Load (kg)",
        description="The instantaneous load of the equipment in kilograms",
        examples=[5000],
    )
    load_height: float = Field(
        ...,
        title="Load height (mm)",
        description="The instantaneous load height in millimeters from the ground",
        examples=[2000],
    )
    hoist_speed: float = Field(
        ...,
        title="Hoist speed (mm/s)",
        description="The instantaneous speed of the equipment hoist move in millimeters per second from the ground",
        examples=[500],
    )
    twist_locks_closed: bool = Field(
        ...,
        title="Twist locks closed",
        description="Whether twist locks are closed or not. When they are closed, the container can be hoisted.",
        examples=[True],
    )

    location_coordinates: LocationCoordinates = Field(
        ...,
        title="Location",
        description="The location of the equipment in GPS coordinates",
    )
    heading: float = Field(
        ...,
        title="Heading (°)",
        description="The GPS heading of the equipment measured from the true north in degrees",
        ge=0.0,
        le=360.0,
        examples=[90.5],
    )
    drive_power: Optional[float] = Field(
        None,
        title="Drive power (kW)",
        description="The instantaneous power of the equipment for driving on the ground in kilowatts",
    )
    hoist_power: Optional[float] = Field(
        None,
        title="Hoist power (kW)",
        description="The instantaneous power of the equipment for hoisting load in kilowatts",
    )
    auxiliary_power: Optional[float] = Field(
        None,
        title="Auxiliary power (kW)",
        description="The instantaneous auxiliary (other) energy consumption in kilowatts",
    )
    spreader_length: Optional[float] = Field(
        None,
        title="Spreader length (ft)",
        description="The length of the equipment spreader measured in feet",
        examples=[20.0],
    )
    idle_status: Optional[bool] = Field(
        None,
        title="Idle status",
        description="The instantaneous idling status of the equipment. Idling means the equipment is not receiving any command from the driver (joystick) and it is not moving any element to perform a job (drive, hoist, gantry, trolley, etc).",
        examples=[True],
    )
    driving_forward: Optional[bool] = Field(
        None,
        title="Driving forward",
        description="The instantaneous driving status of the equipment",
        examples=[True],
    )
    acceleration: Optional[float] = Field(
        None,
        title="Acceleration (mm/s^2)",
        description="The instantaneous acceleration of the equipment on the ground in millimeters per second per second",
        examples=[1000.0],
    )
    hoist_accelerator: Optional[float] = Field(
        None,
        title="Hoist acceleration (mm/s^2)",
        description="The instantaneous acceleration for hoisting the load in millimeters per second per second",
        examples=[500.0],
    )


class SimulationMetricsResponse(CamelCaseModel):
    sample_count: int = Field(
        ...,
        title="Sample count",
        description="The number of samples received in the response",
        examples=[10000],
        ge=0,
    )
    samples: list[Sample] = Field(
        ...,
        title="Samples",
        description="List of equipment's performance samples",
    )


class SimulationMetricsRequest(CamelCaseModel):
    id: str = Field(
        ...,
        title="ID",
        description="The unique identifier of the data source",
    )
    start_time: datetime.datetime = Field(
        ...,
        title="Start time",
        description="The start time of the sample period, in RFC 3339 format",
        examples=[
            datetime.datetime(
                2023, 4, 12, 23, 20, 50, 52, tzinfo=datetime.timezone.utc
            ),
        ],
    )
    end_time: Optional[datetime.datetime] = Field(
        None,
        title="End time",
        description="The end time of the sample period, in RFC 3339 format",
        examples=[
            datetime.datetime(
                2023, 5, 12, 23, 20, 50, 52, tzinfo=datetime.timezone.utc
            ),
        ],
    )
    sample_interval: Optional[int] = Field(
        None,
        title="Sample interval (ms)",
        description="The requested sample interval smaller or equal to 1000 milliseconds",
        example=[500],
        ge=0,
        le=1000,
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Cargo handling equipment simulation metrics",
    description="General simulation metrics of a cargo handling equipment operating in a port",
    request=SimulationMetricsRequest,
    response=SimulationMetricsResponse,
    tags=[
        "Cargo handling equipment",
        "Simulations",
        "Performance",
        "Port",
        "Freight terminal",
        "Logistics",
    ],
)
