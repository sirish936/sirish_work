package com.sirish.interview;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Scanner;

public class SumofQuotients {
	public static void main(String[] args) {
		int listSize, divider, sum = 0;
		System.out.println("Enter the listSize :");
		Scanner scanner = new Scanner(System.in);
		listSize = scanner.nextInt();
		System.out.println("Enter the number to divide the numbers: ");
		divider = scanner.nextInt();
		System.out.println("Enter the list of the numbers: ");
		List<Integer> al = new ArrayList<Integer>();
		for (int i = 0; i < listSize; i++) {
			int x = scanner.nextInt();
			al.add(x);
		}
		for (Integer integer : al) {
			int result = integer/divider;
			sum = sum+result;
		}
		System.out.println("Sum  of quotients is "+sum);
	}
}
