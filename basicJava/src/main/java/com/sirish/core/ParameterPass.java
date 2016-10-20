package com.sirish.core;

public class ParameterPass {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int i=0;
		addTwo(i++);
		System.out.println(i);
	}
	static void addTwo(int i)
	{
		System.out.println("hai");
		System.out.println(i);
		i+=2;
		
	}

}
