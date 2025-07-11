package com.sirish.hpe;

import java.util.HashMap;
import java.util.Map;

import org.apache.commons.lang.StringUtils;

public class CustomJsonNode {
	private void psvm() {
		String location = "Embedded LOM";
		Map<String, Integer> partLocation = new HashMap<String, Integer>();
		if (StringUtils.isNotBlank(location)) {
			final String[] ordinalTokens = location.split(" ");
			final String ordinalVal = ordinalTokens[ordinalTokens.length - 1];
			try {
				partLocation.put("LOCATION_ORDINAL", Integer.parseInt(ordinalVal));
			} catch (final NumberFormatException e) {
				partLocation.put("LOCATION_ORDINAL", 1);
				System.out.print("NumberFormatException: " + ordinalVal);
			}
		}
	}

	public static void main(String[] args) {
		CustomJsonNode customJsonNode = new CustomJsonNode();
		customJsonNode.psvm();
	}

}
