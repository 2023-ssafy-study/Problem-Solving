#include <iostream>
#include <algorithm>

using namespace std;

int arr[2000];
int n, ans;

void Input() {
    cin >> n;
    for(int i = 0; i < n; i ++) cin >> arr[i];
}

void Solution() {
    sort(arr, arr + n);
    ans = 0;
    for (int i = 0; i < n; i++) {
        int num = arr[i]; // 찾을 값
        int l = 0, r = n - 1, sum; // 이분탐색 더할 두 값
        while(l < r) {
            sum = arr[l] + arr[r];
            if(sum == num) {
                if (l != i && r != i) {
                    ans ++;
                    break;
                } else if (l == i) l ++; else if (r == i)r --;
            } else if (sum < num) l ++; else r --;
        }
    }
    cout << ans << "\n";
}

void Solve() {
    Input();
    Solution();
}


int main() {
    ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    Solve();
    return 0;
}