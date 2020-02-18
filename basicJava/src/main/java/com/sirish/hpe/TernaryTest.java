package com.sirish.hpe;

public class TernaryTest {
	public static int getSmallestNumber( int x, int y, int z) {

	     return x < y && x < z ? x : y < x && y < z ? y : z;
	}

	public static void main ( String ... args ) {

	    System.out.println( getSmallestNumber( 1234, 234, 345 ) );
	    String[] contents = {};
		for (int i = 0; i < contents.length; i++) {
			System.out.println(contents.length);
		}
	}
	
	
	
}
