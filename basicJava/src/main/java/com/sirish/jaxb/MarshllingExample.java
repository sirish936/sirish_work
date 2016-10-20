package com.sirish.jaxb;

//import java.io.File;

import java.io.File;

import javax.xml.bind.JAXBContext;
import javax.xml.bind.Marshaller;

public class MarshllingExample {

	/**
	 * @param args
	 */
	public static void main(final String[] args) {
		// TODO Auto-generated method stub
		final Customer customer = new Customer();
		customer.setId(101);
		customer.setName("sirish");
		customer.setAge(22);

		try {
			final File file = new File("C:\\ravi\\file.xml");
			// create root object
			final JAXBContext jaxbcontext = JAXBContext.newInstance(Customer.class);

			final Marshaller jaxbmarshaller = jaxbcontext.createMarshaller();

			jaxbmarshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true);

			jaxbmarshaller.marshal(customer, file);

			jaxbmarshaller.marshal(customer, System.out);

		} catch (final Exception e) {
			e.printStackTrace();
		}
	}
}
