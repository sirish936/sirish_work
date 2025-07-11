package org.work;

import java.io.File;
import java.io.IOException;

import org.codehaus.jackson.JsonNode;
import org.codehaus.jackson.map.ObjectMapper;

public class AlertTypeID {
	public static void main(String[] args) {
//		String alertTypeID = "Redfish.iLOSecurityEvents.6.1.OverallSecAtIgnore";
//		final String[] alertTypeIdParts = alertTypeID.split(".");
//		final String comparablePartAlertId = alertTypeIdParts[alertTypeIdParts.length - 1];
//		System.out.println(comparablePartAlertId);
		
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
