package com.sirish.collections;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

import org.openjdk.jol.info.ClassLayout;
import org.openjdk.jol.info.GraphLayout;

public class ListDemo {

	/**
	 * @param args
	 */
	public static void main(final String[] args) {
		// TODO Auto-generated method stub
		final List<Integer> list = new ArrayList<Integer>();
		list.add(1);
		list.add(2);
		list.add(1, 3);
		for (int i = 0; i < 100; i++) {
			list.add(i);
		}
		System.out.println(list);
		List<Integer> list2 = new LinkedList<Integer>(list);
		System.out.println(list2);
		list.addAll(list2);
		System.out.println(list);
		list2 = list.subList(2, 5);
		System.out.println(list2);
		list2.clear();
		System.out.println(list2);
		System.out.println(list);
		System.out.println(list.size());
		System.out.println("frequency:" + Collections.frequency(list, list2));
		// List list5=Collections.unmodifiableList(list);

		final List<Integer> list3 = new ArrayList<Integer>();
		list3.add(1);
		list3.add(2);
		list3.add(3);
		list3.add(4);
		list3.add(5);
		list3.add(6);
		list3.add(7);
		list2 = list3.subList(2, 5);
		list2.clear();
		System.out.println(list2);
//		long size1 = SizeOf.sizeOf(list);
		long size2 = GraphLayout.parseInstance(list).totalSize();
        System.out.println("Size of list: " + size2 + " bytes");
		System.out.println(list3);
		
		Map<String, String> newMap = new HashMap();
		String value = newMap.get("xxx");
		

	}

}
