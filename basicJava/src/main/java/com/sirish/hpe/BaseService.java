package com.sirish.hpe;

import java.util.ArrayList;
import java.util.List;

public class BaseService {
public Baseline serviceTest()
{
	Baseline baselineNew = new Baseline();
	baselineNew.setBaselineName("sirish");
	
	List<Components> compList = new ArrayList();
	
	Components comp = new Components();
	comp.setComponentGuid("1234");comp.setComponentName("abcd");
	comp.setComponentVersion(1234);
	compList.add(comp);
	comp = new Components();
	comp.setComponentGuid("5678");comp.setComponentName("efgh");
	comp.setComponentVersion(5678);
	compList.add(comp);
	baselineNew.setCompList(compList);
	
	Baseline baselineReturned = null;
	
	baselineReturned = getBaseline(baselineNew);
			
	System.out.println(baselineNew.getBaselineName());
	System.out.println(baselineReturned.getBaselineName());
	
	return baselineNew;
	
}

private Baseline getBaseline(Baseline baselineNew) {
	
	Baseline returnBaseline = new Baseline();
	returnBaseline.setBaselineName("venkat");
	return returnBaseline;
	
	
}

public static void main(String[] args) {
	BaseService service = new BaseService();
	Baseline b = service.serviceTest();
	//get from DB
	Baseline bline =b;
	//bline.setCompList(b.getCompList());
	for(Components comps : bline.getCompList()) {
		System.out.println(comps.getComponentGuid());
		System.out.println(b.getBaselineName());
	}
			
}
}
