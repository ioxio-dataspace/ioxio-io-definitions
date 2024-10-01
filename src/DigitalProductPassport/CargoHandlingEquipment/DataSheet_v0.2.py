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
        description="The number of corresponding batteries in the machine",
        ge=0,
        examples=[2],
    )
    nominal_capacity: Optional[float] = Field(
        None,
        title="Nominal capacity (Ah)",
        description="The total number of ampere-hours that can be withdrawn from "
        "a fully charged battery under reference conditions",
        ge=0,
        examples=[225.0],
    )
    nominal_voltage: Optional[float] = Field(
        None,
        title="Nominal voltage (v)",
        description="The average voltage the battery is rated to provide under typical operating conditions"
        "typical operating conditions",
        ge=0,
        examples=[12.0],
    )
    power: Optional[float] = Field(
        None,
        title="Power (kW)",
        description="The power of the battery in use in the machine in kilowatts",
        examples=[75.0],
        ge=0,
    )


class DataSheetResponse(CamelCaseModel):
    type: EquipmentType = Field(
        ...,
        title="Type",
        description="The type of the cargo handling equipment according to TIC4.0 classification. Options are Straddle Carrier (SC) / Ship-to-Shore Crane (STS) / Mobile Crane (MC) / Rubber-tired Gantry Crane (RTG) / Rail-mounted Gantry Crane (RMG) / Automatic Stacking Crane (ASC) / Reach Stacker (RS) / Top Handler (TH) / Empty Container Handler (ECH) / Terminal Tractor (TT)",
        examples=[EquipmentType.STRADDLE_CARRIER],
    )
    model: str = Field(
        ...,
        title="Model",
        max_length=40,
        description="The model of the machine",
        examples=["Model X 1234"],
    )
    release_year: Optional[int] = Field(
        None,
        title="Release year",
        description="The model year of the machine",
        ge=1900,
        le=2500,
        examples=[2023],
    )
    manufacturer_information: ManufacturerInformation = Field(
        ...,
        title="Manufacturer information",
        description="The details of the manufacturer",
    )
    power_source: PowerSource = Field(
        ...,
        title="Power source",
        description="The power source used by the machine",
        examples=[PowerSource.ELECTRIC],
    )
    batteries: List[Batteries] = Field(
        ...,
        title="Batteries",
        description="The list of the batteries in the machine",
    )
    fuel_volume: Optional[float] = Field(
        None,
        title="Fuel volume (l)",
        description="The maximum fuel amount in litres assuming the vehicle uses fuel for operation",
        examples=[3000.0],
    )
    gas_amount: Optional[float] = Field(
        None,
        title="Gas amount (kg)",
        description="The maximum gas amount in kilograms assuming the vehicle uses gas for operation",
        examples=[50.0],
    )
    expected_range: Optional[float] = Field(
        None,
        title="Expected range (km)",
        description="The expected range with fully charged batteries and/or refilled "
        "tank in kilometers",
        examples=[300.0],
    )
    net_vehicle_mass: float = Field(
        ...,
        title="Net vehicle mass (kg)",
        description="The mass of the machine when unloaded in kilograms",
        examples=[4000.0],
    )
    max_load_capacity: float = Field(
        ...,
        title="Max load capacity (kg)",
        description="The maximum weight that the machine can be loaded with or carry "
        "in kilograms",
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
        title="ID",
        description="The unique identifier of the product",
        examples=["71b51878-8a00-11ee-b9d1-0242ac120002"],
    )


DEFINITION = DataProductDefinition(
    version="0.2.0",
    title="Cargo handling equipment data sheet",
    description="General as-built data of a cargo handling equipment operating in a "
    "port",
    request=DataSheetRequest,
    response=DataSheetResponse,
    tags=["Cargo handling equipment", "Port", "Freight terminal", "Logistics"],
)
