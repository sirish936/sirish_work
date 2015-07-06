package com.sirish.core;

public class GetName {
	
	static String name;

	public static String getName() {
		return name;
	}

	public static void setName(String name) {
		GetName.name = name;
	}

	public static void main(String[] args) {
		
		setName("Hari");
		System.out.println(getName());
		
	}
}
