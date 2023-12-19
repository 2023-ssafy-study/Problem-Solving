#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <queue>

using namespace std;

int n, m;
map<string, vector<string>> adj;
map<string, pair<int, double>> age;
string kingname;
vector<string> wantking;

void init(string name){
    if(age.find(name) == age.end()) age[name] = {0,0};
}

void Input() {
    cin >> n >> m;
    cin >> kingname;
    
    while (n--) {
        string p1, p2;
        string name;
        
        cin >> name >> p1 >> p2;
        init(name); init(p1); init(p2);
        adj[p1].push_back(name);
        adj[p2].push_back(name);
        age[name] = {2, 0};
    }
    while (m --) {
        string name;
        cin >> name;
        wantking.push_back(name);
    }
    age[kingname] = {0, 1};
}

void Solution() {
    queue<string> q;
    string nextking;
    double blood = 0;
    
    for (auto iter : age) {
        if (iter.second.first == 0) q.push(iter.first);
    }
    while (!q.empty()) {
        string c = q.front();
        q.pop();
        
        for(auto iter : adj[c]) {
            string next = iter;
            age[next].second += age[c].second;
            if (--age[next].first == 0) {
                q.push(next);
                age[next].second /= 2;
            }
        }
    }
    for (auto iter: wantking) {
        if (blood < age[iter].second) {
            blood = age[iter].second;
            nextking = iter;
        }
    }
    cout << nextking << endl;
}

int main() {
    Input();
    Solution();
}