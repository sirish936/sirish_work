package com.sirish.interview;

import java.util.Vector;

public class CallByValueUsingObjectParam {
	@SuppressWarnings({ "unchecked", "rawtypes" })
	public static void main(final String[] args) {
		final Vector vc = new Vector();

		vc.add("111");
		vc.add("222");
		functioncall(vc);
		vc.add("333");
		System.out.println(vc);
	}

	public static void functioncall(@SuppressWarnings("rawtypes") Vector vc) {
		// vc.removeAllElements();
		vc = null;
		// vc = new Vector();
		// vc.add("444");
		System.out.println(vc);
	}
}
