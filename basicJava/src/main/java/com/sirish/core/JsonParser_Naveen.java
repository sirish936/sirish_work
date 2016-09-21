package com.sirish.core;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class JsonParser_Naveen {

	@SuppressWarnings("resource")
	public static void main(final String[] args) throws IOException {

		final BufferedReader reader = new BufferedReader(new FileReader(new File("")));
		String line = null;

		final BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(new File(""))));

		while ((line = reader.readLine()) != null) {
			if (line.trim().isEmpty()) {
				break;
			}

			// SCRIPTREP Page
			// if(line.contains("SCRIPT FAILED")){
			// String stringID = line.split(",")[0];
			// String id= stringID.split(":")[1];
			// wr.write(String.format("%s", id.replaceAll("\"", "").trim()));
			// wr.write(String.format("%n"));
			//
			// }
			// SCR PAGE
			if (line.contains("\"login\" : \"INCORRECT CREDENTIALS\"") && !line.contains("ADMIN")) {
				final String[] stringID = line.split(",");

				for (final String str : stringID) {
					if (str.contains("providerId")) {

						final String id = str.split(":")[1];
						wr.write(String.format("%s", id.replaceAll("\"", "").trim()));
						wr.write(String.format("%n"));
					}
				}
			}
			wr.flush();
		}
	}

}
