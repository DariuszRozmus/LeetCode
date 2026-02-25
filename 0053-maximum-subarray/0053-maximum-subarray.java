class Solution {
    public int maxSubArray(int[] nums) {
        if ( nums.length == 1){
            return nums[0];
        }
        int cnt = nums[0];
        for ( int i = 1; i < nums.length; i++){
            nums[i] = Math.max(nums[i], nums[i-1] + nums[i]);
            if (nums[i] > cnt){
                cnt = nums[i];
            }
        }
        return cnt;
    }
}