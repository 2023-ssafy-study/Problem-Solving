#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#define INF 1e9
#define FASTIO cin.tie(0); cout.tie(0);

using namespace std;
int N, H, D;
pair<int, int> Start, End;
vector<pair<int, int> > Umbrella;
int Answer = INF;

void input() {
    cin >> N >> H >> D;
    for (int i = 0; i < N; i++) {
        string S;
        cin >> S;
        for (int j = 0; j < N; j++) {
            if (S[j] == 'U') {
                Umbrella.push_back(make_pair(i, j));
            }
            else if (S[j] == 'E') {
                Umbrella.push_back(make_pair(i, j));
                End = make_pair(i, j);
            }
            else if (S[j] == 'S') {
                Start = make_pair(i, j);
            }
        }
    }
}

void settings() {
    sort(Umbrella.begin(), Umbrella.end());
    do {
        int NowY = Start.first;
        int NowX = Start.second;
        int NowH = H;
        int NowU = 0;
        int Time = 0;
        for (int i = 0; i < Umbrella.size(); i++) {
            int Y = Umbrella[i].first;
            int X = Umbrella[i].second;
            Time += abs(NowY - Y) + abs(NowX - X);
            int Damage = abs(NowY - Y) + abs(NowX - X) - NowU;
            if (Damage < 0) {
                Damage = 0;
            }
            NowH -= Damage;
            if (NowH < 0) {
                break;
            }
            NowU = D;
            NowY = Y;
            NowX = X;
            if (make_pair(Y, X) == End) {
                if (NowH >= 0) {
                    Answer = min(Answer, Time);
                }
                break;
            }
            else {
                if (NowH < 0) {
                    break;
                }
            }
        }
    } while (next_permutation(Umbrella.begin(), Umbrella.end()));
}

void find_Answer() {
    if (Answer == INF) {
        cout << "-1\n";
    }
    else {
        cout << Answer << "\n";
    }
}

int main() {
    FASTIO
    input();
    settings();
    find_Answer();

    return 0;
}