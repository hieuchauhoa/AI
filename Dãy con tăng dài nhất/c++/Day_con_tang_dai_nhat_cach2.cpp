//nguoi dung nhap input, thay doi input trong ham main

#include<iostream>
#define maxn 100
using namespace std;

int main(){
	int a[10]={2,8,11,3,5,9,10,4,17,6};
	int l[10],p[10];
	
	l[0]=1;		//g�n lu�n khoi chay a[1]
	p[0]=0;		//nhu tr�n
	
	for(int i=1;i<10;i++)	//chay het c�c ptu a[]
	{
		int maxai=0;
		int nho;
		
		for(int j=0;j<i;j++)	// v�i m�i thang a[i], chay lai tu a[0] toi a[i-1]
		{
			if(a[j]<a[i])    //neu gi� tri thang chay lai, nho hon thang a[i]
			{
				if(maxai<=l[j]) //neu l[] n� lon hon cac ptu chay lai, thi cho n� d� max de x�t t�p, v� nho thang j 
				{
					maxai=l[j]; //cho do max
					nho=j; //nh� th�ng j
				}
			}	
		}
		l[i]=l[nho]+1;		//chay xong thi se t�m duoc vi tr� nho m� tai d� th�a: 1. a[j]<a[i dang x�t]	2.L[j] l�n nh�t
		p[i]=nho;			//cho c�i vi tr� v�o m�ng p
	}
	

	
	
	
	int maxtam=0,nho2;
	for(int i=0;i<10;i++)  //d�ng for de t�m L[i] l�n nhat trong KQ
	{
		if(maxtam<l[i])
		{
			maxtam=l[i];
			nho2=i;		//l�y vi tr� ch� l�n nhat luon
		} 
	}
	

	
	while(1)
	{
		if(nho2==0)  // dieu ki�n d?ng cua dong while (neu p[i]=0 th� d?ng)
		{
			cout<<a[nho2];
			break;	
		} 
		cout<<a[nho2]<<" ";  //xu�t gia tri tai vi tr� l�n nh�t( dong for ph�a tren)
		nho2=p[nho2];		//m�i l�n lap se dua vi tri nho trong m�ng p cho vao nho2
		
	}
	
}