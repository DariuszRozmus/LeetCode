class Solution {
    public int lengthOfLastWord(String s) {
        String[] a = s.split(" ");
        // System.out.println(a.length);
        int cnt = 0; 
        for (String str : a){
            if(str.length() > cnt){
                cnt = a[a.length -1].length();
            }
            
        }
        return cnt;
    }
}