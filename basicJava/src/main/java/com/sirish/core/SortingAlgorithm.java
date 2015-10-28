package com.sirish.core;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * @author sirish
 *
 */
public class SortingAlgorithm {

	String country,state,district,village;
	
	public SortingAlgorithm(String countryStr,String stateStr,String distStr,String villageStr ) {
		
		country = countryStr;
		state = stateStr;
		district = distStr;
		village = villageStr;
	}

	public String getCountry() {
		return country;
	}

	public String getState() {
		return state;
	}

	public String getDistrict() {
		return district;
	}

	public String getVillage() {
		return village;
	}
	
	
	public static void main(String[] args) {

		SortingAlgorithm sa1 = new SortingAlgorithm("A", "AP", "EG", "ap");
		SortingAlgorithm sa2 = new SortingAlgorithm("NorthAmerica", "Mexico", "SanDiego", "Milpitas");
		SortingAlgorithm sa3 = new SortingAlgorithm("Australia", "Mexico", "SanDiego", "Milpitas");
		SortingAlgorithm sa4 = new SortingAlgorithm("A", "AP", "G", "Bang");
		SortingAlgorithm sa5 = new SortingAlgorithm("NorthAmerica", "NY", "SanJose", "fremont");
		SortingAlgorithm sa6 = new SortingAlgorithm("UK", "Italy", "London", "Paris");
		SortingAlgorithm sa7 = new SortingAlgorithm("C", "X", "T", "Y");
		SortingAlgorithm sa8 = new SortingAlgorithm("Australia", "Melbourne", "Adelide", "DGE");
		SortingAlgorithm sa9 = new SortingAlgorithm("D", "Chile", "DFG", "RD");
		SortingAlgorithm sa10 = new SortingAlgorithm("F", "Amp", "PT", "Che");
		SortingAlgorithm sa11 = new SortingAlgorithm("India", "AP", "XTP", "Che");
		
		List<SortingAlgorithm> sortList = new ArrayList<SortingAlgorithm>();
		
		sortList.add(sa1);sortList.add(sa2);sortList.add(sa3);sortList.add(sa4);sortList.add(sa5);sortList.add(sa6);sortList.add(sa7);sortList.add(sa8);sortList.add(sa9);sortList.add(sa10);sortList.add(sa11);
		
		Collections.sort(sortList,new SortingComparator());
		
		for(SortingAlgorithm sa : sortList){
			System.out.println(sa.getCountry()+ " : "+sa.getState()+"  : "+sa.getDistrict()+"  : "+sa.getVillage());
		}
	}
}
