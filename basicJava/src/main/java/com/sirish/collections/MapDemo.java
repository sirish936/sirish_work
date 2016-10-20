package com.sirish.collections;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class MapDemo {

	/**
	 * @param args
	 */
	public static void main(final String[] args) {
		// TODO Auto-generated method stub
		final Map<Integer, String> map = new HashMap<Integer, String>();
		map.put(1, "sirish");
		map.put(2, "ramana");
		map.put(3, "purush");
		map.put(4, "chaitu");
		map.put(5, "sreenu");
		map.put(6, "anil");
		System.out.println(map);
		final Set<Integer> set = map.keySet();
		System.out.println(set);
		final Iterator<Integer> iterator = set.iterator();
		while (iterator.hasNext()) {
			final Integer integer = iterator.next();
			System.out.println(map.get(integer));
		}

		final List<Integer> list = new ArrayList<Integer>(map.keySet());
		Collections.sort(list);
		System.out.println(list);
		final Iterator<Integer> iterator1 = list.iterator();
		while (iterator1.hasNext()) {
			final Integer integer1 = iterator1.next();
			System.out.println(map.get(integer1));
		}
		// List<Integer> list1=(List<Integer>)set<Integer>;

		System.out.println(map.get(1));
		System.out.println(map.size());
		System.out.println(map.remove(1));
		// System.out.println(map);
		System.out.println(map.entrySet());
		System.out.println(map.getClass());
		System.out.println(map.keySet());
		System.out.println(map.hashCode());
	}

}
