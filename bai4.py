class SinhVien:
	def __init__(self,MSSV,HoTen,MaKhoa):
		self.MSSV = MSSV
		self.HoTen = HoTen
		self.MaKhoa = MaKhoa
	def getMSSV(self):
		return self.MSSV
	def getHoTen(self):
		return self.HoTen
	def getMaKhoa(self):
		return self.MaKhoa
	def setMSSV(self,MSSV):
		self.MSSV = MSSV
	def setHoTen(self,HoTen):
		self.HoTen = HoTen
	def setMaKhoa(self,MaKhoa):
		self.MaKhoa = MaKhoa
	def tostring(self):
		print(self.MSSV," ",self.HoTen," ",self.MaKhoa)
sv = SinhVien("001","Mai A","01")
sv.tostring()
sv1 = SinhVien("002","Tran B","01")
sv1.tostring()
sv2 = SinhVien("003","Van C","02")
sv2.tostring()
sv3 = SinhVien("004","Thi K","001")
sv3.tostring()

class Khoa:
	def __init__(self,MaKhoa,TenKhoa):
		self.MaKhoa = MaKhoa
		self.TenKHoa = TenKhoa
	def getMaKhoa(self):
		return self.MaKhoa
	def getTenKhoa(self):
		return self.TenKhoa
	def setMaKhoa(self,MaKhoa):
		self.MaKhoa = MaKhoa
	def setTenKhoa(self,TenKhoa):
		self.TenKhoa = TenKhoa
	def tostring1(self):
		print(self.MaKhoa," ",self.TenKhoa)
k = Khoa("01","CNTT")
k.tostring1()
k1 = Khoa("02","KToan")
k1.tostring1()
k2 = Khoa("03","CKhi")
k2.tostring1()
k3 = Khoa("04","Nuoi")
k3.tostring1()






