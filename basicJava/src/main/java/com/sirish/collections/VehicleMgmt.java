package com.sirish.collections;

public class VehicleMgmt {

	String vehicleno, vehicletype, companyname, regplace, regdate;
	int regamount;

	public String getVehicleno() {
		return vehicleno;
	}

	public void setVehicleno(final String vehicleno) {
		this.vehicleno = vehicleno;
	}

	public int getRegamount() {
		return regamount;
	}

	public void setRegamount(final int regamount) {
		this.regamount = regamount;
	}

	public String getVehicletype() {
		return vehicletype;
	}

	public void setVehicletype(final String vehicletype) {
		this.vehicletype = vehicletype;
	}

	public String getCompanyname() {
		return companyname;
	}

	public void setCompanyname(final String companyname) {
		this.companyname = companyname;
	}

	public String getRegplace() {
		return regplace;
	}

	public void setRegplace(final String regplace) {
		this.regplace = regplace;
	}

	public String getRegdate() {
		return regdate;
	}

	public void setRegdate(final String regdate) {
		this.regdate = regdate;
	}

	@Override
	public boolean equals(final Object obj) {
		final VehicleMgmt ve = (VehicleMgmt) obj;
		// VehicleMgmt ve1=(VehicleMgmt)obj1;
		if (this.vehicleno.equals(ve.getVehicleno())) {
			return true;
		} else {
			return false;
		}
	}
}
