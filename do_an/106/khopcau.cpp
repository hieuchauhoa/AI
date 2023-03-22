#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

const int N = 1000;
bool khop[N], Qdau[N], Qcuoi[N];
vector <int> k[N], tmp[N];
int num[N], low[N], stt;
int n, m, u, v, tmp1, tmp2;
int P = 0, Q = 0, Pout[N];
ofstream filetmp("./tmp.txt", ios::out);

void tarjan(int u, int parent){ //áp dụng thuật toán Tarjan tìm liên thông mạnh để tìm khớp, cầu
	stt++;
	low[u] = num[u] = stt;
	int children = 0;
	for(auto v : k[u]){
		if(v != parent){
			if(num[v])
		 		low[u] = min(low[u], num[v]);
 			else{
		 		tarjan(v, u);
				low[u] = min(low[u], low[v]);
				children++;
				if(low[v] >= num[v]){
					Q++;
					filetmp << u << ' ' << v << endl;
				}
				if(u == parent){
                    if(children >= 2)
                        khop[u] = true;
				}
				else if(low[v] >= num[u])
                        khop[u] = true;
			}
		}
	}
}

int main(){
 	ifstream file("./graph.inp", ios::in);
 	ofstream fileout("./graph.out", ios::out);
 	file >> n >> m;
	for(int i = 1; i <= m; i++){
		file >> u >> v;
		k[u].push_back(v);
		k[v].push_back(u);
	}
	for(int i = 1; i <= n; i++)
		if(!num[i])
			tarjan(i, i);
    for(int i = 1; i <= n; i++)
        if(khop[i]){
            P++;
            Pout[P] = i;
        }
    fileout << P << ' ' << Q << endl;
    for(int i = 1; i <= P; i++)
        fileout << Pout[i] << endl;
    fileout.close();
    ifstream filetmpin("./tmp.txt", ios::in);
    ofstream filetmpout("./graph.out", ios::app);
    for(int i = 1; i <= Q; i++){
		filetmpin >> u >> v;
        filetmpout << u << ' ' << v << endl;
	}
	return 0;
}


