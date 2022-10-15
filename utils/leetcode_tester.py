from typing import Any, Callable, List


class TestLeetCode:
    def __init__(
        self, test_cases: List[Any], solution: Callable, expected_output: List[Any]
    ):
        self.test_cases = test_cases
        self.solution = solution
        self.expected_output = expected_output
        self.passed_test_cases = []
        self.failed_test_cases = []

    def run_soln(self) -> List[Any]:
        results = []
        for test in self.test_cases:
            results.append(self.solution(test))
        return results

    def check_results(self):
        results = self.run_soln()
        for result, output, test_case in zip(
            results, self.expected_output, self.test_cases
        ):
            if result == output:
                self.passed_test_cases.append(test_case)
            else:
                self.failed_test_cases.append(test_case)
                print(
                    f"test case: {test_case} failed. Result is: {result} but expected output was {output}"
                )

        if len(self.failed_test_cases) == 0:
            print("all test cases passed")
