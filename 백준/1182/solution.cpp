#include <iostream>
#include <algorithm>
#include <sstream>

using namespace std;
int arr[20];
int N, S;
int answer = 0;

void dfs(int ind, int total) {
    if (total == S) {
        answer++;
    }
    if (ind < N) {
        for (int i=ind+1;i<N;i++) {
            dfs(i, total + arr[i]);
        }
    }
}

int main() {
    cin>>N>>S;
    for(int i=0;i<N;i++) {
        cin >> arr[i];
    }
    for(int i=0;i<N;i++) {
        dfs(i, arr[i]);
    }
    cout << answer << '\n';
    return 0;
}