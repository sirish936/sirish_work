package com.sirish.inner;

public class MyClass {
	public static void main(final String[] args) {
		final Outer outer = new Outer();
		System.out.println(outer.new Inner().gerSecret());
	}
}

class Outer {
	int secret;

	Outer() {
		secret = 123;
	}

	class Inner {
		int gerSecret() {
			return secret;
		}
	}
	// Inner createInner(){
	// return new Inner();
	// }
}
