#include<iostream>
#include<algorithm>

using namespace std;

int D, W, K;
int graph[13][20];
int ans = 20;


bool test_w(int w)
{
	int max_count = 0;
	int count = 1;
	for (int i = 1; i < D; i++)
	{
		if (graph[i - 1][w] == graph[i][w]) count++;
		else count = 1;
		if (max_count < count) max_count = count;
	}
	if (max_count >= K) return true;
	else return false;
}


bool check_graph()
{
	for (int i = 0; i < W; i++)
	{
		if (!test_w(i)) return false;
	}
	return true;
}



void recursion_solve(int count, int depth)
{
	if (count >= ans) return;
	if (check_graph())
	{
		ans = count;
		return;
	}

	if (depth == D) return;

	int copy_graph[13][20];
	copy(&graph[0][0], &graph[0][0] + 13 * 20, &copy_graph[0][0]);

	// 1번 재귀 안바꾸고 갓을때
	recursion_solve(count, depth + 1);

	// 2번 재귀 depth 행을 A로 바꿀때
	for (int i = 0; i < W; i++) graph[depth][i] = 0;
	recursion_solve(count + 1, depth + 1);
	copy(&copy_graph[0][0], &copy_graph[0][0] + 13 * 20, &graph[0][0]); // 초기화

	// 3번 재귀 depth 행을 B로 바꿀때
	for (int i = 0; i < W; i++) graph[depth][i] = 1;
	recursion_solve(count + 1, depth + 1);
	copy(&copy_graph[0][0], &copy_graph[0][0] + 13 * 20, &graph[0][0]); // 초기화
}

int main(int argc, char** argv)
{
	int test_case;
	int T;

	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case)
	{
		cin >> D >> W >> K;
		for (int i = 0; i < D; i++)
		{
			for (int j = 0; j < W; j++)
			{
				cin >> graph[i][j];
			}
		}

		if (K == 1)
		{
			cout << '#' << test_case << ' ' << 0 << '\n';
			continue;
		}

		recursion_solve(0, 0);
		cout << '#' << test_case << ' ' << ans << '\n';
		ans = 20; // 초기화 해줘야함
	}
	return 0;
}