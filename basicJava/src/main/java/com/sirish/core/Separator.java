package com.sirish.core;

public class Separator {
	public static void main(final String[] args) {
		final String separator = "|";

		final StringBuffer sb = new StringBuffer();
		sb.append("sirish").append(separator).append(12).append(separator).append(2016);
		final String data = sb.toString();
		System.out.println(data);

		final String[] arr = data.split("\\" + separator);
		for (int i = 0; i < arr.length; i++) {
			System.out.println(arr[i]);
		}
	}
}
