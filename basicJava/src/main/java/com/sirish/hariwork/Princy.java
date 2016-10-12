package com.sirish.hariwork;

public class Princy{
	void method1() throws Exception{
		System.out.println("from super");
	}
}

class SubPrincy extends Princy{
	@Override
	void method1() throws NullPointerException{
		System.out.println("from sub");
	}
 }

class App{
	public static void main(String[] args)throws Exception {
		Princy princy = new SubPrincy();
		princy.method1(); 
	}
}