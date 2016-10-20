package com.sirish.core;

import java.util.Scanner;

public class Pascal {

	/**
	 * @param args
	 */
	@SuppressWarnings("resource")
	public static void main(final String[] args) {
		// TODO Auto-generated method stub
		System.out.println("enter the number rows");
		final Scanner scanner = new Scanner(System.in);
		final int range = scanner.nextInt();
		// write the loop
		for (int i = 0; i < range; ++i) {
			int a = 1;
			for (int b = 0; b < range - 1; b++) {
				System.out.println();
			}
			for (int x = 0; x <= i; x++) {
				System.out.print(a);
				a = a * (i - x) / (x + 1);
			}
		}
	}
}
