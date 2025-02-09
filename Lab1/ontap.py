# khai bao bien------------
# 1. Biến a có giá trị là 10
# 2. Biến chieu_cao được gán giá trị là 20.5
# 3. Biến is_human có giá trị là True
# 4. Biến cat có giá trị là "Mimi"
# 5. Biến x gán là 10.04
a = 10
chieu_cao = 20.5
is_human = True
cat = "Mimi"
x = 10.4

### **Câu 1: Chuyển đổi kiểu dữ liệu**
# Viết một đoạn code Python để chuyển đổi một biến `x` có
#  giá trị là `"123"` (kiểu chuỗi) sang kiểu dữ liệu số
#  nguyên (`int`). Sau đó, in ra kiểu dữ liệu của biến
#  `x` sau khi chuyển đổi
x = "123"
x_new = int(x)
print(x_new)

# Viết một đoạn code Python để kiểm tra kiểu dữ liệu của
#  biến `y` có giá trị là `3.14`. In ra kết quả kiểu dữ 
# liệu của biến `y
y = 3.14
print(type(y))

### **Câu 3: Tính toán với kiểu dữ liệu khác nhau**
# Viết một đoạn code Python để thực hiện phép cộng giữa
#  một biến `a` có giá trị là `10` (kiểu số nguyên) và
#  một biến `b` có giá trị là `"20"` (kiểu chuỗi).
#  Yêu cầu chuyển đổi kiểu dữ liệu phù hợp để kết quả là
#  `30`.
a = 10
b = "20"
b_new = int(b)
sum = a+b_new
print(sum)

### **Câu 4: Khai báo và xác định kiểu dữ liệu**
# Viết một đoạn code Python để khai báo ba biến:
# - Biến `name` có giá trị là `"Alice"` (kiểu chuỗi).
# - Biến `age` có giá trị là `25` (kiểu số nguyên).
# - Biến `height` có giá trị là `1.65` (kiểu số thực).
# Sau đó, in ra kiểu dữ liệu của từng biến
name = "Alice"
age = 25
height = 1.65
print(type(name))
print(type(age))
print(type(height))

### **Câu 5: Ép kiểu dữ liệu**
# Viết một đoạn code Python để thực hiện các yêu cầu sau:
# 1. Khai báo một biến `num` có giá trị là `15.75`
#  (kiểu số thực).
# 2. Ép kiểu biến `num` sang kiểu số nguyên
#  (`int`) và lưu vào biến `num_int`.
# 3. Ép kiểu biến `num` sang kiểu chuỗi (`str`)
#  và lưu vào biến `num_str`.
# 4. In ra giá trị và kiểu dữ liệu của `num_int`
#  và `num_str`.
num = 15.75
num_int = int(num)
num_str = str(num)
print(type(num_int))
print(type(num_str))