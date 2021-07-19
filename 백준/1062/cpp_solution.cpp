#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
 
const int MAX = 50;
 
int N, K, answer;
string word[MAX];
bool visited[26];


void dfs(int alpha, int cnt)
{
    if (cnt == K) {
        int temp = 0;
        for (int i = 0; i < N; i++) {
            bool flag = true;
            for(int j=0; j<word[i].length(); j++)
                if (!visited[word[i][j] - 'a']) {
                    flag = false;
                    break;
                }
 
            if (flag)
                temp++;
        }
        answer = max(answer, temp);
        return;
    }
 
    for (int c = alpha; c < 26; c++) {
        if (!visited[c]) {
            visited[c] = true;
            dfs(c, cnt + 1);
            visited[c] = false;
        }
    }
}



int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> N >> K;
    //edge case
    if (K < 5) {
        cout << 0 << "\n";
        return 0;
    }
    else if(K==26) {
        cout << N << "\n";
        return 0;
    }

    K -= 5;
    for (int i=0; i<N; i++) {
        cin >> word[i];
        //anta
        word[i] = word[i].substr(4, word[i].length());
        //tica
        for(int j=0; j<4; j++) {
            word[i].pop_back();
        }
    }
    visited['a' - 'a'] = true;
    visited['c' - 'a'] = true;
    visited['i' - 'a'] = true;
    visited['n' - 'a'] = true;
    visited['t' - 'a'] = true;

    dfs(0, 0);
    cout << answer << "\n";
    return 0;



}