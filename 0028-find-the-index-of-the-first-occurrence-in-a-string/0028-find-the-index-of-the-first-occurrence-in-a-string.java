class Solution {
    public int strStr(String haystack, String needle) {
        int nlen = needle.length();
        for (int i = 0 ; i < haystack.length() - nlen + 1; i++ ){
            if (haystack.substring(i, i+nlen).equals(needle)){
                return i;
            }
        }
        return -1;
    }
}