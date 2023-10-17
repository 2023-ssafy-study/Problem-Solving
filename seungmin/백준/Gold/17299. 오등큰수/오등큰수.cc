#include <iostream>
#include <stack>
#include <vector>

#define MAX 1000001
using namespace std;
int arr[MAX], cnt[MAX], ngf[MAX];

int main()
{
	ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	int n;
	cin >> n;
	stack<int> s;
	for (int i = 1; i <= n; i++)
	{
		cin >> arr[i];
		cnt[arr[i]] ++;
	}

	for (int i =n; i >= 1; i--)
	{
		while (!s.empty() && cnt[s.top()] <= cnt[arr[i]]) s.pop();
		if (s.empty()) ngf[i] = -1;
		else ngf[i] = s.top();

		s.push(arr[i]);
	}
	for (int i = 1; i <= n; i++)
	{
		cout << ngf[i] << ' ';
	}
	cout << '\n';
	return 0;
}