package com.sirish.io;

import java.io.File;

public class TestReadFiles {
	public static void main(String[] args) {
		File[] files = FileCopy
				.readFiles("C://Users//nimmaksi//Desktop//output");
		for (File file : files) {
			System.out.println("fileNames are :: " + file.getName());
			System.out.println(Integer.valueOf("10"));
				
		}
	}
}
