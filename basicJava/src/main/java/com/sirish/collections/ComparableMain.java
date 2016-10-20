package com.sirish.collections;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class ComparableMain {

	/**
	 * @author sirish
	 */
	public static void main(final String[] args) {
		final Country indiaCountry = new Country(1, "India");
		final Country chinaCountry = new Country(4, "China");
		final Country nepalCountry = new Country(3, "Nepal");
		final Country bhutanCountry = new Country(2, "Bhutan");

		final List<Country> listOfCountries = new ArrayList<Country>();
		listOfCountries.add(indiaCountry);
		listOfCountries.add(chinaCountry);
		listOfCountries.add(nepalCountry);
		listOfCountries.add(bhutanCountry);

		System.out.println("Before Sort  : ");
		for (int i = 0; i < listOfCountries.size(); i++) {
			final Country country = listOfCountries.get(i);
			System.out.println("Country Id: " + country.getCountryId() + "||" + "Country name: " + country.getCountryName());
		}
		Collections.sort(listOfCountries);

		System.out.println("After Sort  : ");
		for (int i = 0; i < listOfCountries.size(); i++) {
			final Country country = listOfCountries.get(i);
			System.out.println("Country Id: " + country.getCountryId() + "|| " + "Country name: " + country.getCountryName());
		}
	}

}