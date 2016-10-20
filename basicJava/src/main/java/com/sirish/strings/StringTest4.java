package com.sirish.strings;

import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class StringTest4 {

	final static String pattern = "\\d+";
	final static String matcher = "Your last bill was sent on 04/22/2014 in the amount of $101.39 due on 05/27/2014.";
	static List<String> list = new ArrayList<String>();

	public static void main(final String[] args) {

		final StringTokenizer st = new StringTokenizer(matcher);
		final int count = st.countTokens();
		final Pattern p = Pattern.compile(pattern);

		for (int i = 0; i < count; i++) {
			boolean b = true;
			final String mat = st.nextToken();
			final Matcher m = p.matcher(mat);
			while (m.find()) {
				if (b) {
					list.add(mat);
					b = false;
				}
			}
		}
		System.out.println(list.get(0) + " : " + list.get(1) + " : " + list.get(2));
	}
}