#include <iostream>
#include <algorithm>

using namespace std;

struct Line {
    int left;
    int right;
};

int n;
int dp[101];
Line arr[101];

void input() {
    cin >> n;
    for (int i = 0; i < n; i ++) {
        cin >> arr[i].left >> arr[i].right;
    }
}

bool Cmp(Line a, Line b) {
    if(a.left < b.left) return true;
    return false;
}

void Solve() {
    int connect = 0;
    sort(arr, arr + n, Cmp);
    for(int i = 0; i < n; i ++) {
        dp[i] = 1;
        for(int j = 0; j < i; j++) {
            if(arr[i].right > arr[j].right) dp[i] = max(dp[i], dp[j] + 1);
        }
        connect = max(dp[i], connect);
    }
    cout << n - connect << "\n";
}

int main() {
    ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    input();
    Solve();
    return 0;
}