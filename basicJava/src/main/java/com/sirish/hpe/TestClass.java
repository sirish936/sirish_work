package com.sirish.hpe;

public class TestClass {
	static String COMPSIG_IN_PARTS = "_part";
	static String compsigfileName ="abc_part1.compsig";
	public static void main(String[] args) {
		Logic l = new Logic();
		l.setAddress("xx");
		System.out.println(l.getAddress());
		l = populate(l);
		System.out.println(l.getAddress());
		
		if(compsigfileName.contains(COMPSIG_IN_PARTS))
		{
			System.out.println("OKKKKK");
		}
	}

	private static Logic populate(Logic l) {
		l.setNo(1);;
		l.setName("a");
		l.setAddress("z");
		return l;
	}
}
