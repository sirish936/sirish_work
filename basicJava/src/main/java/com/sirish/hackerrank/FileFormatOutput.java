package com.sirish.hackerrank;

import java.util.Scanner;

public class FileFormatOutput {

	public static void main(final String[] args) {
		try {
			int i = 1;
			// final File file = new File(args[0]);
			final Scanner scanner = new Scanner(System.in);
			while (scanner.hasNextLine()) {
				System.out.println(i + " " + scanner.nextLine());
				i++;
			}
			scanner.close();
		} catch (final Exception e) {
			e.printStackTrace();
		}
	}

}
