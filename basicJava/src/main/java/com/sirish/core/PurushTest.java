package com.sirish.core;


public class PurushTest {
	
public static void main(String[] args) {
	try {
		throw new Exception();
	} catch (Exception e) {
		System.out.println("from catch:");
		return;
		System.out.println("from catch: after return");
	}finally{
		System.out.println("from finally:");
	}
  }
}