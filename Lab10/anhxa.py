# Bai 1: doi GPA he 10/ 4
danh_sach_diem = [5.0, 6.5, 7.0, 8.0, 9.0, 10.0]
#def doi_gpa_he_10_4(danh_sach_diem):
#     # todo
#     for diem in range(len(danh_sach_diem)):
#         print(diem)
#         danh_sach_diem[diem] = 4 *danh_sach_diem[diem] / 10
#     return danh_sach_diem
# print(doi_gpa_he_10_4(danh_sach_diem))
#su dung map
danh_sach_diem_map = map(lambda gpa: gpa/10 * 4, danh_sach_diem)
print(list(danh_sach_diem_map))

student = ["Hieu", "My Anh", "Tuan Anh"]
student_upper = map(str.upper, student)
print(list(student_upper))