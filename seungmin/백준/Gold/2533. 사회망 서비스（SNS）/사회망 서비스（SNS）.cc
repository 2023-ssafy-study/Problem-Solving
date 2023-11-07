#include <iostream>
#include <vector>
 
using namespace std;
 
int n;
 
int dp[1000001][2];
vector<vector<int> > edges;
vector<int> isVisited;
 
void dfs(int node){
    isVisited[node] = 1;
    dp[node][0] = 0;
    dp[node][1] = 1;
    
    for(int i=0; i<edges[node].size(); i++){
        int conn_node = edges[node][i]; 
        
        if(isVisited[conn_node]) continue;
        
        dfs(conn_node);
        
        dp[node][0] += dp[conn_node][1]; 
        dp[node][1] += min(dp[conn_node][0], dp[conn_node][1]);
    }
}
 
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    cin >> n;
    edges.resize(n+1);
    isVisited.resize(n+1);
    
    int u, v;
    for(int i=1; i<n; i++){
        cin >> u >> v;
        edges[u].push_back(v);
        edges[v].push_back(u);
    }
    
    dfs(1);
    
    cout << min(dp[1][0], dp[1][1]) << endl;
}
