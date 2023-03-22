#include<iostream>
#define maxn 200
using namespace std;
void input(int &m,int &n,char a[][maxn]);


int main(){
int m=0,n=0,doi=0;
char a[maxn][maxn];	
	
    
input(m,n,a);

FILE * fp = NULL;

    fp=fopen("output.txt","wt");
//cout<<m<<" "<<n<<endl;
for(int i=0;i<m;i++)
{
for(int j=0;j<n;j++)
{
	if(a[i][j]=='+') 
	{
		int flag=0;
		for(int k=0;k<m;k++)
		{
			if(a[k][j]=='*') flag=1;
		}
		for(int e=0;e<n;e++)
		{
			if(a[i][e]=='*') flag=1;
		}
		if(flag==0) {a[i][j]='*';doi++;}
		
	}
	 
}	
	
}	

fprintf(fp,"%d\n", doi);

for(int i=0;i<m;i++)
{
for(int j=0;j<n;j++)
fprintf(fp, "%c", a[i][j]);


fputc('\n', fp);
}
fclose(fp);

}


void input(int &m,int &n,char a[][maxn])
{
	FILE *fi;
	fi=fopen("input.txt","rt");
		fscanf(fi,"%d%d",&m,&n);
		char nho;
		
	for(int i=0;i<m;i++)
	for(int j=0;j<n;j++)
	while(1)
	{
		fscanf(fi,"%c",&nho);
		//xoa khoang cach
		if(nho == '\r' || nho == '\n' || nho == ' ')
		{ 
		  continue;
		}
		else 
		{a[i][j]=nho;
		  break;}
	}
		

	
	fclose(fi);
}