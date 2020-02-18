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
		
		String x2 = "0.35.02";
		String x1 = "0.35.01";
		
		if(x2.compareTo(x1)>1){
			System.out.println("greater"+x2);
		}else{
			System.out.println("greater"+x1);
		}
		
	}
}
