
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Dict
from uuid import UUID

from pydantic import BaseModel


class WattUnits(str, Enum):
    MW = "MW"
    kW = "kW"
    GW = "GW"
    W = "W"
    kVAr = "kVAr"
    MVAr = "MVAr"


class WattRecord(BaseModel):
    value: float
    unit: WattUnits
