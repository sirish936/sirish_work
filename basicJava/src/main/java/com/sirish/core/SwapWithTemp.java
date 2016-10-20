package com.sirish.core;

import java.util.Scanner;

public class SwapWithTemp {
	@SuppressWarnings("resource")
	public static void main(final String args[]) {
		int n1, n2, temp;
		final Scanner scan = new Scanner(System.in);
		System.out.println("Please Enter No 1: ");
		n1 = scan.nextInt();
		System.out.println("Please Enter No 2: ");
		n2 = scan.nextInt();
		temp = n1;
		n1 = n2;
		n2 = temp;
		System.out.println("First No: " + n1);
		System.out.println("Second No: " + n2);

	}
}
