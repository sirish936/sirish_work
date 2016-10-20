package com.sirish.core;

import java.util.Scanner;

public class Biggest3 {
	@SuppressWarnings("resource")
	public static void main(final String args[]) {
		int n1, n2, n3, big;
		final Scanner scan = new Scanner(System.in);
		System.out.println("Please Enter No 1: ");
		n1 = scan.nextInt();
		System.out.println("Please Enter No 2: ");
		n2 = scan.nextInt();
		System.out.println("Please Enter No 3: ");
		n3 = scan.nextInt();
		if (n1 > n2) {
			if (n1 > n3) {
				big = n1;
			} else {
				big = n3;
			}
		} else {
			if (n2 > n3) {
				big = n2;
			} else {
				big = n3;
			}
		}
		System.out.println("Biggest No: " + big);
	}
}
