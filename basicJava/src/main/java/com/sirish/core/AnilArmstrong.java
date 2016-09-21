package com.sirish.core;

public class AnilArmstrong {
	
public static void main(String[] args) {
	
	int number = 152;
	int input = number;
	int x=number;
	int sum = 0;
	while(number>0){
		x = number%10;
		sum = sum+ (x*x*x);
		number =number/10;
	}
	if(sum == input){
		System.out.println("armstrong number");
	}else{
		System.out.println("not armstrong number");
	}
	}	
}
