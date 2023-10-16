#include <iostream>
#include <stack>

using namespace std;

int N, idx;
int height;
stack<pair<int, long long>> s;

void solution() {
    cin >> N;
    for (int i; i < N; i ++) {
        cin >> height;
        while(!s.empty()) {
            if (height < s.top().second) {
                cout << s.top().first << " ";
                break;
            }
            s.pop();
        }
        if (s.empty()) {
            cout << 0 << " ";
        }
        
        s.push({i+1, height});
    }
}


int main(){
    ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    solution();
    cout << "\n";
    return 0;
}