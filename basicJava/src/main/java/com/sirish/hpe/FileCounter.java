package com.sirish.hpe;

import java.io.File;
import java.util.Scanner;

public class FileCounter {
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		String dirName =sc.next();
		File Files = new File(dirName);
		int Count = Files.list().length;
		System.out.println("No. Of Files: "+Count);
	}
}