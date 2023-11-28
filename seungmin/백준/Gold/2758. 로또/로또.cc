#include <iostream>
#define ll long long

using namespace std;
ll T, N, M, ans;
ll arr[11][2001];

void Solution() {
    cin >> T;
    for (int i = 0; i < T; i ++) {
        ans = 0;
        cin >> N >> M;
        for(int s = 1; s <= M; s ++) ans += arr[N][s];
        cout << ans << "\n";
    }
}

//arr[i][j] : i개를 골랏을때 j개만큼의 경우의수
//arr[i][j] = 현재수 j보다 j/2보다 작은 수들의 경우를 모두 더한 값
void DP() {
    for(int i = 1; i <= 10; i ++) {
        for(int j = 1; j <= 2000; j ++) {
            ll cnt = 0;
            for (int k = 1; k <= j/2; k ++) cnt += arr[i-1][k];
            if(i == 1) cnt = 1;
            arr[i][j] = cnt;
        }
    }
}

void Solve() {
    DP();
    Solution();
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}