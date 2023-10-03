#include<iostream>
#include<algorithm>

using namespace std;

int n;
int arr[10001] = { 0, };
// 점화식 DP[N] = DP[N] vs (DP[N-a] + Arr[a])
int DP[1001] = { 0, };

int main(void)
{
    cin >> n;
	for (int i = 1; i <= n; i++)
	{
		cin >> arr[i];
	}

	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= i; j++)
		{
			DP[i] = max(DP[i], DP[i - j] + arr[j]);
		}
	}

	cout << DP[n] << endl;


    return 0;
}
