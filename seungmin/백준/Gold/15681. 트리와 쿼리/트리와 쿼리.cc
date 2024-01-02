#include <iostream>
#include <vector>

using namespace std;

int n, r, q;
vector<int> node[100001];
bool visited[100001];
int nums[100001];

int DFS(int cur) {
    if (nums[cur] != 0) return nums[cur];

    visited[cur] = true;

    int cnt = 1;

    for (int i = 0; i < node[cur].size(); i++) {
        int next = node[cur][i];
        if (visited[next]) continue;
        cnt += DFS(next);
    }
    nums[cur] = cnt;
    return cnt;
}

void Input() {
    cin >> n >> r >> q;

    int u, v;
    for (int i = 0; i < n - 1; i++) {
        cin >> u >> v;
        node[u].push_back(v);
        node[v].push_back(u);
    }
    nums[r] = DFS(r);
}


void Solve() {
    Input();
    int m;
    for (int i = 0; i < q; i++) {
        cin >> m;
        cout << nums[m] << "\n";
    }
}


int main() {
    ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    Solve();
    return 0;
}