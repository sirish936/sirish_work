package com.sirish.core;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Date;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.concurrent.TimeUnit;

public class DateDiff {

	@SuppressWarnings("deprecation")
	public static void main(final String[] args) {
		final Set<String> setEx = new HashSet<String>();
		setEx.add("123");
		setEx.add(null);
		setEx.add(null);
		setEx.add(null);
		System.out.println(setEx.size());

		final Date oldDate = new Date();
		oldDate.setMonth(new Date().getMonth() - 1);

		final long timeDiff = getDateDiff(new Date(), oldDate);
		System.out.println("Time Difference is " + timeDiff);
		
		final int value = getDateDiffs(oldDate,new Date());
		System.out.println("value "+value);
		
		List list = new ArrayList<>();
		list.add(oldDate);
		list.add(new Date());
		System.out.println(list);
		Collections.sort(list, new Comparator<Date>()
                {
                    public int compare(final Date object1, final Date object2)
                    {
                        return getDateDiffs(object1, object2);
                    }
                });
		System.out.println(list);
	}


	static long abc = 1422000000000l;

	static long getDateDiff(final Date date1, final Date date2) {
		final long diffInMillies = date1.getTime() - abc;
		return Math.abs(TimeUnit.DAYS.convert(diffInMillies, TimeUnit.MILLISECONDS));
	}
	
	static int getDateDiffs(final Date date1, final Date date2)
	    {
	       
	        if (date2 != null && date1 != null)
	        {
	            return date2.compareTo(date1);
	        }
	        else if (date2 != null)
	        {
	            return 1;
	        }
	        else
	        {
	            return 0;
	        }
	    }
}
