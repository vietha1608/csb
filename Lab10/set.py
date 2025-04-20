arr1 = [1,2,3]
arr2 = [6,2,10]
# gop 2 arr
arr3 = arr1 + arr2
# sap xep danh sach
arr3.sort()
# loc phan tu bi trung
# chuyen kieu du lieu cho arr3 thanh set
arr3 = set(arr3)
print(arr3)
# In tung phan tu trong set arr3
for phantu in arr3:
    print(phantu)
#  Them phan tu '12' vao arr3 (add)
arr3.add(12)
# Gop set {7,8,9} vao arr3 (update)
arr3.update({7, 8, 9})
print(arr3)
# Xoa phan tu 10 (remove)
arr3.remove(10)
# xoa phan tu 15 (discard)
arr3.discard(15)
print(arr3)