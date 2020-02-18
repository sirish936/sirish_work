package com.sirish.hpe;

public class StaticClass {
	
	private static String instance = getInstance();
	
	private static  String getInstance(){
        if (instance == null){
        	instance = new String();;
        }
        return instance;
    }

	public static void main(String[] args) {
		
		System.out.println(instance.concat("Bang"));
		
	}

}
