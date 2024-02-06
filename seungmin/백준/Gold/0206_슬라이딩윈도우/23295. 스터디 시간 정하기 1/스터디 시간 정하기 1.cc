#include <iostream>
#include <algorithm>

using namespace std;
using ll = long long;

ll arr[200000];
ll cnt[200000];
ll sum[200000];
int n, m;
ll t, s, e, maxtime;

void input() {
    cin >> n >> m;
    for (int i = 0; i < n; i ++) {
        cin >> t;
        while(t--) {
            cin >> s >> e;
            arr[s] ++;
            arr[e] --;
            maxtime = max(maxtime, e);
        }
    }
    cnt[0] = arr[0];
    sum[0] = cnt[0];
    for(int i = 1; i < maxtime; i ++) {
        cnt[i] = cnt[i - 1] + arr[i];
        sum[i] = sum[i - 1] + cnt[i];
    }
}

void Solve() {
    ll maxcnt = 0;
    ll ans = 0;
    for(ll i = 0; i <= maxtime; i ++) {
        ll temp;
        if (i == 0) temp = sum[i + m] - cnt[i + m];
        else temp = sum[i + m] - sum[i - 1] - cnt[i + m];
        if (temp > maxcnt) {
            maxcnt = temp;
            ans = i;
        }
    }
    cout << ans << " " << ans + m;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    input();
    Solve();
    
    return 0;
}
