package com.sirish.core;

import java.util.Calendar;
import java.util.Date;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class DateExtract {

	@SuppressWarnings("static-access")
	public static void main(final String[] args) {

		String dateStr = "August 21st, 2015";

		final String pattern = "(\\d+)";
		final Pattern p = Pattern.compile(pattern);
		boolean b;
		b = true;
		final Matcher m = p.matcher(dateStr);
		while (m.find()) {
			if (b == true) {
				final int x = m.end() - 1;
				final char u = dateStr.charAt(x);
				if (Character.isLetter(u)) {
					dateStr = dateStr.substring(m.end(), m.end() + 2);
				}
				b = false;
			}
		}
		final Calendar cal = Calendar.getInstance();
		cal.add(Calendar.MONTH, 1); // setting previous year
		final Date lastcsdDate = cal.getTime();

		System.out.println(lastcsdDate.toString());
		System.out.println(dateStr);
		System.out.println(lastcsdDate);

		final Calendar cal1 = Calendar.getInstance();
		cal1.add(Calendar.DATE, -10);
		final Date dueDate = cal1.getTime();
		System.out.println(dueDate);

		final String str = new String("sirish");
		System.out.println(str.valueOf(str.substring(0)));
	}
}
