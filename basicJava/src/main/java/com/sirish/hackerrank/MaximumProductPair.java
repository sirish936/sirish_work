package com.sirish.hackerrank;

public class MaximumProductPair {
    public static void main(String[] args) {
        int[] nums = {-10,-3,5,6,-2}; // The integer array
        
        int maxProduct = Integer.MIN_VALUE;
        int maxIndex1 = -1;
        int maxIndex2 = -1;
        
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                int product = nums[i] * nums[j];
                if (product > maxProduct) {
                    maxProduct = product;
                    maxIndex1 = i;
                    maxIndex2 = j;
                }
            }
        }
        
        if (maxIndex1 != -1 && maxIndex2 != -1) {
            System.out.println("Maximum product pair: " + nums[maxIndex1] + " and " + nums[maxIndex2]);
            System.out.println("Maximum product: " + maxProduct);
        } else {
            System.out.println("No pair found in the array.");
        }
    }
}

