import java.util.*;

class Solution {    
    int INF = 50000;
    public int solution(int[][] info, int n, int m) {
        int answer = dp(info, n, m);

        if(answer == INF) return -1;
        return answer;
    }

    int dp(int[][] info, int n, int m){
        int size = info.length;
        int[][] memo = new int[size + 1][m];
        for(int i = 1; i < size + 1; i++) Arrays.fill(memo[i], INF);

        int a, b;
        for(int i = 1; i < size + 1; i++){
            a = info[i - 1][0];
            b = info[i - 1][1];

            for(int j = 0; j < m; j++){
                memo[i][j] = Math.min(memo[i][j], memo[i - 1][j] + a);
                if(j + b < m) {
                    memo[i][j + b] = Math.min(memo[i - 1][j], memo[i][j + b]);
                }
            }
        }
        int ans = INF;
        for(int i = 0; i < m; i++) {
            if(memo[size][i] < n) ans = Math.min(ans, memo[size][i]);
        }
        return ans;
    }
}