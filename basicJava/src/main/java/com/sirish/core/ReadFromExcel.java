package com.sirish.core;

import java.io.File;
import java.io.FileInputStream;
import java.util.Iterator;

import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

public class ReadFromExcel {

	public static void main(final String[] args) {
		try {
			final FileInputStream file = new FileInputStream(new File("sirish.xlsx"));

			// Create Workbook instance holding reference to .xlsx file
			final XSSFWorkbook workbook = new XSSFWorkbook(file);

			// Get first/desired sheet from the workbook
			final XSSFSheet sheet = workbook.getSheetAt(0);

			// Iterate through each rows one by one
			final Iterator<Row> rowIterator = sheet.iterator();
			while (rowIterator.hasNext()) {
				final Row row = rowIterator.next();
				// For each row, iterate through all the columns
				final Iterator<Cell> cellIterator = row.cellIterator();

				while (cellIterator.hasNext()) {
					final Cell cell = cellIterator.next();
					// Check the cell type and format accordingly
					switch (cell.getCellType()) {
					case Cell.CELL_TYPE_NUMERIC:
						System.out.print(cell.getNumericCellValue() + " ");
						break;
					case Cell.CELL_TYPE_STRING:
						System.out.print(cell.getStringCellValue() + " ");
						break;
					}
				}
				System.out.println("");
			}
			file.close();
		} catch (final Exception e) {
			e.printStackTrace();
		}
	}
}
