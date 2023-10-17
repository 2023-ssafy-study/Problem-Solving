#include <iostream>
#include <stack>
#include <string>

using namespace std;

string s;
stack<char> st;

int main()
{
    cin >> s;
    int ans = 0;
    for(int i = 0; i < s.size(); i ++)
    {
        if (s[i] == '(') st.push('(');
        else
        {
            st.pop();
            if (s[i-1] == ')') ans ++;
            else ans += st.size();
        }
    }
    cout << ans << '\n';
    return 0;
}