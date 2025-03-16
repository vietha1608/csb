#ham tra ve index cua phan tu can tim
def linear_search(arr, target):
#duyet qua tung phan tu cua mang
    for index, value in enumerate(arr):
        if value == target:
            print(f"phan tu {target} co trong mang")
            return index
    print(f"phan tu {target} ko co trong mang")
    print("phan tu " + str(target) + "ko co trong mang")
    print("phan tu" ,target, "khong co trong mang")
    return -1
    

print(linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))