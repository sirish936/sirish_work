package com.sirish.strings;

public class MaxLengthString {

	public static void main(String[] args) {
		
		String input[] = {"abcd","pedagadavilli","sirish","nivas","nimmakayala"};
		
		String maxStr = input[0];
		for(String inputStr : input){
			
			if(inputStr.length() > maxStr.length()){
				maxStr = inputStr;
			}
		}
		System.out.println("MaxLength String is: "+maxStr);
	}
}
