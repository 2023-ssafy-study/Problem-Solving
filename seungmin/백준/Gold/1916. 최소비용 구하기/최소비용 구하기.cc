#include <iostream>
#include <queue>
#include <vector>
#define INF 10e9

using namespace std;

int N, M;
vector<pair<int, int>> nodes[1001];
int S, E;
int dist[1001];

void input()
{
	cin >> N >> M;

	for (int i = 0; i < M; i++)
	{
		int a, b, c;
		cin >> a >> b >> c;
		nodes[a].push_back({ b,c });
	}
	cin >> S >> E;
	for (int i = 1; i <= N; i++)
	{
		dist[i] = INF;
	}
}

void Dijkstra()
{
	priority_queue<pair<int, int>> pq;

	pq.push({ 0, S });
	dist[S] = 0;
	while (!pq.empty())
	{
		int cost = -pq.top().first;
		int current = pq.top().second;
		pq.pop();

		if (dist[current] < cost) continue;

		for (int i = 0; i < nodes[current].size(); i++)
		{
			int next = nodes[current][i].first;
			int nc = cost + nodes[current][i].second;
			if (dist[next] > nc)
			{
				dist[next] = nc;
				pq.push({ -nc, next });
			}
		}
	}

}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
	input();
	Dijkstra();
	cout << dist[E] << endl;
	return 0;
}