#include <iostream>


using namespace std;

int R, C, K;
char arr[6][6];
int visited[6][6] = { 0, };
int dx[4] = { 0,0,-1,1 };
int dy[4] = { 1,-1,0,0 };
int cnt = 0;

void DFS(int x, int y, int depth)
{
	//종료조건
	if (depth == K && x == 0 && y == C - 1 )
	{
		cnt++;
		return;
	}

	for (int i = 0; i < 4; i++)
	{
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (nx < 0 || nx >= R || ny < 0 || ny >= C) continue;
		if (arr[nx][ny] == 'T') continue;
		if (visited[nx][ny]) continue;
		visited[nx][ny] = 1;
		DFS(nx, ny, depth + 1);
		visited[nx][ny] = 0;
	}

}



int main()
{
	cin >> R >> C >> K;
	for (int i = 0; i < R; i++)
	{
		for (int j = 0; j < C; j++)
		{
			cin >> arr[i][j];
		}
	}
	visited[R - 1][0] = 1;
	DFS(R - 1, 0, 1);
	cout << cnt << endl;
	return 0;
}