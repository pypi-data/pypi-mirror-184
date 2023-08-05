
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Dict
from uuid import UUID

from pydantic import BaseModel


class AmpereUnits(str, Enum):
    A = "A"
    mA = "mA"
    kA = "kA"


class AmpereRecord(BaseModel):
    value: float
    unit: AmpereUnits
