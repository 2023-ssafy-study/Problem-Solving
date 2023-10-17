#include <iostream>
#include <stack>
#include <string>

using namespace std;

stack<char> s;
string str;

int main() {
    ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    cin >> str;
    int n = str.size() - 1;
    int ans = 0;
    stack<pair<int, int>> temp; // {depth, count}
    bool flag = false;
    s.push(str[n]);
    n--;
    int depth = 1;
    while (n >= 0)
    {
        if (!s.empty() && str[n] == '(' && s.top() == ')')
        {
            if (flag || temp.empty())
            {
                temp.push({ depth, 2 });

            }
            else {
                int td = temp.top().first;
                int tn = temp.top().second;
                temp.pop();
                while (!temp.empty() && td == temp.top().first)
                {
                    tn += temp.top().second;
                    temp.pop();
                }
                temp.push({ depth, tn * 2 });
            }
            flag = false;
            depth--;
            n--;
            s.pop();
            continue;
        }

        if (!s.empty() && str[n] == '[' && s.top() == ']')
        {
            if (flag || temp.empty())
            {
                temp.push({ depth, 3 });

            }
            else {
                int td = temp.top().first;
                int tn = temp.top().second;
                temp.pop();
                while (!temp.empty() && td == temp.top().first)
                {
                    tn += temp.top().second;
                    temp.pop();
                }
                temp.push({ depth, tn * 3 });
            }
            flag = false;
            depth--;
            n--;
            s.pop();
            continue;
        }

        flag = true;
        s.push(str[n]);
        depth++;
        n--;

    }

    if (s.empty())
    {
        while (!temp.empty())
        {
            ans += temp.top().second;
            temp.pop();
        }
        cout << ans << '\n';
    }
    else {
        cout << 0 << '\n';
    }
    return 0;
}