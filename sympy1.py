

from sympy import *

def giai_he_pt():
    x, y, z = symbols('x y z')
    a = 2 * x - 5 * y + z + 5
    b = 4 * x + 2 * y - 2 * z - 2
    c = x + y - z
    eq1 = Eq(a, 0)
    eq2 = Eq(b, 0)
    eq3 = Eq(c, 0)
    ghpt = solve((eq1, eq2, eq3), (x, y, z))
    print("nghiệm của hệ pt là:", ghpt)


def tinh_gioi_han():
    x = symbols('x')
    f = ((x ** 3) - 3 * (x ** 2)) ** (1 / 3) + sqrt(x ** 2 - 2 * x)
    gh = limit(f, x, oo)
    print('Kết quả giới hạn của: ', f, "là\n", gh)

def tinh_dao_ham():
    x = symbols('x')
    f = (2 * x - 1) / (x + 2)
    dh = diff(f, x)
    print("ĐẠO HÀM CỦA ", f, "LÀ\n", dh)


def tinh_nguyen_ham():
    x = symbols('x')
    f = x / ((x ** 2) + 2)
    nh = integrate(f, x)
    print("nguyên hàm CỦA ", f, "LÀ\n", nh)

def tinh_tich_phan():
    x = symbols('x')
    f = (1 - x * tan(x)) / (x * x * cos(x) + x)
    tp = integrate(f, (x, (pi), ((2 * pi) / 3)))
    print("tích phân CỦA ", f, "LÀ\n", tp)

def main():
    giai_he_pt()
    tinh_gioi_han()
    tinh_dao_ham()
    tinh_nguyen_ham()
    tinh_tich_phan()


if __name__ == "__main__":
    main()
