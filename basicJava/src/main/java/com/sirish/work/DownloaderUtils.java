package com.sirish.work;

import java.math.BigDecimal;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.regex.Pattern;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class DownloaderUtils {

	private static final Logger log = LoggerFactory.getLogger(DownloaderUtils.class);

	public static final Pattern MM_DD_YYYY_PATTERN = Pattern.compile("(\\d{2}|\\d)/\\d{2}/(\\d{4})$");
	public static final Pattern MM_DD_YY_PATTERN = Pattern.compile("(\\d{2}|\\d)/\\d{2}/(\\d{2})$");

	public static BigDecimal getBigDecimalAmount(final String amount) {
		BigDecimal amountBiDecimal = null;

		try {
			if (amount != null && amount.length() != 0) {
				amountBiDecimal = new BigDecimal(amount.replaceAll("[^.0-9-]", ""));
				if (amount.contains("CR") && amountBiDecimal.intValue() > 0) {
					amountBiDecimal = amountBiDecimal.negate();
				}
			}
		} catch (final Exception e) {
			log.error("Could not '{}' to BigDecimal!", amount);
		}

		return amountBiDecimal;
	}

	/*public static void getDateFromMMDDYYPattern(final String dateString, final StatementDownloadInformation sdi) {
		final Matcher m = MM_DD_YY_PATTERN.matcher(dateString);
		if (m.find()) {
			sdi.month = Short.parseShort(m.group(1).toString());
			sdi.month--;
			sdi.year = (short) (Short.parseShort(m.group(2).toString()) + 2000);
		} else {
			sdi.reset();
		}
	}*/

	/*public static void getDateFromMMDDYYYYPattern(String dateString, final StatementDownloadInformation sdi) {

		final Date date = getFormattedDate(dateString);

		if (date != null) {
			dateString = new SimpleDateFormat("MM/dd/yyyy").format(date);
		}

		final Matcher m = MM_DD_YYYY_PATTERN.matcher(dateString);
		if (m.find()) {
			sdi.month = Short.parseShort(m.group(1).toString());
			sdi.month--;
			sdi.year = Short.parseShort(m.group(2).toString());
		} else {
			sdi.reset();
		}
	}

*//*	public static StatementDownloadInformation getDateFromMMDDYYYYPattern(final String dateString) {
		final StatementDownloadInformation sdi = new StatementDownloadInformation();
		DownloaderUtils.getDateFromMMDDYYYYPattern(dateString, sdi);
		return sdi;
	}
*/
	public static Date getFormattedDate(final DateFormat format, final String date) {
		Date formattedDate = null;
		if (date != null && date.isEmpty() == false) {
			try {
				formattedDate = new SimpleDateFormat(format.toString()).parse(date);
			} catch (final ParseException e) {
				log.error("Could not parse date", e);
			}
		}

		return formattedDate;
	}

	public static Date getFormattedDate(String date) {
		DateFormat format = null;
		if (date != null && !date.isEmpty()) {

			date = date.trim();

			if (date.matches("((\\d){1,2}\\-){1,2}(\\d){4}")) {
				format = DateFormat.MM_DD_YYYY_WITH_HYPHEN;
			} else if (date.matches("((\\d){1,2}\\-){1,2}(\\d){2}")) {
				format = DateFormat.MM_DD_YY_WITH_HYPHEN;
			} else if (date.matches("((\\d){1,2}\\/){1,2}(\\d){2}")) {
				//format = DateFormat.MM_DD_YY;
			} else if (date.matches("((\\d){1,2}\\/){1,2}(\\d){4}")) {
				//format = DateFormat.MM_DD_YYYY;
			} else if (date.matches("((\\d){4}\\-(\\d){1,2}\\-(\\d){1,2})")) {
				//format = DateFormat.YYYY_MM_DD;
			} else if (date.matches("((\\w){3,9}\\s+(\\d){1,2}\\,\\s+(\\d){4})")) {
				//format = DateFormat.MMM_DD_YYYY;
			} else if (date.matches("((\\w){3,9}\\s+(\\d){1,2}\\,(\\d){4})")) {
				format = DateFormat.MMM_DD_YYYY_WITHOUT_SPACE;
			} else if (date.matches("((\\d){1,2}\\s+(\\w){3,9}\\,\\s+(\\d){4})")) {
				//format = DateFormat.DD_MMM_YYYY;
			} else if (date.matches("((\\d){1,2}\\s+(\\w){3,9}\\,(\\d){4})")) {
				format = DateFormat.DD_MMM_YYYY_WITHOUT_SPACE;
			}
		}
		if (format == null) {
			log.error("DateFormat not supported for the date {} ", date);
			return null;
		}

		// Swapnil Maurya : Aug 14, 2015
		// Observed for provider AT&T where date is Sept which is not handled by the parser.
		final String month = date.toLowerCase();
		if (month.contains("sept") && !month.contains("september")) {
			log.error("Scraped date value before formatting: {}", date);
			date = date.replaceAll("t", "");
			log.error("Scraped date value after formatting: {}", date);
		}

		final Date formattedDate = getFormattedDate(format, date);

		return formattedDate;
	}

	public static short getCalendarMonthFromString(String month) throws Exception {
		month = month.toLowerCase();
		switch (month) {
		case "jan":
			return 0;
		case "january":
			return 0;

		case "feb":
			return 1;
		case "february":
			return 1;

		case "mar":
			return 2;
		case "march":
			return 2;

		case "apr":
			return 3;
		case "april":
			return 3;

		case "may":
			return 4;

		case "jun":
			return 5;
		case "june":
			return 5;

		case "jul":
			return 6;
		case "july":
			return 6;

		case "aug":
			return 7;
		case "august":
			return 7;

		case "sep":
			return 8;
		case "september":
			return 8;

		case "oct":
			return 9;
		case "october":
			return 9;

		case "nov":
			return 10;
		case "november":
			return 10;

		case "dec":
			return 11;
		case "december":
			return 11;
		default:
			throw new Exception("Unknown calendar month. We need a new calendar:" + month);
		}
	}
}
