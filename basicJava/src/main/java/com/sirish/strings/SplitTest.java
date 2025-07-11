package com.sirish.strings;

public class SplitTest {
	public static void main(String[] args) {

		//Example 1, existing version format
		String mpFwVersion = "2.40 June 26 2015";
		final String[] mpFwVersionTokens = mpFwVersion.split(" ");
		
		System.out.println("Length of string is:" + mpFwVersionTokens.length);
		
		final String majorMinorVersion = mpFwVersionTokens[0];
		final float majorMinorVersionNumber = Float.parseFloat(majorMinorVersion);
		
        final Integer minVersionMajorInt = 1;
        final Integer minVersionMinorInt = 1;
        final String minMajorMinorVersion = minVersionMajorInt.toString().trim()
                + "."
                + minVersionMinorInt.toString().trim();
        final float minMajorMinorVersionNumber = Float.parseFloat(minMajorMinorVersion);
        
        if(majorMinorVersionNumber >=  minMajorMinorVersionNumber)
        {
        	System.out.println("Apply settings supported");
        }
        else
        {
        	System.out.println("Apply settings not supported");
        }
        
        //Example 2,new version format
        String fwVersion = "1.01.00 June 26 2015";
		final String[] fwVersionTokens = fwVersion.split(" ");
		final String[] fwVersionNumberTokens = fwVersionTokens[0].split("\\.");
		
		System.out.println("Length of string is:" + fwVersionNumberTokens.length);
		
		final String majorMinorNumberVersion = fwVersionNumberTokens[0].toString().trim()
                + "."
                + fwVersionNumberTokens[1].toString().trim();
		
		final float majorMinorVersion2Number = Float.parseFloat(majorMinorNumberVersion);
		
        final Integer minVersionMajorInt2 = 1;
        final Integer minVersionMinorInt2 = 1;
        final String minMajorMinorVersionStr = minVersionMajorInt2.toString().trim()
                + "."
                + minVersionMinorInt2.toString().trim();
        final float minMajorMinorVersion2Str = Float.parseFloat(minMajorMinorVersionStr);
        
        if(majorMinorVersion2Number >=  minMajorMinorVersion2Str)
        {
        	System.out.println("Apply settings supported");
        }
        else
        {
        	System.out.println("Apply settings not supported");
        }
	}
}
