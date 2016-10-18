package com.sirish.core;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class DateExtract {

	public static void main(String[] args) {
		
		String dateStr = "August 21st, 2015";
		
		final String pattern = "(\\d+)";
		final Pattern p = Pattern.compile(pattern);
		boolean b;
		b = true;
		final Matcher m = p.matcher(dateStr);
		while (m.find()) {
			if (b == true) {
				 int x = m.end()-1;
				 char u = dateStr.charAt(x);
				 if(Character.isLetter(u)){
					 dateStr = dateStr.substring(m.end(), m.end()+2);
				 }
				b = false;
			}
		}
		
		System.out.println(dateStr);
	}
}
