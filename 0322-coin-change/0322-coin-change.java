class Solution {
    public int coinChange(int[] coins, int amount) {
        List<Integer> arr = new ArrayList();
        arr.add(0);
        // System.out.println(arr);
        for(int i = 0; i < amount; i++){
            arr.add(-1);
        }
        for (int coin : coins){
            for (int i = 0; i < arr.size(); i++){
                // System.out.println(arr);
                // System.out.println(i);
                if (arr.get(i) != -1){
                    if(i + coin < arr.size() && i+coin > 0){
                        if(arr.get(i+coin) == -1){
                            arr.set(i+coin, arr.get(i) + 1); 
                        } else {
                            arr.set(i+coin, Math.min(arr.get(i+coin),arr.get(i) + 1));
                        }
                    }
                }
            }
        }

        return arr.get(amount);
    }
}