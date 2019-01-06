# coding=utf-8

import copy

rewards = [1, 2, 5, 10]    # 四种面额的纸币


def get_sum_combo(total_reword, result=[]):
    """ 使用函数的递归（嵌套）调用，找出所有可能的奖赏组合

    Args:
        total_reword: 奖赏总金额
        result: 保存当前的解

    Returns: void

    """
    if total_reword == 0:  # 证明它是满足条件的解，结束嵌套调用，输出解

        print(result)
        return
    elif total_reword < 0:  # 证明它不是满足条件的解，不输出
        return
    else:
        for i in range(len(rewards)):
            new_result = copy.copy(result)  # 由于有 4 种情况，需要 clone 当前的解并传入被调用的函数

            new_result.append(rewards[i])  # 记录当前的选择，解决一点问题
            get_sum_combo(total_reword - rewards[i], new_result)  # 剩下的问题，留给嵌套调用去解决


if __name__ == "__main__":
    get_sum_combo(2)
    # [1, 1]
    # [2]
    get_sum_combo(3)
    # [1, 1, 1]
    # [1, 2]
    # [2, 1]
