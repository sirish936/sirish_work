package com.sirish.hackerrank;

import java.util.Scanner;

public class staticAreaTest {
	static int breath;
	static int height;
	static boolean flag = false;

	static {
		final Scanner scanner = new Scanner(System.in);
		breath = scanner.nextInt();
		height = scanner.nextInt();

		if (breath > 0 & height > 0) {
			flag = true;
		} else {
			try {
				throw new Exception("Breadth and height must be positive");
			} catch (final Exception e) {
				System.out.println("java.lang.Exception: " + e.getMessage());
			}
		}
	}

	public static void main(final String[] args) {
		if (flag) {
			final int area = breath * height;
			System.out.print(area);
		}
	}
}
