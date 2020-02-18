package com.sirish.hpe;

import java.io.IOException;
import java.net.URL;
import java.net.URLConnection;
import java.util.List;
import java.util.Map;

public class URLHeaderTest {
	public static void main(String[] args) throws IOException {
        URL url = new URL("https://www.google.co.in/");
        URLConnection conn = url.openConnection();
        conn.setRequestProperty("User-Agent", "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; en-US; rv:1.9.2.2) Gecko/20100316 Firefox/3.6.2");

        //System.out.println(hc.getContentType());
        final Map<String, List<String>> map = conn.getHeaderFields();
        System.out.println(map.size());
        for (final String key : map.keySet())
        {
            final List<String> value = map.get(key);
            System.out.println("Key ::::: " + key + ", Value = " + value.size());
            for (final String val : value)
            {
            	System.out.println("val for key  ::::: " + key + ", Values = " + val);

            }
        }
        
    }
}
