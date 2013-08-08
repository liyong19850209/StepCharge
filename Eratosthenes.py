import math
def eratosthenes(begin,end):
    if begin%2 == 0:
        begin += 1
    e = int(math.pow(end,0.5))+1
    print e
    result = []
    for i in range(begin,end+1,2):
        flag = 1
        for j in range(3,e):
            if i%j == 0 and i != j:
                flag = 0
        if flag == 1:
            result.append(i)
    return result
if __name__ == "__main__":
    print eratosthenes(10001,20000)
