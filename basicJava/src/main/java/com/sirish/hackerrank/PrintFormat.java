package com.sirish.hackerrank;

import java.util.Scanner;

public class PrintFormat {
	public static void main(final String[] args) {
		final Scanner sc = new Scanner(System.in);
		System.out.println("================================");
		for (int i = 0; i < 3; i++) {
			final String s1 = sc.next();
			final int x = sc.nextInt();
			System.out.printf("%-15s", s1);
			System.out.printf("%03d", x);
			System.out.println();
		}
		System.out.println("================================");

	}

}
