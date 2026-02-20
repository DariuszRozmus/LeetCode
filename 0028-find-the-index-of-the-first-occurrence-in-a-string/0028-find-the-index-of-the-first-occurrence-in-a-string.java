class Solution {
    public int strStr(String haystack, String needle) {
        int nlen = needle.length();
        for (int i = 0 ; i < haystack.length() - nlen + 1; i++ ){
            // System.out.println(nlen);
            // System.out.println(needle);
            // System.out.println(haystack.substring(i, i+nlen));
            if (haystack.substring(i, i+nlen).equals(needle)){
                return i;
            }
        }
        return -1;
    }
}