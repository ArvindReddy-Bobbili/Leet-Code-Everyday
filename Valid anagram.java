class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character,Integer> hm = new HashMap<>();
        Map<Character, Integer> hm2 = new HashMap<>();
        if(t.length() != s.length())
        {
            return false;
        }
        for( int i =0; i<t.length(); i++)
            {
                char c = t.charAt(i);
                char a = s.charAt(i);
                hm.put(c, hm.getOrDefault(c,0)+1);
                hm2.put(a,hm2.getOrDefault(a,0)+1);
            }
        if(hm.equals(hm2))
        {
            return true;
        }
        else
        {
            return false;
        }
        
    }
}