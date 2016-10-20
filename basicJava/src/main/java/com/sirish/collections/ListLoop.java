package com.sirish.collections;

import java.util.ArrayList;
import java.util.Collections;
//import java.util.Iterator;
import java.util.List;

public class ListLoop {

	public static void main(final String[] args) {
		final List<Object> list = new ArrayList<Object>();
		final List<Integer> list1 = new ArrayList<Integer>();
		list1.add(1);
		list1.add(2);
		list1.add(3);
		list1.add(4);
		list.add(list1);
		final List<String> list2 = new ArrayList<String>();
		list2.add("a");
		list2.add("a");
		list2.add("b");
		list2.add("c");
		list2.add("d");
		list.add(list2);
		final List<Integer> list3 = new ArrayList<Integer>();
		list3.add(11);
		list3.add(22);
		list3.add(33);
		list3.add(44);
		list.add(list3);
		final List<String> list4 = new ArrayList<String>();
		list4.add("aa");
		list4.add("bb");
		list4.add("cc");
		list4.add("dd");
		list.add(list4);
		System.out.println("list size is:" + list.size());
		System.out.println("list1 size is:" + list1.size());
		System.out.println("list2 size is:" + list2.size());
		System.out.println("list3 size is:" + list3.size());
		System.out.println("list4 size is:" + list4.size());

		for (final Integer in : list1) {
			System.out.println("elements in list1 are:" + in);
		}

		for (final String in : list2) {
			System.out.println("elements in list2 are:" + in);
		}

		for (final Integer in : list3) {
			System.out.println("elements in list3 are:" + in);
		}

		for (final String in : list4) {
			System.out.println("elements in list4 are:" + in);
		}
		System.out.println("frequency:" + Collections.frequency(list2, "a"));

		/*
		 * // iterate list using for loop for(int i=0;i<list.size();++i) { System.out.println(list.get(i).getClass()); ArrayList<ArrayList>
		 * List=(ArrayList<ArrayList>)list.get(i);
		 * 
		 * 
		 * //System.out.println("elements in the list are:"+List); for(int j=0;j<List.size();++j) {
		 * 
		 * System.out.println("elements in the list"+(i+1)+" are:"+List.get(j));
		 * 
		 * } }
		 * 
		 * //iterate list using while loop Iterator<Object> iterator=list.iterator(); while(iterator.hasNext()) { System.out.println();
		 * //System.out.println(iterator.next().getClass()); ArrayList<ArrayList> arraylist=(ArrayList)iterator.next(); Iterator iterator1=arraylist.iterator();
		 * while(iterator1.hasNext()) { //System.out.println(iterator1.next().getClass()); System.out.println("elements in the list are:"+iterator1.next()); }
		 * 
		 * }
		 */
	}
	// }

}
