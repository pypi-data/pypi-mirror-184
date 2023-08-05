
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Dict
from uuid import UUID

from pydantic import BaseModel


class AISPositionSignalDataPoint(BaseModel):
    mmsi: int
    rot: Optional[float] = None
    sog: float
    navStatus: Optional[int] = None
    lon: float
    lat: float
    cog: float
    hdg: float
