package com.sirish.interview;

public class CallByValue {
	void value(int i) {
		i++;
		System.out.println(i);
		method(i++);
	}

	static void method(int i) {
		i++;
		System.out.println(i);
	}

	public static void main(final String[] args) {
		final CallByValue cbv = new CallByValue();
		int i = 12;
		cbv.value(i);
		System.out.println(i++);
	}
}
