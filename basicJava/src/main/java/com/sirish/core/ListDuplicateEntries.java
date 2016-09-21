package com.sirish.core;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ListDuplicateEntries {

	public static void main(final String[] args) {

		final List<Integer> intList = new ArrayList<Integer>();
		final Map<Integer, Integer> countMap = new HashMap<Integer, Integer>();
		for (int i = 0; i < 50; i++) {
			intList.add(i);
		}

		addDuplicates(intList);

		// int temp = 0;
		// final int output[] = new int[20];
		for (int i = 0; i < intList.size(); i++) {

			final int number = intList.get(i);
			final int dupCount = Collections.frequency(intList, number);

			if (dupCount > 1) {
				// output[temp] = number;
				// temp++;
				countMap.put(number, dupCount);
			}
		}

		// for (int i = 0; i < output.length; i++) {
		// System.out.println("Duplicate elements are" + output[i]);
		// }

		for (final Map.Entry<Integer, Integer> entry : countMap.entrySet()) {
			System.out.println("Number : " + entry.getKey() + " is repeated for : " + entry.getValue() + " times");
		}
	}

	private static void addDuplicates(final List<Integer> intList) {
		for (int i = 11; i < 15; i++) {
			intList.add(i);
		}
	}
}
