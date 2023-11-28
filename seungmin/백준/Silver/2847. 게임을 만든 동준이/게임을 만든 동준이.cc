#include <iostream>

using namespace std;

int N;
int cnt=0;
int arr[101];

int main() {
    cin >> N;

    for(int i=0;i<N;i++)
        cin >> arr[i];

    for(int i=N-1;i>=1;i--) {
        while(arr[i]<=arr[i-1]) {
            arr[i-1]-=1;
            cnt++;
        }
    }

    cout << cnt << endl;
}