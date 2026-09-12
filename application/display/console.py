from collections.abc import Callable
from typing import Any

from application.models.test_result import TestResult

DISPLAY_WIDTH = 43


def display_topic(title: str):
    print("=" * DISPLAY_WIDTH)
    print(title.upper().center(DISPLAY_WIDTH))
    print("=" * DISPLAY_WIDTH)


def display_problem(title: str):
    print()
    print("-" * DISPLAY_WIDTH)
    print(title.upper())
    print("-" * DISPLAY_WIDTH)


def display_approach(name: str):
    print(f"\nApproach: {name}")
    print("-" * DISPLAY_WIDTH)


def display_description(description: str):
    print(f"\n{description} - ")


def display_result(result: TestResult, formatter: Callable[[Any], str] = str):
    answer = formatter(result.returned_value)
    print(f"\t{result.original_input} is {answer}")


def display_fields(result: TestResult, fields: dict):
    print(f"\t{result.original_input} is")

    for label, value in fields.items():
        print(f"\t\t{label} --> {value}")

    print()
