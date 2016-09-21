package com.sirish.hackerrank;

import java.util.Scanner;

public class ReadInput {
	public static void main(final String[] args) {
		final Scanner scan = new Scanner(System.in);
		final int i = scan.nextInt();
		final double d = scan.nextDouble();
		scan.nextLine();
		final String str = scan.nextLine();
		System.out.println("String: " + str);
		System.out.println("Double: " + d);
		System.out.println("Int: " + i);
	}
}
