#include <iostream>

using namespace std;
const int INF = (int)1e9;
int tc, n;
int arr[501], sums[501];
int dp[501][501];

int main() {
    cin >> tc;
    while (tc --) {
        cin >> n;
        for(int i = 1; i <= n; i++) {
            cin >> arr[i];
            sums[i] = sums[i-1] + arr[i];
        }
        for (int i = 1; i<=n; i ++) {
            for (int j = 1; j <= n - i; j ++) {
                dp[j][i + j] = INF;
                for (int m = j; m < i+j; m ++){
                    dp[j][i+j] = min(dp[j][i+j], dp[j][m] + dp[m + 1][i + j] + sums[i + j] - sums[j - 1]);
                }
            }
        }
        cout << dp[1][n] << "\n";
    }
    return 0;
}