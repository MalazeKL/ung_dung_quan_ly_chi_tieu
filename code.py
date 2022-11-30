def check(chi_tieu):
    for i in range(len(chi_tieu)):
        print("    danh sách chi tiêu số {số}: ".format(số = i+1))
        for thong_tin in chi_tieu[0]:
            print(thong_tin, ":", chi_tieu[i][thong_tin])
def add(chi_tieu, khoan_chi):
    chi_tieu.append(khoan_chi)
def remove(chi_tieu):
    name = input("Nhập tên ds chi tiêu muốn xóa: ")
    for index in range(len(chi_tieu)):
        if chi_tieu[index]['tên'] == name:
            chi_tieu.remove(chi_tieu[index])
            break
    print("ĐÃ XÓA!")
chi_tieu = []
while True:
    request = input("nhập yêu cầu của bạn(add/remove/check): ")
    if request.lower() == "check":
        check(chi_tieu)
    elif request.lower() == "add":
        tên = input("Nhập tên chi tiêu: ")
        số = int(input("Nhập sô chi tiêu: "))
        ngày = input("Nhập ngày tháng năm chi: ")
        khoan_chi = {
            'tên': tên,
            'số chi': số,
            'ngày chi': ngày,
        }
        add(chi_tieu, khoan_chi)
    elif request.lower() == "remove":
        remove(chi_tieu)
    else:
        print("lệnh không hợp lệ!")
    yn = input("Bạn muốn tiếp tục không (y/n): ")
    if yn.lower() == "n":
        break
