class Solution {
    public int numIslands(char[][] grid) {
        int cnt = 0;
        for (int i = 0; i < grid.length; i++){
            for (int j = 0; j < grid[0].length; j++){
                if(grid[i][j] == '1'){
                    cnt += 1;
                    dfs(grid, i, j);
                }
            }
        }
        return cnt;
    }

    public void dfs(char[][] grid, int y, int x){
        if (grid[y][x] == '1'){
            grid[y][x] = '0';
        } else { 
            return;
        }
        if (x > 0){
            dfs(grid, y, x - 1);
        }
        if (y > 0){
            dfs(grid, y - 1, x);
        }
        if (y < grid.length - 1){
            dfs(grid, y + 1, x);
        }
        if (x < grid[0].length -1 ){
            dfs(grid, y, x + 1);
        }
    } 
}