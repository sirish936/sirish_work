package com.sirish.core;

import java.util.ArrayList;

import java.util.List;
public class StringTest {
	public static void main(final String[] args) {
		final String str1 = "Hello";
		final String str2 = str1.replaceAll("hai", "hoe are you");

		
		List<String> myList = new ArrayList<String>();
		System.out.println(str2);
		myList.add("Nimmakayala");
		myList.add("venkata");
		myList.add("sirish");
		
		myList.add(2, "Asha");
		for (int i = 0; i < myList.size(); i++) {
			System.out.println(myList.get(i));
		}
	}
}
