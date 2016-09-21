package com.sirish.core;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class DateTest1 {

	public static void main(final String[] args) throws ParseException {

		final SimpleDateFormat existedFormat = new SimpleDateFormat("MMMM yyyy");
		final SimpleDateFormat reqformat = new SimpleDateFormat("MM/dd/yyyy");

		final String date = "September 2014";

		final Date reqDate = existedFormat.parse(date);
		System.out.print(reqformat.format(reqDate));
	}
}
