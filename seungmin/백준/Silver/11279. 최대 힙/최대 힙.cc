#include <iostream>
#include <queue>
 
using namespace std;
 
int N;
 
int main()
{
    ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    cin >> N;
    priority_queue<int> pq;
    for (int i = 0; i < N; i++)
    {
        int num;
        cin >> num;
        if (num == 0)
        {
            if (pq.empty())
                cout << 0 << "\n";
            else {
                cout << pq.top() << "\n";
                pq.pop();
            }
        }
        else
            pq.push(num);
    }
    return 0;
}