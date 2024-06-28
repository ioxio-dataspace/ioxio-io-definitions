from enum import Enum
from typing import List, Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class EquipmentType(str, Enum):
    STRADDLE_CARRIER = "SC"
    SHIP_TO_SHORE_CRANE = "STS"
    MOBILE_CRANE = "MC"
    RUBBER_TIRED_GANTRY_CRANE = "RTG"
    RAIL_MOUNTED_GANTRY_CRANE = "RMG"
    AUTOMATIC_STACKING_CRANE = "ASC"
    REACH_STACKER = "RS"
    TOP_HANDLER = "TH"
    EMPTY_CONTAINER_HANDLER = "ECH"
    TERMINAL_TRACTOR = "TT"


class PowerSource(str, Enum):
    ELECTRIC = "electric"
    FUEL = "fuel"
    GAS = "gas"
    HYBRID = "hybrid"
    H2 = "h2"
    HYDRAULIC = "hydraulic"


class ManufacturerInformation(CamelCaseModel):
    name: str = Field(
        ...,
        max_length=250,
        title="Name",
        description="The registered trade name of the manufacturer company",
        examples=["Equipment Manufacturer Company X"],
    )
    website: Optional[str] = Field(
        None,
        pattern=r"^https://",
        max_length=2083,
        title="Website",
        description="The website of the manufacturer",
        examples=["https://example.com/"],
    )


class Batteries(CamelCaseModel):
    cell_type: Optional[str] = Field(
        None,
        max_length=250,
        title="Cell type",
        description="The type of cells used in the battery pack",
        examples=["lithium-ion"],
    )
    count: Optional[int] = Field(
        None,
        title="Count",
        description="The number of corresponding batteries in use in the machine",
        ge=0,
        examples=[2],
    )
    capacity: Optional[float] = Field(
        None,
        title="Capacity",
        description="The total number of ampere-hours (Ah) that can be withdrawn from "
        "a fully charged battery under reference conditions",
        examples=[225.0],
    )
    nominal_voltage: Optional[float] = Field(
        None,
        title="Nominal voltage",
        description="The average voltage of the battery it is rated to provide under "
        "typical operating conditions",
        examples=[12.0],
    )
    power: Optional[float] = Field(
        None,
        title="Power",
        description="The power of the battery in use in the machine in kilowatts (kW)",
        examples=[75.0],
    )


class DataSheetResponse(CamelCaseModel):
    type: EquipmentType = Field(
        ...,
        title="Type",
        description="The type of the cargo handling equipment according to TIC4.0 classification",
        examples=[EquipmentType.STRADDLE_CARRIER],
    )
    model: str = Field(
        ...,
        title="Model",
        max_length=40,
        description="The model of the equipment",
        examples=["Model X 1234"],
    )
    model_year: Optional[int] = Field(
        None,
        title="Model year",
        description="The model year of the equipment",
        ge=1900,
        le=2500,
        examples=[2023],
    )
    manufacturer_information: Optional[ManufacturerInformation] = Field(
        None,
        title="Manufacturer information",
        description="The details of the manufacturer",
    )
    power_source: PowerSource = Field(
        ...,
        title="Power source",
        description="The power source used for the machine operations",
        examples=[PowerSource.ELECTRIC],
    )
    batteries: List[Batteries] = Field(
        ...,
        title="Batteries",
        description="The list of the batteries in the machine",
    )
    fuel_volume: Optional[float] = Field(
        None,
        title="Fuel volume",
        description="The maximum fuel volume stored in the tank litres (l)",
        examples=[3000.0],
    )
    gas_amount: Optional[float] = Field(
        None,
        title="Gas amount",
        description="The maximum gas amount stored in the tank in kilograms (kg)",
        examples=[50.0],
    )
    expected_range: Optional[float] = Field(
        None,
        title="Expected range",
        description="The expected range with fully charged batteries and/or refilled "
        "tank in kilometers (km)",
        examples=[300.0],
    )
    net_vehicle_mass: float = Field(
        ...,
        title="Net vehicle mass",
        description="The mass of the machine when unloaded in kilograms (kg)",
        examples=[4000.0],
    )
    max_load_capacity: float = Field(
        ...,
        title="Max load capacity",
        description="The maximum weight that the machine can be loaded with or carry "
        "in kilograms (kg)",
        examples=[6000.0],
    )


class DataSheetRequest(CamelCaseModel):
    product: str = Field(
        ...,
        max_length=150,
        title="Product",
        description="The product code used for identifying the product type",
        examples=["cargo-handling-equipment-modelX-1234"],
    )
    id: str = Field(
        ...,
        max_length=40,
        title="Id",
        description="The unique identifier of the product",
        examples=["71b51878-8a00-11ee-b9d1-0242ac120002"],
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Cargo Handling Equipment Data Sheet",
    description="General as-built data of a cargo handling equipment operating in a "
    "port",
    request=DataSheetRequest,
    response=DataSheetResponse,
    tags=["Cargo handling equipment", "Port", "Freight terminal", "Logistics"],
)
