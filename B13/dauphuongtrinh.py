# input: chuỗi bao gồm các ngoặc phương trình '[({})]' / '[([(])]'
# output: boolean: True/ False
# Yêu cầu: sử dụng cấu trúc dữ liệu stack/ queue

def validate_parentheses(s):
    stack = []
    mapping = {')': '(',']': '[', '}': '{'}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return not stack
# test
print(validate_parentheses('[({})]'))  # True
print(validate_parentheses('[([(])]'))  # False