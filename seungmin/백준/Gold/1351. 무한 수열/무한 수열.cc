#include <iostream>
#include <unordered_map>

using namespace std;
using ll = long long;

ll N,P,Q;
unordered_map<ll, ll> m;

ll solve(ll num){
    ll ret;
    if(m.find(num) != m.end()){
        return m[num];
    }
    ret = solve(num/P) + solve(num/Q);
    m[num] = ret;
    return ret;
}

int main (){
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> N >> P >> Q;
    m[0] = 1;
    if(N == 0)
        cout << 1;
    else
        cout << solve(N/P) + solve(N/Q);
}