from itertools import combinations


class Polynomial:
    def __init__(self, poly: list):
        self.poly = poly
        self.degree = self.find_degree()

    def find_degree(self):
        try:
            return self.poly[-1]
        except:
            return 0

    def print_poly(self):
        check = False
        for i in self.poly:
            if i == 0:
                print("1", end=" ")
                check = True
            elif i == 1:
                if check:
                    print("+", end=" ")
                print("x", end=" ")
                check = True
            else:
                if check:
                    print("+", end=" ")
                print(f"x^{i}", end=" ")
                check = True

    def rotate_right(self, k: int):
        for i in range(0, len(self.poly)):
            self.poly[i] += k

    def rotate_left(self, k: int):
        for i in range(0, len(self.poly)):
            self.poly[i] -= k

    def __copy__(self):
        new_poly = Polynomial(self.poly.copy())
        return new_poly


def subtract_poly(subtrahend, minus_num):
    res = set(subtrahend).symmetric_difference(set(minus_num))
    return list(res)


def divide_poly_return_surplus(dividend, divisor):
    dividend_copy = dividend.__copy__()
    divisor_copy = divisor.__copy__()
    mul = dividend_copy.degree - divisor_copy.degree
    divisor_copy.rotate_right(mul)
    surplus = Polynomial(subtract_poly(dividend_copy.poly, divisor_copy.poly))
    if surplus.degree >= divisor_copy.degree:
        divisor_copy.rotate_left(mul)
        return divide_poly_return_surplus(surplus, divisor)
    else:
        return surplus


def divide_poly_return_quotient(dividend, divisor):
    dividend_copy = dividend.__copy__()
    divisor_copy = divisor.__copy__()
    res = Polynomial([])
    res.poly = set(res.poly)
    mul = dividend_copy.degree - divisor_copy.degree
    while mul >= 0:
        mul = dividend_copy.degree - divisor_copy.degree
        divisor_copy.rotate_right(mul)
        if mul >= 0:
            res.poly.add(mul)
        dividend_copy = Polynomial(subtract_poly(dividend_copy.poly, divisor_copy.poly))
        divisor_copy.rotate_left(mul)
    res.poly = list(res.poly)
    return res


# Kiểm tra một đa thức cho trước có phải tối giản hay không
def is_irreducible_poly(poly):
    degree = poly.degree
    for i in range(1, degree+1):
        for j in list(combinations(list(range(0, degree)), i)):
            if sum(j) == 0:
                continue
            sur = divide_poly_return_surplus(poly, Polynomial(list(j)))
            if len(sur.poly) == 0:
                return False
    return True


# Liệt kê tất cả các đa tức tối giản (bất khả quy) bậc k
def get_all_irreducible_polynomials(k0):
    all = []
    for i in range(1, k0 + 2):
        all += list(combinations(range(0, k0 + 1), i))
    all = [list(item) for item in all]
    all = [item for item in all if item[-1] == k0]
    for poly in all:
        p = Polynomial(poly)
        if is_irreducible_poly(p):
            p.print_poly()
            print()


# Liệt kê tất cả các nhân tử (ước số) phân biệt của x^n+1
def get_distinct_factors(n0):
    poly = Polynomial([0, n0])
    list_poly = [Polynomial([0])]
    for i in range(1, n0 + 1):
        for j in list(combinations(list(range(0, n0)), i)):
            if sum(j) == 0:
                continue
            p = list(j)
            sur = divide_poly_return_surplus(poly, Polynomial(p))
            if len(sur.poly) == 0:
                poly_factor = Polynomial(p)
                list_poly.append(poly_factor.__copy__())
    list_poly.append(Polynomial([0, n0]))
    return list_poly


# Phân tích x^n+1 thành các nhân tử tối giản
def factorize_polynomial(n0):
    print(f"1 + x^{n0} =", end=" ")
    have_mul = False
    list_poly = get_distinct_factors(n0)
    list_poly = [poly for poly in list_poly[1:-1] if is_irreducible_poly(poly)]
    for poly in list_poly:
        sur = Polynomial([])
        res = Polynomial([0, n0])
        count = 0
        p = poly.__copy__()
        while len(sur.poly) == 0:
            sur = divide_poly_return_surplus(res, p)
            res = divide_poly_return_quotient(res, p)
            if len(sur.poly) == 0:
                count += 1
        if have_mul:
            print("*", end=" ")
        if count == 1:
            print("( ", end="")
            poly.print_poly()
            print(")", end=" ")
            have_mul = True
        elif count > 1:
            print("( ", end="")
            poly.print_poly()
            print(f")^{count}", end=" ")
            have_mul = True
    print()


k = int(input("k = "))
n = int(input("n = "))
print(f"Tất cả các đa thức tối giản bậc {k} là:")
get_all_irreducible_polynomials(k)
print(f"Phân tích x^{n}+1 thành các nhân tử tối giản:")
factorize_polynomial(n)
print(f"Các ước số phân biệt của x^{n}+1 là:")
list_of_poly = get_distinct_factors(n)
for poly in list_of_poly:
    poly.print_poly()
    print()
