package com.sirish.core;

import java.util.ArrayList;
import java.util.List;

public class RemoveString {

	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		List<Object> list=new ArrayList<Object>();
		
		list.add(1);
		list.add("nivas");
		list.add(2);
		list.add("sirish");
		list.add(6);
		for(int i=0;i<list.size();++i){
			if(list.get(i) instanceof String)
				list.remove(i);
			
		}
		System.out.println("size of list is:"+list.size());
		
		
	}

}
