#nhap vao 1 so nguyen duong
number = input()
#chuyen kieu so nguyen
number_new = int(number)
#kiem tra duong
if number_new >= 0:
    pass
else:
    print("Error: input is not greater than 0")
    ### **Câu 1: Nhập và tính tổng hai số**
# Viết chương trình yêu cầu người dùng nhập hai số nguyên,
#  sau đó tính và in ra tổng của chúng. Kiểm tra xem input
#  có phải là số nguyên hợp lệ không
n = input()
m = input()
n_new = int(n)
m_new = int(m)
sum = n_new + m_new
print(sum)
### **Câu 2: Nhập và kiểm tra số nguyên dương**
# Viết chương trình yêu cầu người dùng nhập một số nguyên
#  dương. Nếu người dùng nhập số âm hoặc không phải số
#  nguyên, yêu cầu nhập lại cho đến khi hợp lệ.
z = input()
z_new = int(z)
if z_new >= 0:
    pass
else:
    print("eror:the number must bigger than 0 yêu cầu nhập lại cho đến khi hợp lệ")

#btvn 2
a = input(2)
b = input(4)
a_new = int(a)
b_new = int(b)
sum = a_new + b_new
print(sum)