package com.sirish.hariwork;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class MApTest {
	public static void main(String[] args) {
		Map<String, HashMap<String, ArrayList<String>>> testMap = new HashMap<String, HashMap<String, ArrayList<String>>>();

		ArrayList<String> al1 = new ArrayList<String>();
		al1.add("A");
		al1.add("B");
		ArrayList<String> al2 = new ArrayList<String>();
		al2.add("C");
		al2.add("D");
		ArrayList<String> al3 = new ArrayList<String>();
		al3.add("E");

		HashMap<String, ArrayList<String>> tm1 = new HashMap<String, ArrayList<String>>();
		HashMap<String, ArrayList<String>> tm2 = new HashMap<String, ArrayList<String>>();
		HashMap<String, ArrayList<String>> tm3 = new HashMap<String, ArrayList<String>>();
		tm1.put("1", al1);
		tm1.put("2", al2);
		tm1.put("3", al3);

		testMap.put("!", tm1);

		ArrayList<String> al4 = new ArrayList<String>();
		al4.add("F");
		al4.add("G");
		ArrayList<String> al5 = new ArrayList<String>();
		al5.add("H");

		HashMap<String, ArrayList<String>> tm4 = new HashMap<String, ArrayList<String>>();
		HashMap<String, ArrayList<String>> tm5 = new HashMap<String, ArrayList<String>>();
		tm2.put("4", al4);
		tm2.put("5", al5);

		testMap.put("@", tm2);

		for (final Map.Entry<String, HashMap<String, ArrayList<String>>> entry : testMap
				.entrySet()) {
			final Map<String, ArrayList<String>> targetMap = entry.getValue();

			for (final Map.Entry<String, ArrayList<String>> targetEntry : targetMap
					.entrySet()) {
				final ArrayList<String> targetDeviceList = targetEntry
						.getValue();

				for (final String device : targetDeviceList) {
					System.out.println(device);
				}
			}
		}

		HashMap<String, ArrayList<String>> existingMap;
		if (testMap.containsKey("@")) {
			existingMap = testMap.get("@");
			if (!existingMap.containsKey("$")) {
				existingMap.put("#", al5);
				System.out.println(existingMap.toString());
			} else {

			}
		}
	}
}
