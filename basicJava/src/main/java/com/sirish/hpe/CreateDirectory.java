package com.sirish.hpe;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Scanner;

public class CreateDirectory {
public static void main(String[] args) {
	try {
		Scanner sc = new Scanner(System.in);
		String dirPath = sc.next();
		Path path = Paths.get(dirPath);
		Files.createDirectories(path);
		System.out.println("Directory created successfully");
	} catch (IOException e) {
		System.out.println(e.getMessage());
	}
}
}
