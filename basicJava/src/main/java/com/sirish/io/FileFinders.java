package com.sirish.io;

import java.io.IOException;
import java.nio.file.*;

import static java.nio.file.FileVisitResult.*;
import static java.nio.file.FileVisitOption.*;

import java.util.Collection;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class FileFinders {
public static void main(String[] args) {
	
}
public static List<Path> searchFilesWithRegex(final String sourceDir, final String fileNameRegex)
        throws IOException
{
    final Path path = Paths.get(sourceDir);
    final Finder finder = new Finder(fileNameRegex);
    Path filepath = Files.walkFileTree(path, finder);
}

protected static Collection<Path> find(String fileName, String searchDirectory) throws IOException {
    try (Stream<Path> files = Files.walk(Paths.get(searchDirectory))) {
        int f;
		return files
                .filter(f -> f.getFileName().toString().equals(fileName))
                .collect(Collectors.toList());

    }
}


protected static Collection<Path> find(String searchDirectory, PathMatcher matcher) throws IOException {
    try (Stream<Path> files = Files.walk(Paths.get(searchDirectory))) {
        return files
                .filter(matcher::matches)
                .collect(Collectors.toList());

    }
}

}
