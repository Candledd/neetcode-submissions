class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> s_map = new HashMap<>();
        HashMap<Character, Integer> t_map = new HashMap<>();
        
        for (Character letter : s.toCharArray()){
            s_map.put(letter, s_map.getOrDefault(letter, 0)+1);
        }
        for (Character letter : t.toCharArray()){
            t_map.put(letter, t_map.getOrDefault(letter, 0)+1);
        }

        return s_map.equals(t_map);
    }
}
