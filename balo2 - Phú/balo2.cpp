//lay du lieu tu file input, xuat ket qua vao file output
#include<iostream.h>
#define maxn 1000
#define maxM 10000
int a[maxn],c[maxn],f[maxn][maxM];
int n,M;
void input()
{
	FILE *fi;
	fi=fopen("input.txt","rt");
		fscanf(fi,"%d%d",&n,&M);
	for(int i=1;i<=n;i++)
		fscanf(fi,"%d%d",&a[i],&c[i]);
	fclose(fi);
}
void mofile(char a[maxn],int &m, char	tenfile[maxn]){
	 
 	FILE * fp = NULL;   	//khai bao file
    fp= fopen(tenfile, "r");		//mo file  
    if(!fp){
    	cout<<"file khong to tai"<<endl; exit(1);
    }
    while ((a[m] = fgetc(fp)) != EOF)		//chay dong lap den het file va luu tung ki tu vao a[]
    {   
        m++;    //tang chieu dai cua chuoi
    }
}
int max(int a, int b)
{
	return a>b?a:b;
}
void createtable()
{
	for (int i=1;i<=maxn;i++)
		f[0][i]=0;
	for (int i=1;i<=n;i++)
	for (int j=0; j<=M;j++)
	{
		if(j<a[i])
			f[i][j]=f[i-1][j];
		else
			f[i][j]= max(f[i-1][j],f[i-1][j-a[i]]+c[i]);
	}
}
void reftable()
{
	cout<<"Max value: "<<f[n][M];
	cout<<"\n";
}

int main()
{
	char mang_chua[100];
	int chieu_dai_mang=0;
	mofile(mang_chua,chieu_dai_mang,"input.txt");
	for(int i=0;i<chieu_dai_mang;i++)
	cout<<mang_chua[i]<<" ";
	
	cout<<endl;
	input();																								
	createtable();
	reftable();
	return 0;
	
}