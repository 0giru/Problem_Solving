#include<iostream>
#include<string>
#include<queue>
#include<utility>

int N, M;
int arr[101][101];
int dx[4] = { -1, 1, 0, 0 };
int dy[4] = { 0, 0, -1, 1 };
std::queue<std::pair<int, int>> q;

void bfs(int sx, int sy);


int main() {

   std::cin >> N >> M;
   std::string value;

   for (int i = 0; i < N; i++) {
      std::cin >> value;
      for (int j = 0; j < M;j++) {
         if (value[j] == '1') {
            arr[i][j] = 1;
         }
         else {
            arr[i][j] = 0;
         }

      }
   }

   bfs(0, 0);

   std::cout << arr[N - 1][M - 1];

   return 0;
}

void bfs(int sx, int sy) {
   q.push(std::make_pair(sx, sy));

   while (!q.empty()) {
      std::pair<int, int> temp;
      temp = q.front();

      for (int i = 0; i < 4; i++) {
         int nx = temp.first + dx[i];
         int ny = temp.second + dy[i];

         if (nx >= 0 && nx < N) {
            if (ny >= 0 && ny < M) {
               if (arr[nx][ny] == 1) {
                  q.push(std::make_pair(nx, ny));
                  arr[nx][ny] = arr[temp.first][temp.second] + 1;
               }
            }
         }
      }
      q.pop();
   }
}
