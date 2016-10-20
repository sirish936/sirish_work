package com.sirish.core;

import java.util.Scanner;

public class Armstrong {

	/**
	 * @param args
	 */
	@SuppressWarnings("resource")
	public static void main(final String[] args) {
		// TODO Auto-generated method stub
		int j, sum = 0;
		System.out.println("enter the number");
		final Scanner scanner = new Scanner(System.in);
		final int number = scanner.nextInt();
		j = number;
		// write the loop to check for armstrong
		while (j != 0) {
			final int k = j % 10;
			sum = sum + k * k * k;
			j = j / 10;

		}
		System.out.println(sum);

	}
}
