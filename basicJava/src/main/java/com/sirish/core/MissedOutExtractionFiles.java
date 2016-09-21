package com.sirish.core;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;

import org.w3c.dom.Attr;
import org.w3c.dom.Document;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

public class MissedOutExtractionFiles {

	final static String providerPropertyLookUpPath = "/home/sirish/work/fiport/batchJobs/createSchema/src/main/resources/ProvidersFromAnnotations/providerpropertylookup.xml";

	public static void main(final String[] args) {

		final DocumentBuilderFactory documentBuilderFactory = DocumentBuilderFactory.newInstance();
		DocumentBuilder documentBuilder;
		Document document = null;
		try {
			documentBuilder = documentBuilderFactory.newDocumentBuilder();
			document = documentBuilder.parse(providerPropertyLookUpPath);
		} catch (final Exception e1) {
			System.out.println("Lookup file not found" + e1);
		}

		final NodeList providerPropertyList = document.getElementsByTagName("providerProperty");

		for (int i = 0; i < providerPropertyList.getLength(); i++) {

			final Node node = providerPropertyList.item(i);
			final Attr providerPropertyAttribute = (Attr) node.getAttributes().getNamedItem("name");
			final String providerPropertyValue = providerPropertyAttribute.getValue();
			final MappingObjectNew mappingObj = MappingObjectNew.getMappingObject();
			mappingObj.setKey(providerPropertyValue);

			final Node propertyFileNode = node.getChildNodes().item(3);
			final String providerPropertyFileName = propertyFileNode.getNodeValue();

		}
	}
}

class MappingObjectNew {

	String key;
	String value;

	public String getKey() {
		return key;
	}

	public void setKey(final String key) {
		this.key = key;
	}

	public String getValue() {
		return value;
	}

	public void setValue(final String value) {
		this.value = value;
	}

	public static MappingObjectNew getMappingObject() {
		return new MappingObjectNew();
	}
}
