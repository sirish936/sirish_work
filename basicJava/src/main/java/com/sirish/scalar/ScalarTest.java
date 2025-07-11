package com.sirish.scalar;

public class ScalarTest {
	
	public static int fun(int a, int b) {
		if (b == 0) return a;
		else return fun(a, a%b);
	}
	
	public static void main(String[] args) {
		int ans = fun(100, 2000);
		System.out.println(ans);
		System.out.println(100%2000);
		System.out.println(100%100);
		System.out.println(100/2000);
		System.out.println(100/100);
		
		int x=10;  
		System.out.println(x++);//10 (11)  
		System.out.println(++x);//12  
		System.out.println(x--);//12 (11)  
		System.out.println(--x);//10  
		
		int a=10;  
		int b=5;  
		System.out.println(a/b);//2  
		System.out.println(a%b);//0
		
		int c=5;  
		int d=10;  
		  
		System.out.println(c/d);//0  
		System.out.println(c%d);//5 
	}

}
