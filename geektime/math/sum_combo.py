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
    if total_reword == 0:
        print(result)
        return
    elif total_reword < 0:
        return
    else:
        for i in range(len(rewards)):
            new_result = copy.copy(result)
            new_result.append(rewards[i])
            get_sum_combo(total_reword - rewards[i], new_result)


if __name__ == "__main__":
    get_sum_combo(2)
    # [1, 1]
    # [2]
    get_sum_combo(3)
    # [1, 1, 1]
    # [1, 2]
    # [2, 1]
