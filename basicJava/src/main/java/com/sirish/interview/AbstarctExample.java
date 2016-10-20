package com.sirish.interview;

public abstract class AbstarctExample {

	public abstract void method1();

	// public static void method2();

	public void method3() {

	}

	public static void method4() {

	}
}

class MyAbstarct extends AbstarctExample {

	@Override
	public void method1() {
		System.out.println("from subclass");
	}

	@Override
	public void method3() {

	}

	// @Override
	public static void method4() {

	}
}
