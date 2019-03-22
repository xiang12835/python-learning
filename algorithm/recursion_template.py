# coding=utf-8

def recursion(level, param1, param2):
    # recursion terminator
    if level > MAX_LEVEL:
        print result

        return

    # process logic in current level
    process_data(level, data)

    # drill down
    recursion(level+1, new_param1, new_param2)

    # reverse the current level status if needed 可能的收尾工作
    reverse_state(level)
