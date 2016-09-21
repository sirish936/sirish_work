package com.sirish.core;

import java.io.IOException;
import java.util.Scanner;
@SuppressWarnings("resource")

public class LCM {
	public static void main(final String args[]) throws IOException {
		final Scanner sc1 = new Scanner(System.in);
		final Scanner sc2 = new Scanner(System.in);
		final int a = sc1.nextInt();
		final int b = sc2.nextInt();
		int lcm = 1;
		for (int i = 1; i <= a * b; i++) // Even if you start the for loop by 1, you will get the answer, but starting it from either the first or the second
											// number reduces the number of times the for loop is executed.
		{
			if (i % a == 0 && i % b == 0) // Checking the first number which is divisible by both the numbers
			{
				lcm = i;
				break; // exiting from the loop, as we don’t need anymore checking after getting the LCM
			}
		}
		System.out.println("L.C.M. = " + lcm);
	}

}
