#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;
int N;
int Alphabet[26];
vector<string> S;


void input()
{
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		string ts;
		cin >> ts;
		S.push_back(ts);
	}
}
bool compare(int i, int j)
{
	return j < i;
}
void solution()
{
	for (int i = 0; i < N; i++)
	{
		string ts = S[i];
		int num = 1;
		for (int j = ts.size() -1 ; j >= 0; j--)
		{
			int temp = ts[j] - 'A';
			Alphabet[temp] = Alphabet[temp] + num;
			num *= 10;
		}
	}
	sort(Alphabet, Alphabet + 26, compare);
	int Ans = 0;
	int cnt = 9;
	for (int i = 0; i < 26; i++)
	{
		if (Alphabet[i])
		{
			Ans += (Alphabet[i] * cnt);
			cnt--;
		} else 
		{
			break;
		}
	}
	cout << Ans << endl;
}


int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	input();
	solution();

	return 0;
}