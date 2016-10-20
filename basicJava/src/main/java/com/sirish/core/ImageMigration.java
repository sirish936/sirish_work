package com.sirish.core;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class ImageMigration {

	public static void main(String[] args) throws IOException {

		String[] folder = new String[] { "62x36", "172x100", "86x50" };

		for (String str : folder) {
			copyFiles(str);
		}
	}

	private static File[] readFilesName(String path, String folder) {

		String str = "/home/vinay/work/" + path + "/static/src/main/webapp/resources/images/logos/" + folder;

		File file = new File(str);

		File[] files = file.listFiles();

		return files;
	}

	private static void copyFiles(String str) throws IOException {

		File destFile = new File("/home/vinay/work/finovera/web/static/src/main/webapp/resources/images/logos/" + str);

		File[] fiportFiles = readFilesName("fiport/webapps", str);
		File[] finoveraFiles = readFilesName("finovera/web", str);

		boolean found = false;

		for (File fp : fiportFiles) {

			found = false;

			for (File fn : finoveraFiles) {

				if (fp.getName().trim().equalsIgnoreCase(fn.getName().trim())) {
					found = true;
				}
			}

			if (found == false) {
				Path sourcePath = fp.toPath();
				Path destPath = destFile.toPath();
				Files.copy(sourcePath, destPath.resolve(sourcePath.getFileName()));
				
				System.out.println(fp.getName() + ": Image copied to Finovera.");
			}
		}

	}

}
