from application.tester.loader import load_test_cases
from application.tester.runner import run_test_case

from application.display.console import (
    display_approach,
    display_description,
    display_fields,
    display_problem,
    display_result,
    display_topic,
)

from topics.T03_arrays.P01_largest_element import (
    largest_element_naive,
    largest_element_optimal,
)

test_cases_default = load_test_cases("application/templates/default_test_cases.json")


def largest_element():
    display_topic("ARRAYS")

    display_problem("LARGEST ELEMENT")

    display_approach("Naive")

    display_description("Largest Element From")

    for test_case in test_cases_default:
        result = run_test_case(largest_element_naive, test_case)
        display_result(result)

    display_approach("Optimal")

    display_description("Largest Element From")

    for test_case in test_cases_default:
        result = run_test_case(largest_element_optimal, test_case)
        display_result(result)
