package com.sirish.collections;

import java.util.ArrayList;
import java.util.List;
import java.util.ListIterator;

public class Iterate {

	/**
	 * @param args
	 */
	public static void main(final String[] args) {
		// TODO Auto-generated method stub
		final List<String> list = new ArrayList<String>();
		list.add("A");
		list.add("B");
		list.add("C");
		list.add("D");
		list.add("E");
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
