package com.sirish.core;

import java.util.HashMap;
import java.util.IdentityHashMap;

public class MapTest {

	public static void main(final String[] args) {
		final HashMap<Integer, String> myMap = new HashMap<Integer, String>();
		myMap.put(new Integer(10), "pavan");
		myMap.put(new Integer(10), "kalyan");
		System.out.println(myMap);

		final IdentityHashMap<Integer, String> myIMap = new IdentityHashMap<Integer, String>();
		myIMap.put(new Integer(10), "pavan");
		myIMap.put(new Integer(10), "kalyan");
		System.out.println(myIMap);

		final HashMap<String, String> mySMap = new HashMap<String, String>();
		mySMap.put(new String("pavan"), "pavan");
		mySMap.put(new String("pavan"), "kalyan");
		System.out.println(mySMap);

		final IdentityHashMap<String, String> myIsMap = new IdentityHashMap<String, String>();
		myIsMap.put(new String("pavan"), "pavan");
		myIsMap.put(new String("pavan"), "kalyan");
		System.out.println(myIsMap);

		final String s = "sirish";
		System.out.println(s.hashCode());
	}
}
