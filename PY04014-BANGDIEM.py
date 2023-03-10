from decimal import ROUND_HALF_UP, Decimal

id = 1
class HocSinh :
    maHS = 'HS'
    diemTrungBinh = 0
    xepLoai = ''
    def __init__(self, ten, diem) :
        global id
        self.maHS += '{:02d}'.format(id)
        id += 1
        self.ten = ten
        x = 2 * diem[0] + 2 * diem[1]
        for i in range(2, 10) :
            x += diem[i]
        x /= 12
        if x < 5 : self.xepLoai = 'YEU'
        elif x < 7 : self.xepLoai = 'TB'
        elif x < 8 : self.xepLoai = 'KHA'
        elif x < 9 : self.xepLoai = 'GIOI'
        else : self.xepLoai = 'XUAT SAC'
        self.diemTrungBinh = x.quantize(Decimal('0.1'), ROUND_HALF_UP)

    def output(self) :
        print(self.maHS, self.ten, self.diemTrungBinh, self.xepLoai)

n = int(input())
a = []
for i in range(n) :
    b = input()
    c = [Decimal(x) for x in input().split()]
    a.append(HocSinh(b, c))

a = sorted(a, key= lambda x : (- x.diemTrungBinh, x.maHS))
for i in a :
    i.output()