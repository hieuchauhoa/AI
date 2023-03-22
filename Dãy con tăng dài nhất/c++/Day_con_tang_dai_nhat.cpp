//nguoi dung nhap input, thay doi input trong ham main
#include <iostream.h>
using namespace std;



int allArray(int A[],int L[],int P[], int n)
{
    L[0] = 1;
    P[0] = 0;
    for (int i = 1; i < n; i++) 
	{   
        L[i] = 1;      
        for (int j = 0; j < i; j++)
            if (A[i] > A[j] && L[i] < L[j] + 1)
                L[i] = L[j] + 1;
        for(int j=0; j<i; j++)
        	if(A[i] > A[j] && L[i] == L[j]+1)
       			P[i] = j+1;
    }
}
int findLIS(int A[],int L[],int P[],int LIS[], int n)
{
	int max=0;
	int pos;
	for(int i=0 ; i<n; i++)
	{
		if(L[i] > max)
		{
			max = L[i];
			pos = i;
		}	
	}
	int test[100],dem=0;
	cout<<"LIS = {";
	while(max!=0)
	{	
		test[dem]=A[pos];
		dem++;			
		pos = P[pos]-1;	
		max--;			
	}
	for(int k=dem-1;k>=0;k--)
	cout<<test[k]<<",";
	cout<<"}"<<endl;
}
void printList(int A[], int L[], int P[], int n)
{
	cout<<"A[i] = "<<"{";
    for(int i=0;i<n;i++)
    {
    	cout<< A[i] <<",";
    }
    cout<<"}"<<endl;
    cout<<"L[i] = "<<"{";
    for(int i=0;i<n;i++)
    {
    	cout<< L[i] <<",";
    }
    cout<<"}"<<endl;
    cout<<"P[i] = "<<"{";
    for(int i=0;i<n;i++)
    {
    	cout<< P[i] <<",";
    }
    cout<<"}"<<endl;                
}                   
int main()          
{                   
	int A[] = { 2, 8, 11, 3, 5, 9, 10, 4, 17, 6 };
	int n = sizeof(A) / sizeof(A[0]);
	int L[n], P[n], LIS[n];
	allArray(A,L,P,n);	
	printList(A,L,P,n);
 	findLIS(A,L,P,LIS,n);	
 	cout<<endl;
    return 0;
}