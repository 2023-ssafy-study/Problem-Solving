#include <iostream>

using namespace std;

int n, m, s, e;
int arr[2001];
int dp[2001][2001] = {false, };

void pelindrom() {
    cin >> n;
    for (int i = 1; i <= n; i++) cin >> arr[i];
    
    for (int i = 1; i < n; i++) {
        if (arr[i] == arr[i+1]) dp[i][i + 1] = true;
    }
    for (int i = 1; i <= n; i++) dp[i][i] = true;
    
    for (int start = n - 2; start >= 1; start --) {
        for (int end = start + 2; end <= n; end ++) {
            if (arr[start] == arr[end] && dp[start + 1][end - 1]) dp[start][end] = true;
        }
    }
}

void solve() {
    cin >> m;
    while(m--) {
        cin >> s >> e;
        cout << dp[s][e] << "\n";
    }
}

int main() {
    ios::sync_with_stdio(false), cin.tie(0); cout.tie(0);
    pelindrom(); solve();
    return 0;
}