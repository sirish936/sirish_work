package com.sirish.collections;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class ComparatorMain {

	/**
	 * @param args
	 */
	public static void main(final String[] args) {
		// TODO Auto-generated method stub

		final Country indiaCountry = new Country(1, "India");
		final Country chinaCountry = new Country(4, "China");
		final Country nepalCountry = new Country(3, "Nepal");
		final Country bhutanCountry = new Country(2, "Bhutan");

		final List<Country> listOfCountries = new ArrayList<Country>();
		listOfCountries.add(indiaCountry);
		listOfCountries.add(chinaCountry);
		listOfCountries.add(nepalCountry);
		listOfCountries.add(bhutanCountry);

		System.out.println("Before Sort by id : ");
		for (int i = 0; i < listOfCountries.size(); i++) {
			final Country country = listOfCountries.get(i);
			System.out.println("Country Id: " + country.getCountryId() + "||" + "Country name: " + country.getCountryName());
		}
		Collections.sort(listOfCountries, new CountrySortByIdComparator());

		System.out.println("After Sort by id: ");
		for (int i = 0; i < listOfCountries.size(); i++) {
			final Country country = listOfCountries.get(i);
			System.out.println("Country Id: " + country.getCountryId() + "|| " + "Country name: " + country.getCountryName());
		}

		// Sort by countryName
		Collections.sort(listOfCountries, new Comparator<Country>() {
			@Override
			public int compare(final Country o1, final Country o2) {
				return o1.getCountryName().compareTo(o2.getCountryName());
			}
		});

		System.out.println("After Sort by name: ");
		for (int i = 0; i < listOfCountries.size(); i++) {
			final Country country = listOfCountries.get(i);
			System.out.println("Country Id: " + country.getCountryId() + "|| " + "Country name: " + country.getCountryName());
		}
	}

}
