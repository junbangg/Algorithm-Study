#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <queue>
using namespace std;
#define MAX 100

int N;
int M;
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};
int arr[MAX][MAX] = {0, };
bool visited[MAX][MAX] = {false, };

int bfs(int x, int y, int count) {
    // queue <pair <pair <int, int>, int>> q;
    queue <pair <pair <int, int>, int>> q;
    q.push(make_pair(make_pair(x, y), count));



}

int main() {
    
    cin >> N >> M;
    // initialize array
    for (int i=0; i<N; i++) {
        string temp;
        cin >> temp;
        for (int j=0; j<M; j++) {
            arr[i][j] = temp[j] - '0';
        }
    }
    visited[0][0] = true;

    cout << bfs(0, 0, 1) << endl;
    return 0;


}
