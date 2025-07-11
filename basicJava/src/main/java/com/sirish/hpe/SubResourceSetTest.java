package com.sirish.hpe;

import java.util.HashSet;
import java.util.Set;

public class SubResourceSetTest {
	public static void main(String[] args) {
		final Set<SubResourceName> names = new HashSet<SubResourceName>();
		names.add(SubResourceName.Memory);
		names.add(SubResourceName.Processors);
		
		if (names != null && !names.isEmpty())
		{
			System.out.printf("Adding initial subResource to the server: " +  names.toString());
			names.forEach(name -> {
				System.out.printf("Added initial subResource '{}' to the server", name);
			});
		}
		
	}

}
