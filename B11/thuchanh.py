class Browser():
    def __init__(self):
        self.backstack = []
        self.forward_stack = []
        self.current_page = None
    #quay lai trang truoc do
    def back(self):
        #*:neu back rong => in: ko co trang de quay ve +> out lam
            if len(self.backstack) == 0:
                return
        #1. them trang hien tai vao danh sach forward
            self.forward_stack.append(self.current_page)
        #2.doi trang hien tai
            self.current_page = self.backstack.pop()
        #3.xoa trang hien tai trong danh sach back
    # di toi trang gan nhat
    def forward(self):
        if len(self.forward_stack) == 0 :
             return
        self.backstack.append(self.current_page)
        self.current_page = self.forward_stack.pop()
    #chuyen trang
    def visit_page(self, url):
        #2.xoa forward
        self.forward_stack.clear()
        #3. them trang quay ve cho back
        self.backstack.append(self.current_page)
        #1. cap nhat gia tri current page
        self.current_page = url
        print(url)
    #--------------
browser = Browser()

browser.visit_page("google.com")
browser.visit_page("facebook.com")
browser.visit_page("youtube.com")

browser.back()     # về facebook.com
browser.back()     # về google.com
browser.forward()  # tới facebook.com
browser.visit_page("wikipedia.org")  # forward_stack sẽ bị xoá
browser.forward()  # không đi tiếp được
print(browser.current_page)