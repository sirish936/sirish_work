package com.sirish.io;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;

public class ReadTextFileData {
	
	@SuppressWarnings("resource")
	public static void main(String[] args)throws Exception {
		
		File inputFile = new File(args[0]);
		File outputFile = new File(args[1]);
		FileInputStream fis = new FileInputStream(inputFile);
		FileOutputStream fos = new FileOutputStream(outputFile);
		
		byte[] b=new byte[1024];
		int i;
		
		while((i=fis.read(b))!=-1){
			fos.write(b,0,i);			
		}
	}
}
