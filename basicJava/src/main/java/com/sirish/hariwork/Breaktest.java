package com.sirish.hariwork;

public class Breaktest {

	@SuppressWarnings("unused")
	public static void main(final String[] args) {
		int count = 0;
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 5; j++) {
				count++;
				break;
			}
		}
		System.out.println(count);
		System.out.println(-Math.pow(2, 31));
	}
}
