#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
int tc;

int main() {
    cin >> tc;
    while (tc --) {
        string w;
        int k;
        cin >> w >> k;
        int minn = 100000;
        int maxx = 0;
        vector<int> alpha[26];
        for(int i = 0; i < w.length(); i ++) {
            int num = w[i] - 'a';
            alpha[num].push_back(i);
        }
        
        for(int i = 0; i< 26; i ++) {
            int asize = (int)alpha[i].size();
            if (asize >= k) {
                for(int j = 0; j <= asize - k; j ++) {
                    minn = min(minn, alpha[i][j+k - 1] - alpha[i][j] + 1);
                    maxx = max(maxx, alpha[i][j+k - 1] - alpha[i][j] + 1);
                }
            }
        }
        if (minn == 100000 || maxx == 0) cout << -1 << "\n";
        else cout << minn << " " << maxx << "\n";
    }
    
    return 0;
}