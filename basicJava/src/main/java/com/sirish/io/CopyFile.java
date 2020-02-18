package com.sirish.io;

import java.io.*;

public class CopyFile {

	public static void main(String args[]) throws IOException {
		FileReader in = null;
		FileWriter out = null;

		try {
			in = new FileReader("input.txt");
			out = new FileWriter("output.txt");

			int c;
			while ((c = in.read()) != -1) {
				out.write(c);
			}
		} catch (Exception e) {
			System.out.println("Exception --->" + e.getMessage());
		} finally {
			if (in != null) {
				in.close();
			}
			if (out != null) {
				out.close();
			}
		}
	}
}