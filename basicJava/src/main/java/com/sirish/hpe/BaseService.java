package com.sirish.hpe;

public class BaseService {
public Baseline serviceTest()
{
	Baseline baselineNew = new Baseline();
	baselineNew.setBaselineName("sirish");
	
	Baseline baselineReturned = null;
	
	baselineReturned = getBaseline(baselineNew);
			
	System.out.println(baselineNew.getBaselineName());
	System.out.println(baselineReturned.getBaselineName());
	
	return baselineReturned;
	
}

private Baseline getBaseline(Baseline baselineNew) {
	
	Baseline returnBaseline = new Baseline();
	returnBaseline.setBaselineName("venkat");
	return returnBaseline;
	
	
}

public static void main(String[] args) {
	BaseService service = new BaseService();
	service.serviceTest();
}
}
