package com.sirish.core;

import java.io.File;

public class ExtractorUtility {

	public static void main(final String[] args) {

		final String[] folder = new String[] { "bank", "brokerage", "creditcard", "home", "insurance", "internet", "investment", "loan", "mortgage", "phone",
				"retirement", "utilities" };

		for (final String categoryFolder : folder) {

			getCategoriedFiles(categoryFolder);

		}
	}

	private static void getCategoriedFiles(final String categoryFolder) {

		final String fileStr = "/home/sirish/work/fiport/batchJobs/createSchema/src/main/resources/ProvidersFromAnnotations/" + categoryFolder;

		final File file = new File(fileStr);

		final File[] files = file.listFiles();

		for (final File subfiles : files) {

			final String name = subfiles.getName();

			getAllFiles(categoryFolder, name);

		}
	}

	private static void getAllFiles(final String str1, final String str2) {

		final String fileStr = "/home/sirish/work/fiport/batchJobs/createSchema/src/main/resources/ProvidersFromAnnotations/" + str1 + "/" + str2;

		final File file = new File(fileStr);

		final File[] files = file.listFiles();

		for (final File subfiles : files) {

			final String name = subfiles.getName();

			System.out.println(name);

		}

		// System.out.println("===========================================");
	}
}