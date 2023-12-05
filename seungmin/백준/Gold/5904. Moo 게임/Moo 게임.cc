#include <iostream>
#include <vector>
using namespace std;

int n;
char s1[3] = {'m', 'o','o'};

void solution(int n, int k, int len){
    int new_len = len*2 + k+3;
    if(n<=3){
        cout << s1[n-1] << "\n";
        exit(0);
    }
    if(new_len < n){
        solution(n, k+1, new_len);
    }
    else{
        if(n > len && n <= len+k+3){
            if(n-len != 1)
                cout << "o" << "\n";
            else
                cout << "m" << "\n";
            exit(0);
        }
        else{
            solution(n-(len+k+3), 1, 3);
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> n;
    
    solution(n, 1, 3);
    
    return 0;
    
}