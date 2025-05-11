#class queue trong python
from queue import Queue

#khai bao
q = Queue()
print(type(q))
#them vao dau sach sach
q.put(1)
q.put(2)
q.put(3)
q.put(4)
#duyet qua phan tu
print(q)#in ra q chi luu gia tri
for item in q.queue:
    print(item)
#xoa : mac dinh xoa o cuoi
print(q.get())
print(q.get())
print("...........")
for item in q.queue:
    print(item)
#len
print("Len:", q.qsize())
#check empty
print("Is empty:", q.empty())
