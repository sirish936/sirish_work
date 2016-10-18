package com.sirish.core;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class DateTest {

	public static void main(final String[] args) throws ParseException {

		final String dueDate = "May 2015";

		final SimpleDateFormat dateFormat = new SimpleDateFormat("MMM yyyy");
		final Date convertedDate = dateFormat.parse(dueDate);

		System.out.println(convertedDate);

		final SimpleDateFormat reqformat = new SimpleDateFormat("dd MMM yyyy");
		final String s = reqformat.format(convertedDate);
		System.out.println(s);

		final SimpleDateFormat finaldateFormat = new SimpleDateFormat("dd MMM yyyy");
		final Date finalconvertedDate = finaldateFormat.parse(s);
		System.out.println(finalconvertedDate);

	}

}
