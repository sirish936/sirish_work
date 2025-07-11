package com.sirish.hackerrank;

import java.util.HashSet;
import java.util.Set;

public class SplitString {

    public static int countValidSplits(String S) {
        int n = S.length();
        if (n < 2) {
            return 0;
        }

        int[] rightDistinctCount = new int[n];
        Set<Character> rightDistinct = new HashSet<>();

        for (int i = n - 1; i >= 0; i--) {
            rightDistinct.add(S.charAt(i));
            rightDistinctCount[i] = rightDistinct.size();
        }

        Set<Character> leftDistinct = new HashSet<>();
        int count = 0;

        for (int i = 0; i < n - 1; i++) {
            leftDistinct.add(S.charAt(i));

            if (leftDistinct.size() == rightDistinctCount[i + 1]) {
                count++;
            }
        }

        return count;
    }

    public static void main(String[] args) {
        String S = "abcdefghijklmnopqrstuvwxyz";
        System.out.println(countValidSplits(S)); // Output should be 2
    }
}