''' CÔNG THỨC '''
class CONGTHUC:
    yeutos =[] # yếu tố bao gồm trong công thức
    name="undefined" # tên công thức
    def __init__(self,name ,*yeutos):
        self.name = name
        temp =[]  
        for yeuto in yeutos:
            temp.append(yeuto)
        self.yeutos = temp
    def display (self):  
        print("List: " , self.yeutos)  
    def getTongSo_YeuTo(self):
        return len(self.yeutos)
''' BƯỚC GIẢI'''
class BUOCGIAI:
    yeutogiai = -1
    congthuc=-1
    def __init__(self, yeuto, congthuc):
      self.yeutogiai = yeuto
      self.congthuc = congthuc 

''' MAIN: BÀI TOÁN TAM GIÁC''' 
class BAITOAN_TAMGIAC:
    yeutocanthiets =[] # (thành phần phụ) sử dụng cho chuẩn hóa bước giải
    congthucs = []  # lưu các tri thức (các công thức)
    yeutodabiets =[] # lưu các yếu tố đã biết
    yeutocantim =-1 # chỉ định yếu tố cần tìm
    buocgiais = [] # lưu các bước giải bài toán

    def clear(self):
        self.yeutocanthiets.clear()
        self.yeutodabiets.clear()
        self.yeutocantim =-1
        self.buocgiais.clear()
    def setYeuToCanTim(self, yeuto):
        self.yeutocantim = yeuto
    def setYeuToDaBiets(self,*yeutos):
        self.yeutodabiets =[]
        for yeuto in yeutos:
            self.yeutodabiets.append(yeuto)

    '''themCongThuc(*congthucs): thêm tri thức <*congthucs> vào Bài Toán Tam Giác. '''
    def themCongThuc(self, *congthucs):
        for congthuc in congthucs:
            self.congthucs.append(congthuc)
    ''' getSoYeuToDaBiet_congthuc(congthuc): return số lượng yếu tố đã biết trong <congthuc>. '''
    def getSoYeuToDaBiet_congthuc(self, congthuc):
        count = 0
        for yeuto in congthuc.yeutos:
            if(yeuto in self.yeutodabiets):
                count+=1
        return count
    ''' getYeuToChuaBiet_congthuc(congthuc): trả về yếu tố chưa biết trong <congthuc>'''
    def getYeuToChuaBiet_congthuc(self, congthuc):
        for yeuto in congthuc.yeutos:
            if (yeuto not in self.yeutodabiets):
                return yeuto
        raise ValueError('you got error!')

    ''' getYeuTo_cothetinh(self, congthuc):
            trả về yếu tố có thể kích hoạt
                trả về -1 nếu không tìm được'''
    def getYeuTo_cothetinh(self, congthuc):
        if(self.getSoYeuToDaBiet_congthuc(congthuc)+1 == congthuc.getTongSo_YeuTo() ):
            return self.getYeuToChuaBiet_congthuc(congthuc) 
        return -1
    ''' KichHoat_YeuTo(yeutoCoTheTinh): kích hoạt yếu tố được truyền vào '''
    def KichHoat_YeuTo(self, yeutoCoTheTinh):
        self.yeutodabiets.append(yeutoCoTheTinh)
    ''' themBuocGiai(yeuto, congthuc): thêm một bước giải vào <buocgiai>
            tham số: 
                yeuto: yếu tố cần tính
                congthuc: công thức để tính yeuto '''
    def themBuocGiai(self, yeuto, congthuc):
        self.buocgiais.append((yeuto,congthuc))
    ''' is_Success(): kiểm tra trạng thái đích của bài toán.
            nếu yếu tố cần tìm đã được kích hoạt -> return True
                else: return Flase'''
    def is_Success(self):
        if(self.yeutocantim in self.yeutodabiets):
            return True
        return False
    ''' chuanhoaBuocGiai(congthucdich): loại bỏ các bước giải không cần thiết trong viễa (hàm bổ sung) '''
    def chuanhoaBuocGiai(self, congthucdich):
        # thêm các yếu tố có trong công thức đích vào @yeutocanthiets
        for yeuto in congthucdich.yeutos:
            self.yeutocanthiets.append(yeuto)
        # loại bỏ các bước dư thừa
        for i in range(len(self.buocgiais)-1,-1,-1): # duyệt từ cuối
            if(self.buocgiais[i][0] not in self.yeutocanthiets):
                 del self.buocgiais[i]
            else:
                for yeuto in self.buocgiais[i][1].yeutos:
                    self.yeutocanthiets.append(yeuto)
    '''  GiaiBaiToan(): 
        duyệt từng công thức:
            nếu công thức hiện tại có thể tính được một yếu tố chưa biết:
                thêm bước giải
                thêm yếu tố tính được vào danh sách yếu tố đã biết
                kiểm tra yếu tố cần tìm đã tính được chưa:
                    nếu tính được rồi thì return true
                    nếu chưa tính được thì tiếp tục giải
            else: tiếp tục tới công thức tiếp theo
    '''
    def GiaiBaiToan(self):
        flag = True;
        while (flag):
            flag = False
            for congthuc in self.congthucs:
                yeutoCoTheTinh = self.getYeuTo_cothetinh(congthuc) 
                #print("tính được", yeutoCoTheTinh)
                if (yeutoCoTheTinh != -1):
                    #congthuc.display() # testing
                    self.KichHoat_YeuTo(yeutoCoTheTinh) 
                    self.themBuocGiai(yeutoCoTheTinh, congthuc)
                    flag = True
                    if (self.is_Success()):
                        self.chuanhoaBuocGiai(congthuc)
                        temp = []
                        loigiai = temp
                        for buocgiai in self.buocgiais:
                            loigiai.append("tính " + buocgiai[0] + " thông qua "+ buocgiai[1].name)
                        return loigiai
        return ["bài toán không thể giải, hãy bổ sung thêm thông tin hoặc tri thức"];




