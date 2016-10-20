package com.sirish.io;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.Scanner;

public class PrintFromFile {

	/**
	 * @param args
	 */
	@SuppressWarnings("resource")
	public static void main(final String[] args) {
		// TODO Auto-generated method stub
		try {
			final Scanner scanner1 = new Scanner(new File("C:\\ravi\\Examples\\f1.txt")).useDelimiter(" ");
			final String string1 = scanner1.next();

			final Scanner scanner2 = new Scanner(new File("C:\\ravi\\Examples\\f2.txt")).useDelimiter(" ");
			final String string2 = scanner2.next();

			final byte[] b = new byte[1024];
			int i;

			if (string1.length() > string2.length()) {
				final File file1 = new File("C:\\ravi\\Examples\\f1.txt");
				final InputStream inputstream1 = new FileInputStream(file1);
				final OutputStream outputstream1 = new FileOutputStream("C:\\ravi\\Examples\\g1.txt");
				while ((i = inputstream1.read(b)) != -1) {
					outputstream1.write(b, 0, i);
				}// while
			}// if
			else {
				final File file2 = new File("C:\\ravi\\Examples\\f2.txt");
				final InputStream inputstream2 = new FileInputStream(file2);
				final OutputStream outputstream2 = new FileOutputStream("C:\\ravi\\Examples\\g2.txt");
				while ((i = inputstream2.read(b)) != -1) {
					outputstream2.write(b, 0, i);
				}// while
			}// else
		}// try
		catch (final Exception e) {
			e.printStackTrace();
		}// catch
	}// main
}// class