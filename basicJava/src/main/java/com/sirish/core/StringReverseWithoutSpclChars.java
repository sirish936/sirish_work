package com.sirish.core;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class StringReverseWithoutSpclChars {
	
	public static void main(String[] args) {
		
	 Scanner scanner = new Scanner(System.in);
	 final String inputStr = scanner.nextLine();
	 final char[] myChars = new char[inputStr.length()] ;
	 List<Integer> spclCharIndexList = new ArrayList<Integer>();
	 List<Character> outputList = new ArrayList<Character>();
 	 
	 for (int i = 0; i < inputStr.length(); i++) {
		 if(isSpclChar(inputStr.charAt(i))){
			 spclCharIndexList.add(inputStr.indexOf(inputStr.charAt(i)));
		 }
	 }
	 
	 for (int i = inputStr.length()-1;i >=0; i--) {
		 if(isSpclChar(inputStr.charAt(i))){
			 continue;
		 }
		 outputList.add(inputStr.charAt(i));
	 }
	 
	 for (int i = 0; i < spclCharIndexList.size(); i++) {
		 int x = spclCharIndexList.get(i);
		 char ch = inputStr.charAt(x);
		 outputList.add(x, ch);
	}
	 
	 for (int i = 0,j=0; i < outputList.size(); i++) {
		 myChars[j++] = outputList.get(i);
	}

	 System.out.println(new String(myChars));
	 
	}

	private static boolean isSpclChar(Character ch) {
		if(ch.toString().matches("[^0-9a-zA-Z]")){
			return true;
		}
		return false;
	}
}
