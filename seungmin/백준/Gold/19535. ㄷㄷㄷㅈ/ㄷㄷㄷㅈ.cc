#include <iostream>
#include <vector>

using namespace std;

int N;

vector<int> tree[300003];

long long count_d = 0;
long long count_g = 0;

void find_g() {
	for (int n = 1;n <= N;n++) {
		int cnt = tree[n].size(); // 자식 개수
		if (cnt >=3) 
			count_g += (cnt*(cnt - 1)*(cnt - 2)) / 6;
	}
}

void find_d() { 
	for (int n = 1;n <= N;n++) {
		if (tree[n].size() < 2) continue;
		for (int i = 0;i < tree[n].size();i++) {
			if (tree[n][i] < n) continue;
			if (tree[tree[n][i]].size() < 2) continue;
			count_d += ((tree[n].size()-1)*(tree[tree[n][i]].size()-1));
		}
	}
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> N;
	for (int i = 1;i < N;i++) { 
		int u, v;
		cin >> u >> v;
		tree[u].push_back(v);
		tree[v].push_back(u);	
	}
	
	find_d();
	find_g();

	if (count_d > count_g * 3) cout << "D";
	else if (count_d == count_g * 3) cout << "DUDUDUNGA";
	else cout << "G";

	return 0;
}