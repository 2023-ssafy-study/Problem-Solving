#include <iostream>
#include <algorithm>
#define INF 0x3f3f3f3f

using namespace std;

int N, r, c;
int sum[501], arr[501][2], dp[501][501];

void Input() {
    cin >> N;
    for(int i = 1; i <=N; i ++) {
        cin >> arr[i][0] >> arr[i][1];
    }
}

void Solution() {
    // i : 구간 범위 크기 dp[x][x + i] x부터 x+i까지 곱햇을때 최소 곱셉연산 횟수 
    for(int i = 1; i < N; i ++) {
        // j : 시작지점 j ~ j + i까지
        for(int j = 1; i+j <=N; j ++) {
            dp[j][j+i] = INF;
            for(int k = j; k <= i + j; k ++) {
                // k를 기준으로 두구간으로 나눔
                dp[j][i+j] = min(dp[j][i+j], dp[j][k] + dp[k + 1][i + j] + arr[j][0]*arr[k][1]*arr[i+j][1]);
            }
        }
    }
}
void Solve() {
    Input();
    Solution();
    cout << dp[1][N] << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}