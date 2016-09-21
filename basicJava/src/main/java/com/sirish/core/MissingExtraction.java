package com.sirish.core;

import java.io.IOException;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;

import org.w3c.dom.Attr;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

public class MissingExtraction {

	final static String EXTRACTION_FILE_PATH = "D:/sirish/work_files/extractionInput.xml";

	public static void main(String[] args) throws ParserConfigurationException, SAXException, IOException {

		try {

			DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
			DocumentBuilder docBuilder = dbf.newDocumentBuilder();
			Document document = docBuilder.parse(EXTRACTION_FILE_PATH);
			NodeList providerPropertyList = document.getElementsByTagName("providerProperty");

			for (int i = 0; i < providerPropertyList.getLength(); i++) {

				Node providerPropertyNode = providerPropertyList.item(i);
				Attr providerPropertyAttr = (Attr) providerPropertyNode.getAttributes().getNamedItem("name");
				final String providerPropertyName = providerPropertyAttr.getValue();
				MappingObject mappingObj = MappingObject.getMappingObject();
				mappingObj.setKey(providerPropertyName);

				Element section = (Element) providerPropertyList.item(i);

				Node title = section.getFirstChild();
				System.out.println("aaaa" + title.getNodeValue());
				while (title != null && title.getNodeType() != Node.ELEMENT_NODE) {
					title = title.getNextSibling();
				}
			}
		} catch (ParserConfigurationException e) {
			System.out.println("extractionInput document not found " + e);
		}
	}
}

class MappingObject {
	String key;
	String value;

	public String getKey() {
		return key;
	}

	public void setKey(String key) {
		this.key = key;
	}

	public String getValue() {
		return value;
	}

	public void setValue(String value) {
		this.value = value;
	}

	public static MappingObject getMappingObject() {
		return new MappingObject();
	}
}