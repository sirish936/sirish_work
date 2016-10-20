package com.sirish.io;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class FileDataRead {

	public static void main(String[] args) throws IOException {
		String line = null;
		BufferedWriter wr = null;
		BufferedReader reader =null;
		try {
			reader = new BufferedReader(new InputStreamReader(new FileInputStream(args[0])));
			wr = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(args[1])));
			while ((line = reader.readLine()) != null) {
				wr.write(line);
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}finally{
			wr.close();
			reader.close();
		}
	}
}
