package com.sirish.core;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class DateTest {

	public static void main(final String[] args) throws ParseException {

		final String dueDate = "May 2015";

		final SimpleDateFormat dateFormat = new SimpleDateFormat("MMM yyyy");
		final SimpleDateFormat reqformat = new SimpleDateFormat("dd/MM/yyyy");
		
		final Date convertedDate = dateFormat.parse(dueDate);
		
		final String s = reqformat.format(convertedDate);
		System.out.println(s);

	}
}