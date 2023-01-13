import random
import os
import pickle


def sinh_list_nn():
    list1 = []
    n = abs(int(input("mời nhập số phần tử của list :")))
    print("mời nhập giá trị khoảng [a,b]")
    a = float(input("a ="))
    b = float(input('b ='))

    for i in range(n):
        snn = (b - a) * random.random() + a
        list1.append(snn)

    return list1


def sap_sep(list1):
    r = input('mời nhập true hoặc false :\n')

    while r != 'true' and r != 'false':
        r = input('mời nhập lại true hoặc false :\n')

    if r == "true":
        print("list1 sắp xếp theo chiều tắng dần\n")
        sx = sorted(list1, reverse=False)
        print(sx)

    elif r == "false":
        print("list1 sắp xếp theo chiều giảm dần\n")
        sx1 = sorted(list1, reverse=True)
        print(sx1)


def tim_n_trong_list(list1):
    ketqua = []
    x = float(input("Mời nhập 1 số bất kì trong list1 khi chưa sắp xếp :"))
    for i in range(0, len(list1)):
        if (list1[i] == x):
            ketqua.append(i)

    if len(ketqua) > 0:
        print("Vị trí xuất hiện của", x, "là:", ketqua)

    else:
        print("Không tìm thấy !")


def luu_tap_tin(tm, ten_tt, list1):
    k = input('mời nhập wb hoặc w :\n ')
    while k != 'wb' and k != 'w':
        k = input('mời nhập lại wb hoặc w :\n')

    if k == 'wb':
        luu = open(os.path.join(tm, ten_tt), "wb")
        pickle.dump(list1, luu)
        luu.close()
        print('lưu list1 thành công')
    elif k == "w":
        luu = open(os.path.join(tm, ten_tt), "w")
        luu.writelines(str(list1))
        luu.close()
        print('lưu list1 thành công')


def main():
    list1 = sinh_list_nn()
    print("list1 =", list1)

    sx = sap_sep(list1)
    print(sx)

    tim_n_trong_list(list1)

    tm = 'F:\data'
    ten_tt = 'list1'
    luu_tap_tin(tm, ten_tt, list1)


if __name__ == "__main__":
    main()

