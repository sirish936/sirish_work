package com.sirish.collections;

//If this.cuntryId < country.countryId:then compare method will return -1
//If this.countryId > country.countryId:then compare method will return 1
//If this.countryId==country.countryId:then compare method will return 0
public class Country implements Comparable<Country> {
	int countryId;
	String countryName;

	public Country(final int countryId, final String countryName) {
		this.countryId = countryId;
		this.countryName = countryName;
	}

	public int getCountryId() {
		return countryId;
	}

	public void setCountryId(final int countryId) {
		this.countryId = countryId;
	}

	public String getCountryName() {
		return countryName;
	}

	public void setCountryName(final String countryName) {
		this.countryName = countryName;
	}

	@Override
	public int compareTo(final Country arg0) {
		// Country country=(Country) arg0;
		// return (this.countryId < country.countryId ) ? -1: (this.countryId > country.countryId ) ? 1:0 ;
		if (this.getCountryId() < arg0.getCountryId()) {
			return -1;
		} else if (this.getCountryId() > arg0.getCountryId()) {
			return 1;
		} else {
			return 0;
		}

	}
}