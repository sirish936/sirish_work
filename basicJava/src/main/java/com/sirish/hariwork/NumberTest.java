package com.sirish.hariwork;

import java.util.ArrayList;
import java.util.List;

public class NumberTest {
public static void main(String[] args) {
	List<Number> list = new ArrayList<Number>();
	Number n = Integer.valueOf(1);
	list.add(n);
	Float f = Float.valueOf(1.0f);
	list.add(f);
	Double d = Double.valueOf(1.0d);
	list.add(d);
	for (Number number : list) {
		System.out.println(number);
	}
	
}
}
