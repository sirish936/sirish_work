package com.sirish.collections;

import java.util.ArrayList;
import java.util.List;

public class StudentTest {

	/**
	 * @param args
	 */

	public static void main(final String[] args) {
		// TODO Auto-generated method stub

		final List<Student1> list = new ArrayList<Student1>();
		final Student1 student1 = new Student1();
		student1.setNo(101);
		student1.setName("ramana");
		list.add(student1);

		final Student1 student2 = new Student1();
		student2.setNo(102);
		student2.setName("srinu");
		list.add(student2);

		final Student1 student3 = new Student1();
		student3.setNo(103);
		student3.setName("uday");
		list.add(student3);

		final Student1 student4 = new Student1();
		student4.setNo(104);
		student4.setName("anil");
		list.add(student4);

		final Student1 student5 = new Student1();
		student5.setNo(109);
		student5.setName("prakash");
		list.add(student5);

		final Student1 student6 = new Student1();
		student6.setNo(106);
		student6.setName("manoj");
		list.add(student6);

		// iterate the list
		for (final Student1 st : list) {
			System.out.println("elements in the list are:" + st.getNo() + "--->" + st.getName());

		}

		final List<Student1> list1 = new ArrayList<Student1>();

		final Student1 student7 = new Student1();
		student7.setNo(107);
		student7.setName("kiran");
		list1.add(student7);

		final Student1 student8 = new Student1();
		student8.setNo(108);
		student8.setName("kishore");
		list1.add(student8);

		final Student1 student9 = new Student1();
		student9.setNo(109);
		student9.setName("prakash");
		list1.add(student9);

		// iterate the list
		for (final Student1 st : list1) {
			System.out.println("elements in the list are:" + st.getNo() + "--->" + st.getName());

		}

		System.out.println("size of first list. i.e list  " + list.size());

		System.out.println("size of second list. i.e list1 " + list1.size());

		list.removeAll(list1);

		System.out.println("size of first list. i.e list  " + list.size());

		System.out.println("size of second list. i.e list1 " + list1.size());

		// iterate the list
		for (final Student1 st : list) {
			System.out.println("elements in the list are:" + st.getNo() + "--->" + st.getName());

		}

		// iterate the list
		for (final Student1 st : list1) {
			System.out.println("elements in the list are:" + st.getNo() + "--->" + st.getName());

		}

	}

}
