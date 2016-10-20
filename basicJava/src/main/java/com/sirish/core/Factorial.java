package com.sirish.core;

import java.util.Scanner;

public class Factorial {
	@SuppressWarnings("resource")
	public static void main(final String args[]) {
		int n, i, prod = 1;
		final Scanner scan = new Scanner(System.in);
		System.out.println("Please Enter a No.");
		n = scan.nextInt();
		for (i = n; i >= 1; i--) {
			prod *= i;
		}
		System.out.println("Factorial of " + n + " is  " + prod);
	}

}
