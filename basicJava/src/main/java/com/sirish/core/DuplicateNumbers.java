package com.sirish.core;

public class DuplicateNumbers {

	public static void main(final String[] args) {
		int index = 0;
		final int output[] = new int[10];
		for (int number = 1; number <= 100; number++) {
			if (number % 11 == 0) {
				output[index] = number;
				index++;
			}
		}
		for (int i = 0; i < output.length - 1; i++) {
			System.out.println(output[i]);
		}
	}
}


private int add(int x, int y) {
	return x+y;
}