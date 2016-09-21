package com.sirish.core;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Properties;

import org.junit.Test;

import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;

public class GetProviderIDs {

	private String scrUIR;
	private String scrLOGIN;
	private String jsonFilePath;
	private String outputFilePath;
	private ArrayList<String> providersNameList = null;

	@Test
	public void testProviderIdDump() throws IOException {

		long startTime = System.nanoTime();

		init();
		getProviderIds();

		startTime = (System.nanoTime() - startTime) / 1000000;
		System.out.println("Took " + startTime + " ms to complete.");
	}

	private void getProviderIds() throws IOException {

		final JsonArray array = getJsonArray();
		final FileWriter fr = new FileWriter(outputFilePath);

		int count = 0;
		boolean flag = false;

		for (String providerName : providersNameList) {

			count = 0;

			System.out.println("Provider name: " + providerName);
			System.out.println("=============================================================================================================================");

			providerName = providerName.trim();

			for (final JsonElement ele : array) {

				flag = false;
				final JsonObject jsonObject = (JsonObject) ele;

				if (!(jsonObject.get("scraping") == null) && !(jsonObject.get("providerName") == null)) {

					final String login = jsonObject.get("login").toString().replaceAll("[^A-Za-z]", "");
					final String scraping = jsonObject.get("scraping").toString().replaceAll("[^A-Za-z]", "");
					final String download = jsonObject.get("download").toString().replaceAll("[^A-Za-z]", "");
					final String logout = jsonObject.get("logout").toString().replaceAll("[^A-Za-z]", "");

					final String uir = jsonObject.get("uir").toString().replaceAll("[^A-Za-z_]", "");
					final String providerNm = jsonObject.get("providerName").toString().replaceAll("[^A-Za-z-@_.]", "");
					final String providerId = jsonObject.get("providerId").toString().replaceAll("[^A-Za-z0-9]", "");
					final String emailId = jsonObject.get("email").toString().replaceAll("[^A-Za-z0-9.@_]", "");

					if (providerNm.equalsIgnoreCase(providerName) && login.equalsIgnoreCase(scrLOGIN) && uir.equalsIgnoreCase(scrUIR)) {

						flag = true;

					} else if ((scraping.equalsIgnoreCase("FAIL") || download.equalsIgnoreCase("FAIL") || logout.equalsIgnoreCase("FAIL"))
							&& providerNm.equalsIgnoreCase(providerName) && login.equalsIgnoreCase(scrLOGIN) && uir.equalsIgnoreCase(scrUIR)) {

						flag = true;
					}

					if (flag == true) {

						fr.write(providerId);
						fr.write("\n");

						System.out.println("Provider Id:" + providerId + ", Email Id:" + emailId);

						count++;
					}
				}
			}

			System.out.println("Count: " + count);
			System.out.println("=============================================================================================================================");
		}
		fr.flush();
		fr.close();
	}

	private JsonArray getJsonArray() {

		final JsonParser parser = new JsonParser();
		JsonArray array = null;

		try {
			array = (JsonArray) parser.parse(new FileReader(jsonFilePath));
		} catch (final Exception ex) {
			System.out.println("SOMETHING WENT WRONG WITH JSON FILE...!!!");
			System.exit(0);
		}

		return array;
	}

	private void init() {

		final Properties properties = new Properties();

		try {

			properties.load(GetProviderIDs.class.getClassLoader().getResourceAsStream("init.properties"));

			jsonFilePath = properties.getProperty("inputFilePath");
			outputFilePath = properties.getProperty("outputFilePath");
			scrUIR = properties.getProperty("uir");
			scrLOGIN = properties.getProperty("login");

			final String pr[] = properties.getProperty("providers").split(",");

			providersNameList = new ArrayList<String>();

			for (final String prName : pr) {
				providersNameList.add(prName);
			}

		} catch (final Exception e) {
			System.out.println("INITIALIZATION FAILED...!!!");
			System.exit(0);
		}
	}
}
