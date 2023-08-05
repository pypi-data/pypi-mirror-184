
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Dict
from uuid import UUID

from pydantic import BaseModel


class AISStaticVoyageDataPoint(BaseModel):
    mmsi: int
    callSign: str
    imo: int
    name: str
    draught: float
    shipType: int
