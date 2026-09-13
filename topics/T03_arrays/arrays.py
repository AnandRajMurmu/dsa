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
    second_smallest_element_optimal,
)

from topics.T03_arrays.P04_array_is_sorted import (
    array_is_sorted_optimal,
)

from topics.T03_arrays.P05_remove_duplicates_from_sorted_array import (
    remove_duplicates_from_sorted_array_naive,
    remove_duplicates_from_sorted_array_optimal,
)

from topics.T03_arrays.P06_left_rotate_array_by_one import (
    left_rotate_array_by_one_optimal,
)

from topics.T03_arrays.P07_left_rotate_array_by_k import (
    left_rotate_array_by_k_naive,
    left_rotate_array_by_k_optimal,
)

from topics.T03_arrays.P08_right_rotate_array_by_k import (
    right_rotate_array_by_k_naive,
    right_rotate_array_by_k_optimal,
)


test_cases_default = load_test_cases("application/templates/test_cases_default.json")
test_cases_01_overall = load_test_cases("application/templates/test_cases_01_overall.json")
test_cases_02_sorted_arrays = load_test_cases("application/templates/test_cases_02_sorted_arrays.json")
test_cases_03_rotate_arrays_by_k = load_test_cases("application/templates/test_cases_03_rotate_arrays_by_k.json")


def largest_element(test_cases=test_cases_default):
    display_problem("LARGEST ELEMENT")

    display_approach("Naive")

    display_description("The largest element for")

    for test_case in test_cases:
        result = run_test_case(largest_element_naive, test_case)
        display_result(f"{result.original_input} is {result.returned_value}")

    display_approach("Optimal")

    display_description("The largest element for")

    for test_case in test_cases:
        result = run_test_case(largest_element_optimal, test_case)
        display_result(f"{result.original_input} is {result.returned_value}")


def second_largest_element(test_cases=test_cases_default):
    display_problem("SECOND LARGEST ELEMENT")

    display_approach("Naive")

    display_description("The second largest element for")

    for test_case in test_cases:
        result = run_test_case(second_largest_element_naive, test_case)
        display_result(f"{result.original_input} is {result.returned_value}")

    display_approach("Better")

    display_description("The second largest element for")

    for test_case in test_cases:
        result = run_test_case(second_largest_element_better, test_case)
        display_result(f"{result.original_input} is {result.returned_value}")

    display_approach("Optimal")

    display_description("The second largest element for")

    for test_case in test_cases:
        result = run_test_case(second_largest_element_optimal, test_case)
        display_result(f"{result.original_input} is {result.returned_value}")


def second_smallest_element(test_cases=test_cases_default):
    display_problem("SECOND SMALLEST ELEMENT")

    display_approach("Naive")

    display_description("The second smallest element for")

    for test_case in test_cases:
        result = run_test_case(second_smallest_element_naive, test_case)
        display_result(f"{result.original_input} is {result.returned_value}")

    display_approach("Better")

    display_description("The second smallest element for")

    for test_case in test_cases:
        result = run_test_case(second_smallest_element_better, test_case)
        display_result(f"{result.original_input} is {result.returned_value}")

    display_approach("Optimal")

    display_description("The second smallest element for")

    for test_case in test_cases:
        result = run_test_case(second_smallest_element_optimal, test_case)
        display_result(f"{result.original_input} is {result.returned_value}")


def array_is_sorted(test_cases=test_cases_default):
    display_problem("ARRAY IS SORTED")

    display_approach("Optimal")

    display_description("The array")

    for test_case in test_cases:
        result = run_test_case(array_is_sorted_optimal, test_case)

        status = "Sorted" if result.returned_value else "Not Sorted"

        display_result(f"{result.original_input} is {status}")


def remove_duplicates_from_sorted_array(test_cases=test_cases_02_sorted_arrays):
    display_problem("REMOVE DUPLICATES FROM ARRAY")

    display_approach("Naive")

    for test_case in test_cases:
        result = run_test_case(remove_duplicates_from_sorted_array_naive, test_case)

        resulting_array, length = result.returned_value

        display_result(f"For {result.original_input}")

        display_fields(
            fields={
                "Resulting Array ": resulting_array,
                "Length          ": length,
            }
        )

    display_approach("Optimal")

    for test_case in test_cases:
        result = run_test_case(remove_duplicates_from_sorted_array_optimal, test_case)

        resulting_array, length = result.returned_value

        display_result(f"For {result.original_input}")

        display_fields(
            fields={
                "Resulting Array ": resulting_array,
                "Length          ": length,
            }
        )


def left_rotate_array_by_one(test_cases=test_cases_default):
    display_problem("LEFT ROTATE ARRAY BY ONE")

    display_approach("OPTIMAL")

    display_description("The array")

    for test_case in test_cases:
        result = run_test_case(left_rotate_array_by_one_optimal, test_case)
        display_result(f"{result.original_input} rotated by 1 is {result.returned_value}")


def left_rotate_array_by_k(test_cases=test_cases_03_rotate_arrays_by_k):
    display_problem("LEFT ROTATE ARRAY BY K")

    display_approach("NAIVE")

    display_description("The array")

    for test_case in test_cases:
        result = run_test_case(left_rotate_array_by_k_naive, test_case["array"], test_case["k"])
        display_result(f"{result.original_input} rotated by {test_case['k']} is {result.returned_value}")

    display_approach("OPTIMAL")

    display_description("The array")

    for test_case in test_cases:
        result = run_test_case(left_rotate_array_by_k_optimal, test_case["array"], test_case["k"])
        display_result(f"{result.original_input} rotated by {test_case['k']} is {result.returned_value}")


def right_rotate_array_by_k(test_cases=test_cases_03_rotate_arrays_by_k):
    display_problem("RIGHT ROTATE ARRAY BY K")

    display_approach("NAIVE")

    display_description("The array")

    for test_case in test_cases:
        result = run_test_case(right_rotate_array_by_k_naive, test_case["array"], test_case["k"])
        display_result(f"{result.original_input} rotated by {test_case['k']} is {result.returned_value}")

    display_approach("OPTIMAL")

    display_description("The array")

    for test_case in test_cases:
        result = run_test_case(right_rotate_array_by_k_optimal, test_case["array"], test_case["k"])
        display_result(f"{result.original_input} rotated by {test_case['k']} is {result.returned_value}")
