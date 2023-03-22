from collections import deque
# Input nhập trực tiếp từ bàn phím
n=int(input("nhập số pt: "))
a=[]
for i in range(0, n):
	ele = int(input())
	a.append(ele) # thêm số vào mảng
print(a)
global l
l = [1 for _ in range(n)]
global p
p = [-1 for _ in range(n)]
for i in range(1, n):
        for j in range(i):
            if a[j] < a[i]:                
                if l[j] + 1 > l[i]:
                    l[i] = l[j] + 1
                    p[i] = j
#truy vết
max_length = max(l)
finish = l.index(max_length) 
sub_seq = deque()
while not p[finish] == -1:
	sub_seq.append(a[finish])
	finish = p[finish]  
sub_seq.append(a[finish])
sub_seq.reverse()#append theo thứ tự giảm dần nên reverse lại
print("dãy con tăng dài nhất:")
print(sub_seq)