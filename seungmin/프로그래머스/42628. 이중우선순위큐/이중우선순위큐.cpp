#include <string>
#include <vector>
#include <iostream>
#include <queue>
#include <string>

using namespace std;

vector<int> solution(vector<string> operations) {
    vector<int> answer(2);
    priority_queue<int, vector<int>, greater<int>> pq_asc;
    priority_queue<int, vector<int>> pq_des;
    int cnt = 0;
    
    for(string op : operations) {
        // 큐가 비었으면 싹 초기화
        if(!cnt) {
            while(!pq_asc.empty()) pq_asc.pop();
            while(!pq_des.empty()) pq_des.pop();
        }
        
        // 삽입
        if(op[0] == 'I') {
            pq_des.push(stoi(op.substr(2)));
            pq_asc.push(stoi(op.substr(2)));
            cnt++;
        }
        // 삭제
        else {
            // 빈 큐에 데이터를 삭제하라는 연산일 경우 무시
            if(!cnt) continue;
            
            // 최댓값 삭제
            if(op[2] == '1') {
                pq_des.pop();
                cnt--;
            }
            // 최솟값 삭제
            else {
                pq_asc.pop();
                cnt--;
            }
        }
        
    }
    
    if(cnt) {
        answer[0] = pq_des.top();
        answer[1] = pq_asc.top();
    }
    
    return answer;
}