#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
vector<int> man_p;
vector<int> man_m;
vector<int> woman_p;
vector<int> woman_m;


void Input() {
    cin >> n;
    int temp;
    for (int i = 0; i < n; i++) {
        cin >> temp;
        if (temp > 0) man_p.push_back(temp);
        else man_m.push_back(abs(temp));
    }
    for (int i = 0; i < n; i++) {
        cin >> temp;
        if (temp > 0) woman_p.push_back(temp);
        else woman_m.push_back(abs(temp));
    }

    sort(man_p.begin(), man_p.end(), greater<int>());
    sort(man_m.begin(), man_m.end(), greater<int>());
    sort(woman_p.begin(), woman_p.end(), greater<int>());
    sort(woman_m.begin(), woman_m.end(), greater<int>());
}

void Solve() {
    int cnt = 0;
    int i = 0;
    int j = 0;
    while (i < man_p.size() && j < woman_m.size()) {
        //cout << "mp = " << man_p[i] << " wm = " << woman_m[j] << " " << cnt << "\n";
        if (woman_m[j] > man_p[i]) {
            cnt++;
            i++;
            j++;
        }
        else i++;
    }

    i = 0; j = 0;
    while (i < man_m.size() && j < woman_p.size()) {
        //cout << "mm = " << man_m[i] << " wp = " << woman_p[j] << " " << cnt << "\n";
        if (woman_p[j] < man_m[i]) {
            cnt++;
            i++;
            j++;
        }
        else j++;
    }
    cout << cnt;
}

void Solution() {
    Input();
    Solve();
}
int main() {
    ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    Solution();
}