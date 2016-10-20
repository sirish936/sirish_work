package com.sirish.collections;

//import java.util.HashSet;
import java.util.Iterator;
//import java.util.LinkedHashSet;
import java.util.Set;
import java.util.TreeSet;

public class SetDemo {

	/**
	 * @param args
	 */
	public static void main(final String[] args) {
		// TODO Auto-generated method stub
		/*
		 * Set<Integer> set=new HashSet<Integer>(); set.add(3); set.add(6); set.add(2); set.add(2); set.add(4); set.add(5); set.add(5); set.add(5); set.add(6);
		 * set.add(2); set.add(4); System.out.println(set); Iterator<Integer> iterator=set.iterator(); while(iterator.hasNext()) {
		 * System.out.println(iterator.next()); }
		 * 
		 * 
		 * /* Set<Integer> set=new LinkedHashSet<Integer>(); set.add(3); set.add(6); set.add(2); set.add(2); set.add(4); set.add(5); set.add(5); set.add(5);
		 * set.add(6); set.add(2); set.add(4); System.out.println(set); Iterator<Integer> iterator=set.iterator(); while(iterator.hasNext()) {
		 * System.out.println(iterator.next()); }
		 */

		final Set<Integer> set = new TreeSet<Integer>();
		set.add(3);
		set.add(6);
		set.add(2);
		set.add(2);
		set.add(4);
		set.add(5);
		set.add(5);
		set.add(5);
		set.add(6);
		set.add(2);
		set.add(4);
		System.out.println(set);
		final Iterator<Integer> iterator = set.iterator();
		while (iterator.hasNext()) {
			System.out.println(iterator.next());
		}
		for (final Integer inte : set) {
			System.out.println(inte);
		}

	}

}
