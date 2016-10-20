/**
 *
 */
package com.sirish.collections;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

/**
 * @author Murali
 *
 */
public class ComparatorTest implements Comparator<ComparatorTest> {

	/**
	 * @param args
	 */

	int sno;

	public int getSno() {
		return sno;
	}

	public void setSno(final int sno) {
		this.sno = sno;
	}

	public String getSname() {
		return sname;
	}

	public void setSname(final String sname) {
		this.sname = sname;
	}

	public String getSadd() {
		return sadd;
	}

	public void setSadd(final String sadd) {
		this.sadd = sadd;
	}

	String sname, sadd;

	public static void main(final String[] args) {
		// TODO Auto-generated method stub
		final List<ComparatorTest> list = new ArrayList<ComparatorTest>();

		final ComparatorTest comparatorTest1 = new ComparatorTest();
		comparatorTest1.setSno(101);
		comparatorTest1.setSname("ramana");
		comparatorTest1.setSadd("vizag");
		list.add(comparatorTest1);

		final ComparatorTest comparatorTest2 = new ComparatorTest();
		comparatorTest2.setSno(102);
		comparatorTest2.setSname("srinu");
		comparatorTest2.setSadd("rjy");
		list.add(comparatorTest2);

		final ComparatorTest comparatorTest3 = new ComparatorTest();
		comparatorTest3.setSno(103);
		comparatorTest3.setSname("sudheer");
		comparatorTest3.setSadd("yml");
		list.add(comparatorTest3);

		Collections.sort(list, new ComparatorTest());

		for (final ComparatorTest ctest : list) {
			System.out.println(ctest.getSname());
		}

	}

	@Override
	public int compare(final ComparatorTest arg0, final ComparatorTest arg1) {
		// TODO Auto-generated method stub
		return arg0.getSadd().compareTo(arg1.getSadd());
	}

}
