class Solution {
    public String longestCommonPrefix(String[] strs) {
        
        int len = strs[0].length(); 
        for(String str : strs){
            if(str.length() < len){
                len = str.length();
            }
        }
        if(len == 0){
            return "";
        }
        for(int i = 0; i < len; i++){
            String s = strs[0].substring(0,i+1);
            for(int j = 0; j < strs.length; j++){
                if(!s.equals(strs[j].substring(0,i+1))){
                    System.out.println(s);
                    System.out.println(strs[j].substring(0,i+1));
                    if(i == 0){
                        return "";
                    } else{
                        return strs[j].substring(0,i);
                    }
                }
            }
        }
        return strs[0].substring(0,len);
    }
}