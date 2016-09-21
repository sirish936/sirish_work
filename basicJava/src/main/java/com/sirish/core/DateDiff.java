package com.sirish.core;

import java.util.Date;
import java.util.HashSet;
import java.util.Set;
import java.util.concurrent.TimeUnit;

public class DateDiff {

	@SuppressWarnings("deprecation")
	public static void main(final String[] args) {
		final Set<String> setEx = new HashSet<String>();
		setEx.add("123");
		setEx.add(null);
		setEx.add(null);
		setEx.add(null);
		System.out.println(setEx.size());

		final Date oldDate = new Date();
		oldDate.setMonth(new Date().getMonth() - 1);

		final long timeDiff = getDateDiff(new Date(), oldDate);
		System.out.println("Time Difference is " + timeDiff);

	}

	static long abc = 1422000000000l;

	static long getDateDiff(final Date date1, final Date date2) {
		final long diffInMillies = date1.getTime() - abc;
		return Math.abs(TimeUnit.DAYS.convert(diffInMillies, TimeUnit.MILLISECONDS));
	}
}
