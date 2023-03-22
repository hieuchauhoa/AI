//nguoi dung nhap input, thay doi input trong ham main

#include<iostream>
#define maxn 100
using namespace std;

int main(){
	int a[10]={2,8,11,3,5,9,10,4,17,6};
	int l[10],p[10];
	
	l[0]=1;		//gán luôn khoi chay a[1]
	p[0]=0;		//nhu trên
	
	for(int i=1;i<10;i++)	//chay het các ptu a[]
	{
		int maxai=0;
		int nho;
		
		for(int j=0;j<i;j++)	// vói mõi thang a[i], chay lai tu a[0] toi a[i-1]
		{
			if(a[j]<a[i])    //neu giá tri thang chay lai, nho hon thang a[i]
			{
				if(maxai<=l[j]) //neu l[] nó lon hon cac ptu chay lai, thi cho nó dô max de xét típ, và nho thang j 
				{
					maxai=l[j]; //cho do max
					nho=j; //nhó thàng j
				}
			}	
		}
		l[i]=l[nho]+1;		//chay xong thi se tìm duoc vi trí nho mà tai dó thõa: 1. a[j]<a[i dang xét]	2.L[j] lón nhát
		p[i]=nho;			//cho cái vi trí vào mãng p
	}
	

	
	
	
	int maxtam=0,nho2;
	for(int i=0;i<10;i++)  //dòng for de tìm L[i] lón nhat trong KQ
	{
		if(maxtam<l[i])
		{
			maxtam=l[i];
			nho2=i;		//láy vi trí chõ lón nhat luon
		} 
	}
	

	
	while(1)
	{
		if(nho2==0)  // dieu kiên d?ng cua dong while (neu p[i]=0 thì d?ng)
		{
			cout<<a[nho2];
			break;	
		} 
		cout<<a[nho2]<<" ";  //xuát gia tri tai vi trí lón nhát( dong for phía tren)
		nho2=p[nho2];		//mõi làn lap se dua vi tri nho trong mãng p cho vao nho2
		
	}
	
}