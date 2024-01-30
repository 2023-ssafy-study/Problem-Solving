#include <iostream>
#include <algorithm>
using namespace std;

int team[100000];
int N;

void Input() {
    cin >> N;
    for(int i = 0; i < N; i ++){
        cin >> team[i];
    }
}

int Solve() {
    int s = 0;
    int e = N - 1;
    int ans = 0;
    while (s <= e) {
        int between = e - s - 1;
        ans = max(ans, between * min(team[s], team[e]));
        if (team[s] < team[e]) s++;
        else e --;
    }
    return ans;
}

void Solution() {
    Input();
    cout << Solve() << endl;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    Solution();
    return 0;
}
