class Sinhvien:
    def __init__(self, masv , tensv , ngaysinh , toan , van , anh):
        self.masv = masv
        self.tensv = tensv
        self.ngaysinh = ngaysinh
        self.toan = float(toan)
        self.van = float(van)
        self.anh = float(anh)
    def diemTB(self):
        return round((self.toan+self.van+self.anh)/3,3)
    def xeploai(self):
        diem = self.diemTB()
        if(diem >=8.0):
            return "giỏi"
        elif diem<8 and diem >=6.5:
            return "khá"
        elif diem>=5 and diem <6.5:
            return "trung bình"
        elif diem<5:
            return "yếu"
         
    def __str__(self):
        return f"{self.masv} -- {self.tensv} -- {self.ngaysinh} -- {self.toan} -- {self.van} -- {self.anh} -- {self.diemTB()} -- {self.xeploai()}"
    
        