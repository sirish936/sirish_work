package com.sirish.core;

import java.util.UUID;

public class GUID {
	@SuppressWarnings("static-access")
	public static void main(final String[] args) {
		// creating UUID
		final UUID uid = UUID.fromString("38400000-8cf0-11bd-b23e-10b96e4ef00d");

		// checking the value of random UUID
		System.out.println("Random UUID value: " + uid.randomUUID());
	}
}