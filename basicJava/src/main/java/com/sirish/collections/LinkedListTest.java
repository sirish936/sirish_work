package com.sirish.collections;

import java.util.LinkedList;
import java.util.List;
import java.util.ListIterator;

public class LinkedListTest {

	/**
	 * @param args
	 */
	public static void main(final String[] args) {
		// TODO Auto-generated method stub
		final List<String> list = new LinkedList<String>();
		list.add("A");
		list.add("B");
		list.add("C");
		list.add("D");
		list.add("E");
		System.out.println(list);
		list.add(2, "F");
		System.out.println(list);

		final ListIterator<String> iterate = list.listIterator();
		iterate.next();
		iterate.next();
		iterate.next();
		iterate.next();
		iterate.remove();
		iterate.previous();
		iterate.previous();
		iterate.remove();
		System.out.println(list);

	}

}
