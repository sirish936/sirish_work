package com.sirish.core;

import java.util.Comparator;

/**
 * @author sirish
 *
 */
public class SortingComparator  implements Comparator<SortingAlgorithm>{
	
	public int compare(SortingAlgorithm o1, SortingAlgorithm o2) {
		
		if( o1.getCountry().compareTo(o2.getCountry()) == 0){
			if(o1.getState().compareTo(o2.getState()) ==0){
				if(o1.getDistrict().compareTo(o2.getDistrict()) == 0){
					if(o1.getVillage().compareTo(o2.getVillage()) ==0){
						return 0;
					}else if(o1.getVillage().compareTo(o2.getVillage()) ==1){
						return 1;
					}else{
						return -1;
					}
				}else if(o1.getDistrict().compareTo(o2.getDistrict()) ==1){
					return 1;
				}else{
					return -1;
				}
			}else if(o1.getState().compareTo(o2.getState()) ==1){
				return 1;
			}else{
				return -1;
			}
		}else if(o1.getCountry().compareTo(o2.getCountry()) ==1){
			return 1;
		}else{
			return -1;
		}
	}
}	
