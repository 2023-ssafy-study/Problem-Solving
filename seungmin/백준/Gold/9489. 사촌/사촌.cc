#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int n, k;
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    while (1)
    {
        cin >> n >> k;
        if (n == 0 && k == 0)
            break;
        int parent_idx = -1, before = 0, ans = 0, data;
        int parent[1000001];
        vector<int> node;
        for (int i = 0; i < n; i++){
            cin >> data;
            node.push_back(data);
            if (i == 0){ 
                before = data;
                parent[data] = -1; 
            }
            else{
                if (before + 1 == data){
                    parent[data] = node[parent_idx];
                    before = data;
                }
                else{
                    before = data;
                    parent_idx++;
                    parent[data] = node[parent_idx]; 
                }
            }
        }

        if (k == node[0]){
            ans = 0;
        }
        else{
            for (int i = 0; i < node.size(); i++){
                
                if (parent[parent[node[i]]] == parent[parent[k]] && parent[node[i]] != parent[k]){
                    ans++;
                }
            }
        }
        cout << ans << endl;
    }
}