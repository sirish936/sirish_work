package com.sirish.core;

import java.util.Scanner;

public class SumOfDigits {
	@SuppressWarnings("resource")
	public static void main(final String args[]) {
		int n, sum = 0, i, res;
		final Scanner scan = new Scanner(System.in);
		System.out.println("Please Enter No.: ");
		n = scan.nextInt();
		i = n;
		while (i != 0) {
			res = i % 10;
			sum += res;
			i = i / 10;
		}
		System.out.println("Sum is: " + sum);

	}
}
