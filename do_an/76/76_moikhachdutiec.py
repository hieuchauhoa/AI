from xml.etree.ElementTree import tostring
a=[]#list để thực hiện tính toán
d=[]#list tạm để tạo bộ cho list a
file1 = open("D:\guest_input.txt","r")#đọc file (đặt trong ổ D)
for x in file1:#xét từng dòng trong file
    for j in x.split():#bỏ xuống dòng
        j=int(j)#đổi string sang int để tiện cho việc tính toán đằng sau
        d.append(j)#thêm j vào list d mà mỗi dòng có 2 j nên d có 2 phần tử
    a.append(d)#list a thêm list d vào
    d=[]#d lại trở thành rỗng để tiếp tục ghép bộ 2
print(a)
# a=[[2,9],[3,7],[4,8],[0,10],[4,2],[5,11],[6,6],[6,4],[4,6],[9,6]]
h=[]#list để chứa độ vui của tất cả các thành viên
out=[]#list chứa các thành viên có độ vui cao nhất
for i in a:#tạo list h
    for j in range(0,1):
        h.append(i[1])
print(h)
def kt():
    dem=0
    for i in h:
        if(i<0):
            dem+=1
    if(dem==len(h)):
        return dem
    else:
        return 0
def bai76():
    global tong#tong để tính tổng độ vui của các tv có độ vui cao nhất
    for i in a:
        if(i[1]==max(h)):#xét các thành viên có độ vui cao nhất
            if(h[i[0]-1]==-2):#nếu người quản lý mình đi dự tiệc thì tự loại bản thân
                h[h.index(max(h))]=-1
                a[a.index(i)]=[-1,-1]
            elif((i[0]!=-2)and kt()!=len(h)):#nếu mình chưa bị loại và tất cả mọi người chưa bị loại
                out.append(a.index([i[0],i[1]])+1)#thêm vào người hài nhất
                tong=tong+i[1]
                h[h.index(max(h))]=-2#sau đó loại bản thân khỏi danh sách
                if(i[0]!=0):#nếu không phải là chủ tịch 
                    h[i[0]-1]=-1 #thì loại người quản lý mình 
                    a[i[0]-1]=[-1,-1]
                    a[a.index(i)]=[-2,-2]#sau đó tự loại bản thân
                else:#nếu là chủ tịch thì không loại người khác
                    a[a.index(i)]=[-2,-2]#sau đó tự loại bản thân
tong=0
for i in h:#cho quá trình lặp đến khi tất cả các thành viên đều được xét qua
    if(i>0):
        bai76();
print(out)     
print(tong)  
out.sort()#sắp xếp lại cho giống với đề 
for i in range(0, len(out)):#đổi int sang string để chuẩn bị ghi ra file
    out[i] = str(out[i])
textfile = open("D:\guest_output.txt", "w")#ghi file (đặt trong ổ D)
textfile.write(str(len(out))+" ")
textfile.write(str(tong)+"\n")
for element in out:#ghi từng phần tử ra file
    textfile.write(element+ "\n")
textfile.close()
# Input từ file guest_input.txt
# Output ra file guest_output.txt

