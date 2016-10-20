/**
 *
 */
package com.sirish.collections;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * @author Murali
 *
 */
public class StudentDemo {

	/**
	 * @param args
	 */
	public static void main(final String[] args) {
		// TODO Auto-generated method stub
		final List<Student> list = new ArrayList<Student>();

		final Student student1 = new Student();
		student1.setNo(101);
		student1.setName("ramana");
		student1.setAddr("vizag");
		list.add(student1);

		final Student student3 = new Student();
		student3.setNo(103);
		student3.setName("purush");
		student3.setAddr("hyd");
		list.add(student3);

		final Student student2 = new Student();
		student2.setNo(102);
		student2.setName("srinu");
		student2.setAddr("rjy");
		list.add(student2);

		Collections.sort(list);

		for (final Student s : list) {
			System.out.println(s.getName());
		}

	}

}
