package com.sirish.hpe;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

import org.codehaus.jackson.JsonProcessingException;
import org.codehaus.jackson.annotate.JsonProperty;
import org.codehaus.jackson.annotate.JsonPropertyOrder;
import org.codehaus.jackson.map.ObjectMapper;

public class GetJsonFromMap {

	public static void main(String[] args) {
		final Map<Object, Object> componentsPresent = new HashMap<Object, Object>();
		final Map<Object, Object> componentsPresent1 = new HashMap<Object, Object>();
		final Map<Object, Object> componentsPresent2 = new HashMap<Object, Object>();
		final Map<Object, Object> componentsPresent3 = new HashMap<Object, Object>();
		final Map<Object, Object> componentsPresent4 = new HashMap<Object, Object>();
		
		componentsPresent.put("EM", true);
		componentsPresent.put("iLo4", true);
		componentsPresent.put("iLo5", true);
		componentsPresent.put("VC", true);
		componentsPresent.put("OA", true);
		
		componentsPresent1.put("EM", "EM");
		componentsPresent1.put("iLo4", "iLo4");
		componentsPresent1.put("iLo5", "iLo5");
		componentsPresent1.put("VC", "VC");
		componentsPresent1.put("OA", "OA");
		
		componentsPresent2.put(1, "EM");
		componentsPresent2.put(2, "iLo4");
		componentsPresent2.put(3, "iLo5");
		componentsPresent2.put(4, "VC");
		componentsPresent2.put(5, "OA");
		
		
		componentsPresent3.put(1, 1);
		componentsPresent3.put(2, 2);
		componentsPresent3.put(3, 3);
		componentsPresent3.put(4, 4);
		componentsPresent3.put(5, 5);
		componentsPresent3.put("", getJsonFromMap(componentsPresent2) != null ? "" : "");
		
		
		
		
		componentsPresent4.put(true, true);
		componentsPresent4.put(false, false);
		
		final String jsonString = getJsonFromMap(componentsPresent4);
		System.out.println(jsonString);
		ComponentsPresent cmp = new ComponentsPresent();
		cmp.setCompPrest(jsonString);
		System.out.println(cmp.toString());
	}

	private static String getJsonFromMap(final Map<Object, Object> componentsPresent) {
		String json = "";
		if (componentsPresent != null) {
			try {
				json = new ObjectMapper().writeValueAsString(componentsPresent);
			} catch (final JsonProcessingException jpe) {
				System.out.println("unable to parse the Map to JsonString {}"
						+ jpe.getMessage());
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		return json;
	}

	static class ComponentsPresent {

		@JsonProperty
		String compPrest;

		public String getCompPrest() {
			return compPrest;
		}

		public void setCompPrest(String compPrest) {
			this.compPrest = compPrest;
		}

	}

	
	@JsonPropertyOrder({
	    "xInfo"
	})
	static class XInfoClass {

		String xInfo;

		public String getxInfo() {
			return xInfo;
		}

		public void setxInfo(String xInfo) {
			this.xInfo = xInfo;
		}

	}
}
