from student import Sinhvien
class quanlysv:
    def __init__(self):
        self.sinhvien = []
    def themsinhvien(self):
        masv = input("Nhập mã sinh viên: ").upper()
        for sv in self.sinhvien:
            if sv.masv.upper() == masv.upper():
                print("------Đã tồn tại mã sinh viên này")
        tensv = input("Nhập tên sinh viên: ").upper()
        ngaysinh = input("Nhập ngày tháng năm sinh: ")
        toan = float(input("Nhập điểm toán: "))
        van = float(input("Nhập điểm văn: "))
        anh = float(input("Nhập điểm anh"))
        sv = Sinhvien(masv , tensv , ngaysinh , toan, van , anh)
        self.sinhvien.append(sv)
        print("-----Đã lưu sinh viên--------")
    def hienthidanhsach(self):
        for sv in self.sinhvien:
            print(sv)
    def timkiemsv(self):
        masv = input("Nhập mã sinh viên cần tìm: ").upper()
        for sv in self.sinhvien:
            if sv.masv == masv:
                print(sv)
    def xoasv(self):
        masv = input("Nhập mã sinh viên cần tìm: ").upper()
        for sv in self.sinhvien:
            if sv.masv == masv:
                self.sinhvien.remove(sv)
                print("-------Đã xóa sinh viên thành công---------")
    def suasv(self):
        masv = input("Nhập mã sinh viên: ")
        for sv in self.sinhvien:
            if sv.masv.upper() == masv.upper():
                tensv = input("Nhập tên sinh viên mới: ").upper()
                if tensv != "":
                    sv.tensv = tensv
                ngaysinh = input("Nhập ngày sinh mới: ")
                if ngaysinh != "":
                    sv.ngaysinh =ngaysinh
                toan = input("Nhập điểm toán: ")
                if toan != "":
                    sv.toan = toan
                van = input("Nhập điểm van: ")
                if van != "":
                    sv.van = van
                anh = input("Nhập điểm anh: ")
                if anh != "":
                    sv.anh = anh
    def sapxep(self):
        loai = {"giỏi":0,"khá":1,"trung bình":2,"yếu":3}
        self.sinhvien.sort(key=lambda sv:loai[sv.xeploai()],reverse=True)
    def thongke(self):
        thongke = {"giỏi":0,"khá":0,"trung bình":0,"yếu":0}
        for sv in self.sinhvien:
            loai = sv.xeploai()
            if loai in thongke:
                thongke[loai]+=1
        tong = len(self.sinhvien)
        for loai in ["giỏi","khá","trung bình","yếu"]:
            so_luong = thongke.get(loai) 
            ti_le = so_luong*tong/100
            print(f"{loai}:{so_luong}---{ti_le}%")
                
                
                        
        