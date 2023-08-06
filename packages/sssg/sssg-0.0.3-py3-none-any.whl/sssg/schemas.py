from dataclasses import dataclass
from typing import Dict


@dataclass 
class Page:
    template: str 
    target: str 
    content: Dict[str, str]