package com.sirish.core;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class IntuitlogFileExtractor {

	/**
	 * @param args
	 */
	public static void main(final String[] args) {
		final String logFileWithPath = args[0];
		try {
			extract(logFileWithPath);
		} catch (final IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (final InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

	static ArrayList<String> getSearchStrings() {
		final ArrayList<String> searchStrlist = new ArrayList<String>();
		searchStrlist.add("com.intuit.ipp.aggcat.interceptor.ConnectionInterceptor");
		return searchStrlist;
	}

	public static void extract(final String logFileWithPath) throws IOException, InterruptedException {

		final File f = new File(logFileWithPath);
		final String absolutePath = f.getAbsolutePath();
		final String filePath = absolutePath.substring(0, absolutePath.lastIndexOf(File.separator));

		System.out.println(filePath);

		final ArrayList<String> searchStrList = getSearchStrings();
		final BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(filePath + "//result.txt")));
		@SuppressWarnings("resource")
		final BufferedReader reader = new BufferedReader(new InputStreamReader(new FileInputStream(logFileWithPath)));
		String line = null;

		int count = 0;

		while ((line = reader.readLine()) != null) {
			count++;

			try {
				for (final String searchStr : searchStrList) {
					if (line.contains(searchStr)) {
						final String[] lineParts = line.split(" - ");
						wr.write(lineParts[1]);
						wr.write(String.format("%n"));
					} else {
						System.out.println("Not found for line " + count);
					}
				}
			} catch (final Exception ex) {

			}

		}

		wr.flush();
		wr.close();

	}
}
