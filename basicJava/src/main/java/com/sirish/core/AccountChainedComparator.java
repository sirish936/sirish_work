package com.sirish.core;

import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class AccountChainedComparator implements Comparator<Account>{

List<Comparator<Account>> listComparators; 
	
	AccountChainedComparator(Comparator<Account>...comparator){
		listComparators = Arrays.asList(comparator) ;
	}
	
	public int compare(Account a1, Account a2) {
		
		for(Comparator<Account> comparator : listComparators){

			int result = comparator.compare(a1, a2);
			
			if(result != 0){
				return result;
			}
		}
		return 0;
	}	
}


class AccountNameComparator implements Comparator<Account>{
	
	public int compare(Account a1, Account a2) {
		if(a1.getAccName().compareTo(a2.getAccName()) == 0){
			return 0;
		}else if(a1.getAccName().compareTo(a2.getAccName()) == 1){
			return 1;
		}else{
			return -1;
		}
	}
}

 class AccountNumberComparator implements Comparator<Account>{

	public int compare(Account a1, Account a2) {
		if(a1.getAccNumber().compareTo(a2.getAccNumber()) == 0){
			return 0;
		}else if(a1.getAccNumber().compareTo(a2.getAccNumber()) == 1){
			return 1;
		}else{
			return -1;
		}
	}
}


class AmountDueComparator implements Comparator<Account> {

	public int compare(Account a1, Account a2) {
		if(a1.getAmountDue().compareTo(a2.getAmountDue()) == 0){
			return 0;
		}else if(a1.getAmountDue().compareTo(a2.getAmountDue()) == 1){
			return 1;
		}else{
			return -1;
		}
	}
}