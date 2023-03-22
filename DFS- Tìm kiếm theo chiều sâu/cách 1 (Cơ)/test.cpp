#include <iostream>
#include <fstream>
#include <stack>

using namespace std;

#define MAX 100

int dothi[MAX][MAX];
bool daxet[MAX];
int n, dich;

void khoitao(){
  ifstream file("./DFS.txt", ios::in);
  //freopen("DFS.IN", "r", stdin);
  cout<<"nhap n"; 
  file >> n;
  
  for(int i = 1; i <= n; i++){
    for(int j = 1; j <= n; j++){
      file >> dothi[i][j];
    } 
    daxet[i] = false;
  }
}
void DFS(int u);


int main(){
  khoitao();
  int s;
  cout << "Hay nhap dinh xuat phat: ";
 cin >> s;
  cout << "Hay nhap dinh tim kiem: ";
  cin >> dich;
  DFS(s); 
}


void DFS(int u){
 
  stack<int> open;
  open.push(u);
  daxet[u] = true;
  cout << u << " ";
  while(!open.empty()){
  
    int s = open.top();
    open.pop();
    for(int i = 1; i <= n; i++){
      if(dothi[s][i] == 1 && daxet[i] == false){
        cout << i << " ";
        daxet[i] = true;
         if(i == dich){
		cout << "da tim kiem thanh cong dinh " << dich << " !";
		exit(1);
		
	}
        open.push(s);
        open.push(i);
        break;
      }
    }
  }
}