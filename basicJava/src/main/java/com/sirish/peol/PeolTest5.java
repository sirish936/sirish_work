package com.sirish.peol;

public class PeolTest5 {

	/**
	 * @param args
	 */
	public static void main(final String[] args) {
		// TODO Auto-generated method stub
		try {
			final int x = 5, y = 0;
			final int z = x / y;
			System.out.println(z);
		} catch (final Exception e) {
			System.out.println("Exception");
		}
		/*
		 * catch(ArithmeticException ae) { System.out.println("ArithmeticException"); }
		 */

		System.out.println("finished");
	}

}
