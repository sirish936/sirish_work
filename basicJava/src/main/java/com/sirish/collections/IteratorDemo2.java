package com.sirish.collections;

import java.util.ArrayList;
//import java.util.Collections;
import java.util.List;

/**
 * @author Murali
 *
 */
public class IteratorDemo2 {

	public static void main(final String[] args) {
		// TODO Auto-generated method stub
		final Student st1 = new Student();
		final Student st2 = new Student();
		final Student st3 = new Student();
		final Student st4 = new Student();
		final Student st5 = new Student();
		final Student st6 = new Student();
		final List<Student> l = new ArrayList<Student>();
		l.add(st1);
		l.add(st2);
		l.add(st3);
		l.add(st6);
		l.add(st5);
		l.add(st4);
		System.out.println(l);
		// Collections.sort(l);

	}

}
