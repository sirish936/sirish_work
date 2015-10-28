package com.sirish.core;


public class EquilibriumIndex {
	
	public static void main(String[] args) {
		
	int number[] =  {2,4,3,7,0,2};
    int leftSum=0,rightSum = 0;
    
    for (int i = 0; i < number.length/2; i++) {
    	
    	leftSum = leftSum + number[i];
    	rightSum = rightSum + number[number.length-i-1];
    	
    	if(leftSum == rightSum){
    		System.out.println("Equilibrium index is "+ i + " and the number is " +number[i]);
    	}
	}
  }
}
