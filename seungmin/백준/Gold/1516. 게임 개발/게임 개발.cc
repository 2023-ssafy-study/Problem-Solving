#include <iostream>
#include <queue>
#include <vector>


#define MAX 501
using namespace std;

int n;
int entry[MAX], Time[MAX]; // entry[n] : n을 짓기전에 필요한 건물수, Time[n] : n번 건물 짓는 시간
int ans[MAX];
vector<int> V[MAX];// V[n]안의 값들은 n을 지어야만 지을 수 있다.

void Input() {
	cin >> n;
	for (int i = 1; i <= n; i++) {
		cin >> Time[i];
		while (1)
		{
			int a;
			cin >> a;
			if (a == -1) break;
			V[a].push_back(i);
			entry[i]++;
		}
	}
}

int Bigger(int A, int B) { if (A > B) return A; return B; }

void Solution() {
	queue<int> Q;
	for (int i = 1; i <= n; i++)
	{
		if (entry[i] == 0) {
			Q.push(i);
			ans[i] = Time[i];
		}
	} // 큐 시작값들 입력 전에 건물을 지을 필요가 없는것들

	while (!Q.empty()) {
		int cur = Q.front();
		Q.pop();

		for (int i = 0; i < V[cur].size(); i++)
		{
			int Next = V[cur][i];
			entry[Next]--;
			ans[Next] = Bigger(ans[Next], ans[cur] + Time[Next]);
			if (entry[Next] == 0) Q.push(Next);
		}
	}

	for (int i = 1; i <= n; i++) cout << ans[i] << "\n";

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