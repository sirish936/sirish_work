package com.sirish.core;
public class Test extends Thread implements Runnable{
	
	public static void main(String[] args) {
		try{
			
			float f = \u0038;
			System.out.println(f);
			Thread tj = new Thread(new Test());
			tj.start();
		}catch(Exception  e){
			System.out.println(e);
		}
	}
}
