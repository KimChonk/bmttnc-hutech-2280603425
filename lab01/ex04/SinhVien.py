class SinhVien:
    def __init__(self, stt, mssv, hoten, gioitinh, nganh, diemTB):
        self._stt = stt
        self._mssv = mssv
        self._hoten = hoten
        self._nganh = nganh
        self._gioitinh = gioitinh
        self._diem = diemTB
        self._hocluc = ""
        
    def __str__(self):
        return "{:<5} {:<8} {:<20} {:<10} {:<15} {:<10} {:<10}".format(
            self._stt,
            self._mssv,
            self._hoten,
            self._gioitinh,
            self._nganh,
            self._diem,
            self._hocluc
        )