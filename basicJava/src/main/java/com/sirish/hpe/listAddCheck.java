package com.sirish.hpe;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

class Filename {
	String name;

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getCompsigName() {
		return compsigName;
	}

	public void setCompsigName(String compsigName) {
		this.compsigName = compsigName;
	}

	String compsigName;

}

public class listAddCheck {
	public static void main(String[] args) {
		List<Filename> fileList = new ArrayList<Filename>();
		Filename name1 = new Filename();
		name1.setName("name10");
		fileList.add(name1);
		
		List<Filename> fileList2 = new ArrayList<Filename>();
		Filename name2 = new Filename();
		name1.setName("name5");
		Filename name3 = new Filename();
		name1.setName("name17");
		Filename name4 = new Filename();
		name1.setName("name2");
		Filename name5 = new Filename();
		name1.setName("name9");
		fileList2.add(name2);fileList2.add(name3);fileList2.add(name4);fileList2.add(name5);
		
		fileList.addAll(fileList2);
		fileList.sort(Comparator.comparing(Filename::getName));
		for(Filename name : fileList) {
			System.out.println(name);
		}
	}
}
