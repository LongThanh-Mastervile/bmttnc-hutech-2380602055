import itertools

def liet_ke_hoan_vi(danh_sach):
    print(f"Danh sách ban đầu: {danh_sach}")
    tat_ca_hoan_vi = list(itertools.permutations(danh_sach))
    
    print(f"Có tổng cộng {len(tat_ca_hoan_vi)} hoán vị:")
    for hv in tat_ca_hoan_vi:
        print(hv)

if __name__ == "__main__":
    my_list = [1, 2, 3]
    liet_ke_hoan_vi(my_list)