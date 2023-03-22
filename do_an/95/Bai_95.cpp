//BUY.inp de lay du lieu và BUY.out de xuat ket qua
#include <iostream.h>

using namespace std;

int a[100],b[100],take[100],m,n,pos;

int timNextMin(int b[], int n, int min)
{
	int posMin=0, value=2000;
	for(int i=0;i<n;i++){
		if(b[i]>min && b[i]<value){			
				value = b[i];
				posMin = i;
		}			
	}		
	return posMin;
}
int muaHang(int a[], int b[],int take[],int m, int n, int pos)
{
    if (m == 0)
        return 0;
    if (take[pos]==a[pos]){
		pos=timNextMin(b,n,b[pos]);
		return muaHang(a,b,take,m,n,pos);
    }       
    else{
    	take[pos] = take[pos] + 1;
    	return b[pos]+ muaHang(a, b,take,m - 1, n,pos);
    }        
}
void ghiFile(int take[], int total, int &n)
{
	FILE *f=fopen("BUY.out","wt");
	fprintf(f,"%d\n",total);
	for(int i=0;i<n;i++)
	{
		fprintf(f,"%d\n",take[i]);
	}
	fclose(f);
}
void docFile(int a[],int b[], int &m, int &n)
{
	FILE *f;
	int row=0;
	f=fopen("BUY.inp","rt");
	fscanf(f,"%d",&m);
	fscanf(f,"%d",&n);
	while(!feof(f))
	{
		if(fgetc(f)!=13)
		{
			fscanf(f,"%d",&a[row]);
			fscanf(f,"%d",&b[row]);
			row++;
		}
	}	
	n=row;
	fclose(f);	
}
int main()
{	
	int minValue,minPos;
	docFile(a,b,m,n);
	for(int i=0;i<n;i++)
	if(b[i]<b[i+1]){
		minValue=b[i];
		minPos = i;
	}		
	int total = muaHang(a,b,take,m,n,minPos);
	ghiFile(take,total,n);
	return 0;
}
