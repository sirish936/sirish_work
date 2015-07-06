package com.sirish.core;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class FileRead {

	public static void main(String[] args) {
		try {
		File file = new File(args[0]);
        Scanner scanner = new Scanner(file);
        while (scanner.hasNextLine()) {
          System.out.println(scanner.nextLine());
        }
        scanner.close();
      } catch (FileNotFoundException e) {
        e.printStackTrace();
      }
	}
}
