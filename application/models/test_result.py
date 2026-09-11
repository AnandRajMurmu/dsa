from dataclasses import dataclass
from typing import Any


@dataclass
class TestResult:
    original_input: list[int]
    returned_value: Any
    final_input: list[int]
