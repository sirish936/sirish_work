package com.sirish.hackerrank;

import java.util.Scanner;

/**
 * @author sirish.
 */
/***
 * Java class to print the numbers of the series : a+2^0b,a+2^0b+2^1b,a+2^0b+2^1b+2^2b,....+ a+2^0b+2^1b+2^(n-1)b
 */
public class NumberSeries {
	public static void main(final String[] args) {

		final Scanner scanner = new Scanner(System.in);

		// System.out.println("Enter the loop count");
		final int loopCount = scanner.nextInt();
		// System.out.println("Enter the numbers : input 1,input2,range");

		for (int i = 0; i < loopCount; i++) {
			final int a = scanner.nextInt();
			final int b = scanner.nextInt();
			final int range = scanner.nextInt();

			printSeries(a, b, range);
			System.out.println();
		}
	}

	private static void printSeries(final int a, final int b, final int range) {
		final StringBuilder sb = new StringBuilder();
		int tempSum = (int) (a + Math.pow(2, 0) * b);
		sb.append(String.valueOf(tempSum));
		for (int index = 1; index < range; index++) {
			tempSum = tempSum + (int) (Math.pow(2, index) * b);
			sb.append(String.valueOf(" " + tempSum));
		}
		System.out.printf(sb.toString());
	}
}
