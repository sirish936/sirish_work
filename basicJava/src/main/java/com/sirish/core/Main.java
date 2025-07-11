package com.sirish.core;

import java.util.*;

public class Main {
    public static int solution(ArrayList<Integer> arr) {
        int ans = Integer.MIN_VALUE;
        int result = -1;
        ArrayList<Integer> weight = new ArrayList<>(Collections.nCopies(arr.size(), 0));
        for (int i = 0; i < arr.size(); i++) {
            int source = i;
            int dest = arr.get(i);
            if (dest != -1) {
                weight.set(dest, weight.get(dest) + source);
                if (ans <= weight.get(dest)) {
                    ans = Math.max(ans, weight.get(dest));
                    result = dest;
                }
            }
        }
        if (ans != Integer.MIN_VALUE)
            return result;
        return -1;
    }

    public static void main(String[] args) {
        ArrayList<Integer> arr = new ArrayList<>(Arrays.asList(1, 3, 0, 2));
        System.out.println(solution(arr));
    }
}