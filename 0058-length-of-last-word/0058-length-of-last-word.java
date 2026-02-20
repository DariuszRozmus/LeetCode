class Solution {
    public int lengthOfLastWord(String s) {
        String[] a = s.split(" ");
        // System.out.println(a.length);
        int cnt = 0; 
        cnt = a[a.length -1].length();
        return cnt;
    }
}