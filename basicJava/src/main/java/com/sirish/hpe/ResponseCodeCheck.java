package com.sirish.hpe;

import java.net.HttpURLConnection;
import java.net.URL;

class ResponseCodeCheck {

	public static void main(String args[]) throws Exception {

		URL url = new URL("http://172.20.3.65.com");
		HttpURLConnection connection = (HttpURLConnection) url.openConnection();
		connection.setRequestMethod("GET");
		connection.connect();

		int code = connection.getResponseCode();
		System.out.println("Response code of the object is " + code);
		if (code == 200) {
			System.out.println("OK");
		}
	}
}