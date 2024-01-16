#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

long long N, K;
long long Low, High, Mid;
long long cnt;

long long count(long long x)
{
	long long sum = 0;
	for (int i = 1; i <= N; i++)
	{
		sum += min(x / i, N);
	}
	return sum;
}

int main()
{
	cin >> N >> K;

	K = min((long long)1000000000, K);

	Low = 1;
	High = N * N;

	while (Low <= High)
	{
		Mid = (Low + High) / 2;

		cnt = count(Mid); // Mid보다 작거나 같은 수들의 개수

		if (cnt >= K)
		{
			// Mid보다 작거나 같은 수들의 개수가 목표 인덱스보다 많으므로
			// 이므로 Mid값을 더 작게 찍어줘야 합니다.
			// 따라서 High값 조정
			High = Mid - 1;
		}
		else
		{
			// Mid보다 작거나 같은 수들의 개수가 목표 인덱스보다 작으므로
			// 이므로 Mid값을 더 크게 찍어줘야 합니다.
			// 따라서 Low값 조정
			Low = Mid + 1;
		}
	}
	cout << Low;
}