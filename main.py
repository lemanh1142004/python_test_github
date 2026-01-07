from quanly import quanlysv
def main():
    ql = quanlysv()
    while(True):
        print("0: Kết thúc chương trình")
        print("1: thêm sinh viên")
        print("2 : hiển thị danh sách sinh viên")
        print("3: tìm kiếm sinh viên")
        print("4: xóa sinh viên")
        print("5: sửa sinh viên")
        print("6: sắp xếp sinh viên theo học lực")
        print("7: thống kê sinh viên")
        n = input("Nhập hành động tương ứng")
        if n == '0':
            return
        elif n == '1':
            ql.themsinhvien()
        elif n == '2':
            ql.hienthidanhsach()
        elif n == '3':
            ql.timkiemsv()
        elif n == '4':
            ql.xoasv()
        elif n == '5':
            ql.suasv()
        elif n =='6':
            ql.sapxep()
        elif n == '7':
            ql.thongke()
if __name__ == "__main__":
    main()