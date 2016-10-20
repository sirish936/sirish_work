package com.sirish.collections;

//import java.util.Comparator;

public class Student implements Comparable<Student> {
	Integer no;

	public Integer getNo() {
		return no;
	}

	public void setNo(final Integer no) {
		this.no = no;
	}

	public String getName() {
		return name;
	}

	public void setName(final String name) {
		this.name = name;
	}

	public String getAddr() {
		return addr;
	}

	public void setAddr(final String addr) {
		this.addr = addr;
	}

	String name;
	String addr;

	@Override
	public int compareTo(final Student arg0) {
		// TODO Auto-generated method stub
		/*
		 * if(this.getNo()<arg0.getNo()) return -1; else if(this.getNo()>arg0.getNo()) return 1; else return 0;
		 */
		return this.getNo().compareTo(arg0.getNo());

	}

}
