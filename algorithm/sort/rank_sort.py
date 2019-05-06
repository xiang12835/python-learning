# coding=utf-8

def is_equal(data,left,right):     #判断left到当前right是否有相等的，如果有说明之前已经对这个进行过全排序了
    for i in range(left,right):
        if data[i] == data[right]:
            return True
    return False
def rank(data, step):
    if len(data) == step+1:
        print(data)
        return
    else:
        for i in range(step, len(data)):
            if is_equal(data,step,i):  #加一个判断
                continue
            else:
                data[step], data[i] = data[i], data[step]
                rank(data, step + 1)
                data[step], data[i] = data[i], data[step]
if __name__ == '__main__':
    data = list("bcc")
    rank(data, 0)
