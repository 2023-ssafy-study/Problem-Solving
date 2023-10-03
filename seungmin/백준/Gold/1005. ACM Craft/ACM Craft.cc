#include <iostream>
#include <vector>
#include <queue>
#include <cstring>
using namespace std;

const int MAX = 1001;

int n, k, w, T;
int t[MAX];
int cnt[MAX];
int DP[MAX];
vector<int> graph[MAX];

void init_clear()
{
	memset(cnt, 0, sizeof(cnt));
	memset(t, 0, sizeof(t));
	memset(DP, 0, sizeof(DP));
	for (int i = 0; i < MAX; i++)
	{
		graph[i].clear();
	}
}

void t_Sort() // 위상정렬
{
	queue<int> q;

	for (int i = 1; i <= n; i++)
	{
		if (cnt[i] == 0)
		{
			DP[i] = t[i];
			q.push(i);
		}
	}

	for (int i = 1; i <= n; i++)
	{
		int v = q.front();
		q.pop();

		for (int j = 0; j < graph[v].size(); j++)
		{
			int N = graph[v][j];

			cnt[N] --;

			// 점화식 DP[N] = DP[N] VS t[N] + DP[V];
			DP[N] = max(DP[N], DP[v] + t[N]);

			if (cnt[N] == 0)
			{
				q.push(N);
			}
		}
	}
}


int main()
{
	cin >> T;

	while (T --)
	{
		cin >> n >> k;
		init_clear();
		for (int i = 1; i <= n; i++)
		{
			cin >> t[i];
		}
		
		while (k--)
		{
			int u, v;
			cin >> u >> v;
			graph[u].push_back(v);
			cnt[v] ++;

		}

		cin >> w;

		t_Sort();
		cout << DP[w] << '\n';

	}
}