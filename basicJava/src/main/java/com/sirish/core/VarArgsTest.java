package com.sirish.core;

public class VarArgsTest {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		int x[]={1,2,3};
		int y[]={4,5,6};
		new VarArgsTest().go(x,y);
	}
	void go(int[]...z){
		for(int[] a: z)
			System.out.print(a[1]);

	}

}
