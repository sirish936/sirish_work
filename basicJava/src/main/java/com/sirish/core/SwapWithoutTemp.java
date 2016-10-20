package com.sirish.core;

import java.util.Scanner;

public class SwapWithoutTemp {
	@SuppressWarnings("resource")
	public static void main(final String args[]) {
		int n1, n2;
		final Scanner scan = new Scanner(System.in);
		System.out.println("Please Enter No 1: ");
		n1 = scan.nextInt();
		System.out.println("Please Enter No 2: ");
		n2 = scan.nextInt();
		n1 = n1 + n2;
		n2 = n1 - n2;
		n1 = n1 - n2;
		System.out.println("First No: " + n1);
		System.out.println("Second No: " + n2);

	}

}
