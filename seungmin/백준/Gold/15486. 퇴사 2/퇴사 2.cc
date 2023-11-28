#include <iostream>
#include <algorithm>

#define M_N 1500010

using namespace std;

int N, ans;
int DP[M_N];
int arr[M_N][2]; // arr[n][0] : 걸리는 날짜, arr[n][1] : 버는 돈

void Input() {
    cin >> N;
    for(int i = 1; i<=N; i ++) {
        cin >> arr[i][0] >> arr[i][1];
    }
}

void Solution() {
    int c_m = 0;
    for(int i = 1; i <= N + 1; i++) {
        c_m = max(c_m, DP[i]);
        if(i+ arr[i][0] > N + 1) continue; //일정을 넘겻을때
        
        DP[i+ arr[i][0]] = max(c_m + arr[i][1], DP[arr[i][0] + i]);
    }
    ans = c_m;
}

void Solve() {
    Input();
    Solution();
    cout << ans << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}