package com.sirish.scalar;

public class ScalarTest2 {
	public static int fib(int a) {
		if (a <= 1) return a;
		int x = fib(a-1);
		int y = fib(a-2);
		return x + y;
	}
	public static void main(String[] args) {
		int ans = fib(5);
		System.out.print(ans);
	}

}
