package com.sirish.hpe;

import java.util.Scanner;

public class TestUPR {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		String upr = sc.next(); 
		
		if (upr != null && upr.isEmpty() == false)
        {
            if (upr.equalsIgnoreCase(UpgradeRequirement.CRITICAL.toString()))
            {
            	System.out.println(UpgradeRequirement.CRITICAL.toString());
            }
            else if (upr.equals(UpgradeRequirement.RECOMMENDED.toString()))
            {
                System.out.println(UpgradeRequirement.RECOMMENDED);
            }
            else
            {
            	System.out.println(UpgradeRequirement.OPTIONAL);
            }
        }
	}
}
