package com.sirish.hpe;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Logic {
	/**
	 * @param args
	 */
	int no;
	public int getNo() {
		return no;
	}
	public void setNo(int no) {
		this.no = no;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getAddress() {
		return address;
	}
	public void setAddress(String address) {
		this.address = address;
	}

	String name,address;
	
	public static void main(String[] args) {
		check();
		
		//Optional<Boolean> matching = componentsPresent.values().stream().filter(p->p==false).findAny();
		//System.out.println(matching.orElseGet(null)); Administrator
		
		test();
		
		if(false && (false||true)){
			System.out.println("sirish");
		}
		
		String targtGuid = "a6b1a447-382a-5a4f-9005-028f103c0652";
		if (targtGuid.length() > 4)
        {
			targtGuid = targtGuid.substring(targtGuid.length() - 4);
        }
		
		List<String> list = new ArrayList<String>();
		list.add("1.15");
		list.add("1.00");
		list.add("5.75");
		list.add("1.30");
		list.add("1.25");
		System.out.println(list.size());
		Collections.sort(list);
		System.out.println(list);
//		String s1="sirish";  
//		String replaceString=s1.replaceAll(s1,s1);//replaces all occurrences of "a" to "e"  
//		System.out.println(replaceString);  
//		
//		String str = getLatestString();
//		
//		List list = new ArrayList<>();
//		System.out.println(list.size());
//		list.add("sirish");
//		System.out.println(list.size());
		
		
        //List<String> keyList = new ArrayList<String>();

		
//		if(true && true){
//			return false;
//			break;
//		}
//		}
		
	}	
private static void test(){
	int x=-1;
	int y = -1;
				
			if(x==y){
				System.out.println("sirish");
			}
}
	private static String getLatestString() {
		for(int i=0; i<3 ;i++){
			if(i==1)continue;
			
			String str = "sirish";
			
		}
		
		return "";
	}

	private static boolean check() {
		final Map<Object, Object> componentsPresent = new HashMap<Object, Object>();
		componentsPresent.put("EM", true);
		componentsPresent.put("VC", false);
		
		if(componentsPresent.isEmpty()){
			
		}
		
		for (Map.Entry<Object,Object> entry : componentsPresent.entrySet()){ 
            System.out.println("Key = " + entry.getKey() +
                             ", Value = " + entry.getValue());
        }
		
		for (Object entry : componentsPresent.values()){ 
			boolean di = (Boolean) entry;
			if(di == false){
				return false;
			}
        }
		return true;
	}
}
