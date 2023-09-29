#include <iostream>

using namespace std;

int N;
int L;
int m[100][100];
int m2[100][100];
int ans;

void check_col(int arr[][100]) {
	for (int i = 0; i < N; i ++) {
		bool flag = true;
		int count = 1;
		for (int j = 0; j < N - 1; j++) {
			if (arr[i][j] == arr[i][j + 1]) count++;
			else if (arr[i][j] == arr[i][j + 1] - 1) {
				if (count >= L) count = 1;
				else flag = false;
			}
			else if (arr[i][j] == arr[i][j + 1] + 1) {
				if (count < 0) flag = false;
				else count = -(L - 1);
			}
			else flag = false;
		}
		if (count >= 0 && flag) ans++;
	}
}




int main() {
	ans = 0;
	cin >> N >> L;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++) {
			int a;
			cin >> a;
			m[i][j] = a;
			m2[j][i] = a;
		}
	}
	check_col(m);
	check_col(m2);

	cout << ans << endl;

	return 0;
}