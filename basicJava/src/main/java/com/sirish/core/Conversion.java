package com.sirish.core;

public class Conversion {

	public static void main(String[] args) {
		//String to int conversion
		int x = Integer.parseInt("10");
		System.out.println(x);
		
		String js = String.format("window.hack.$scope.formData.login.j_password='%s';", "sirish");
		System.out.println(js);

	}
}
