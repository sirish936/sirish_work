package com.sirish.core;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

@SuppressWarnings("resource")
public class AlphabeticalSorting {
	public static void main(final String[] args) {
		try {

			final File file = new File("/home/sirish/Desktop/doc1");
			final FileWriter fw = new FileWriter("/home/sirish/Desktop/result");

			final FileReader fileReader = new FileReader(file);
			final BufferedReader bufferedReader = new BufferedReader(fileReader);

			final List<String> lineList = new ArrayList<String>();
			String line;
			while ((line = bufferedReader.readLine()) != null) {
				// line = line.substring(line.indexOf(":") + 1, line.inde xOf(";"));
				lineList.add(line);
			}

			// while ((line = bufferedReader.readLine()) != null) {
			// inputData = line.split("/")[1];
			// System.out.println(inputData);
			// }

			Collections.sort(lineList);

			for (final String outputLine : lineList) {
				fw.write(outputLine);
			}
			fw.flush();
			fileReader.close();
		} catch (final IOException e) {
			e.printStackTrace();
		}
	}
}
