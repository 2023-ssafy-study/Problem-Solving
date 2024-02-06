#include <iostream>
#include <vector>

using namespace std;
int tc;
void steal_house() {
    int n,m,k;
    vector<int> house;
    cin >> n >> m >> k;
    for (int i = 0; i < n; i++) {
        int temp;
        cin >> temp;
        house.push_back(temp);
    }
    
    int ans = 0, t_money = 0;
    
    for(int i = 0; i< m; i ++) {
        t_money += house[i];
    }
    if (t_money < k) ans ++;
    
    if(n != m) {
        for(int i = 0; i < n - 1; i ++) {
            int n_house = (i + m) % n;
            t_money = t_money - house[i] + house[n_house];
            if (t_money < k) ans ++;
        }
    }
    cout << ans << "\n";
}

int main() {
    ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    cin >> tc;
    while(tc --) steal_house();
    return 0;
}