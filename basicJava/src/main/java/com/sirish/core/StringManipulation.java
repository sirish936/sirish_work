package com.sirish.core;

import java.util.Scanner;

public class StringManipulation {
	
	@SuppressWarnings("resource")
	public static void main(String[] args) {
		
		System.out.println("Enter the string for manipulation");
		
		Scanner scanner = new Scanner(System.in);
		String input = scanner.nextLine();
		String splittedString[] =  input.split(" ");
		StringBuffer finalString = new StringBuffer();
		boolean revFlag = false;
		
		for (int i = 0; i < splittedString.length; i++) {
			if(revFlag  == false){
				finalString.append(splittedString[i]);
				revFlag =true;
			}else{
				String x= reversedString(splittedString[i]);
				finalString.append(" "+ x +" ");
				revFlag = false;
			}
		}
		System.out.println(finalString);
	}
	
		private static String reversedString(String str){
			char ch[] = new char[str.length()];
			for (int i = str.length() - 1, j = 0; i >= 0; i--) {
				ch[j++] = str.charAt(i);
			}
			return new String(ch);
		}
}
