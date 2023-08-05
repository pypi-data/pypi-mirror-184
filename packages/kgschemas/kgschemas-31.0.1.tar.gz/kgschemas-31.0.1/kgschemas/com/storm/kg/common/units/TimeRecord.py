
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Dict
from uuid import UUID

from pydantic import BaseModel


class TimeUnits(str, Enum):
    s = "s"


class TimeRecord(BaseModel):
    value: float
    unit: TimeUnits
