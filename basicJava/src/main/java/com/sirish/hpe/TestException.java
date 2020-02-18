package com.sirish.hpe;

public class TestException {
	public static void main(String[] args) throws Exception {
		
		String str =test();
		System.out.println(str.length());
	}

	private static String test() throws Exception {
		String s="";
		try{
			s = genException();
			System.out.println(s);
		}catch(Exception e){
			throw new Exception();
		}
		return s;
	}

	private static String genException() throws Exception {
		throw new Exception();
	}
}
