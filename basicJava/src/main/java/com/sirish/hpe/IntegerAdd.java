package com.sirish.hpe;

import java.io.File;

public class IntegerAdd {
	public static void main(String[] args) throws Exception {
		String input = "00";
		int output = Integer.parseInt(input);
		output = output+1;
		System.out.println("output is : " + output);
		String fileNamePortion;
		String filePartPortion;
		Integer partPosition;
		String finalPartPosition;
		String finalSplitFileName;
		String splittedFiles[] = { "cp036946_00", "cp036946_01", "cp036946_02","cp036946_03","cp036946_04","cp036946_05","cp036946_06","cp036946_07","cp036946_08","cp036946_09","cp036946_10","cp036946_11" };

		for (int index = 0; index < splittedFiles.length; index++) {
			final String splitPortionFile = splittedFiles[index];
			if (splitPortionFile != null && splitPortionFile.contains("_")) {
				try {
					fileNamePortion = splitPortionFile.split("_")[0];
					filePartPortion = splitPortionFile.split("_")[1];
					partPosition = Integer.valueOf(filePartPortion);
					partPosition = partPosition + 1;
					finalPartPosition = (partPosition < 10 ? "0" : "")
							+ partPosition;
					finalSplitFileName = fileNamePortion + "_"
							+ finalPartPosition;
					System.out.println("finalSplitFileName::"
							+ finalSplitFileName);
				} catch (final NumberFormatException nfe) {
					throw new Exception();
				}

				final String splitDirPath = "/ci/data/sum_repository/abs/1234"
						+ "/" + finalSplitFileName;
				System.out.println("creating sub directory {} for the file "
						+ splitDirPath);
			}
		}
	}
}