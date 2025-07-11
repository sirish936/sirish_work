package com.sirish.core;

import java.util.ArrayList;
import java.util.Arrays;

public class Student {
	
	String name;
	String age;
	String weight;
	String[] phno;
	
	public String[] getPhno() {
		return phno;
	}

	public void setPhno(String[] phno) {
		this.phno = phno;
	}

	public Student(String name, String age, String weight, String[] phnos){
		this.name = name;
		this.age = age;
		this.weight = weight;
		this.phno = phnos.clone();
	}

	public String getName() {
		return name;
	}

	public void setName(final String name) {
		this.name = name;
	}

	public String getAge() {
		return age;
	}

	public void setAge(final String age) {
		this.age = age;
	}

	public String getWeight() {
		return weight;
	}

	public void setWeight(final String weight) {
		this.weight = weight;
	}

	public static void main(final String[] args) {

		final ArrayList<Student> studentList = new ArrayList<Student>();

		final Student st1 = new Student();
		st1.setName("Hari");
		st1.setAge("35");
		st1.setWeight("65");

		final Student st2 = new Student();
		st2.setName("Krishna");
		st2.setAge("40");
		st2.setWeight("70");

		final Student st3 = new Student();
		st3.setName("Hari Krishna");
		st3.setAge("45");
		st3.setWeight("75");

		studentList.add(st1);
		studentList.add(st2);
		studentList.add(st3);

		for (final Student st : studentList) {
			System.out.println("Student names are " + st.getName());
		}
	}
}
