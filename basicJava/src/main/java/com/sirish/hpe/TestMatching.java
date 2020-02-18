package com.sirish.hpe;

import java.util.ArrayList;
import java.util.List;

public class TestMatching {
	public static void main(String[] args) {
		String targetGuid = "002340a5-4d00-3642-3030-304a45585942";
		List<String> newList = new ArrayList<String>();
		newList.add("F6DE0320-2E0F-489A-B238-6DD8AE7C3811002340a5-4d00-3442-3030-304a45585941");
		newList.add("F6DE0320-2E0F-489A-B238-6DD8AE7C3811002340A5-4D00-3642-3030-304A45585942");
		newList.add("aa148d2e-6e09-453e-bc6f-63baa5f5ccc400000000-0000-0000-0000-00000000020b");
		
		for(String str : newList)
		{
			if(str.toLowerCase().contains(targetGuid)){
				System.out.println("TargetGuid matched {}"+str.toLowerCase());
			}
		}
		outerloop:for(int i=0;i<10;i++)
		{
			for(int j=i;j<10;j++)
			{
				for(int k=j;k<10;k++)
				{
					if(k<5)
					{
					System.out.println("hii");
					break outerloop;
					}
				}
			}
		}
	}
	
	
	
	
}
