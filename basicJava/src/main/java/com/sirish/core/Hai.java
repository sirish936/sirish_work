package com.sirish.core;

import java.util.Scanner;

public class Hai {

	public static void main(final String args[]) {

		final Scanner sc = new Scanner(System.in);
		final int input = sc.nextInt();
		System.out.println(Hai.Grade(input));
	}

	static String Grade(final int num) {
		final String str1 = "Grade A";
		final String str2 = "Grade B";
		final String str3 = "Grade C";
		final String str4 = "Fail";

		if (num >= 90 && num <= 100) {
			return str1;
		}
		if (num >= 80 && num <= 89) {
			return str2;
		}
		if (num >= 70 && num <= 79) {
			return str3;
		}
		return str4;
	}
}
