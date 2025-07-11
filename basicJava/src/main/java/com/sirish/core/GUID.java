package com.sirish.core;

import java.util.HashSet;
import java.util.Set;
import java.util.UUID;

import org.apache.commons.lang.RandomStringUtils;

public class GUID {
	@SuppressWarnings("static-access")
	public static void main(final String[] args) {
		// creating UUID
		final UUID uid = UUID.fromString("38400000-8cf0-11bd-b23e-10b96e4ef00d");

		// checking the value of random UUID
		System.out.println("Random UUID value: " + uid.randomUUID());
		System.out.println("Random UUID length: " + uid.randomUUID().toString().length());
		System.out.println("Random UUID length: " + RandomStringUtils.randomAlphanumeric(32).toLowerCase());
		
		     Set<String> strings = new HashSet();
				/*
				 * strings.add("hi"); strings.add("hello"); strings.add("how");
				 * strings.add("are"); strings.add("you");
				 */
		     
		     System.out.println("Test:1  " + strings.contains("sirish"));
		     System.out.println("Test:2  " + strings.contains("hi"));
		     System.out.println("Test:3  " + strings.contains("HOW"));
	}
}