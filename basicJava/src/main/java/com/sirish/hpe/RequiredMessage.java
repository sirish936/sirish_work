package com.sirish.hpe;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.concurrent.ConcurrentHashMap;

public class RequiredMessage {
	
	static String oneCmp = "Onboard Administartor";
	static String twoCmp = "Onboard Administartor Virtual Connect";
	static String fstMsg = "This Service Pack for ProLiant can be used to applying a firmware baseline for the managed hardware. However, it cannot be used in the following cases";
	static String lstMsg = "If these do not apply to the managed hardware, then the alert can be cleared. Otherwise, include the required components and re-add the SPP.";
	static String mdlMsg = "firmware are required when applying a firmware baseline to a blade system enclosure";
	static String isStr ="is";
	static String areStr ="are";
	static String andStr ="and";
	
	public static void main(String[] args) {
		StringBuffer str = new StringBuffer();
		str.append(fstMsg);
		if(oneCmp.contains("Onboard Administartor")){
			str.append(oneCmp);
			str.append(isStr);
		}
//		if(twoCmp.contains("Virtual Connect")){
//			mdlMsg.replaceAll(isStr, areStr);
//		}
//		str.append(lstMsg);
		
	List<String> strList = new ArrayList<String>(); 
	boolean remove =strList.remove("sirish");
	System.out.println("list size is "+strList.size());
	
	ConcurrentHashMap certificationCosts = new ConcurrentHashMap<>();
	Set concurrentHashSet = certificationCosts.newKeySet();
	concurrentHashSet.add("OCEJWCD"); //OK
	concurrentHashSet.add("OCEJWCT"); //OK
	concurrentHashSet.add("OCEJWCD"); //OK
	
	concurrentHashSet.contains("OCEJWCD"); //OK
	concurrentHashSet.remove("OCEJWCD"); //OK

	}
}
