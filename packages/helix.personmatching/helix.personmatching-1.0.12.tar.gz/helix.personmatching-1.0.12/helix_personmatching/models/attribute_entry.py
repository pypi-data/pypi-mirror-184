from dataclasses import dataclass
from typing import Optional


@dataclass
class AttributeEntry:
    name: str
    exact_only: Optional[bool] = None
