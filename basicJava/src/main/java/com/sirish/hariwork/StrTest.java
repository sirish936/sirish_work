package com.sirish.hariwork;

import java.util.UUID;

public class StrTest {
	public static void main(String[] args) {
		String str = "";
		// if(!Strings.isNullorEmpty){
		// str="sirish";
		// }else{
		// str="";
		// }
		// System.out.println("value ::"+str);

		String finalValue = getValue().toString();
		if (finalValue != null) {
			System.out.println(finalValue);
		}

		String deviceClass = "757378B9-0016-4DEB-97DB-02BF1CD0B86A";
		String targetGuid = "a6b1a447-382a-5a4f-1077-2031103C17E8";

		System.out.println(deviceClass.toLowerCase());
		System.out.println(targetGuid.toLowerCase());
		if (str.contains("_")) {
			System.out.println("NOT NULL ::" + str);
		}

		UUID uuid = UUID.randomUUID();
		String randomUUIDString = uuid.toString();

		System.out.println("Random UUID String = " + randomUUIDString);

		if (!(setBaselineUri("abcd").isEmpty())) {
			System.out.println("XXX");
		}
		if (!(setBaselineUri("abcd")).isEmpty()) {
			System.out.println("YYY");
		}
	}

	private static String setBaselineUri(final String resourceId) {
		String baselineUri = "";
		if (resourceId != null) {
			baselineUri = resourceId + "sirish";
		}
		return baselineUri;
	}

	private static Integer getValue() {
		// TODO Auto-generated method stub
		return 10;
	}

}
