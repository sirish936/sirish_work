package com.sirish.core;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

@SuppressWarnings("resource")
public class GetProviderNames {
	public static void main(final String[] args) {
		try {
			final File file = new File("/home/sirish/Documents/sirish/myWork/docs/doc");
			final FileReader fileReader = new FileReader(file);
			final FileWriter fw = new FileWriter("/home/sirish/Documents/sirish/myWork/docs/result");
			final BufferedReader bufferedReader = new BufferedReader(fileReader);
			final StringBuffer sb = new StringBuffer();
			String line;
			while ((line = bufferedReader.readLine()) != null) {
				line = line.substring(line.indexOf(":") + 1, line.indexOf(";"));
				if (line.contains("_")) {
					continue;
				}
				sb.append(line.trim());
				sb.append(",");
			}
			fw.write(sb.toString());
			fw.flush();
			fileReader.close();
		} catch (final IOException e) {
			e.printStackTrace();
		}
	}
}
