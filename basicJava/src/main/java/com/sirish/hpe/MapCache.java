package com.sirish.hpe;

public class MapCache {
	public static void main(String[] args) {
		MApHelper mapHelper = new MApHelper();
		String value1 = mapHelper.getSwKeyForICModel("Cat");
		System.out.println("Cat : " + value1);
		String value2 = mapHelper.getSwKeyForICModel("Eagle");
		System.out.println("Eagle : " + value2);
	}
}


