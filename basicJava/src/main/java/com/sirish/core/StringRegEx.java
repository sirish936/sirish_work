package com.sirish.core;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class StringRegEx {

	public static void main(final String[] args) {

		final String str = "javascript:getStatement(20160412,1061556863)";

		String formattedHrefValue = str.replace("javascript:getStatement", "");
		formattedHrefValue = formattedHrefValue.replace("(", "");
		formattedHrefValue = formattedHrefValue.replace(")", "");

		final String[] formattedHrefValueArray = formattedHrefValue.split(",");

		final String newStr = "https://onlinebanking.tdbank.com/accts/acct_eStatement_View.asp?viewDate=" + formattedHrefValueArray[0] + "&statementIndex="
				+ formattedHrefValueArray[1] + "&acctID=";

		System.out.println(newStr);

		final String inputStr1 = "https://docsight.net/XDSServer/CCW_60654572.pdf?HID=CCWS2210&TID=60654572&LGD=2016-06-28%2013:24:45&AID=593759-150148&DDT=06/02/2016&OLI=Y&PWD=6C8C7F122F3559065E0251675A191CD7";
		final String inputStr2 = "https://docsight.net/XDSServer/CCW_60116837.pdf?HID=CCWS2210&TID=60116837&LGD=2016-06-28%2013:24:45&AID=593759-150148&DDT=05/03/2016&OLI=Y&PWD=7FBFE0E85C40A19AA85E55085C55B7A8";

		final String strArray1[] = inputStr1.split("=");
		System.out.println(strArray1[5].replaceAll("[^0-9/]", ""));

		final String strArray2[] = inputStr2.split("=");
		System.out.println(strArray2[5].replaceAll("[^0-9/]", ""));

		getFormattedStatementDate();

		getEmailString();

	}

	private static void getFormattedStatementDate() {

		boolean matchFound = true;
		// final String pattern = "((\\d){1,2}/){2}(\\d){4}";
		final String pattern = "((\\d){4}-)((\\d){1,2}-)(\\d){1,2}";
		// final String pattern = "(\\d){4}[-](\\d){1,2}[-](\\d){1,2}";
		final Pattern p = Pattern.compile(pattern);

		// String stmtDate =
		// "https://docsight.net/XDSServer/CCW_60116837.pdf?HID=CCWS2210&TID=60116837&LGD=2016-06-28%2013:24:45&AID=593759-150148&DDT=05/03/2016&OLI=Y&PWD=7FBFE0E85C40A19AA85E55085C55B7A8";
		String stmtDate = "popUp('StatementContainer?storeId=10451&catalogId=10001&langId=-1&closeDate=2015-03-10&storeNum=2462')";

		final Matcher m = p.matcher(stmtDate);
		while (m.find()) {
			if (matchFound) {
				stmtDate = stmtDate.substring(m.start(), m.end());
				matchFound = false;
			}
		}
		System.out.println(stmtDate);
	}

	private static void getEmailString() {

		boolean matchFound = true;
		final String pattern = "[*A-Za-z0-9._%-]+@[*A-Za-z0-9.-]+[A-Za-z]{2,4}";
		final Pattern p = Pattern.compile(pattern);

		String inputStr = "Please enter the code we sent to your b**81@hotmail.com account in the field below to verify it's really you";

		final Matcher m = p.matcher(inputStr);
		while (m.find()) {
			if (matchFound) {
				inputStr = inputStr.substring(m.start(), m.end());
				matchFound = false;
			}
		}
		System.out.println(inputStr);
	}
}
