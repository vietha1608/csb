#### **Câu 2 (3 điểm):**

#Viết một chương trình Python thực hiện các thao tác sau:

#1. Yêu cầu người dùng nhập vào một chuỗi chứa nhiều từ, các từ được phân tách bởi dấu phẩy (`,`).
#2. Ghi chuỗi này vào một tệp văn bản có tên `words.txt`.
#3. Đọc lại nội dung từ tệp `words.txt`, sử dụng phương thức `.split(',')` để tách chuỗi thành danh sách các từ.
#4. In danh sách các từ ra màn hình.
#5. Xử lý trường hợp tệp không tồn tại hoặc gặp lỗi khi đọc/ghi.

chuoi = input()
tu = chuoi.split(',')
with open ('/Lap1/words.txt','a') as file :
    file.write(tu)
with open ('/Lap1/words.txt','r') as file :
    file.readlines()
print(tu)
