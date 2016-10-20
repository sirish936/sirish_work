package com.sirish.strings;

import java.util.Scanner;

public class ReverseString {

	/**
	 * @param args
	 */
	@SuppressWarnings("resource")
	public static void main(final String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Enter any String");
		final Scanner scanner = new Scanner(System.in);
		final String string = scanner.next();
		// reverse the string using for loop
		for (int i = string.length() - 1; i >= 0; --i) {
			final char ch = string.charAt(i);
			System.out.print(ch);

		}

	}

}
