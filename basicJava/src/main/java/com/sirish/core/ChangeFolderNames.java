package com.sirish.core;

import java.io.File;
import java.io.IOException;

public class ChangeFolderNames {

	public static void main(String[] args) throws IOException {

		changeFolderNames(args[0]);

	}

	private static void changeFolderNames(String input) throws IOException {

		File[] inputFiles = readFiles(input);

		for (File ipf : inputFiles) {
			
			File dir = new File(ipf.getPath());
			
			 if (!dir.isDirectory()) {
				 System.err.println("There is no directory at given path");
				 System.exit(0);
			 }
			
			String fileName = ipf.getName().toLowerCase();
			fileName = fileName.replaceAll("[^a-zA-Z0-9. ]", "").trim();
			
			String[] fileNameArray = fileName.split(" ");
			StringBuffer fileNameBuffer = new StringBuffer();

			int counter = 0;
			
			for (int i = 0; i < fileNameArray.length; i++) {
				
				if(counter > 2){
					break;
				}
				
				fileNameBuffer.append(fileNameArray[i]);
				fileNameBuffer.append(" ");
				counter++;
			}
			
			String finalName = new String(fileNameBuffer).replaceAll("hindi", "").trim(); 
			finalName = finalName.replaceAll("600mbshaanig asian planet", "").trim();
			finalName = finalName.replaceAll("dvdrip", "");
			finalName = finalName.replaceAll("brrip", "");
			finalName = finalName.replaceAll("bdrip", "");
			finalName = finalName.replaceAll("x264", "");
			finalName = finalName.replaceAll("webdlaacetrg", "");
			finalName = finalName.replaceAll("1080p", "").trim();
			finalName = finalName.replaceAll("720p", "").trim();
			
			 File newDir = new File(dir.getParent() + "/" + finalName);
			 dir.renameTo(newDir);
		}
	}

	private static File[] readFiles(String filePath) {

		File file = new File(filePath);
		File[] files = file.listFiles();

		return files;
	}
}
