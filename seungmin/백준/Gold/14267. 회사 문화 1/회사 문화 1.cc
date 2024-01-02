#include <iostream>
#include <vector>

using namespace std;

int n,m;
vector<vector<int>> graph;
vector<int> praise;

void Input() {
    cin >> n >> m;
    graph.assign(n + 1, vector<int> (0, 0)); // assign (n+1만큼, 구조체 인자)를 체움
    praise.assign(n + 1, 0);
    
    for(int i = 1; i <= n ; i++) {
        int emp;
        cin >> emp;
        if (emp != -1) graph[emp].emplace_back(i); //emplace_back : push_back보다 빠름
    }
    
    for(int i = 0; i < m; i ++ ) {
        int person, num;
        cin >> person >> num;
        praise[person] += num;
    }
}

void DFS(int cur) {
    for(int i = 0; i < graph[cur].size(); i ++) {
        int next = graph[cur][i];
        praise[next] += praise[cur];
        DFS(next);
    }
}

void Solve() {
    Input();
    DFS(1);
    for(int i = 1; i <= n; i ++) {
        cout << praise[i] << " ";
    }
    cout << endl;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    Solve();
    return 0;
}
