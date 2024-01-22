#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

const double INF = 987654321.0;
int n;
double map[16][2];
double dp[16][1 << 16];

double GetDis(int cur, int togo) {
    return sqrt(pow(map[cur][0] - map[togo][0], 2) + pow(map[cur][1] - map[togo][1], 2));
}

double DFS(int cur, int visit) {
    if (visit == (1 << n) - 1) {
        return GetDis(cur, 0);
    }
/*
    if (dp[cur][visit] != 0) return dp[cur][visit];

    dp[cur][visit] = INF;

    for (int i = 0; i < n; i++) {
        if ((visit & (1 << i)) == (1 << i)) continue;
        dp[cur][visit] = min(dp[cur][visit], GetDis(cur, i) + DFS(i, visit | 1 << i));
    }
    return dp[cur][visit];
*/
  
    double& ret = dp[cur][visit];
    if (ret != 0) return ret;
    ret = INF;
    for(int i = 0; i < n; i ++) {
        if(visit & 1 << i) continue;
        ret = min(ret, GetDis(cur, i) + DFS(i, visit | 1 << i));
    }
    return ret;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 2; j++) {
            cin >> map[i][j];
        }
    }
    memset(dp, 0, sizeof(dp));
    cout << fixed; // 소수점 6자리 출력을 위한 설정
    cout.precision(6); //fixed는 기본이 소수점 6자리라 설정안해줘도됨
    cout << DFS(0, 1) << endl;
    return 0;
}