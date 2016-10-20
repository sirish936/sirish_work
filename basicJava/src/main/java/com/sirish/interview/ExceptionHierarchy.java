package com.sirish.interview;

public class ExceptionHierarchy {

	public void method() throws NullPointerException {
		System.out.println("from super");
	}

}

class HierarchyNew extends ExceptionHierarchy {
	// @Override
	// public void method() throws Exception {
	// System.out.println("from sub");
	// }

	@Override
	public void method() throws RuntimeException {
		System.out.println("from sub");
	}
}
