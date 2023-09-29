#include <iostream>
#include <vector>

using namespace std;

int n;
int x, y, d, g;
int ans = 0;

int arr[101][101];
int dy[4] = { 0,-1,0,1 };
int dx[4] = { 1, 0, -1, 0};
vector<int> dir;


void Curve()
{
	int size = dir.size();
	for (int i = size - 1; i >= 0; i--)
	{
		int t = (dir[i] + 1) % 4;
		x += dx[t];
		y += dy[t];
		arr[x][y] = 1;
		dir.push_back(t);
	}
}




int main()
{
	cin >> n;
	while (n--)
	{
		dir.clear();
		cin >> x >> y >> d >> g;
		arr[x][y] = 1;
		x += dx[d];
		y += dy[d];
		arr[x][y] = 1;
		dir.push_back(d);

		while (g--)
		{
			Curve();
		}

	}

	for (int i = 0; i < 101; i++)
	{
		for (int j = 0; j < 101; j++)
		{
			if (arr[i][j] == 1 && arr[i][j + 1] == 1 && arr[i + 1][j + 1] && arr[i + 1][j] == 1)
				ans++;
		}
	}

	cout << ans << endl;

	return 0;
}