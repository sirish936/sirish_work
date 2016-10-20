/**
 *
 */
package com.sirish.collections;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;

/**
 * @author sirish
 *
 */

public class IteratorDemo {

	/**
	 * @param args
	 */
	public static void main(final String[] args) {
		// TODO Auto-generated method stub
		final List<Integer> l = new ArrayList<Integer>();
		l.add(10);
		l.add(20);
		l.add(30);
		l.add(40);
		l.add(50);
		l.add(60);
		l.add(70);
		l.add(10);
		System.out.println(l);

		final List<Integer> ll = new ArrayList<Integer>();
		ll.add(50);
		ll.add(20);
		ll.add(60);
		ll.add(40);
		ll.add(10);
		ll.add(60);
		ll.add(70);
		ll.add(8);
		Collections.sort(ll);
		System.out.println(ll);
		// iterate the loop
		final Iterator<Integer> it = ll.iterator();
		while (it.hasNext()) {
			System.out.println(it.next());
		}
		System.out.println();
		// forEach loop
		for (final Integer x : ll) {
			System.out.println(x);
		}
	}

}
