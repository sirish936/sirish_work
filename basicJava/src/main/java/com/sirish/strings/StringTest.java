package com.sirish.strings;

import java.util.ArrayList;
import java.util.List;

public class StringTest {
	public static void main(final String[] args) {

		final String s = "sirish";
		final String s2 = s;
		s.concat("nimmakayala");
		System.out.println(s.concat("nimmaka"));
		System.out.println(s2);
		System.out.println(s);

		final String str1 = "Hello";
		final String str2 = str1.replaceAll("hai", "hoe are you");

		final List<String> myList = new ArrayList<String>();
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
