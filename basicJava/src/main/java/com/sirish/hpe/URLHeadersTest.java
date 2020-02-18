package com.sirish.hpe;

import java.io.IOException;
import java.net.URL;
import java.net.URLConnection;

public class URLHeadersTest {
	public static void main(String[] args) throws IOException {
        URL url = new URL("http://localhost:8080/foobar");
        URLConnection hc = url.openConnection();
        hc.setRequestProperty("User-Agent", "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; en-US; rv:1.9.2.2) Gecko/20100316 Firefox/3.6.2");

        System.out.println(hc.getContentType());
    }
}
