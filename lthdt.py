
import os
import pickle


class NhanVien:
    def __init__(self, fullname, age, wage):
        self.hoten = fullname
        self.tuoi = age
        self.luong = wage

    def __str__(self):
        nv = "# Họ Tên : " + self.hoten + "\n tuổi : " + str(self.tuoi) + "\n Lương : " + str(self.luong)
        return nv

    def __gt__(self, obj):
        return (self.tuoi > obj.tuoi)

    def __ge__(self, obj):
        return (self.tuoi >= obj.tuoi)

    def __lt__(self, obj):
        return (self.tuoi < obj.tuoi)

    def __le__(self, obj):
        return (self.tuoi <= obj.tuoi)

    def __eq__(self, obj):
        return (self.tuoi == obj.tuoi)


def nhap_nhan_vien():
    nv = []
    n = int(input("nhập số nhân viên :"))
    for i in range(n):
        a = input("mời nhập họ tên nhân viên :")
        b = int(input("mời nhập tuổi nhân viên :"))
        c = int(input("mời nhập lương nhân viên :"))
        nv.append(NhanVien(a, b, c))
    return nv


def in_list_nhan_vien(nv):
    for item in nv:
        print(item)


def sx_list_nhan_vien(nv):
    sv = sorted(nv, reverse=True)
    for i in sv:
        print(i)


def luu_list_nv(nv, tm, ten_tt):
    luu = open(os.path.join(tm, ten_tt), "wb")
    pickle.dump(nv, luu)
    luu.close()
    print('lưu list1 thành công')


def doc_list_nv(nv, tm, ten_tt):
    f = open(os.path.join(tm, ten_tt), 'rb')
    doc1 = f.read()
    print('đọc thành công')
    print(doc1)
    f.close()


def main():
    tm = 'F:\data'
    ten_tt = 'list1'
    nv = nhap_nhan_vien()
    in_list_nhan_vien(nv)
    sx_list_nhan_vien(nv)
    luu_list_nv(nv, tm, ten_tt)
    doc_list_nv(nv, tm, ten_tt)


if __name__ == "__main__":
    main()