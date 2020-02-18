package com.sirish.hpe;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class TestScenario {
	public static void main(String[] args) {
		ArrayList<String> strList = new ArrayList<String>();
		HashMap<String, ArrayList<String>> myMap = new HashMap<String, ArrayList<String>>();
		strList.add("hyderabad");
		populateList(strList);
		myMap.put("Telangana", strList);
		System.out.println(myMap.size());  
		MapClass myClass  = new MapClass();
		myClass.setMyMap(myMap);
		myMap.put("Banglore", strList);
		System.out.println(myClass.getMyMap().size());
		
		Map<String, ArrayList<String>> map = myClass.getMyMap();
		map.put("chennai", strList);
		System.out.println(myClass.getMyMap().size());
		
	}

	private static void populateList(ArrayList<String> strList) {
		for(String str : strList){
			strList.add("warangal");
			break;
		}
	}
}
