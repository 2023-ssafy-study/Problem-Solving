#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#define MAX 100001
#define LL long long
#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);

using namespace std;
int N, T, K, S, E;
int DP[MAX];
int Sum[MAX];
int Maximum;
pair<int, int> Answer;

void input() {
    cin >> N >> T;
    for (int i = 0; i < N; i++) {
        cin >> K;
        while (K--) {
            cin >> S >> E;
            S++;
            DP[S]++;
            DP[E + 1]--;
        };
    }
}

void settings() {
    for (int i = 1; i < MAX; i++) {
        Sum[i] = Sum[i - 1] + DP[i];
    }
    for (int i = 1; i <= T; i++) {
        Maximum += Sum[i];
    }
    Answer = make_pair(0, T);
    int Now = Maximum;
    for (int i = (T + 1); i < MAX; i++) {
        Now += (Sum[i] - Sum[i - T]);
        if (Maximum < Now) {
            Maximum = Now;
            Answer = make_pair(i - T, i);
        }
    }
}

void find_Answer() {
    cout << Answer.first << " " << Answer.second << "\n";
}

int main() {
    FASTIO
    input();
    settings();
    find_Answer();

    return 0;
}