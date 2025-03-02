from QLSV import QLSV
QLSV = QLSV()
while(True) :
    print("\n\tChuong trinh quan ly sinh vien")
    print("1. Them sinh vien")
    print("2. Cap nhat sinh vien")
    print("3. Xoa sinh vien")
    print("4. Tim kiem sinh vien")
    print("5. Sap xep sinh vien theo GPA")
    print("6. Sap xep sinh vien theo ten chuyen nganh")
    print("7. Hien thi danh sach sinh vien")
    print("0. Thoat")
    choice = int(input("Chon chuc nang: "))
    if(choice == 1):
        print("Them sinh vien")
        QLSV.ThemSV()
        print("Them sinh vien thanh cong")
    elif(choice == 2):
        if(QLSV.Soluong() > 0):
            print("Cap nhat sinh vien")
            mssv = input("Nhap ma so sinh vien: ")
            QLSV.updateSV(mssv)
        else:
            print("Danh sach sinh vien rong")
    elif(choice == 3):
        if(QLSV.Soluong() > 0):
            print("Xoa sinh vien")
            mssv = input("Nhap ma so sinh vien: ")
            if(QLSV.deleteByID(mssv)):
                print("Xoa sinh vien thanh cong")
            else:
                print("Khong tim thay sinh vien")
        else:
            print("Danh sach sinh vien rong")
    elif(choice == 4):
        print("Tim kiem sinh vien")
        if(QLSV.Soluong() > 0):
            print("1. Tim kiem theo ma so")
            print("2. Tim kiem theo ten")
            searchChoice = int(input("Chon cach tim kiem: "))
            if(searchChoice == 1):
                mssv = input("Nhap ma so sinh vien: ")
                sv = QLSV.findByID(mssv)
                if(sv != None):
                    print(sv)
                else:
                    print("Khong tim thay sinh vien")
            elif(searchChoice == 2):
                name = input("Nhap ten sinh vien: ")
                sv = QLSV.findByName(name)
                if(len(sv) > 0):
                    for i in sv:
                        print(i)
                else:
                    print("Khong tim thay sinh vien")
            else:
                print("Lua chon khong hop le")
        else:
            print("Danh sach sinh vien rong")
    elif(choice == 5):
        if(QLSV.Soluong() > 0):
            print("Sap xep sinh vien theo GPA")
            QLSV.sortbyScore()
            print("Sap xep thanh cong")
        else:
            print("Danh sach sinh vien rong")
    elif(choice == 6):
        if(QLSV.Soluong() > 0):
            print("Sap xep sinh vien theo chuyen nganh")
            QLSV.sortbyMajor()
            print("Sap xep thanh cong")
        else:
            print("Danh sach sinh vien rong")
    elif(choice == 7):
        if(QLSV.Soluong() > 0):
            print("Danh sach sinh vien")
            print("=" * 100)
            print("{:<5} {:<8} {:<20} {:<10} {:<15} {:<10} {:<10}".format(
                "STT", "MSSV", "Ho Ten", "Gioi Tinh", "Nganh Hoc", "Diem TB", "Hoc Luc"))
            print("=" * 100)
            for sv in QLSV.listSV:
                print(sv)
        else:
            print("Danh sach sinh vien rong")
    elif(choice == 0):
        print("Thoat chuong trinh")
        break
    else:
        print("Lua chon khong hop le")