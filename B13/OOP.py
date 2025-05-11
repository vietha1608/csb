# bai 1: Thanh toán máy tự động
# input: danh sách món hàng
# output: tổng tiền
# Yêu cầu: hỏi lại có cần mua không + thay đổi số lượng món hàng
# + CartItem: id, tên món, giá trị món
# + Cart: danh sách món hàng {cartItemid, số lượng} + thêm/ xóa/ cập nhật số lượng món
# + Cashier: id, in bill (mỗi món hàng đều phải được hỏi trước khi tính, vd: Ao thun: qty 2 => tổng tiền ? y/n)
class CartItem:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

class Cart:
    def __init__ self, CartItem:list, quantity:
        pass