
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Dict
from uuid import UUID

from pydantic import BaseModel


class FrequencyUnits(str, Enum):
    Hz = "Hz"
    kHz = "kHz"
    MHz = "MHz"
    mHz = "mHz"


class FrequencyRecord(BaseModel):
    value: float
    unit: FrequencyUnits
