#include <iostream>
#include <unordered_map>
#include <algorithm>

using namespace std;

int n, d, k, c, arr[3000000];
int s, cnt, ans;
unordered_map<int, int> m;

void Input() {
    cin >> n >> d >> k >> c;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
}

void Solve() {
    for (int i = 0; i < k - 1; i++) m[arr[i]] ++; // k -1개의 초밥을 너어둔고 시작
    
    // 회전
    int e = k - 1;
    for (int i = 0; i < n; i++) {
        // 마지막 초밥 추가
        int del = arr[s];
        int fin = arr[e % n];
        m[fin] ++;
        int cnt = m.size();
        if (m.find(c) == m.end()) ans = max(ans, cnt + 1);
        else ans = max(ans, cnt);
        // 다음 탐색을 위한 맨앞 초밥 제거
        m[del] --;
        if (m[del] == 0) m.erase(m.find(del));
        // 다음 탐색을 위한 위치 이동
        s++;
        e++;
        // cout << "start = " << s << " end = " << e << " " << ans <<"\n";
    }
    cout << ans;
}

void Solution() {
    Input();
    Solve();
}

int main() {
    ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    Solution();

    return 0;
}