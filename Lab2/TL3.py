#a) Viết đoạn code yêu cầu người dùng nhập vào một số nguyên và kiểm tra xem số đó có lớn hơn 100 hay không.
#Nếu có, in ra "Lớn hơn 100".
x = input()
x_new = int(x)
if x_new > 100:
    print("Lớn hơn 100")

####
a = int(input())
print("<100") if a <100 else print (">100")

#toan tu 3 ngôi
#b = int(input())
#output = b >100 ? ">100" : "=<100"
#print(output)

#b) Viết đoạn code yêu cầu người dùng nhập vào một số nguyên và kiểm tra xem số đó có phải là số chẵn hay không.
#Nếu là số chẵn, in ra "Số chẵn"
c = int(input())
if c % 2 == 0 :
    print("Số chẵn")