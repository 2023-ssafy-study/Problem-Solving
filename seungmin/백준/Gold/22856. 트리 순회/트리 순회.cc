#include<iostream>
#include<vector>
#include<algorithm>
#include<map>

using namespace std;

int n,a=-1,r=-1;

map<int,pair<int,int>> relation;

void travel(int cur,bool flag){
    if(cur == -1) return;

    a ++,travel(relation[cur].first,0);

    if(flag) r++,travel(relation[cur].second,1);
    else travel(relation[cur].second,0);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> n;
    for(int i=0,a,b,c; i<n; i++){
        cin >> a >> b >> c;
        relation[a].first = b;
        relation[a].second = c;
    }
    travel(1,1);
    cout << 2* a - r;
    return 0;
}