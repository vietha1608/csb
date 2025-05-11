#chu y: vao truoc -ra truoc(FIFO-first in, first out)
#khai bao danh sach queue
queue = [1 , 2, 3, 4]
#lay phan tu dau tieu trong queue
print(queue[0])
#enqueue: them phan tu vao cuoi danh sach
queue.append(5)
print(queue)
#dequeue: xoa phan tu dau tien (pop(0))
queue.pop(0)
print(queue)
#kiem tra rong bang len
def is_empty(queue):
    return len(queue) == 0
print(is_empty(queue))