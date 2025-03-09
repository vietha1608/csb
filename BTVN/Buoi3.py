class Taikhoan:
    def __init__ (self, ten, so_du, stk):
        self.__ten = ten
        self.__so_du = so_du
        self.__stk = stk
    def rut_tien(self, so_tien):
        self.__so_du = self.__so_du - so_tien
    def nap_tien(self,so_tien):
        self.__so_du = self.__so_du + so_tien
    def get_so_du(self):
        return self.__so_du
    def set_so_du(self, so_du_moi):
        self.__so_du = so_du_moi
    def lay_so_du(self):
        print(self.__so_du)

class TaiKhoanTietKiem(Taikhoan):
    def __init__ (self,lai_suat, so_du, stk, ten):
        super().__init__(ten=ten, so_du=so_du, stk=stk)
        self.lai_suat = lai_suat
    def tinh_lai_suat(self):
        self.set_so_du (so_du_moi=self.get_so_du()*(1+self.lai_suat/100))
stk1 = TaiKhoanTietKiem(6.7, 1000,"0xx01xx1", "Vox")
stk1.nap_tien(so_tien=1000)
stk1.rut_tien(so_tien=10)
stk1.tinh_lai_suat()
stk1.lay_so_du()