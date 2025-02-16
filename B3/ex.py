# import time
# for sec in range(10, 0, -1) :
#     print(sec)
#     time.sleep(1)
# print("happy new year")
# [CAU 2] ------------------------------------------
# neu nguoi dung nhap y/yes => dung lai => khac thi lam tiep
answer = input("Do you love me? ").lower()
while(not answer in ["y", "yes"]):
    print("Please yessss")
    answer = input("Do you love me? ").lower()
print("Thanks!")