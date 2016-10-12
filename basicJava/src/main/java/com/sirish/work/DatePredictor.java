package com.sirish.work;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class DatePredictor {

	static final Logger log = LoggerFactory.getLogger(DatePredictor.class);

	public PredictDates predictYear(final PredictDates predictDates) {

		PredictDates predictedDates = null;

		final PredictYearFor predictYearFor = getYearPredictor(predictDates);

		switch (predictYearFor) {

		case STATEMENT_DATE:
			predictedDates = predictStmtDateFromDueDates(predictDates);
			break;
		case DUE_DATE:
			predictedDates = predictDueDateFromStmtDates(predictDates);
			break;
		case STATEMENT_DATE_AND_DUE_DATE:
			predictedDates = predictStmtDateAndDueDate(predictDates);
			break;
		case NULLITY:
			log.error("Prediction is very difficult, {} ", predictDates);
			break;
		default:
			log.error("Prediction is very difficult, stmtDate: {} dueDate: {} ", predictDates.getStmtDate(), predictDates.getStmtDate());
			break;
		}

		return predictedDates;
	}

	protected PredictDates predictStmtDateAndDueDate(final PredictDates predictDates) {

		log.info("Predicting year in stmt Date {} and Due date {}", predictDates.getStmtDate(), predictDates.getDueDate());

		return null;
	}

	protected PredictDates predictDueDateFromStmtDates(final PredictDates predictDates) {

		log.info("Predicting year in Due date {}", predictDates.getDueDate());

		return null;
	}

	protected PredictDates predictStmtDateFromDueDates(final PredictDates predictDates) {

		log.info("Predicting year in stmt Date {} ", predictDates.getStmtDate());

		return null;
	}

	protected PredictYearFor getYearPredictor(final PredictDates predictDates) {

		final boolean isCorrectStatementDate, isCorrectDueDate;
		PredictYearFor predictYearFor = null;

		if (predictDates == null || predictDates.getStmtDate() == null || predictDates.getDueDate() == null) {
			log.warn("Null Refrence found it not possible to predict");
			predictYearFor = PredictYearFor.NULLITY;
		}

		isCorrectStatementDate = getFormattedDate(predictDates.getStmtDate()) == null ? false : true;

		isCorrectDueDate = getFormattedDate(predictDates.getDueDate()) == null ? false : true;

		if (!isCorrectStatementDate && !isCorrectDueDate) {
			log.info("Missing year in StmtDate {} and Due date {} ", predictDates.getStmtDate(), predictDates.getDueDate());
			predictYearFor = PredictYearFor.STATEMENT_DATE_AND_DUE_DATE;
		} else if (!isCorrectStatementDate) {
			log.info("Missing year in Statement date {}", predictDates.getStmtDate());
			predictYearFor = PredictYearFor.STATEMENT_DATE;
		} else if (!isCorrectDueDate) {
			log.info("Missing year in Due date {}", predictDates.getDueDate());
			predictYearFor = PredictYearFor.DUE_DATE;
		}

		return predictYearFor;

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
				format = DateFormat.MM_DD_WITH_HYHEN;
			} else if (date.matches("((\\d){1,2}\\/){1,2}(\\d){4}")) {
				format = DateFormat.MM_DD_YYYY_WITH_SLASH;
			} else if (date.matches("((\\d){4}\\-(\\d){1,2}\\-(\\d){1,2})")) {
				format = DateFormat.YYYY_MM_DD_WITH_SLASH;
			} else if (date.matches("((\\w){3,9}\\s+(\\d){1,2}\\,\\s+(\\d){4})")) {
				format = DateFormat.MMM_DD_YYYY_WITH_SPACE;
			} else if (date.matches("((\\w){3,9}\\s+(\\d){1,2}\\,(\\d){4})")) {
				format = DateFormat.MMM_DD_YYYY_WITHOUT_SPACE;
			} else if (date.matches("((\\d){1,2}\\s+(\\w){3,9}\\,\\s+(\\d){4})")) {
				format = DateFormat.DD_MMM_YYYY_WITH_SPACE;
			} else if (date.matches("((\\d){1,2}\\s+(\\w){3,9}\\,(\\d){4})")) {
				format = DateFormat.DD_MMM_YYYY_WITHOUT_SPACE;
			}
		}
		if (format == null) {
			log.error("DateFormat not supported for the date {} ", date);
			return null;
		}

		final String month = date.toLowerCase();
		if (month.contains("sept") && !month.contains("september")) {
			log.error("Scraped date value before formatting: {}", date);
			date = date.replaceAll("t", "");
			log.error("Scraped date value after formatting: {}", date);
		}

		final Date formattedDate = getFormattedDate(format, date);

		return formattedDate;
	}

	public static Date getFormattedDate(final DateFormat format, final String date) {
		Date formattedDate = null;
		if (date != null && date.isEmpty() == false) {

			try {
				formattedDate = new SimpleDateFormat(format.toString()).parse(date);
			} catch (final ParseException e) {
				log.error("Error", e);
			}
		}

		return formattedDate;
	}

}

enum PredictYearFor {
	STATEMENT_DATE,
	DUE_DATE,
	STATEMENT_DATE_AND_DUE_DATE,
	NULLITY;
}

class PredictDates {

	private String dueDate;
	private String stmtDate;

	public String getDueDate() {
		return dueDate;
	}

	public void setDueDate(final String dueDate) {
		this.dueDate = dueDate;
	}

	public String getStmtDate() {
		return stmtDate;
	}

	public void setStmtDate(final String stmtDate) {
		this.stmtDate = stmtDate;
	}
}