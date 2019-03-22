# coding=utf-8

def divide_conquer(problem, param1, param2):
    # recursion terminator
    if problem is None:
        print result
        return

    # process data
    data = prepare_data(problem)
    subproblems = split_problem(problem, data)

    # conquer subproblems
    subresult1 = divide_conquer(subproblems[0], new_param1, new_param2)
    subresult2 = divide_conquer(subproblems[1], new_param1, new_param2)

    # process and generate the final result
    result = process_result(subresult1, subresult2)
