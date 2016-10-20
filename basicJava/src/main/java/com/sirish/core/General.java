package com.sirish.core;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Scanner;

public class General {

	@SuppressWarnings("resource")
	public static void main(final String[] args) throws FileNotFoundException {
		final Scanner sc = new Scanner(new File("C:\\ravi\\Examples\\f1.txt"));
		final List<String> dataList = new ArrayList<String>();
		while (sc.hasNextLine()) {
			dataList.add(sc.nextLine());
		}
		System.out.println(dataList);
		System.out.println(dataList.size());
		final Map<String, String> map = new HashMap<String, String>();
		for (int i = 0; i < dataList.size(); i = i + 2) {
			map.put(dataList.get(i), dataList.get(i + 1));
		}

		for (final Entry<String, String> en : map.entrySet()) {
			System.out.println(en.getKey() + " : " + en.getValue());
		}
		// String problemC = map.get("Problem C:");
		// String splitted[] = problemC.split("\\|");
		// System.out.println("Get me problem C: "+String.format("a:%s, b:%s, c:%s, d:%s",splitted[0],splitted[1],splitted[2],splitted[3]));
	}
}