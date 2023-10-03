#include <iostream>
#include <algorithm>

using namespace std;

int c, n;
int cost[21], client[21];
// DP[i] 명의 손님을 i원만큼 사용해서 늘릴수 있다
int DP[100001]; // 1000 * 100

int main()
{
	cin >> c >> n;
	for (int i = 1; i <= n; i++)
	{
		cin >> cost[i] >> client[i];
	}

	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= 100000; j++)
		{
			if (j - cost[i] >= 0)
			{
				DP[j] = max(DP[j], DP[j - cost[i]] + client[i]);
			}
		}
	}

	for (int i = 1; i <= 100000; i++)
	{
		if (DP[i] >= c)
		{
			cout << i << endl;
			break;
		}
	}

	return 0;
}
