# Bai1: kiem tra bieu thuc (phan mo - dong ngoac)
def is_valid_parentheses(f:list) -> bool:
    # tao danh sach da kiem tra
    clone = f
    # kiem tra: neu co dong ngoac => tim mo ngoac gan nhat => xoa cap ngoac
    
    # neu khong co ngoac dong => return false
    return True

print(is_valid_parentheses(['{', "}", '[', '(', ')'])) # false