#include<iostream>
#include<queue>
#include<string>

#define MAX 50
using namespace std;
 
int N;
int MAP[MAX][MAX];
int Visit[MAX][MAX];
 
int dx[] = { 0, 0, 1, -1 };
int dy[] = { 1, -1, 0, 0 };
 
int Min(int A, int B) { if (A < B) return A; return B; }
 
void Input()
{
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        string S; cin >> S;
        for (int j = 0; j < S.length(); j++)
        {
            MAP[i][j] = S[j] - '0';
        }
    }
}
 
void Solution()
{
    for (int i = 0; i < MAX; i++)
    {
        for (int j = 0; j < MAX; j++)
        {
            Visit[i][j] = 987654321;
        }
    }
 
    queue<pair<int, int>> Q;
    Q.push(make_pair(0, 0));
    Visit[0][0] = 0;
 
    while (Q.empty() == 0)
    {
        int x = Q.front().first;
        int y = Q.front().second;
        Q.pop();
 
        for (int i = 0; i < 4; i++)
        {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx >= 0 && ny >= 0 && nx < N && ny < N)
            {
                if (MAP[nx][ny] == 1)
                {
                    if (Visit[nx][ny] > Visit[x][y])
                    {
                        Visit[nx][ny] = Visit[x][y];
                        Q.push(make_pair(nx, ny));
                    }
                }
                else
                {
                    if (Visit[nx][ny] > Visit[x][y] + 1)
                    {
                        Visit[nx][ny] = Visit[x][y] + 1;
                        Q.push(make_pair(nx, ny));
                    }
                }
            }
        }
    }
}
 
void Solve()
{
    Input();
    Solution();
    cout << Visit[N - 1][N - 1] << endl;
}
 
int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
 
    Solve();
 
    return 0;
}