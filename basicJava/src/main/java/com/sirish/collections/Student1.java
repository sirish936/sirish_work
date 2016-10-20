package com.sirish.collections;

public class Student1 {

	int no;
	String name;

	public int getNo() {
		return no;
	}

	public void setNo(final int no) {
		this.no = no;
	}

	public String getName() {
		return name;
	}

	public void setName(final String name) {
		this.name = name;
	}

	@Override
	public boolean equals(final Object obj) {
		final Student1 st = (Student1) obj;
		if (this.name.equals(st.getName())) {
			return true;
		} else {
			return false;
		}
	}
}
