package com.sirish.io;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class FileCopy {

	public static void main(String[] args) throws IOException {
		
			copyFiles(args[0],args[1]);
		
		}

			private static void copyFiles(String input,String output) throws IOException {

				File destFile = new File(output);

				File[] inputFiles = readFiles(input);
				File[] outputFiles = readFiles(output);

				boolean found = false;

				for (File ipf : inputFiles) {

					found = false;

					for (File fn : outputFiles) {

						if (ipf.getName().trim().equalsIgnoreCase(fn.getName().trim())) {
							found = true;
						}
					}

					if (found == false) {
						Path sourcePath = ipf.toPath();
						Path destPath = destFile.toPath();
						Files.copy(sourcePath, destPath.resolve(sourcePath.getFileName()));
						
						System.out.println(ipf.getName() + ": File copied");
					}
				}
			}
			
			
			private static File[] readFiles(String filePath) {

				File file = new File(filePath);

				File[] files = file.listFiles();

				return files;
			}

}
