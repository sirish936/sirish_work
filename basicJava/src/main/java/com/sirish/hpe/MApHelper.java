package com.sirish.hpe;

import java.util.HashMap;
import java.util.Map;

public class MApHelper {

	HashMap<String, String> fwbaselineAttributesMap = null;
	public String getSwKeyForICModel(final String interconnectModel)
    {
        //Skip doing comparison if interconnect model is null.
        String swKeyName = null;
        
        if(fwbaselineAttributesMap == null ){
        	fwbaselineAttributesMap = getFwIndexAttributes();
        }
        if (fwbaselineAttributesMap != null&& !fwbaselineAttributesMap.isEmpty())
        {
            for (final Map.Entry<String, String> entry : fwbaselineAttributesMap.entrySet())
            {
                final String modelName = entry.getKey();
                if (interconnectModel.equalsIgnoreCase(modelName))
                {
                    swKeyName = entry.getValue();
                    break;
                }
            }
        }

        return swKeyName;
    }

	private HashMap<String, String> getFwIndexAttributes() {
		System.out.println("Entered Map population logic");
		final HashMap<String, String> fwIndexAttributesMap = new HashMap<String, String>();
		fwIndexAttributesMap.put("Animal","A");
		fwIndexAttributesMap.put("Ball","B");
		fwIndexAttributesMap.put("Cat","C");
		fwIndexAttributesMap.put("Dog","D");
		fwIndexAttributesMap.put("Eagle","E");
		fwIndexAttributesMap.put("Fox","F");
		fwIndexAttributesMap.put("Gate","G");
		fwIndexAttributesMap.put("Hen","H");
		return fwIndexAttributesMap;
	}
}
