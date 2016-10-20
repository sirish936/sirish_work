package com.sirish.io;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class FileContentManipulation {

	public static void main(String[] args) throws Exception{
		
		File inputFile = new File(args[0]);
		List<String> strList = new ArrayList<String>();
		
		 Scanner scanner = new Scanner(inputFile);
	     while (scanner.hasNext()) {
	        strList.add(scanner.next());
	       }
	     
	    FileWriter writer = new FileWriter(inputFile);
	    BufferedWriter bufferedWriter = new BufferedWriter(writer);


		for(int i=0;i<strList.size();i++){
			bufferedWriter.write(strList.get(strList.size()-(i+1)));
		}
		 scanner.close();
		 bufferedWriter.flush();
		 bufferedWriter.close();
	}
}
