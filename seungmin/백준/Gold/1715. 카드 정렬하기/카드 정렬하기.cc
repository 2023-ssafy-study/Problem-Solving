#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

priority_queue<int, vector<int>, greater<int> > pq;
int N;

int main(void)
{
    int sum = 0;

    cin >> N;
    int n;
    for (int i = 0; i < N; i++) {     
        cin >> n;
        pq.push(n);  
    }

    while(pq.size() > 1) {
        int n1, n2;

        n1 = pq.top(), pq.pop();
        n2 = pq.top(), pq.pop();
        sum += (n1 + n2);
        pq.push(n1 + n2);
    }

    cout << sum << "\n";
    return 0;
}