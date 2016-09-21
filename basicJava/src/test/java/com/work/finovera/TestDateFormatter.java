package com.work.finovera;


import org.junit.Assert;
import org.junit.Test;


public class TestDateFormatter {

	@Test
	public void testDateFormats(){
		DateFormat format = null;
		DateFormatter df = new DateFormatter();
		
		String testDate1 = "2016-01-26";
		format = df.getFormattedDate(testDate1);
		Assert.assertEquals(DateFormat.YYYY_MM_DD_WITH_HYPHEN,format);
		
		String testDate2 = "2016/01/26";
		format = df.getFormattedDate(testDate2);
		Assert.assertEquals(DateFormat.YYYY_MM_DD_WITH_SLASH,format);

		String testDate3 = "01-26-2016";
		format = df.getFormattedDate(testDate3);
		Assert.assertEquals(DateFormat.MM_DD_YYYY_WITH_HYPHEN,format);

		String testDate4 = "01/26/2016";
		format = df.getFormattedDate(testDate4);
		Assert.assertEquals(DateFormat.MM_DD_YYYY_WITH_SLASH,format);

		String testDate5 = "01-26-16";
		format = df.getFormattedDate(testDate5);
		Assert.assertEquals(DateFormat.MM_DD_YY_WITH_HYPHEN,format);

		String testDate6 = "01/26/16";
		format = df.getFormattedDate(testDate6);
		Assert.assertEquals(DateFormat.MM_DD_YY_WITH_SLASH,format);

		String testDate7 = "Jan 26, 2016";
		format = df.getFormattedDate(testDate7);
		Assert.assertEquals(DateFormat.MMM_DD_YYYY_WITH_SPACE,format);

		String testDate8 = "Jan 26,2016";
		format = df.getFormattedDate(testDate8);
		Assert.assertEquals(DateFormat.MMM_DD_YYYY_WITHOUT_SPACE,format);
		
		String testDate9 = "26 Jan, 2016";
		format = df.getFormattedDate(testDate9);
		Assert.assertEquals(DateFormat.DD_MMM_YYYY_WITH_SPACE,format);
		
		String testDate10 = "26 Jan,2016";
		format = df.getFormattedDate(testDate10);
		Assert.assertEquals(DateFormat.DD_MMM_YYYY_WITHOUT_SPACE,format);
		
		String testDate11 = "Jan 26, 16";
		format = df.getFormattedDate(testDate11);
		Assert.assertEquals(DateFormat.MMM_DD_YY_WITH_SPACE,format);
		
		String testDate12 = "Jan 26,16";
		format = df.getFormattedDate(testDate12);
		Assert.assertEquals(DateFormat.MMM_DD_YY_WITHOUT_SPACE,format);
		
		String testDate13 = "26 Jan, 16";
		format = df.getFormattedDate(testDate13);
		Assert.assertEquals(DateFormat.DD_MMM_YY_WITH_SPACE,format);
		
		String testDate14 = "26 Jan,16";
		format = df.getFormattedDate(testDate14);
		Assert.assertEquals(DateFormat.DD_MMM_YY_WITHOUT_SPACE,format);
		
		String testDate15 = "26 Jan";
		format = df.getFormattedDate(testDate15);
		Assert.assertEquals(DateFormat.DD_MMM,format);

		String testDate16 = "Jan 26";
		format = df.getFormattedDate(testDate16);
		Assert.assertEquals(DateFormat.MMM_DD,format);
		
		String testDate17 = "01-26";
		format = df.getFormattedDate(testDate17);
		Assert.assertEquals(DateFormat.MM_DD_WITH_HYHEN,format);
		
		String testDate18 = "01/26";
		format = df.getFormattedDate(testDate18);
		Assert.assertEquals(DateFormat.MM_DD_WITH_SLASH,format);
		
		String testDate19 = "January 26";
		format = df.getFormattedDate(testDate19);
		Assert.assertEquals(DateFormat.MMM_DD,format);
	
		String testDate20 = "26th Jan";
		format = df.getFormattedDate(testDate20);
		Assert.assertEquals(DateFormat.DD_MMM,format);
		
		String testDate21 = "26 August";
		format = df.getFormattedDate(testDate21);
		Assert.assertEquals(DateFormat.DD_MMM,format);
		
		String testDate22 = "26th August, 2015";
		format = df.getFormattedDate(testDate22);
		Assert.assertEquals(DateFormat.DD_MMM_YYYY_WITH_SPACE,format);

		String testDate23 = "";
		format = df.getFormattedDate(testDate23);
		Assert.assertNull(format);

	}
}
