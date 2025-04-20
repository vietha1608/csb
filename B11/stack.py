# STACK: Last in (phai) First out (trai) (LIFO)
#khai bao stack
stack = [1, 2, 3, 4]
# peek: lấy phần tử cuối cùng trong danh sách (KHÔNG XÓA)
print(stack[-1])
# push: thêm phần tử vào cuối (đỉnh stack) - O(1)
stack.append(4)
#lay phan tu khoi dinh stack
top = stack.pop()
print(top)
#kiem tra rong
def is_empty(stack):
    #cach1
    #return len(stack) == 0

#cach2
#if len(stack) == 0
#return true
#return false

#cach3:
    return True if len(stack) == 0 else False
print(is_empty(stack))