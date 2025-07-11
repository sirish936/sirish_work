package com.sirish.core;

import java.util.Scanner;

public class UserInput {
	public static void main(String[] args) {
		String s1 = new String("hello");
		String s2 = s1.intern();
		System.out.println(s2);
		s2.concat( "e3");
		System.out.println(s2);

	}}
