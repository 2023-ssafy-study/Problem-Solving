#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int year[367] = { 0, };
	int n, height = 0, width = 0, ans = 0;
	vector<pair<int, int>> plan;
	cin >> n;
	for (int k = 0, s, e; k < n; k++) {
		cin >> s >> e;
		plan.push_back({ s,e });
	}

	for (auto& p : plan) {
		for (int i = p.first; i <= p.second; i++) {
			year[i] ++;
		}
	}

	for (int i = 1; i <= 366; i++) {
		if (year[i])
		{
			height = max(height, year[i]);
			width++;
		}
		else
		{
			ans += width * height;
			width = 0;
			height = 0;
		}
	}

	cout << ans << endl;
}