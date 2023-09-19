#include <iostream>
#include <vector>
#include <math.h>

#define MAX 1000001

using namespace std;
int n, m, k;
long long arr[MAX];

long long make_Tree(vector<long long> &tree, int node, int start, int end)
{
	if (start == end) return tree[node] = arr[start];

	int mid = (start + end) / 2;

	return tree[node] = make_Tree(tree, node * 2, start, mid) + make_Tree(tree, node * 2 + 1, mid + 1, end);
}

void update_Tree(vector<long long> &tree, int node, int start, int end, int idx, long long diff)
{
	if (idx<start || idx > end) return;
	tree[node] += diff;
	if (start != end) 
	{
		int mid = (start + end) / 2;
		update_Tree(tree, node * 2, start, mid, idx, diff);
		update_Tree(tree, node * 2 + 1, mid + 1, end,idx, diff);
	}
}

long long sum_Tree(vector<long long>& tree, int node, int left, int right, int start, int end)
{
	if (left > end || right < start) return 0;
	if (left <= start && right >= end) return tree[node];
	int mid = (start + end) / 2;
	return sum_Tree(tree, node * 2, left, right, start, mid) + sum_Tree(tree, node * 2 + 1, left, right, mid + 1, end);
}

int main() 
{
	ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	cin >> n >> m >> k;
	for (int i = 0; i < n; i++)
	{
		cin >> arr[i];
	}
	int Depth = ceil(log2(n));
	int treeSize = 1 << (Depth + 1);
	vector<long long> s_tree(treeSize);
	make_Tree(s_tree, 1, 0, n-1);

	for (int i = 0; i < m + k; i++)
	{
		int a, b;
		long long c;
		cin >> a >> b >> c;
		if (a == 1)
		{
			update_Tree(s_tree, 1, 0, n - 1, b - 1, c - arr[b - 1]);
			arr[b - 1] = c;
		}
		else
		{
			cout << sum_Tree(s_tree, 1, b - 1, c - 1, 0, n - 1) << '\n';
		}

	}

	return 0;
}