package com.sirish.collections;

//Demonstrate iterators.
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.Iterator;
import java.util.ListIterator;

class IteratorDemo3 {
	public static void main(final String args[]) {
		// create an array list
		final ArrayList<String> al = new ArrayList<String>();
		// add elements to the array list
		al.add("C");
		al.add("A");
		al.add("E");
		al.add("B");
		al.add("D");
		al.add("F");
		final boolean b = al.contains("A");
		System.out.println(b);
		// use iterator to display contents of al
		System.out.print("Original contents of al: ");
		Collections.sort(al);
		Iterator<String> itr = al.iterator();
		for (final String element : al) {
			System.out.print(element + " ");

		}
		System.out.println();
		// modify objects being iterated
		final ListIterator<String> litr = al.listIterator();
		while (litr.hasNext()) {

			final Object element = litr.next();
			litr.set(element + "+");

		}
		System.out.print("Modified contents of al: ");
		itr = al.iterator();
		while (itr.hasNext()) {

			final Object element = itr.next();
			System.out.print(element + " ");

		}
		System.out.println();
		// now, display the list backwards
		System.out.print("Modified list backwards: ");
		while (litr.hasPrevious()) {

			final Object element = litr.previous();
			System.out.print(element + " ");

		}
		System.out.println();
		final HashSet<String> hs = new HashSet<String>();
		hs.add("a");
		hs.add("b");
		hs.add("c");
		hs.add("d");
		hs.add("a");
		System.out.println(hs);
		for (final String s1 : hs) {
			System.out.println(s1);
		}

	}
}
