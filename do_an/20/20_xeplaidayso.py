import itertools
file1 = open("D:\sort_input.txt","r")#đọc file (đặt trong ổ D)
content = file1.read()
content_list = content.split()#tách để tạo list
file1.close()
for i in range(0, len(content_list)):#do list lấy từ file đang ở string nên đổi lại int
    content_list[i] = int(content_list[i])
hv=[]
hv=(list(itertools.permutations(content_list)))#hàm lấy hoán vị
def per():
    for i in hv:
        for j in list(i):
            for k in list(i):
                if((list(i).index(k)-list(i).index(j)>1)):#index phần tử sau lớn hơn trước >=2
                    max=k+j
                    for l in range(list(i).index(j),list(i).index(k)):#xét đoạn giữa của 2 index trên
                        if(2*i[l]==max and i in hv):#kt 2P=M+N 
                            hv.pop(hv.index(i))#xóa hoán vị vi phạm 2P=M+N
                            per()#đệ quy để cập nhật lại phần tử vì số lượng phần tử bị thay đổi
per()
print(hv)
for i in range(0, len(hv)):#đổi int sang string để chuẩn bị ghi ra file
    hv[i] = str(hv[i])
textfile = open("D:\sort_output.txt", "w")#ghi file (đặt trong ổ D)
for element in hv:#ghi từng phần tử ra file
    textfile.write(element+ "\n")
textfile.write(str(len(hv)))#ghi số lượng hoán vị sau khi lọc
textfile.close()
# Input từ file sort_input.txt
# Output ra file sort_output.txt

            
