package com.sirish.hpe;

import java.io.File;
import java.io.IOException;

import org.codehaus.jackson.JsonNode;
import org.codehaus.jackson.map.ObjectMapper;

public class JsonBuilder {
	public static void main(String[] args) {
		ObjectMapper mapper = new ObjectMapper();
        try {
            // Read JSON into a JsonNode
            JsonNode root = mapper.readTree(new File("Drives.json"));
            
            // Access array
            JsonNode skillsNode = root.get("skills");
            System.out.print("Skills: ");
            for (JsonNode skill : skillsNode) {
                System.out.print(skill.asText() + " ");
            }

            // Output the data
        } catch (IOException e) {
            e.printStackTrace();
        }
	}
}
