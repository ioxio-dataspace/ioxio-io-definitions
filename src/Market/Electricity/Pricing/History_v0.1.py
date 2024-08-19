import datetime
from typing import List

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class EnergyPriceRequest(CamelCaseModel):
    location: str = Field(
        ...,
        title="Location",
        description="E.g. the country in ISO 3166-1 alpha-3 or other location identifier",
        examples=["FIN"],
    )
    start_time: datetime.datetime = Field(
        ...,
        title="Start time",
        description="Start time of the requested time period, in RFC 3339",
        examples=[
            datetime.datetime(
                2024,
                1,
                1,
                0,
                0,
                0,
                tzinfo=datetime.timezone(datetime.timedelta(hours=2)),
            ),
        ],
    )
    end_time: datetime.datetime = Field(
        ...,
        title="End time",
        description="End time of the requested time period, in RFC 3339",
        examples=[
            datetime.datetime(
                2024,
                1,
                1,
                23,
                59,
                59,
                tzinfo=datetime.timezone(datetime.timedelta(hours=2)),
            ),
        ],
    )


class PeriodPrice(CamelCaseModel):
    price: float = Field(
        ...,
        title="Price (per MWh)",
        description="Market price per megawatt-hour for this pricing period",
        examples=[29.12],
    )
    start_time: datetime.datetime = Field(
        ...,
        title="Start time",
        description="Start time of the pricing period, in RFC 3339",
        examples=[
            datetime.datetime(
                2024,
                1,
                1,
                2,
                0,
                0,
                tzinfo=datetime.timezone(datetime.timedelta(hours=2)),
            )
        ],
    )


class EnergyPriceResponse(CamelCaseModel):
    currency_code: str = Field(
        ...,
        title="Currency",
        description="Three letter currency code for the price, from ISO 4217",
        examples=["EUR", "USD"],
        pattern=r"^[A-Z]{3}$",
    )
    prices: List[PeriodPrice] = Field(
        ...,
        title="Prices",
        description="List of the prices for the given time period",
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Electricity market price",
    description="Electricity price per MWh",
    request=EnergyPriceRequest,
    response=EnergyPriceResponse,
)
