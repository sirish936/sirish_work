package com.sirish.core;

import java.util.Scanner;

public class BinaryToDecimal {
	@SuppressWarnings("resource")
	public static void main(final String[] args) {
		System.out.println("Enter the binary number:");
		final Scanner sc = new Scanner(System.in);
		final String str = sc.next();
		long num = Long.parseLong(str);
		long rem;
		while (num > 0) {
			rem = num % 10;
			num = num / 10;
			if (rem != 0 && rem != 1) {
				System.out.println("This is not a binary number.");
				System.out.println("Please try once again.");
				System.exit(0);
			}
		}
		final int i = Integer.parseInt(str, 2);
		System.out.println("Decimal:=" + i);
	}
}
