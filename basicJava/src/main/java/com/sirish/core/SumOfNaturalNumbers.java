package com.sirish.core;

public class SumOfNaturalNumbers {
	public static void main(String args[])
	{		
		int n, sum=0;
		for(n=1;n<=10;n++)
		{
			sum+=n;    //or sum=sum+n;
		}
		System.out.println(sum);
	}
}
