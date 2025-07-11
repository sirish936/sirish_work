package com.sirish.hackerrank;

import java.util.HashSet;
import java.util.Set;

public class MaxSumDistinctCharacters {

    public static int maxSumDistinctCharacters(String S) {
        int n = S.length();
        
        if (n <= 1) {
            return 0;
        }
        
        Set<Character> leftDistinct = new HashSet<>();
        Set<Character> rightDistinct = new HashSet<>();
        
        for (int i = 0; i < n; i++) {
            rightDistinct.add(S.charAt(i));
        }
        
        int maxSum = 0;
        
        for (int i = 0; i < n - 1; i++) {
            leftDistinct.add(S.charAt(i));
            rightDistinct.remove(S.charAt(i));
            
            int currentSum = leftDistinct.size() + rightDistinct.size();
            
            maxSum = Math.max(maxSum, currentSum);
        }
        
        return n - maxSum;
    }
    
    public static void main(String[] args) {
        String S = "abcabc";
        System.out.println(maxSumDistinctCharacters(S));  // Output: 0
    }
}