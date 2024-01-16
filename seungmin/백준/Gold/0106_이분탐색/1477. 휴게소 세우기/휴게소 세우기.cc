#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
int n,m,l;
vector<int> v;
bool chk(int mid){
	int cnt = 0;
	for(int i=1; i<v.size(); i++){
		int dist = v[i] - v[i-1];
		cnt += dist / mid;
		if(dist % mid == 0){
			cnt--;
		}
	}
	return cnt > m;
}
int main(void){
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	cin >> n >> m >> l;
	
	v.push_back(0);
	v.push_back(l);
	
	for(int i=0; i<n; i++){
		int x; cin >> x;
		v.push_back(x);
	}
	sort(v.begin(), v.end());
	
	int st = 1, en = l;
	int mid,ret=0;
	while(st <= en){
		mid = (st + en) / 2;
		if(chk(mid)){
			st = mid + 1;
		}else{
			ret = mid;
			en = mid - 1;
		}
	}
	
	cout << ret;
	return 0;
}