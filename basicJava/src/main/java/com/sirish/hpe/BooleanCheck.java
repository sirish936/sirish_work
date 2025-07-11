package com.sirish.hpe;

public class BooleanCheck {
	public static void main(String[] args) {
		Boolean isReq = isValReq();
		if (isReq.booleanValue()) {
			System.out.println("inside true");
		}
		if(isReq) {
			System.out.println("inside Bool true");
		}
	}

	private static Boolean isValReq() {
		Boolean bool;
		if(true) {
			return bool = Boolean.TRUE;
		}
		return bool=Boolean.FALSE;
	}
}
