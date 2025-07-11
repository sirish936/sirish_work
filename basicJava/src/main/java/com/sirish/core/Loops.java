package com.sirish.core;

public class Loops {

	public static void main() {

		for (int i = 0; i < 3; i++) {
			System.out.println(i);
			for (int j = 0; j < 3; j++) {
				if (j == 1)
					break;
				System.out.println(j);
			}
		}
	}

	public static void main(String[] args) {

		main();
		System.out.println("sirish");

	}
}
