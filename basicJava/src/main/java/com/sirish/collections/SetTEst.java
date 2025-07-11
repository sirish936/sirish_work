package com.sirish.collections;

import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

public class SetTEst {
public static void main(String[] args) {
	final Set<Integer> set1 = new HashSet();
	set1.add(3);
	set1.add(6);
	set1.add(2);
	set1.add(2);
	set1.add(4);
	set1.add(5);
	set1.add(5);
	set1.add(5);
	set1.add(6);
	set1.add(2);
	set1.add(4);
	System.out.println(set1);
	
	final Set<Integer> set2 = new HashSet();
	set2.add(7);
	set2.add(8);
	
	
	System.out.println(set2);
	set1.retainAll(set2);
	
	System.out.println(set1);
	System.out.println(set2);
	
	final Iterator<Integer> iterator1 = set1.iterator();
	while (iterator1.hasNext()) {
		//System.out.println(iterator1.next());
	}
	for (final Integer inte : set2) {
		//System.out.println(inte);
	}

}
}
