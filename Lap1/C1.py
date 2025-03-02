#Viết một chương trình Python cho phép người dùng nhập một số nguyên dương `n`. Chương trình sẽ kiểm tra và in ra:
#- Nếu `n` là số nguyên tố, in `"Đây là số nguyên tố"`
#- Nếu `n` là số chẵn nhưng không phải số nguyên tố, in `"Đây là số chẵn nhưng không phải số nguyên tố"`
#- Nếu `n` là số lẻ nhưng không phải số nguyên tố, in `"Đây là số lẻ nhưng không phải số nguyên tố"`
n =int(input())
def is_prime(n) :
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0 :
                return False
        return True
while n > 0 :
    num = int(input())
    if num > 0 :
        if is_prime(num):
            print("Đây là số nguyên tố")
        else :
             print("ko phải số nguyên tố")
        if n % 2 == 0 :
             print("Đây là số chẵn")
        else :
             print("Đây không phải số chẵn")
