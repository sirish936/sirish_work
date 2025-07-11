package com.sirish.hpe;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

import com.sirish.core.Student;

public class ArrayCheck {
	
	public String[] getStringArray(List<String> strings) {
		  return strings.toArray(new String[0]);
		}

		public static void main(String[] args) {
			Student st1 = new Student("Ten","10","10",new String[]{"123","456"});
			st1.setAge("10");
			st1.setName("Ten");
			st1.setWeight("10");

			Student st2 = new Student("Twenty","20","20",new String[]{"456","789"});
			st2.setAge("20");
			st2.setName("Twenty");
			st2.setWeight("20");

			Student[] stArray1 = { st1, st2 };

			for (int i = 0; i < stArray1.length; i++) {
				Student st = stArray1[i];
				for (int j = 0; j < st.getPhno().length; j++) {
					String[] ph = st.getPhno();
					String phno = ph[j];
					System.out.println("PHNO IS: "+phno);
				}
				System.out.println(st.getAge());
			}

			List<Student> stList = new ArrayList<Student>();
			stList.add(st1);
			stList.add(st2);
			
			Student[] stringArray = stList.toArray(new Student[0]);
			
			for (int i = 0; i < stringArray.length; i++) {
				Student st = stringArray[i];
				System.out.println(st.getAge());
			}

			Student[] convArray = (Student[]) stList.toArray();

			for (int i = 0; i < convArray.length; i++) {
				Student st = convArray[i];
				System.out.println(st.getAge());
			}

			Student st3 = new Student("Thirty","30","30",new String[]{"789","987"});
			st3.setAge("30");
			st3.setName("Thirty");
			st3.setWeight("30");

			Student st4 = new Student("Fourty","40","40",new String[]{"987","654"});
			st4.setAge("40");
			st4.setName("Fourty");
			st4.setWeight("40");

			Student[] stArray2 = { st3, st4 };

			stArray2 = stArray1;

			for (int i = 0; i < stArray2.length; i++) {
				Student st = stArray2[i];
				System.out.println(st.getAge());
			}

		}

}
