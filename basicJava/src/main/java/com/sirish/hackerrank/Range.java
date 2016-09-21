package com.sirish.hackerrank;

import java.util.Scanner;

public class Range {
	public static void main(final String[] argh) {

		final Scanner sc = new Scanner(System.in);
		final int t = sc.nextInt();

		for (int i = 0; i < t; i++) {
			try {
				final long x = sc.nextLong();
				System.out.println(x + " can be fitted in:");
				if (x >= -128 && x <= 127) {
					System.out.println("* byte");
					System.out.println("* short");
					System.out.println("* int");
					System.out.println("* long");
				} else if (x >= -32768 && x <= 32767) {
					System.out.println("* short");
					System.out.println("* int");
					System.out.println("* long");
				} else if (x >= -Math.pow(2, 31) && x < Math.pow(2, 31)) {
					System.out.println("* int");
					System.out.println("* long");
				} else {
					System.out.println("* long");
				}
			} catch (final Exception e) {
				System.out.println(sc.next() + " can't be fitted anywhere.");
			}
		}
	}
}
