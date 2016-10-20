package com.sirish.interview;

public class CBV {
	public static void main(final String[] args) {
		final int x = 3;
		System.out.println("Value of x before calling increment() is " + x);
		increment(x);
		System.out.println("Value of x after calling increment() is " + x);
	}

	public static void increment(int a) {
		System.out.println("Value of a before incrementing is " + a);
		a = a + 1;
		System.out.println("Value of a after incrementing is " + a);
	}
}
