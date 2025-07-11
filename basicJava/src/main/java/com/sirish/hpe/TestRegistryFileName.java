package com.sirish.hpe;

public class TestRegistryFileName {
	public static void main(String[] args) {
		String registryNameWithVersionActual = "biosattributeregistrya55.v1_1_20";
		String registryNameWithVersionNew = "biosattributeregistrya55.v1.1.20";
		String registryVersionActual = null;
		String registryVersionNew = null;
		if (registryNameWithVersionActual != null)
        {
            registryVersionActual = registryNameWithVersionActual.substring(registryNameWithVersionActual.indexOf(".") + 1);
            registryVersionNew = registryNameWithVersionNew.substring(registryNameWithVersionNew.indexOf(".") + 1);
        }
		System.out.println(registryVersionActual);
		System.out.println(registryVersionNew);
		
		testVersionCompare();
	}

	private static void testVersionCompare() {
		final String registryName1 = "biosattributeregistrya55.v1.1.30.json";
        final String registryName2 = "biosattributeregistrya55.v1.1.20.json";
        if (!registryName1.contains(".v") || !registryName2.contains(".v"))
        {
        	System.out.println("registry names {} or {} are in incorrect format");
        	System.out.println(0);
        }
        final String version1 = registryName1.substring(registryName1.indexOf(".v") + 2, registryName1.length())
                .replaceAll("_", ".").replaceAll(".json", "");
        final String version2 = registryName2.substring(registryName2.indexOf(".v") + 2, registryName2.length())
                .replaceAll("_", ".").replaceAll(".json", "");
        if (version1.isEmpty() || version2.isEmpty())
        {
        	System.out.println("registry names {} or {} are in incorrect format");
            System.out.println(0);
        }
        if (!version1.matches("[0-9,.]+") || !version2.matches("[0-9,.]+"))
        {
        	System.out.println("registry names {} or {} are in incorrect format");
            System.out.println(0);
        }
        System.out.println(version1);
        System.out.println(version2);
	}
}
