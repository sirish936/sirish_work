package com.sirish.io;

import java.io.IOException;
import java.io.InputStream;

public class RunSHFile {

	public static void main(final String[] args) {

		final Runtime runtime = Runtime.getRuntime();
		try {
			final Process process = runtime.exec("/home/sirish/Documents/sirish/myWork/shell/sampleshell");
			final InputStream is = process.getInputStream();

			int i = 0;
			while ((i = is.read()) != -1) {
				System.out.print((char) i);
			}
		} catch (final IOException ioException) {
			System.out.println(ioException.getMessage());
		}
	}
}
