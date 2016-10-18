package com.sirish.core;

import java.util.Scanner;

public class Conversion {

	@SuppressWarnings("resource")
	public static void main(final String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Enter the number to be converted");
		final Scanner scanner = new Scanner(System.in);
		final int number = scanner.nextInt();
		int j = number;

		System.out.println("the number is:");
		while (j != 0) {
			final int x = j % 2;
			j = j / 2;
			// int a[]=x;
			System.out.print(x);
		}
		// System.out.print(j);

	}

}
