package com.sirish.inner;

public class Nesting {
	public static void main(final String[] args) {
		final B.C obj = new B().new C();
		System.out.println("hai " + obj.val);
	}
}

class A {
	int val;

	A(final int v) {
		val = v;
	}
}

class B extends A {
	int val = 1;

	B() {
		super(2);
	}

	class C extends A {
		int val = 3;

		C() {
			super(4);
			System.out.println(B.this.val);
			System.out.println(C.this.val);
			System.out.println(super.val);
		}
	}
}