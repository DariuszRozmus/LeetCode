class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] sTable = s.split(" ");
        Map<String,String> map = new HashMap<>();
        Map<String,String> mapTwo = new HashMap<>();
        if (sTable.length != pattern.length()){
            return false;
        }
        for (int i = 0; i < pattern.length(); i++){
            String a = pattern.substring(i, i+1);
            if (map.get(a) == null){
                if (mapTwo.get(sTable[i]) == null){
                    map.put(a, sTable[i]);
                    mapTwo.put(sTable[i], a);
                } else {
                    return false;
                }
            } else {
                if (!map.get(a).equals(sTable[i])){
                    return false;
                }
                if (mapTwo.get(sTable[i]) == null){
                    return false;
                }
            }
        }
        return true;
    }
}




























        // Map<String, String> map = new HashMap();
        // Map<String, String> map2 = new HashMap();
        // String[] sArr = s.split(" ");
        // for (int i = 0; i < pattern.length(); i++){
        //     String key = pattern.substring(i, i+1);
        //     String sCurr = sArr[i];
        //     if (map.get(key) == null){
        //         if (map2.get(sCurr) != null){
        //             if (!map2.get(sCurr).equals(key)){
        //                 return false;
        //             }
        //         }
        //         map.put(key, sCurr);
        //         map2.put(sCurr, key);
        //     }
        //     if (!map.get(key).equals(sCurr)){
        //         return false;
        //     }
        //     if (!map2.get(sCurr).equals(key)){
        //         return false;
        //     }
        // }
        // return true;