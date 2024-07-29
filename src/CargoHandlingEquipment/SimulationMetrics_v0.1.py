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
        title="Time (RFC 3339)",
        description="The time of the equipment's performance sample in RFC 3339 format",
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
    loadHeight: float = Field(
        ...,
        title="Load height (mm)",
        description="The instantaneous load height in millimeters from the ground",
        examples=[2000],
    )
    hoistSpeed: float = Field(
        ...,
        title="Hoist speed (mm/s)",
        description="The instantanous speed of the equipment hoist move in millmeters per second from the ground",
        examples=[500],
    )
    twistLocksClosed: bool = Field(
        ...,
        title="Twist locks closed",
        description="When twist locks are closed, the container can be hoisted",
        examples=["True"],
    )

    location: LocationCoordinates = Field(
        ...,
        title="Location",
        description="The location of the equipment in GPS coordinates",
    )
    heading: float = Field(
        ...,
        title="Heading (°)",
        description="The GPS heading of the equipment measured from the true north in degrees",
        ge=0.0,
        le=359.0,
        examples=["90.5"],
    )
    drivePower: Optional[float] = Field(
        None,
        title="Drive power (kW)",
        description="The instantaneous power of the equipment for driving on the ground in kilowatts",
    )
    hoistPower: Optional[float] = Field(
        None,
        title="Hoist power (kW)",
        description="The instantaneous power of the equipment for hoisting load in kilowatts",
    )
    auxiliaryPower: Optional[float] = Field(
        None,
        title="Auxiliary power (kW)",
        description="Other energy consumption in kilowatts",
    )
    spreaderLenght: Optional[float] = Field(
        None,
        title="Spreader length (ft)",
        description="The instantaneous length of the equipment spreader measured in feet",
        examples=["20"],
    )
    idleStatus: bool = Field(
        ...,
        title="Idle status",
        description="The instantaneous idling status of the equipment. Idling means the equipment is not receiving any command# from the driver (joystick) and it is not moving any element to perform a job (drive, hoist, gantry, trolley, etc)",
        examples=["True", "False"],
    )
    drivingForward: bool = Field(
        ...,
        title="Driving forward",
        description="The instantaneous driving status of the equipment",
        examples=["True", "False"],
    )
    acceleration: Optional[float] = Field(
        None,
        title="Acceleration (mm/s^2)",
        description="The instantaneous acceleration of the equipment on the ground in millimeters per second per second",
        examples=["1000"],
    )
    hoistAccelerator: Optional[float] = Field(
        None,
        title="Hoist acceleration (mm/s^2)",
        description="The instantaneous acceleration for hoisting the load in millimeters per second per second per second",
    )


class SimulationMetricsResponse(CamelCaseModel):
    sampleCount: int = Field(
        ...,
        title="Sample count",
        description="The number of samples received in the response",
        examples=["10000"],
    )
    samples: Sample = Field(
        ..., title="Samples", description="List of equipment's performance samples"
    )


class SimulationMetricsRequest(CamelCaseModel):
    id: str = Field(
        ...,
        title="ID",
        description="The unique identifier of the data source",
    )
    startTime: datetime.datetime = Field(
        ...,
        title="Start time (RFC 3339)",
        description="The start time of the sample period in RFC 3339 format.",
        examples=[
            datetime.datetime(
                2023, 4, 12, 23, 20, 50, 52, tzinfo=datetime.timezone.utc
            ),
        ],
    )
    sampleInterval: int = Field(
        title="Sample interval (ms)",
        description="The requested sample interval smaller or equal to 1000 milliseconds",
        example=["500"],
    )
    endTime: datetime.datetime = Field(
        ...,
        title="End time (RFC 3339)",
        description="The end time of the sample period in RFC 3339 format",
        examples=[
            datetime.datetime(
                2023, 4, 12, 23, 20, 50, 52, tzinfo=datetime.timezone.utc
            ),
        ],
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Cargo handling equipment Simulation metrics",
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
