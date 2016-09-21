package com.sirish.core;

import java.util.ArrayList;

public class GenericTest {
	public static void main(final String[] args) {
		final ArrayList<String> al = new ArrayList<String>();
		al.add("sirish");
		al.add("ramana");
		al.add("sudheer");
		al.add("uday");

		addData(al);
		al.add("mani");

		for (int i = 0; i < al.size(); i++) {
			System.out.println(al.get(i));
		}
	}

	public static void addData(final ArrayList al) {
		al.add(10);
		al.add(20);
		al.add(true);
	}
}
