# coding=utf-8

def combine(data, step, select_data, target_num):
    if len(select_data) == target_num:   #选择的元素已经够了，就输出并返回
        print(select_data)
        return
    if step >= len(data):               #没有元素选了而且还没够，也是直接返回
        return
    select_data.append(data[step])             #选择当前元素
    combine(data, step + 1, select_data, target_num)
    select_data.pop()                         #别忘了从已选择元素中先删除
    combine(data, step + 1, select_data, target_num) #不选择当前元素
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6]
    combine(data, 0, [], 3)
