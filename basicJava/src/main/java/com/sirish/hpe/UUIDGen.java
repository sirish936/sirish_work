package com.sirish.hpe;

import java.io.File;
import java.io.ObjectStreamClass;
import java.io.Serializable;
import java.util.HashMap;
import java.util.Map;

public class UUIDGen implements Serializable{
	/**
	 * 
	 */
	private static final long serialVersionUID = -1246175219574289924L;

	public static void main(String[] args) {
		ObjectStreamClass c = ObjectStreamClass.lookup(UUIDGen.class);
		long serialID = c.getSerialVersionUID();
		System.out.println(serialID);
		System.out.println(new Long("3"));
		
		Map<String,String> myMap = new HashMap<String,String>();
		String str = null+"abc";
		myMap.put(null+"abc","Bang");
		myMap.put("bcd","Hyd");
		myMap.put("cde","Mas");
		
		System.out.println("My map size is::"+myMap.size());
		
		String value = myMap.get("bcde");
		System.out.println("Value is ::"+value);
		
		File[] files = {};
		if(files.length<=0){
			System.out.println("file size is: "+files.length);
		}
		
		for(File file : files){
			System.out.println("No files");
		}
		
		String uri = "http://15.212.172.94/nossl/fwbundles/abs/37383738-3631-4753-4838-333159505432/cp036946_02/cp036946_part2.compsig";
		final String[] sigFileName = uri.split("/", uri.length());
		String sys = sigFileName[sigFileName.length - 1];
		
		String filename= "cp36946.zip";
		String otherfilename= "cp36946_01/cp3694623.zip";
		System.out.println(otherfilename.contains(filename));
		
		if(!new File("C://Users//nimmaksi//Desktop//Issues//sirish.txt").exists())
			System.out.println("File doesnot exists");
		else
			System.out.println("File exists");	
				
			
		}
	
	
	}
	
	
	
