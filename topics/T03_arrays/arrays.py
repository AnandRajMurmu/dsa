from application.tester.loader import load_test_cases
from application.tester.runner import run_test_case

from application.display.console import (
    display_approach,
    display_description,
    display_fields,
    display_problem,
    display_result,
)

from topics.T03_arrays.P01_largest_element import (
    largest_element_naive,
    largest_element_optimal,
)

from topics.T03_arrays.P02_second_largest_element import (
    second_largest_element_naive,
    second_largest_element_better,
    second_largest_element_optimal,
)

from topics.T03_arrays.P03_second_smallest_element import (
    second_smallest_element_naive,
    second_smallest_element_better,
    second_smallest_element_optimal
)

from topics.T03_arrays.P04_array_is_sorted import (
    array_is_sorted_optimal
)

from topics.T03_arrays.P05_remove_duplicates_from_sorted_array import (
    remove_duplicates_from_sorted_array_naive,
    remove_duplicates_from_sorted_array_optimal,
)

test_cases_default = load_test_cases("application/templates/test_cases_default.json")
test_cases_02_sorted_arrays = load_test_cases("application/templates/test_cases_02_sorted_arrays.json")


def largest_element(test_cases=test_cases_default):
    display_problem("LARGEST ELEMENT")

    display_approach("Naive")

    display_description("The largest element from")

    for test_case in test_cases:
        result = run_test_case(largest_element_naive, test_case)
        display_result(result)

    display_approach("Optimal")

    display_description("The largest element from")

    for test_case in test_cases:
        result = run_test_case(largest_element_optimal, test_case)
        display_result(result)


def second_largest_element(test_cases=test_cases_default):
    display_problem("SECOND LARGEST ELEMENT")

    display_approach("Naive")

    display_description("The second largest element from")

    for test_case in test_cases:
        result = run_test_case(second_largest_element_naive, test_case)
        display_result(result)

    display_approach("Better")

    display_description("The second largest element from")

    for test_case in test_cases:
        result = run_test_case(second_largest_element_better, test_case)
        display_result(result)

    display_approach("Optimal")

    display_description("The second largest element from")

    for test_case in test_cases:
        result = run_test_case(second_largest_element_optimal, test_case)
        display_result(result)


def second_smallest_element(test_cases=test_cases_default):
    display_problem("SECOND SMALLEST ELEMENT")

    display_approach("Naive")

    display_description("The second smallest element from")

    for test_case in test_cases:
        result = run_test_case(second_smallest_element_naive, test_case)
        display_result(result)

    display_approach("Better")

    display_description("The second smallest element from")

    for test_case in test_cases:
        result = run_test_case(second_smallest_element_better, test_case)
        display_result(result)

    display_approach("Optimal")

    display_description("The second smallest element from")

    for test_case in test_cases:
        result = run_test_case(second_smallest_element_optimal, test_case)
        display_result(result)


def array_is_sorted(test_cases=test_cases_default):
    display_problem("ARRAY IS SORTED")

    display_approach("Optimal")

    display_description("The array")

    def format_array_is_sorted(value: bool) -> str:
        return "Sorted" if value else "Not Sorted"

    for test_case in test_cases:
        result = run_test_case(array_is_sorted_optimal, test_case)
        display_result(result, formatter=format_array_is_sorted)


def remove_duplicates_from_sorted_array(test_cases=test_cases_02_sorted_arrays):
    display_problem("REMOVE DUPLICATES FROM ARRAY")

    display_approach("Naive")

    for test_case in test_cases:
        result = run_test_case(remove_duplicates_from_sorted_array_naive, test_case)

        resulting_array, length = result.returned_value

        display_fields(result,
            fields={
                "Resulting Array ": resulting_array,
                "Length          ": length,
            }
        )

    display_approach("Optimal")

    for test_case in test_cases:
        result = run_test_case(remove_duplicates_from_sorted_array_optimal, test_case)

        resulting_array, length = result.returned_value

        display_fields(result,
            fields={
                "Resulting Array ": resulting_array,
                "Length          ": length,
            }
        )
