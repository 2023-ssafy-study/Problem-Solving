#include <iostream>
#include <cstring>

using namespace std;

#define INF 987654321;

int n, map[16][16];
int dp[16][1 << 16]; // 2^16

int DFS(int cur, int visit) {
    if(visit == (1<<n) - 1) { //11...111 모든 방문 완료
       if(map[cur][0] == 0) return INF; //이동 불가능
       return map[cur][0];
    }
    if(dp[cur][visit] != -1) return dp[cur][visit]; //이미 방문
    
    dp[cur][visit] = INF;
    
    for(int i = 0; i < n; i ++) {
        if(map[cur][i] == 0) continue; // 길이 없음
        if((visit & (1 << i)) == (1 << i)) continue; //이미 방문2
        dp[cur][visit] = min(dp[cur][visit], map[cur][i] + DFS(i, visit | 1 << i));
    }
    return dp[cur][visit];
}

int main() {
    ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    cin >> n;
    for(int i = 0; i<n; i ++) {
        for(int j = 0; j < n; j ++) {
            cin >> map[i][j];
        }
    }
    memset(dp, -1, sizeof(dp)); // dp -1로 초기화
    cout << DFS(0, 1) << endl;
    return 0;
}