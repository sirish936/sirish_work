package com.sirish.core;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Properties;

public class PropertyRead {

	public static void main(final String[] args) throws IOException {

		final Properties p = new Properties();
		p.load(PropertyRead.class.getClassLoader().getResourceAsStream("abc.properties"));

		final File file = new File("output.txt");
		final FileWriter fw = new FileWriter(file);

		fw.write(p.getProperty("sirish"));
		fw.write(p.getProperty("vinay"));

		fw.flush();
		fw.close();

		System.out.println(p.getProperty("sirish"));
		System.out.println(p.getProperty("vinay"));
	}
}
