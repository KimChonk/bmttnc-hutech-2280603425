from SinhVien import SinhVien
class QLSV:
    listSV = []
    def generateID(self):
        maxId = 1
        if (self.Soluong() > 0):
            maxId = self.listSV[0]._mssv
            for sv in self.listSV:
                if (sv._mssv > maxId):
                    maxId = sv._mssv
            maxId += 1
        return maxId
    def Soluong(self):
        return self.listSV.__len__()
    def ThemSV(self):
        mssv = input("Nhap ma so sinh vien: ")
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh: ")
        major = input("Nhap nganh hoc: ")
        score = float(input("Nhap diem trung binh: "))
        stt = self.Soluong() + 1
        sv = SinhVien(stt, mssv, name, sex, major, score)
        self.listSV.append(sv)
        self.HocLuc(sv)
    def updateSV(self, mssv):
        found = False
        for sv in self.listSV:
            if (sv._mssv == mssv):
                name = input("Nhap ten sinh vien: ")
                sex = input("Nhap gioi tinh: ")
                major = input("Nhap nganh hoc: ")
                score = float(input("Nhap diem trung binh: "))
                sv._hoten = name
                sv._gioitinh = sex
                sv._nganh = major
                sv._diem = score
                self.HocLuc(sv)
                found = True
                print("Cap nhat thong tin sinh vien thanh cong!")
                break
        if not found:
            print("Khong tim thay sinh vien")
    def sortByID(self):
        self.listSV.sort(key=lambda x: x._mssv, reverse=False)
    def sortByName(self):
        self.listSV.sort(key=lambda x: x._hoten, reverse=False)
    def sortbyScore(self):
        self.listSV.sort(key=lambda x: x._diem, reverse=True)
    def sortbyMajor(self):
        self.listSV.sort(key=lambda x: x._nganh, reverse=False)
    def findByID(self, mssv):
        SearchRersult = None
        if(self.Soluong() > 0):
            for sv in self.listSV:
                if(sv._mssv == mssv):
                    SearchRersult = sv
                    break
        return SearchRersult
    def findByName(self, name):
        SearchRersult = []
        if(self.Soluong() > 0):
            for sv in self.listSV:
                if(name.upper() in sv._hoten.upper()):
                    SearchRersult.append(sv)
        return SearchRersult
    def updateSTT(self):
        for i in range(len(self.listSV)):
            self.listSV[i]._stt = i + 1
    def deleteByID(self, mssv):
        isDeleted = False
        sv = self.findByID(mssv)
        if(sv != None):
            self.listSV.remove(sv)
            self.updateSTT()
            isDeleted = True
        return isDeleted
    def HocLuc(self, sv):
        if (sv._diem >= 8):
            sv._hocluc = "Gioi"
        elif (sv._diem >= 6.5):
            sv._hocluc = "Kha"
        elif (sv._diem >= 5):
            sv._hocluc = "Trung Binh"
        else:
            sv._hocluc = "Yeu"
    def show(self):
        print("{:<5} {:<8} {:<20} {:<10} {:<15} {:<10} {:<10}".format(
            "STT", "MSSV", "Ho Ten", "Gioi Tinh", "Chuyen Nganh", "Diem TB", "Hoc Luc"
        ))
        print("-" * 85)
        for sv in self.listSV:
            print(sv)
        print("\n")
    def getListSV(self):
        return self.listSV