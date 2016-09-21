package com.sirish.core;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.JsonParser;

public class JsonParser_Vinay {

	final static String[] PROVIDER_NAME = new String[] { "paypal" };

	final static String JSON_FILE_PATH = "";
	final static String OUTPUT_FILE_NAME = "";

	public static void main(final String[] args) throws JsonParseException, IOException {

		final JsonParser parser = new JsonParser();
		JsonArray array = null;

		try {
			array = (JsonArray) parser.parse(new FileReader(JSON_FILE_PATH));
		} catch (final Exception ex) {
			System.out.println("FILE NOT FOUND...!!!");
			System.exit(0);
		}

		getProviderIds(array);
	}

	static private void getProviderIds(final JsonArray array) throws IOException {

		final FileWriter fr = new FileWriter(OUTPUT_FILE_NAME);

		int count = 0;

		for (final String providerName : PROVIDER_NAME) {

			count = 0;

			System.out.println("Provider name: " + providerName);
			System.out.println("=============================================================================================================================");

			for (final JsonElement ele : array) {

				final JsonObject jsonObject = (JsonObject) ele;

				if (!(jsonObject.get("scraping") == null) && !(jsonObject.get("providerName") == null)) {

					if ((jsonObject.get("scraping").toString().replaceAll("[^A-Za-z]", "").equalsIgnoreCase("FAIL")
							|| jsonObject.get("download").toString().replaceAll("[^A-Za-z]", "").equalsIgnoreCase("FAIL") || jsonObject.get("logout")
							.toString().replaceAll("[^A-Za-z]", "").equalsIgnoreCase("FAIL"))
							&& jsonObject.get("providerName").toString().replaceAll("[^A-Za-z-@_.]", "").equalsIgnoreCase(providerName)
							&& jsonObject.get("login").toString().replaceAll("[^A-Za-z]", "").equalsIgnoreCase("SUCCESS")
							&& jsonObject.get("uir").toString().replaceAll("[^A-Za-z_]", "").equalsIgnoreCase("NOT_REQUIRED")) {

						fr.write(jsonObject.get("providerId").toString().replaceAll("[^A-Za-z0-9]", ""));
						fr.write("\n");

						System.out.println("Provider Id:" + jsonObject.get("providerId").toString().replaceAll("[^A-Za-z0-9]", "") + ", Email Id:"
								+ jsonObject.get("email").toString().replaceAll("[^A-Za-z0-9.@_]", ""));

						count++;
					}
				}
			}

			System.out.println("No of provider account: " + count);
			System.out.println("=============================================================================================================================");
		}
		fr.flush();
		fr.close();
	}
}