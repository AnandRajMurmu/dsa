from copy import deepcopy

from application.models.test_result import TestResult


def run_test_case(algorithm, test_case, *args, **kwargs):
    original_input = deepcopy(test_case)
    working_input = deepcopy(test_case)

    returned_value = algorithm(working_input, *args, **kwargs)

    return TestResult(
        original_input=original_input,
        returned_value=returned_value,
        final_input=working_input,
    )
