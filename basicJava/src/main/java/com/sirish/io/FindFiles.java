package com.sirish.io;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.stream.Stream;

public class FindFiles {
	public static void main(String[] args) throws IOException {
		String rootDirPath = null;
		final File files = new File(rootDirPath);
		final File[] payloadJsonFiles = files
				.listFiles((file1, filename) -> filename.startsWith("payload") && filename.endsWith(".json"));
		final String payloadJsonPath = payloadJsonFiles[0].getAbsolutePath();
		System.out.println("PayloadJsonPath is :" + payloadJsonPath);
		
//		Files.walk(root.toPath())
//	      .filter(path -> !Files.isDirectory(path))
//	      .forEach(path -> System.out.println(path));
		
		Path rootDir = Paths.get(rootDirPath);
		Stream<Path> stream =
                Files.find(rootDir, 100,
                        (path, basicFileAttributes) -> {
                            File file = path.toFile();
                            return !file.isDirectory() &&
                                    file.getName().contains(".json");
                        });
        
		System.out.println(stream.findFirst());
	}
	
//	public List<Path> searchFilesWithRegex(final String sourceDir, final String fileNameRegex)
//            throws IOException
//    {
//        final Path path = Paths.get(sourceDir);
//        final FileFinder finder = new FileFinder(fileNameRegex);
//        Files.walkFileTree(path, finder);
//        return finder.done();
//    }
}
