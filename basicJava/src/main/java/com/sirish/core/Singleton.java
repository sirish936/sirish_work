package com.sirish.core;

public class Singleton {
	private static Singleton singleInstance = null;

	// Make default constructor private
	private Singleton() {
	}

	// Get instance for class Singleton
	public static Singleton getInstance() {

		if (singleInstance == null) {
			singleInstance = new Singleton();
		}

		return singleInstance;
		}
		public  static void main(String[]args){
			Singleton s=Singleton.getInstance();
			System.out.println(s);
			Singleton s1=Singleton.getInstance();
			System.out.println(s1);
			Singleton s2=Singleton.getInstance();
			System.out.println(s2);
					
		} 
}
