
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Dict
from uuid import UUID

from pydantic import BaseModel


class UnitlessUnits(str, Enum):
    integerCategorical = "integerCategorical"
    unitlessMeasurement = "unitlessMeasurement"


class UnitlessRecord(BaseModel):
    value: float
    unit: UnitlessUnits
