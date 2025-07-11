package com.sirish.strings;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

public class SBTest {
	public static void main(String[] args) {
		StringBuffer sb = new StringBuffer("Server hardware");
		for (int i = 0; i < 5; i++) {
			if (sb.toString().contains("Server")) {
				sb.append("Server hardware");
			}
		}
		System.out.println(sb.toString());
		if(sb.equals(null)){
			System.out.println(sb.toString());
		}
		
		
		List list = new ArrayList<>();
		list.add(2);
		list.add(4);
		list.add(3);
		list.add(1);
		System.out.println(list);
		Collections.sort(list);
		System.out.println(list);
		
		
		int a = 20;
		int b = 21;
		int s = Math.max(a, b);
		System.out.println(s);
				
		
	}
	
}
