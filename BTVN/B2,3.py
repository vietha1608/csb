#**Câu 1:**
#a) Nhập vào nguyên a và b, nếu 1 trong 2 số a và b chia hết cho 2 thì in ra True, ngược lại in ra False
a = int(input())
b = int(input())
if a % 2 == 0 :
    print("true")
else :
     print("false")
if b % 2 == 0 : print("true")
else :
    print("flase")
#b) Nhập vào số nguyên a, nếu a là số chia hết cho 3 và nằm trong khoảng từ 50 - 100 thì in ra True, ngược lại in ra False
x = int(input())
if x % 3 ==0 and 50 <= x <= 100 : print("true")
else : print("false")