package com.sirish.core;

import java.util.List;

public class HariTest {
	public static void main(String[] args) {
		int i=3;
		display(i);
		System.out.println(i);
	}
	private static void display(int i) {
		i++;
		System.out.println(i++);
	}
}