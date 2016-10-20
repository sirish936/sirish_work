/**
 *
 */
package com.sirish.collections;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;

/**
 * @author Murali
 *
 */
public class IteratorDemo1 {

	/**
	 * @param args
	 */
	public static void main(final String[] args) {
		// TODO Auto-generated method stub
		final List<String> l = new ArrayList<String>();
		l.add("10");
		l.add("20");
		l.add("sirish");
		l.add("ramana");
		l.add("srinu");
		l.add("uday");
		l.add("purush");
		l.add("anil");
		System.out.println(l);

		final List<String> ll = new ArrayList<String>();
		ll.add("10");
		ll.add("20");
		ll.add("sirish");
		ll.add("ramana");
		ll.add("srinu");
		ll.add("uday");
		ll.add("purush");
		ll.add("anil");
		System.out.println(ll);

		final boolean b = ll.contains("ramana");
		System.out.println(b);
		Collections.sort(ll);
		System.out.println(ll);
		// iterate the loop
		final Iterator<String> it = ll.iterator();
		while (it.hasNext()) {
			System.out.println(it.next());
		}
		System.out.println();

		while (it.hasNext()) {
			System.out.println(it.next());
		}

		// forEach loop
		for (final String x : ll) {
			System.out.println(x);
		}
	}

}
