package com.sirish.hpe;

import com.sirish.core.Student;


public class CompleXMapTest {
	public static void main(String[] args) {
		Student st = new Student();
		st.setName("Bang");
		populateStudent(st);
		System.out.println(st.getName() + st.getAge() + st.getWeight());
		 
		
	}

	private static void populateStudent(Student st) {
		st.setAge("25");
		st.setWeight("50");
	}

	
	

}
