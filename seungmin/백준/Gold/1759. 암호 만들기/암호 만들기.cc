#include <iostream>
#include <algorithm>
#include <vector>
#include <set>


using namespace std;
int L, C;


int main()
{
	cin >> L >> C;
	vector<string> password(C);
	vector<int> temp(C);
	for (int i = 0; i < L; i++)
	{
		temp[i] = 1;
	}
	for (int i = 0; i < C; i++)
	{
		cin >> password[i];
	}

	sort(password.begin(), password.end());

	vector<string> gather = { "a", "e", "i", "o", "u" };

	do
	{
		vector<string> word;  // 만들어진 문자
		vector<string> word2(C + 5); // 교집합
		vector<string>::iterator itr;
		for (int i = 0; i < password.size(); i++)
		{
			if (temp[i] == 1) {
				word.push_back(password[i]);
			}
		}

		itr = set_intersection(word.begin(), word.end(), gather.begin(), gather.end(), word2.begin());
		word2.resize(itr - word2.begin());
		
		if (word2.size() >= 1 && word.size() - word2.size() >= 2)
		{
			for (int i = 0; i < L; i++)
			{
				cout << word[i];
			}
			cout << '\n';
		}

	} while (prev_permutation(temp.begin(), temp.end()));
	cout << endl;



	return 0;
}