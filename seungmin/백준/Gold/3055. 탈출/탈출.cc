#include <bits/stdc++.h>
using namespace std;

int r, c;
char arr[53][53];
bool s_check[53][53], wt_check[53][53];
int ch[53][53];
int dx[4] = { 1,0,-1,0 };
int dy[4] = { 0,1,0,-1 };
//물 먼저 이동 후 고슴도치 이동

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> r >> c;
	queue<pair<int, int> > wt;
	queue<pair<int, int> > s;
	for (int i = 1; i <= r; i++) {
		for (int j = 1; j <= c; j++) {
			cin >> arr[i][j];
			if (arr[i][j] == '*') {
				ch[i][j] = -1;
				wt.push({ i,j });
				wt_check[i][j] = 1;
			}
			else if (arr[i][j] == 'S') {
				ch[i][j] = 1;
				s.push({ i,j });
				s_check[i][j] = 1;
			}
			else if (arr[i][j] == 'X') {
				ch[i][j] = 2;
			}
			else if (arr[i][j] == 'D') {
				ch[i][j] = 3;
			}
		}
	}
	int t = 0;
	while (true) {

		int s_size = s.size();
		int wt_size = wt.size();

		if (s_size == 0) break;

		for (int i = 0; i < wt_size; i++) {
			int x = wt.front().first;
			int y = wt.front().second;
			wt.pop();

			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];

				if (nx <= 0 || nx > r || ny <= 0 || ny > c||wt_check[nx][ny] == 1) continue;
				if (ch[nx][ny] == 0 || ch[nx][ny]==1) {
					wt_check[nx][ny] = 1;
					ch[nx][ny] = -1;
					wt.push({ nx,ny });
				}
			}
		}

		for (int i = 0; i < s_size; i++) {
			int x = s.front().first;
			int y = s.front().second;
			s.pop();

			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				
				if (nx <= 0 || nx > r || ny <= 0 || ny > c || s_check[nx][ny] == 1) continue;
				if (ch[nx][ny] == 0 || ch[nx][ny] == 1 ) {
					ch[nx][ny] = 1;
					s_check[nx][ny] = 1;
					s.push({ nx,ny });
				}
				else if (ch[nx][ny] == 3) {
					cout << t+1;
					return 0;
				}
			}

		}
		t++;
	}

	cout << "KAKTUS" << '\n';

	return 0;
}