if __name__ == "__main__":
    # define names
    canh_a = "cạnh a";
    canh_b = "cạnh b";
    canh_c = "cạnh c";
    goc_A = "góc A";
    goc_B = "góc B";
    goc_C = "góc C";
    nuaChuVi_p = "nửa chu vi";
    dienTich_S = "diện tích";
    trungTuyen_Ma = "trung truyến Ma";
    trungTuyen_Mb = "trung truyến Mb";
    trungTuyen_Mc = "trung truyến Mc";
    duongCao_Ha = "đường cao Ha";
    duongCao_Hb = "đường cao Hb";
    duongCao_Hc = "đường cao Ha";
    bk_NoiTiep_r = "bán kính đường tròn nội tiếp TG r";
    bk_NgoaiTiep_R = "bán kính đường tròn ngoại tiếp TG R";
    # define công thức (tri thức )
    # congthuc1= CONGTHUC("công thức 1", canh_a,canh_b, canh_c, nuaChuVi_p)
    # congthuc2= CONGTHUC("công thức 2", canh_a,canh_b, goc_C, dienTich_S)
    # congthuc3= CONGTHUC("công thức 3",canh_a,canh_b, goc_A, goc_B) 
    # congthuc4= CONGTHUC("công thức 4", canh_a,canh_b, canh_c, goc_C)
    # congthuc5= CONGTHUC("công thức 5", goc_A, goc_B, goc_C)
    # congthuc6= CONGTHUC("công thức 6",nuaChuVi_p,dienTich_S,bk_NoiTiep_r)
    # congthuc7= CONGTHUC("công thức 7",canh_a,canh_c,goc_A,goc_C) 
    # congthuc8= CONGTHUC("công thức 8",canh_a,canh_b, canh_c, nuaChuVi_p, dienTich_S) 
    # congthuc9= CONGTHUC("công thức 9",canh_a,canh_b, canh_c, trungTuyen_Ma)
    # congthuc10= CONGTHUC("công thức 10",canh_a,canh_b, canh_c, trungTuyen_Mb)
    # congthuc11= CONGTHUC("công thức 11",canh_a,canh_b, canh_c, trungTuyen_Mc) 
    # congthuc12= CONGTHUC("công thức 12",canh_a,dienTich_S, duongCao_Ha)
    # congthuc13= CONGTHUC("công thức 13",canh_b,dienTich_S, duongCao_Hb)
    # congthuc14= CONGTHUC("công thức 14",canh_c,dienTich_S, duongCao_Hc) 
    # congthuc15= CONGTHUC("công thức 15",canh_a, canh_b, canh_c, dienTich_S, bk_NgoaiTiep_R)
    # congthuc16= CONGTHUC("công thức 16", duongCao_Hc,canh_b,goc_A)
    # congthuc17= CONGTHUC("công thức 17", canh_b,canh_c, goc_B,goc_C)
    
    congthuc1= CONGTHUC("công thức 1", goc_A, goc_B, goc_C)
    congthuc2= CONGTHUC("công thức 2",canh_a,canh_b, goc_A, goc_B) 
    congthuc3= CONGTHUC("công thức 3", duongCao_Hc,canh_b,goc_A)
    congthuc4= CONGTHUC("công thức 4", canh_b,canh_c, goc_B,goc_C)
    congthuc5= CONGTHUC("công thức 5", canh_a,canh_b, canh_c, nuaChuVi_p)
    congthuc6= CONGTHUC("công thức 6",canh_c,dienTich_S, duongCao_Hc)
    baitoan = BAITOAN_TAMGIAC()
    #1 Thêm tri thức / Input công thức vào hàm themCongThuc(...,...)
    baitoan.themCongThuc(congthuc1,congthuc2,congthuc3,congthuc4,congthuc5,congthuc6)
    #2 input Yếu tố đã biết vào hàm setYeuToDaBiets() và Yếu tố cần tìm vào hàm setYeuToCanTim()
    baitoan.setYeuToDaBiets(goc_A, goc_B, canh_c) 
    baitoan.setYeuToCanTim(dienTich_S)
    loigiais = baitoan.GiaiBaiToan()
    print("Lời Giải: ")
    for loigiai in loigiais:
        print(loigiai)
    baitoan.clear()
    loigiais =[]
    
    

##  ##   ## THE END ##   ## ##   

''' v0.1 
bước 1: duyệt từng công thức, nếu thấy công thức có thể tính ra được yếu tố nào đó thì thực hiện bước giải. tiếp tục lặp lại cho đến khi yếu tố cần tìm được kích hoạt

bước 2: chuẩn hóa các bước giải (loại bỏ các bước giải không cần thiết để trả về lời giải ngắn hơn (cách này vẫn chưa tối ưu, để tối ưu: xem semantic v0.2))
'''