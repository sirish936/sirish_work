package com.sirish.io;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.Scanner;

public class PrintData {

	/**
	 * @param args
	 */
	@SuppressWarnings("resource")
	public static void main(final String[] args) {
		// TODO Auto-generated method stub
		try {
			final Scanner s1 = new Scanner(new File("C:/ravi/Examples/f1.txt")).useDelimiter(" ");
			final String ss1 = s1.next();
			System.out.println(ss1);
			while (s1.hasNext()) {
				final String string1 = s1.next();
				System.out.println(string1.length());
			}// while

			final Scanner s2 = new Scanner(new File("C:\\ravi\\Examples\\f2.txt")).useDelimiter(" ");
			while (s2.hasNext()) {
				final String string2 = s2.next();
				System.out.println(string2.length());
			}// while

			final File file1 = new File("C:\\ravi\\Examples\\f1.txt");
			// File file2=new File("C:\\ravi\\Examples\\f2.txt");
			// File file3=new File("C:\\ravi\\Examples\\f3.txt");
			final OutputStream outputstream1 = new FileOutputStream("C:\\ravi\\Examples\\g1.txt");

			final InputStream inputstream1 = new FileInputStream(file1);
			final byte[] b = new byte[1024];
			int i;
			while ((i = inputstream1.read(b)) != -1) {
				outputstream1.write(b, 0, i);
			}// while
		}// try

		catch (final Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}

	}

}
