package com.work.finovera;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class DateFormatter {
	
	static final Logger log = LoggerFactory.getLogger(DateFormatter.class);	

	public  DateFormat getFormattedDate(String date) {
		DateFormat format = null;
		if (date != null && !date.isEmpty()) {
			date = date.replaceFirst("st", "").replaceFirst("nd", "").replaceFirst("rd", "").replaceFirst("th", "");
			date = date.trim();

			if (date.matches("((\\d){4}-)((\\d){1,2}-)(\\d){1,2}")) {
				format = DateFormat.YYYY_MM_DD_WITH_HYPHEN;
			}else if(date.matches("((\\d){4}/)((\\d){1,2}/)(\\d){1,2}")){
				format = DateFormat.YYYY_MM_DD_WITH_SLASH;
			}else if(date.matches("((\\d){1,2}-){2}(\\d){4}")){
				format = DateFormat.MM_DD_YYYY_WITH_HYPHEN;
			}else if(date.matches("((\\d){1,2}/){2}(\\d){4}")){
				format = DateFormat.MM_DD_YYYY_WITH_SLASH;
			}else if(date.matches("((\\d){1,2}-){2}(\\d){2}")){
				format = DateFormat.MM_DD_YY_WITH_HYPHEN;
			}else if(date.matches("((\\d){1,2}/){2}(\\d){2}")){
				format = DateFormat.MM_DD_YY_WITH_SLASH;
			} else if (date.matches("(\\w){3,9}\\s+((\\d){1,2},)\\s+((\\d){4})")) {
				format = DateFormat.MMM_DD_YYYY_WITH_SPACE;
			}else if (date.matches("(\\w){3,9}\\s+((\\d){1,2},)((\\d){4})")) {
				format = DateFormat.MMM_DD_YYYY_WITHOUT_SPACE;
			}else if (date.matches("(\\d){1,2}\\s+((\\w){3,9},)\\s+((\\d){4})")) {
				format = DateFormat.DD_MMM_YYYY_WITH_SPACE;
			}else if (date.matches("(\\d){1,2}\\s+((\\w){3,9},)((\\d){4})")) {
				format = DateFormat.DD_MMM_YYYY_WITHOUT_SPACE;
			}	else if (date.matches("(\\w){3,9}\\s+((\\d){1,2},)\\s+((\\d){2})")) {
				format = DateFormat.MMM_DD_YY_WITH_SPACE;
			}else if (date.matches("(\\w){3,9}\\s+((\\d){1,2},)((\\d){2})")) {
				format = DateFormat.MMM_DD_YY_WITHOUT_SPACE;
			}else if (date.matches("(\\d){1,2}\\s+((\\w){3,9},)\\s+((\\d){2})")) {
				format = DateFormat.DD_MMM_YY_WITH_SPACE;
			}else if (date.matches("(\\d){1,2}\\s+((\\w){3,9},)((\\d){2})")) {
				format = DateFormat.DD_MMM_YY_WITHOUT_SPACE;
			}else if (date.matches("(\\d){1,2}\\s+((\\w){3,9})")) {
				format = DateFormat.DD_MMM;
			}else if (date.matches("((\\w){3,9})\\s+(\\d){1,2}")) {
				format = DateFormat.MMM_DD;
			}else if (date.matches("((\\d){1,2}-)(\\d){1,2}")) {
				format = DateFormat.MM_DD_WITH_HYHEN;
			}else if (date.matches("((\\d){1,2}/)(\\d){1,2}")) {
				format = DateFormat.MM_DD_WITH_SLASH;
			}
			
			
			if (format == null) {
				 log.error("DateFormat not supported for the date {} ", date);
				return null;
			}
		}
		return format;
	}
}