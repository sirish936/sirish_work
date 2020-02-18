package com.sirish.hpe;

import java.util.UUID;

public class PopulateStudent {
	public static void main(String[] args) {
		System.out.println(UUID.randomUUID().toString());
		
		long startTime = System.currentTimeMillis();
		System.out.println(startTime);
		long endTime = 0;

		    for(int i=0; i < 1000000000; i++) {

		    String x= "123";
		    x= x+"456";
		    

		    }
		    
		System.out.println("sirish".toLowerCase());
		System.out.println("SIRISH".toLowerCase());

		endTime = System.currentTimeMillis();
		System.out.println(endTime);

		long timeneeded =  ((endTime - startTime) /1000);
		System.out.println(timeneeded);
	}
	

}
