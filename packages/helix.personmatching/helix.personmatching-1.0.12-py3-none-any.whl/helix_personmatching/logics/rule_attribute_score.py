from dataclasses import dataclass
from typing import Optional

from helix_personmatching.models.attribute_entry import AttributeEntry


@dataclass
class RuleAttributeScore:
    attribute: AttributeEntry
    score: float
    present: bool
    source: Optional[str]
    target: Optional[str]
