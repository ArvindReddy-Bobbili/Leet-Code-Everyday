import java.util.HashSet;
import java.util.Set;

class Solution {
    public int[] findMissingAndRepeatedValues(int[][] grid) {
        int n = grid.length;
        int size = n * n;
        Set<Integer> seen = new HashSet<>();
        int repeated = -1, missing = -1;

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                int num = grid[i][j];
                if (seen.contains(num)) {
                    repeated = num; 
                } else {
                    seen.add(num);
                }
            }
        }

        
        for (int num = 1; num <= size; num++) {
            if (!seen.contains(num)) {
                missing = num;
                break;
            }
        }
        return new int[]{repeated, missing};
    }
}
