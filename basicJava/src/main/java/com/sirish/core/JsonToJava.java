package com.sirish.core;

import java.io.File;
import java.io.IOException;

import org.codehaus.jackson.JsonParseException;
import org.codehaus.jackson.map.JsonMappingException;
import org.codehaus.jackson.map.ObjectMapper;

public class JsonToJava {
	
	 public static void main(String[] args) throws JsonParseException, JsonMappingException, IOException {

		ObjectMapper objMapper = new ObjectMapper(); 
		 
		//JsonToJava
		User user = objMapper.readValue(new File("D:/sirish/work_files/samplejson.json"), User.class);
		
		System.out.println("user name is : "+ user.getName());
		System.out.println("user city is : "+ user.getCity());
		System.out.println("user job is : "+ user.getJob());

		for (String str : user.getHobbies()) {
			System.out.println("user hobbies are : "+ str);
		}

		User newUser = new User();
		newUser.setName("loknath");
		newUser.setCity("Odisha");
		newUser.setJob("swe");
		newUser.setHobbies(new String[]{"browsing","travelling"});
		
		//JavaToJson
		objMapper.writeValue(new File("D:/sirish/work_files/sampleoutputjson.json"), newUser);


	 }
}
