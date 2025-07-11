package com.sirish.hpe;

import java.io.File;
import java.io.IOException;

import org.codehaus.jackson.JsonGenerationException;
import org.codehaus.jackson.JsonNode;
import org.codehaus.jackson.map.JsonMappingException;
import org.codehaus.jackson.map.ObjectMapper;
import org.codehaus.jackson.node.ObjectNode;

public class SDP {
	public static void main(String[] args) throws JsonGenerationException, JsonMappingException, IOException {
		/*
		 * ObjectMapper objectMapper = new ObjectMapper();
		 * 
		 * // Create an ObjectNode to represent a JSON object ObjectNode objectNode =
		 * objectMapper.createObjectNode(); objectNode.put("securityParam",
		 * "Secure Boot"); objectNode.put("securityParamSetting", true);
		 * 
		 * String json = objectMapper.writeValueAsString(objectNode);
		 * System.out.println(json);
		 * 
		 * // Parse JSON string back to JsonNode JsonNode parsedNode =
		 * objectMapper.readTree(json); // Access values from parsedNode String name =
		 * parsedNode.get("securityParam").asText(); System.out.println(name);
		 */
		
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
