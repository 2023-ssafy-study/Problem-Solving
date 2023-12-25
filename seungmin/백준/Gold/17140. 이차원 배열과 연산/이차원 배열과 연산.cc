#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>

#define MAX 101
using namespace std;

int r, c, k, ans;
int Map[MAX][MAX];
int cnt[MAX];

void Input() {
	cin >> r >> c >> k;
	for (int i = 1; i<= 3; i++)
	{
		for (int j = 1; j <= 3; j++) {
			cin >> Map[i][j];
		}
	}
}

void Find() {
	int Time = 0;
	int row = 3;
	int col = 3;
	while (true)
	{
		// 종료 조건 Map[r][c] ==k와 시간이 100초가 지낫을때
		if (Map[r][c] == k) { ans = Time; break; }
		if (Time > 100) { ans = -1; break; }
		int Size = 0;
		// 행이 열보다 크거나 같을때
		if (row >= col) 
		{
			for (int i = 1; i <= row; i++)
			{
				vector<pair<int, int>> V; // vector<숫자갯수, 숫자>
				memset(cnt, 0, sizeof(cnt)); // 숫자 샌거 초기화
				for (int j = 1; j <= col; j++) cnt[Map[i][j]]++;
				for (int j = 1; j < MAX; j++) {
					if (cnt[j] == 0) continue;
					V.push_back(make_pair(cnt[j], j));
				}
				sort(V.begin(), V.end());
				for (int j = 1; j <= col; j++) Map[i][j] = 0; // 초기화 해주는 이유 : 열이 더 줄어들수 있음
				int idx = 1; // Map이 1,1 부터 시작함 V = 0부터 시작해 차이가남
				for (int j = 0; j < V.size(); j++)
				{
					Map[i][idx++] = V[j].second;
					Map[i][idx++] = V[j].first;
				}
				idx--;
				Size = max(Size, idx);//열의 최대값을 저장
			}
			col = Size;
		}
		else // 열이 클때
		{
			for (int j = 1; j <= col; j++)
			{
				vector<pair<int, int>> V; // vector<숫자갯수, 숫자>
				memset(cnt, 0, sizeof(cnt)); // 숫자 샌거 초기화
				for (int i = 1; i <= row; i++) cnt[Map[i][j]]++;
				for (int i = 1; i < MAX; i++) {
					if (cnt[i] == 0) continue;
					V.push_back(make_pair(cnt[i], i));
				}
				sort(V.begin(), V.end());
				for (int i = 1; i <= row; i++) Map[i][j] = 0; // 초기화 해주는 이유 : 열이 더 줄어들수 있음
				int idx = 1; // Map이 1,1 부터 시작함 V = 0부터 시작해 차이가남
				for (int i = 0; i < V.size(); i++)
				{
					Map[idx++][j] = V[i].second;
					Map[idx++][j] = V[i].first;
				}
				idx--;
				Size = max(Size, idx);//행의 최대값을 저장
			}
			row = Size;
		}
		Time++;
	}
}

void Solution() {
	if (Map[r][c] == k)
	{
		ans = 0;
		cout << ans << endl;
		return;
	}
	Find();
	cout << ans << endl;
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