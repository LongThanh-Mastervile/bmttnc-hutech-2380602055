import re

def tinh_tong_so_trong_chuoi(chuoi):
    cac_so_dang_chuoi = re.findall(r'-?\d+', chuoi)
    
    tong_duong = 0
    tong_am = 0

    for so_str in cac_so_dang_chuoi:
        so_nguyen = int(so_str)
        if so_nguyen > 0:
            tong_duong += so_nguyen
        elif so_nguyen < 0:
            tong_am += so_nguyen
            
    print(f'Chuỗi ban đầu là: "{chuoi}"')
    print(f"Kết quả: Giá trị dương: {tong_duong}. Giá trị âm: {tong_am}.")

if __name__ == "__main__":
    chuoi_vi_du = "-100#^sdfkj8902w3ir021@swf-20"
    tinh_tong_so_trong_chuoi(chuoi_vi_du)