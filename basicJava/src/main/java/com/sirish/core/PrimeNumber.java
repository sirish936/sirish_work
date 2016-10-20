package com.sirish.core;

import java.util.Scanner;

public class PrimeNumber {

	/**
	 * @param args
	 */

	@SuppressWarnings("resource")
	public static void main(final String[] args) {
		// TODO Auto-generated method stub
		int i, j, x;
		System.out.println("enter the range of numbers to print");
		final Scanner scanner = new Scanner(System.in);
		final int range = scanner.nextInt();
		// write the loop to print the numbers
		for (i = 1; i < range; ++i) {
			for (j = 2; j < i; j++) {
				x = i % j;
				if (x == 0) {
					break;
				}

			}
			if (i == j) {
				System.out.println("prime numbers are:" + i);
			}

		}

	}

}
