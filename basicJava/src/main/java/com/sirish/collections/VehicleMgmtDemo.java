package com.sirish.collections;

import java.util.ArrayList;
import java.util.List;

public class VehicleMgmtDemo {

	/**
	 * @param args
	 */
	public static void main(final String[] args) {
		// TODO Auto-generated method stub
		final List<VehicleMgmt> list = new ArrayList<VehicleMgmt>();
		final List<VehicleMgmt> list1 = new ArrayList<VehicleMgmt>();

		final VehicleMgmt vehicle1 = new VehicleMgmt();
		vehicle1.setVehicleno("1221");
		vehicle1.setVehicletype("two wheeler");
		vehicle1.setCompanyname("Honda");
		vehicle1.setRegplace("Hyderabad");
		vehicle1.setRegdate("1/4/2000");
		vehicle1.setRegamount(1000);

		list.add(vehicle1);

		final VehicleMgmt vehicle2 = new VehicleMgmt();
		vehicle1.setVehicleno("1222");
		vehicle1.setVehicletype("two wheeler");
		vehicle1.setCompanyname("Yamaha");
		vehicle1.setRegplace("Secunderabad");
		vehicle1.setRegdate("1/4/2001");
		vehicle1.setRegamount(1000);

		list.add(vehicle2);

		final VehicleMgmt vehicle3 = new VehicleMgmt();
		vehicle1.setVehicleno("1223");
		vehicle1.setVehicletype("two wheeler");
		vehicle1.setCompanyname("Bajaj");
		vehicle1.setRegplace("Vizag");
		vehicle1.setRegdate("1/4/2002");
		vehicle1.setRegamount(1000);

		list.add(vehicle3);

		final VehicleMgmt vehicle4 = new VehicleMgmt();
		vehicle1.setVehicleno("1224");
		vehicle1.setVehicletype("two wheeler");
		vehicle1.setCompanyname("TVS");
		vehicle1.setRegplace("Vijayawada");
		vehicle1.setRegdate("1/4/2003");
		vehicle1.setRegamount(1000);

		list.add(vehicle4);

		final VehicleMgmt vehicle5 = new VehicleMgmt();
		vehicle1.setVehicleno("1225");
		vehicle1.setVehicletype("four wheeler");
		vehicle1.setCompanyname("Honda");
		vehicle1.setRegplace("Hyderabad");
		vehicle1.setRegdate("1/4/2004");
		vehicle1.setRegamount(5000);

		list1.add(vehicle5);

		final VehicleMgmt vehicle6 = new VehicleMgmt();
		vehicle1.setVehicleno("1226");
		vehicle1.setVehicletype("four wheeler");
		vehicle1.setCompanyname("Yamaha");
		vehicle1.setRegplace("Secunderabad");
		vehicle1.setRegdate("1/4/2005");
		vehicle1.setRegamount(5000);

		list1.add(vehicle6);

		final VehicleMgmt vehicle7 = new VehicleMgmt();
		vehicle1.setVehicleno("1227");
		vehicle1.setVehicletype("four wheeler");
		vehicle1.setCompanyname("suzuki");
		vehicle1.setRegplace("rjy");
		vehicle1.setRegdate("1/4/2006");
		vehicle1.setRegamount(5000);

		list1.add(vehicle7);

		final VehicleMgmt vehicle8 = new VehicleMgmt();
		vehicle1.setVehicleno("1228");
		vehicle1.setVehicletype("four wheeler");
		vehicle1.setCompanyname("toyota");
		vehicle1.setRegplace("Hyderabad");
		vehicle1.setRegdate("1/4/2007");
		vehicle1.setRegamount(1000);

		list1.add(vehicle8);

		final VehicleMgmt vehicle9 = new VehicleMgmt();
		vehicle1.setVehicleno("5555");
		vehicle1.setVehicletype("two wheeler");
		vehicle1.setCompanyname("mahindra");
		vehicle1.setRegplace("kkd");
		vehicle1.setRegdate("1/4/2008");
		vehicle1.setRegamount(1000);

		list1.add(vehicle9);

		/*
		 * if(true) { System.out.println("the vehicleno is already registered at Hyderabad in 1/4/2000"); } // else {
		 * System.out.println("Ur Registration is success"); }
		 */

		final VehicleMgmtDemo vmd = new VehicleMgmtDemo();
		final boolean b = vmd.equals(vehicle9);
		if (b == true) {
			System.out.println("the vehicleno is already registered at Hyderabad in 1/4/2000");
		} else {
			System.out.println("Ur Registration is success");
		}

	}

}
