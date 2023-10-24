#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>

using namespace std;
int N;
int answer;
vector<pair<int, int>> v;
priority_queue<int, vector<int>, greater<int>> pq;
 
int main() {
    ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    cin >> N;
    for (int i = 0; i < N; i++) {
        int start, end;
        cin >> start >> end;
        v.push_back({ start,end });
    }

    sort(v.begin(), v.end()); 
 
    pq.push(v[0].second);
    for (int i = 1; i < v.size(); i++) {
        if (v[i].first >= pq.top()) {
            pq.pop();
            pq.push(v[i].second);
        }
        else {
            pq.push(v[i].second);
        }
    }
    cout << pq.size() << "\n";
    return 0;
}
