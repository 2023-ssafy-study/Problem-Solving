#include <iostream>
#include <algorithm>
#include <map>

using namespace std;
using ll = long long;

ll psum[200005];
map<ll, ll> m;
ll n, k, ans;

int main() {
    cin >> n >> k;
    for(ll i = 1; i <= n; i++) {
        ll tmp;
        cin >> tmp;
        psum[i] = psum[i-1] + tmp;
    }
    for(ll i = 1; i<= n; i++) {
        if(psum[i] == k) ans++;
        ans += m[psum[i] - k];
        m[psum[i]] ++;
    }
    cout << ans << endl;
}