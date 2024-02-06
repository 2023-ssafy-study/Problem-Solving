#include <iostream>
#include <string>

using namespace std;

int n,k;
long long ans;
int names[600001];
int cnt[20];

void input() {
    string s;
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        cin >> s;
        names[i] = s.size();
    }    
}

void solve() {
    for(int i = 0; i <= k; i ++) cnt[names[i]] ++;
    for(int i = 0; i < n - 1; i ++) {
        cnt[names[i]] --;
        ans += cnt[names[i]];
        cnt[names[i+k + 1]] ++;
    }
    
    cout << ans;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    input(); solve();
    return 0;
}