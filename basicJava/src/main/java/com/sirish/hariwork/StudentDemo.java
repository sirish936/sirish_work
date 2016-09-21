package com.sirish.hariwork;

import java.util.ArrayList;

class Student {
	String sname;
	int rollno;
	double kannada;
	double english;
	double hindi;
}

public class StudentDemo {

	public static void main(final String[] args) {
		final ArrayList<Student> al = new ArrayList<Student>();
		final Student s1 = new Student();
		final Student s2 = new Student();

		s1.sname = "amulya";
		s1.rollno = 1;
		s1.english = 22.6;
		s1.hindi = 22.0;
		s1.kannada = 21.5;

		s2.sname = "sud";
		s2.rollno = 2;
		s2.english = 21.2;
		s2.hindi = 24.1;
		s2.kannada = 17.6;

		al.add(s1);
		al.add(s2);

		final Princy p = new StudentDemo().new Princy();
		p.displayStudents(al);

	}

	class Princy {
		void displayStudents(final ArrayList<Student> x) {

			for (final Student r : x) {
				System.out.println("Name" + r.sname);
				System.out.println("rollno" + r.rollno);
				System.out.println("English" + r.english);
				System.out.println("Kannada" + r.kannada);
				System.out.println("Hindi" + r.hindi);
			}
		}
	}
}
