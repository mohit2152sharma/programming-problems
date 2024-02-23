from typing import List, Callable, Any
import timeit
# check examples:

# input, function or callable, can be more than one function

def print_answers(
        funcs: List[Callable],
        examples: List[Any]
) -> None:

    results = {}
    for i, func in enumerate(funcs):
        rs = []
        for example in examples:
            r = func(example)
            # time = timeit.timeit(lambda: func(example))
            rs.append({'input': example, 'output': r})
        results[func.__name__] = rs 

    for key, result in results.items():
        print(f'Result from function: {key}:')
        for i, r in enumerate(result):
            print(f'\tResult for input {r["input"]}: {r["output"]}')

        print(f'{" end of section ":*^40}')
