package com.sirish.strings;

public class StringTest3 {
	static String[] accNo;

	public static void main(final String[] args) {
		String accountNumber = "0004567567-000035454";
		accNo = accountNumber.split("-");
		accountNumber = Integer.valueOf(accNo[0]) + "-" + Integer.valueOf(accNo[1]);
		System.out.println(accountNumber);

	}

}


