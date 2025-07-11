package com.sirish.hpe;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class ILOMpModelUtil
{
	private static final Pattern pattern = Pattern.compile("(\\d+)");
	public static boolean isILOModelAtLeast(String iLOModel, int modelAtLeast)
	{
		Matcher matcher = pattern.matcher(iLOModel);
		if (matcher.find()) {
			String modelNumber = matcher.group(1);
			int mpModel = Integer.parseInt(modelNumber);
			boolean value = mpModel >= modelAtLeast;
			System.out.println(value);
			return value;
		} else {
			System.out.println("false");
			return false;
		}
	}
    
    public static void main(String[] args)
    {
    	isILOModelAtLeast("iLO 7",7);
    	isILOModelAtLeast("ILO 7", 7);
    	isILOModelAtLeast("iLO7", 7);
    	isILOModelAtLeast("ILO7", 7);
    	isILOModelAtLeast("integrated Lights Out 7", 7);
    	isILOModelAtLeast("iLO 7", 8);
    	isILOModelAtLeast("iLO 6", 7);
    	isILOModelAtLeast("iLO 6", 6);
    	isILOModelAtLeast("iLO 6", 5);
    	isILOModelAtLeast("iLO 6", 9);
    	isILOModelAtLeast("iLO 8", 6);
    	isILOModelAtLeast("iLO 8", 7);
    }
}
