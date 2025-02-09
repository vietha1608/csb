#input/output
#input: la ham co du lieu string
age = input("How old are you?")
print(type(age)) #str
#print (param): in ra man hinh du lieu ghi trong (...)
print("hello","world",3,4.12, True)
#int kieu so Nguyen
#float so thuc
#string chuoi ky tu
#constant hang so
#variable bien so 
#1.(ko co ky tu dac biet)
#2.ko co khoang trong
#3. ko co so o dau ten bien
#4. ko dat bien trung keyword cua ngon ngu
#style dat ten
#1. camel case (yourFullName = "Kevin")
#2.snake case(your_full_name = "kevin Delima")
#Data type------------------------------------
#type(): trả về dữ liệu của biến
#print(type("hello")) # str

# string (str) kiểu dữ liệu chuỗi (dựa vào bảng ASCII)
# chuỗi có thể viết bằng dấu '' hoặc ""
name = "HA"
#interger (int) kiểu dữ liệu số nguyên
age=69

#float kiểu dữ liệu số thực
weight = 99

#booleran kiểu dữ liệu logic
is_admin = True

#type casting------------
#1. int()
#string -> int
#str = int("12.5") lỗi
#float -> int
fl =  int(12.5) #làm tròn xuống chỉ lấy phần nguyên
# boolean -> int
#is_admin = int(true) #1 -true

#2.float()
float = (8)
#string ->
str = float("12.5") # 12.5
#int -> float
int = float(123) #123.0
#boolean -> float
bool = float(True) # 1.0