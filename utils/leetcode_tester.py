from typing import Any, Callable, Dict, List


class TestLeetCode:
    def __init__(
        self,
        test_cases: List[Any],
        solution: List[Callable],
        expected_output: List[Any],
    ):
        self.test_cases = test_cases
        self.solution = solution
        self.expected_output = expected_output
        self.passed_test_cases = []
        self.failed_test_cases = []

    def run_soln(self) -> Dict[str, List[Any]]:
        results = {}
        for solution in self.solution:
            answers = []
            for test in self.test_cases:
                if isinstance(test, list):
                    answers.append(solution(*test))
                elif isinstance(test, dict):
                    answers.append(solution(**test))
                else:
                    answers.append(solution(test))
            results[solution.__name__] = answers
        return results

    def check_results(self):
        answers = self.run_soln()
        for solution, results in answers.items():
            print(f"Solution: {solution}")
            for result, output, test_case in zip(
                results, self.expected_output, self.test_cases
            ):
                if result == output:
                    self.passed_test_cases.append(test_case)
                    print(
                        f"test case: {test_case} passed. Result was: {result} and expected output was {output}"
                    )
                else:
                    self.failed_test_cases.append(test_case)
                    print(
                        f"test case: {test_case} failed. Result is: {result} but expected output was {output}"
                    )

        if len(self.failed_test_cases) == 0:
            print("all test cases passed")
