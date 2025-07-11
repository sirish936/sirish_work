package com.sirish.strings;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class HelloWorld {

	public static void main(String[] args) {
//		String fileName = "firmware-ilo5-2.10-1.1.x86_64_part1.compsig";
//		String normalizedFileName = "firmware-ilo5-2_10-1_1_x86_64_part1.compsig";
//		String resourceId = "firmware-ilo5-2_10-1_1_x86_64_part1";
		
		String fileName = "firmware-ilo5-2.10-1.1.x86_64.compsig";
		String normalizedFileName = "firmware-ilo5-2_10-1_1_x86_64.compsig";
		String resourceId = "firmware-ilo5-2_10-1_1_x86_64";
		
//		String fileName = "cp036916_part1.compsig";
//		String normalizedFileName = "cp036916_part1.compsig";
//		String resourceId = "cp036916_part1";
		resourceId = getResourceIDForMultiCompsigHotfix(fileName, normalizedFileName,resourceId);
			
		}
		
		

	static String getResourceIDForMultiCompsigHotfix(final String fileName, final String normalizedFileName, String resourceId)
    {
        final String PART_PATTERN = "_part[\\d]+.compsig";
        final Pattern p = Pattern.compile(PART_PATTERN);
        final String partCompSig = fileName.split("_(?!.*_)")[1];
        final Matcher m = p.matcher(partCompSig);
        if (m.find())
        {
            resourceId = normalizedFileName.split("_(?!.*_)")[0];
        }
        return resourceId;
    }
}