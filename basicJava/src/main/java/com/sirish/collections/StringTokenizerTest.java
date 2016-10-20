package com.sirish.collections;

import java.util.StringTokenizer;

public class StringTokenizerTest {

	/**
	 * @param args
	 */
	public static void main(final String[] args) {
		// TODO Auto-generated method stub
		final String string = new String("Banglore is the capital of Karnataka.");
		final StringTokenizer stringtokenizer = new StringTokenizer(string, "a");
		System.out.println(stringtokenizer.countTokens());

		while (stringtokenizer.hasMoreTokens()) {
			System.out.println(stringtokenizer.nextToken());
		}
	}

}
