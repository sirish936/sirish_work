package com.sirish.core;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.Properties;

public class PropertyRead {
	
	public static void main(String[] args) throws IOException {
		
		File file  = new File("/home/sirish/Desktop/properties.properties");
		FileInputStream fis = new FileInputStream(file);
		Properties p = new Properties();
		p.load(fis);
		
		System.out.println(p.getProperty("sirish"));
		System.out.println(p.getProperty("vinay"));
		System.out.println(p.getProperty("lok"));
	
	}
}
	