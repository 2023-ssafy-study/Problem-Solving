#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool comp(const vector<int> &a, const vector<int> &b){
    return a[1] <= b[1];
}

int solution(vector<vector<int>> jobs) {
    int answer = 0, timer = 0, cnt = jobs.size();
    sort(jobs.begin(), jobs.end(), comp);
    while(!jobs.empty()){
        for(int i=0; i<jobs.size(); i++){
            if(jobs[i][0]<=timer){
                timer += jobs[i][1];
                answer += (timer-jobs[i][0]);
                jobs.erase(jobs.begin()+i);
                break;
            }
            if(i==jobs.size()-1) timer++;
        }
    }
    return answer/cnt;
}