//input lay tu file greendy.txt, output ra man hinh
#include<stdio.h>

 
int ary[10][10],co_cua_dong[10],n,cost=0;
void takeInput();
void khoitao();
void tsp(int nut);
int least(int nut);


int main()
{
	khoitao();
 
	printf("\n Duong di: \n ");
	tsp(0); 
	
 	printf("\n Chi phi: %d\n",cost);


 
return 0;
}


void khoitao()
{
	
	FILE * fp = NULL;
	fp = fopen("./greendy.txt", "r");
	
	if (!fp)  {printf("%s","File khong ton tai\n");exit(1);}
	
	fscanf(fp, "%d",&n);  //lay chieu dai mang
	
	int i,j;
 	for(i = 0; i < n; i++)
 	{
 		
    	for(j = 0; j < n; j++)
		{
     		fscanf(fp, "%d",&ary[i][j]);   //dua data tu file vao mang
    	} 
    	co_cua_dong[i]=0;   //gan co cho 1 dong
	}
  
  for( i=0;i < n;i++)		//xuat mang
	{
		printf("\n");
		for(j=0;j < n;j++)
			printf("\t%d",ary[i][j]);
	}
	printf("\n");
 
}



void tsp(int nut)
{
	int i,nut2;
 
	co_cua_dong[nut]=1;  //dungwj co dong da chay
 
	printf("%d--->",nut+1);
	nut2=least(nut);
 
	if(nut2==999)
	{
		nut2=0;
		printf("%d",nut2+1);
		cost+=ary[nut][nut2];
 
		return;
	}
 
	tsp(nut2);
}


 
int least(int nut)
{
	int i,nc=999;
	int min=999,kmin;
 
	for(i=0;i < n;i++)
	{
		if((ary[nut][i]!=0)&&(co_cua_dong[i]==0))  //neu o do khac khong va chua chay qua dong nay
			if(ary[nut][i]< min) //so sanh ptu dang xet voi min
			{
				min=ary[nut][i];  //neu nho hon thi cho vao min
				nc=i;				//nho vi tri 
			}
	}
 
 	if(min!=999)
	cost+=min;
 
return nc;
}
 