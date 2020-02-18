package com.sirish.hpe;

import java.text.DecimalFormat;

public class DecimalFOrmat {
	public static void main(String[] args) {
		DecimalFormat twodigits = new DecimalFormat("00");
	    for(int i=0;i<100;i++)
	    {
	    	System.out.println(twodigits.format(i));
	    	
	    }
	    
	}
}
