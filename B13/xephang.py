# Quy định: bánh tròn: 0, bánh vuông: 1
# input: 
#   + danh sach hoc sinh xep hang theo queue vd: [1,0,1,0]
#   + danh sach bánh được xếp theo stack vd: [1,1,0,0]
# output: số lượng bánh và học sinh còn dư sau khi dã phát hết 
# Vấn đề: nếu học sinh không trùng mã với bánh trong hàng đợi => đi về cuối hàng chờ tiếp
from collections import deque
def phat_banh(students, banh):
    queue = deque(students)
    stack = banh[:]
    dem = 0
    while queue and stack :
        if queue[0] == stack[-1]:
            queue.popleft()
            stack.pop()
            dem = 0
        else:
            queue.append(queue.popleft())
            dem += 1

            if dem == len(queue):
                break

    return len(queue), len(stack)

students = [1, 0, 1, 0]
banh = [1, 1, 0, 0]
print(phat_banh(students, banh))