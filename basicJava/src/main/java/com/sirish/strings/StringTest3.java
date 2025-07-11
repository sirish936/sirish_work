package com.sirish.strings;

public class StringTest3 {
	static String[] accNo;

	public static void main(final String[] args) {
		String accountNumber = "0004567567-000035454";
		accNo = accountNumber.split("-");
		accountNumber = Integer.valueOf(accNo[0]) + "-" + Integer.valueOf(accNo[1]);
		System.out.println(accountNumber);
		String regex = "(?!.*/).+";
		String data = "/ci/data/sum_repository/hotfix_repsitory/internal/cp036916_part1.compsig";
		System.out.println(data.substring(data.lastIndexOf("/")+1));
		String response0 = data.split(regex)[0];
		String response1 = data.split(regex)[0];
		System.out.println("Response0 "+response0+" Response1 "+response1 );

		int x = (24000/ 10000)+1;
		System.out.println(x);
		
	}

}


