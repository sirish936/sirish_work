

package com.sirish.core;

import java.util.Arrays;

public class HackerCoinTest {
	public static void main(String[] args) {

		int num = 3;

		int temp = num;

		int ar[] = new int[8];

		int k = 0;

		for (int i = 1; i < num; i++) {

			for (int j = 1; j <= i; j++) {

				if (temp == 0) {
					break;
				}

				ar[k] = j;

				if (temp == 0) {
					break;
	
				
				
				
				 }
				
				temp--;
			}
			k++;
		}
		
		Arrays.sort(ar);

		System.out.println(ar[ar.length-1]);
		

	}
}
