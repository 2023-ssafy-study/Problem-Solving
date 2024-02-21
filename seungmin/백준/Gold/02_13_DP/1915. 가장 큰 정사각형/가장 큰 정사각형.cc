#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int n, m;
int arr[1001][1001];
int ans;

void input() {
    cin >> n >> m;
    for (int i = 1; i <= n; i ++) {
        string s;
        cin >> s;
        for (int j = 0; j < m; j ++) {
            arr[i][j + 1] = s[j] - '0';
        }
    }
}
void Solve() {
    for (int i = 1; i <= n; i ++) {
        for (int j = 1; j <= m; j ++) {
            if (arr[i][j] != 0) {
                arr[i][j] = min(arr[i-1][j-1], min(arr[i-1][j], arr[i][j -1])) + 1;
                ans = max(arr[i][j], ans);
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    input();
    Solve();
    cout << ans * ans << endl;
    return 0;
}