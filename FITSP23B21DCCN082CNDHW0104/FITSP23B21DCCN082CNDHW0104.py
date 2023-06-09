# Họ và tên: Chử Thị Mai
# Mã sinh viên: B21DCCN082
# Nhóm lớp tín chỉ: 06
# Lớp quản lý: D21CQCN10-B
# Bài 04

import numpy as np

H = [[1, 0, 1, 1, 1, 0, 0],
     [0, 1, 0, 1, 1, 1, 0],
     [0, 0, 1, 0, 1, 1, 1]]
rows = len(H)
columns = len(H[0])
c = [1, 1, 0, 1, 0, 0, 0]


def is_zero(arr):
    for i in arr:
        if i:
            return False
    return True


def add(all_col):
    res_v = []
    for i in range(0, len(all_col[0])):
        s = 0
        for column in all_col:
            s = (s + column[i]) % 2
        res_v.append(s)
    return  res_v


def take_column(n):
    res = []
    for row in H:
       res.append(row[n])
    return res


def next_combination(arr):
    last_arr = [i for i in range(columns-len(arr), columns)]
    if arr == last_arr:
        return [0 for i in range(0, len(arr))]
    else:
        for i in range(len(arr)-1, -1, -1):
            if arr[i] < last_arr[i]:
                arr[i] += 1
                for j in range(i, len(arr)):
                    arr[j] = arr[i] + j - i
                break
        return arr


# Tìm dmin dựa theo số cột của ma trận kiểm tra H
def find_dmin():
    s = 1
    res = [0]
    # kiem tra TH dau tien
    check = is_zero(add([take_column(i) for i in res]))
    if check:
        return s

    loop = True
    while loop:
        res = next_combination(res)
        if is_zero(res):
            s += 1
            res = [i for i in range(0, s)]
        check = is_zero(add([take_column(i) for i in res]))
        if check:
            return s
        if s == columns:
            loop = False


# Kiểm tra một vec-tơ cho trước có phải là một vec-tơ mã hợp lệ
def check_correct_code(code):
    H_T = np.array(H, dtype=int).transpose()
    code = np.array(code, dtype=int).transpose()
    code_dot_H_T = np.dot(code, H_T).tolist()
    for i in range(0, len(code_dot_H_T)):
        code_dot_H_T[i] %= 2
    return is_zero(code_dot_H_T)


def binary_generation(arr):
    last_arr = [1 for i in arr]
    if last_arr == arr:
        return -1
    else:
        for i in range(len(arr)-1, -1, -1):
            if arr[i] == 0:
                arr[i] = 1
                for j in range(i+1, len(arr)):
                    arr[j] = 0
                break
        return arr


# Liệt kê các từ mã cho bộ mã
def all_codes():
    codes = []
    code = [0 for i in range(0, columns)]
    while code != -1:
        if check_correct_code(code):
            codes.append(code.copy())
        code = binary_generation(code)
    return codes


def different(code1, code2):
    diff = 0
    for i in range(0, columns):
        if code1[i] != code2[i]:
            diff += 1
    return diff


# Tìm dmin theo định nghĩa
def find_d_min_by_definition(codes):
    size_of_all_codes = len(codes)
    d_min = columns
    for i in range(0, size_of_all_codes):
        for j in range(i+1, size_of_all_codes):
            diff = different(codes[i], codes[j])
            if diff < d_min:
                d_min = diff
    return d_min


# Tìm dmin theo tính chất của mã khối tuyến tính
def find_d_min_by_property(codes):
    d_min = columns
    for code in codes:
        w = sum(code)
        if w < d_min and w != 0:
            d_min = w
    return d_min


all_of_code = all_codes()
print(f"Tìm dmin dựa theo số cột của ma trận kiểm tra H: dmin = {find_dmin()}")
print(f"Kiểm tra vec-tơ c = {c} có phải là một vec-tơ mã hợp lệ không? {check_correct_code(c)}")
print(f"Các từ mã cho bộ mã là: {all_of_code}")
print(f"Tìm dmin theo định nghĩa: dmin = {find_d_min_by_definition(all_of_code)}")
print(f"Tìm dmin theo tính chất của mã khối tuyến tính: dmin = {find_d_min_by_property(all_of_code)}")



