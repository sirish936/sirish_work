package com.sirish.core;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Account {

	String accName;
	Long accNumber;
	BigDecimal amountDue;
	
	public String getAccName() {
		return accName;
	}
	public Long getAccNumber() {
		return accNumber;
	}
	public BigDecimal getAmountDue() {
		return amountDue;
	}
	
	Account(String accountName,Long accountNumber, BigDecimal dueAmount){
		accName = accountName;
		accNumber = accountNumber;
		amountDue = dueAmount;
	}
	
	@SuppressWarnings("unchecked")
	public static void main(String[] args) {
		
		List<Account> accList = new ArrayList<Account>();
		
		 Account acc3 = new Account("CD", new Long(34), new BigDecimal(345));
		 Account acc6 = new Account("AB", new Long(12), new BigDecimal(123));
		 Account acc9 = new Account("BC", new Long(23), new BigDecimal(234));
		 Account acc2 = new Account("AB", new Long(23), new BigDecimal(234));
		 Account acc5 = new Account("AB", new Long(12), new BigDecimal(121));
		 Account acc8 = new Account("BC", new Long(45), new BigDecimal(456));
		 Account acc1 = new Account("BC", new Long(23), new BigDecimal(121));
		 Account acc4 = new Account("CD", new Long(34), new BigDecimal(121));
		 Account acc7 = new Account("CD", new Long(12), new BigDecimal(346));

		 accList.add(acc3);accList.add(acc6);accList.add(acc9);accList.add(acc2);accList.add(acc5);accList.add(acc8);accList.add(acc1);accList.add(acc4);accList.add(acc7);

		 System.out.println("Before Sorting::");
		 for(Account acc : accList){
			 System.out.println(acc.getAccName() + " " + acc.getAccNumber()+" "+acc.getAmountDue());
		 }
		 
		 Collections.sort(accList,new AccountChainedComparator(new AccountNameComparator(),new AccountNumberComparator(),new AmountDueComparator()));
		
		 System.out.println("After Sorting::");
		 for(Account acc : accList){
			 System.out.println(acc.getAccName() + " " + acc.getAccNumber()+" "+acc.getAmountDue());
		 }
	}
}

