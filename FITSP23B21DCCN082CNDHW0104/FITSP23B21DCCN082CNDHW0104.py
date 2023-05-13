# Họ và tên: Chử Thị Mai
# Mã sinh viên: B21DCCN082
# Nhóm lớp tín chỉ: 06
# Lớp quản lý: D21CQCN10-B
# Bài 04

H = [[1, 0, 1, 1, 1, 0, 0],
     [0, 1, 0, 1, 1, 1, 0],
     [0, 0, 1, 0, 1, 1, 1]]
rows = len(H)
columns = len(H[0])
mark = [0 for i in range(0, columns)]


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


def generation(arr):
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


def find_dmin():
    s = 1
    res = [0]
    # kiem tra TH dau tien
    check = is_zero(add([take_column(i) for i in res]))
    if check:
        return s

    loop = True
    while loop:
        res = generation(res)
        if is_zero(res):
            s += 1
            res = [i for i in range(0, s)]
        check = is_zero(add([take_column(i) for i in res]))
        if check:
            return s
        if s == columns:
            loop = False


print(find_dmin())



