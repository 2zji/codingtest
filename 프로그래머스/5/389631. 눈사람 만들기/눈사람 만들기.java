import java.util.*;

class Solution {
    
    int dx[] = {1,0,-1,0};
    int dy[] = {0,1,0,-1};
    
    public long solution(String[] grid) {
        
        int snowball[][] = new int[2][2];
        int n = grid.length;
        int m = grid[0].length();
        
        int snowballIdx = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(grid[i].charAt(j) == 'o'){
                    snowball[snowballIdx][0] = j;
                    snowball[snowballIdx][1] = i;
                    snowballIdx++;
                }
            }
        }
        
        boolean been[][][] = new boolean[2][n][m];
        long sharedBlocks = 0;
        long aOnlyBlocks = 0;
        long bOnlyBlocks = 0;
        
        int threeWays[][] = new int[2][3];
        threeWays[0][2] = -1;
        threeWays[1][2] = -1;
        
        long snowballDistance = n * m + 1;
        boolean isCase2 = false;
        
        for(int s = 0; s < 2; s++){
            Queue<int[]> queue = new LinkedList<>();
            queue.add(new int[]{snowball[s][0], snowball[s][1], 0});
            
            been[s][snowball[s][1]][snowball[s][0]] = true;
            
            while(!queue.isEmpty()){
                int p[] = queue.poll();
                int x = p[0];
                int y = p[1];
                int dis = p[2];
                
                int nx, ny;
                int choices = 0;
                for(int i = 0; i < 4; i++){
                    nx = x + dx[i];
                    ny = y + dy[i];

                    if(nx < 0 || nx >= m || ny < 0 || ny >= n || grid[ny].charAt(nx) == '#'){
                        continue;
                    }

                    choices++;

                    if(been[s][ny][nx]){
                        continue;
                    }
                    
                    if(grid[ny].charAt(nx) == 'o'){
                        snowballDistance = Math.min(snowballDistance, dis + 1);
                        continue;
                    }
                    
                    been[s][ny][nx] = true;

                    queue.add(new int[]{nx, ny, dis+1});
                }

                if(choices >= 3){

                    if(s == 1 && been[0][y][x] && grid[y].charAt(x) == '.'){
                        isCase2 = true;
                    }

                    if(threeWays[s][2] == -1){
                        threeWays[s][0] = x;
                        threeWays[s][1] = y;
                        threeWays[s][2] = dis;    
                    }

                }
                
            }
            
        }
        
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                
                if(grid[i].charAt(j) == 'o'){
                    continue;
                }
                else if(been[0][i][j] && been[1][i][j]){
                    sharedBlocks ++;
                }
                else if(been[0][i][j]){
                    aOnlyBlocks++;
                }
                else if(been[1][i][j]){
                    bOnlyBlocks++;
                }
            }
        }
        
        if(threeWays[0][2] == -1 && threeWays[1][2] == -1){

            return calculateAnswer(1, snowballDistance, sharedBlocks, Math.min(aOnlyBlocks, bOnlyBlocks),
                                  Math.max(aOnlyBlocks, bOnlyBlocks), 250001);
        }
        
        if((threeWays[0][2] != -1 && threeWays[1][2] != -1 ) || isCase2){
            return calculateAnswer(2, snowballDistance, sharedBlocks, aOnlyBlocks, bOnlyBlocks, 0);   
        }
        
        if(threeWays[0][2] == -1){
            
            return calculateAnswer(3, snowballDistance, sharedBlocks, aOnlyBlocks, bOnlyBlocks
                                   , threeWays[1][2]);
        } else {
            
            return calculateAnswer(3, snowballDistance, sharedBlocks, bOnlyBlocks, aOnlyBlocks
                                   , threeWays[0][2]);
        } 
        
    }
    
    long calculateAnswer(int caseType, long snowballDistance, long sharedBlocks, long aOnlyBlocks,
                         long bOnlyBlocks, long disToThreeWay){
        long ret = 0;
        
        long sum = sharedBlocks + aOnlyBlocks + bOnlyBlocks;
       
        for(long i = snowballDistance-1; i <= sum; i++){
            
            if(caseType == 3 && i > sharedBlocks + aOnlyBlocks + disToThreeWay + 1){
                sharedBlocks ++;
            }
            
            if(caseType == 2){
                ret += i/2 + 1;
            } else{
                ret += Math.min(i/2 + 1, aOnlyBlocks + sharedBlocks + 1) ;
            }
            
            if(caseType == 1 && i > bOnlyBlocks + sharedBlocks){
                ret -= i - bOnlyBlocks - sharedBlocks;
            }
        }
        
        return ret;
    }
}