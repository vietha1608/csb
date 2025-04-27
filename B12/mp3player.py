class MP3player :
    def __init__(self) :
        self.current_song = None
        self.music_queue = []
    def add_song(self, music_name):
        self.music_queue.append(music_name)
    def play_next_song(self) :
        # kiem tra danh sach con hay khong
        if len(self.music_queue) == 0 :
            return
        self.current_song = None
         # cap nhat lai ten current song
        self.current_song = self.music_queue.pop(0)
    def skip_song(self):
        # kiem tra danh sach con hay khong
        if len(self.music_queue) == 0 :
            self.current_song = None
            return
            # xoa truoc 1 bai hat trong hang doi
        #self.music_queue.pop(0)
            # goi lai ham play_next_song
        self.play_next_song()
# Ví dụ sử dụng:
player = MP3player()
player.add_song("Bài 1")
player.add_song("Bài 2")
player.play_next_song()
player.skip_song()
print(player.current_song)