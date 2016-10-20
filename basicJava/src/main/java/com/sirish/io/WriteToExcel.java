package com.sirish.io;

import java.io.File;
import java.io.FileOutputStream;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;

import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

public class WriteToExcel {

	public static void main(final String[] args) {

		// Blank workbook
		final XSSFWorkbook workbook = new XSSFWorkbook();

		// Create a blank sheet
		final XSSFSheet sheet = workbook.createSheet("Employee Data");

		// This data needs to be written (Object[])
		final Map<String, Object[]> data = new TreeMap<String, Object[]>();
		data.put("1", new Object[] { "ID", "NAME", "LASTNAME" });
		data.put("2", new Object[] { 1, "Amit", "Shukla" });
		data.put("3", new Object[] { 2, "Lokesh", "Gupta" });
		data.put("4", new Object[] { 3, "John", "Adwards" });
		data.put("5", new Object[] { 4, "Brian", "Schultz" });

		// Iterate over data and write to sheet
		final Set<String> keyset = data.keySet();
		int rownum = 0;
		for (final String key : keyset) {
			final Row row = sheet.createRow(rownum++);
			final Object[] objArr = data.get(key);
			int cellnum = 0;
			for (final Object obj : objArr) {
				final Cell cell = row.createCell(cellnum++);
				if (obj instanceof String) {
					cell.setCellValue((String) obj);
				} else if (obj instanceof Integer) {
					cell.setCellValue((Integer) obj);
				}
			}
		}
		try {
			// Write the workbook in file system
			final FileOutputStream out = new FileOutputStream(new File("sirish.xlsx"));
			workbook.write(out);
			out.close();
			System.out.println("created excel file and copied data");
		} catch (final Exception e) {
			e.printStackTrace();
		}
	}
}
