package com.sirish.jaxb;

import java.io.File;

import javax.xml.bind.JAXBContext;
import javax.xml.bind.Unmarshaller;

public class UnmarshallingExample {

	/**
	 * @param args
	 */
	public static void main(final String[] args) {
		// TODO Auto-generated method stub
		try {
			final File file = new File("C:/ravi/file.xml");
			// create root object
			final JAXBContext jaxbcontext = JAXBContext.newInstance(Customer.class);

			final Unmarshaller jaxbunmarshaller = jaxbcontext.createUnmarshaller();

			final Customer customer = (Customer) jaxbunmarshaller.unmarshal(file);

			System.out.println(customer);
		} catch (final Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
	}

}
