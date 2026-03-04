class Solution {
    public int maxSubarraySumCircular(int[] nums) {
        int res = nums[0];
        int min = nums[0];
        int total = nums[0];
        int[] num = nums.clone();
        for (int i = 1; i < num.length; i++){
            total += num[i];
            if (num[i] < num[i-1] + num[i]){
                num[i] = num[i-1] + num[i];
            }
            if (res < num[i]){
                res = num[i];
            }
        }
        if (res < 0){
            return res;
        }
        int[] num2 = nums.clone();
        for (int i = 1; i < num2.length; i++){
            if (num2[i] > num2[i-1] + num2[i]){
                num2[i] = num2[i-1] + num2[i];
            }
            if (min > num2[i]){
                min = num2[i];
            }
        }
        if (res < total - min){
            res = total - min;
        }
        return res;
    }
}