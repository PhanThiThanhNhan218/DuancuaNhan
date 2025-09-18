p = 36
q = 23
e = 5
thong_diep = "PhanThiThanhNhan"

n = p * q
phi = (p - 1) * (q - 1)

def ky_tu_sang_so(text):
    return [ord(c) for c in text]

def ma_hoa_rsa(danh_sach_so, e, n):
    return [pow(so, e, n) for so in danh_sach_so]

so_thong_diep = ky_tu_sang_so(thong_diep)
thong_diep_ma_hoa = ma_hoa_rsa(so_thong_diep, e, n)

print("Thông điệp gốc:", thong_diep)
print("Thông điệp mã hóa:", thong_diep_ma_hoa)