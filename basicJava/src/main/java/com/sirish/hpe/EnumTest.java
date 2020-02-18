package com.sirish.hpe;

public class EnumTest {
public static void main(String[] args) {
	System.out.println(ServerSecurityState.PRODUCTION.value);
	System.out.println(ServerSecurityState.PRODUCTION.getName());
	String serverSecurityMode = "Factory";
	if (ServerSecurityState.FACTORY.toString().equals(serverSecurityMode))
    {
	   System.out.println(ServerSecurityState.PRODUCTION.toString());
       System.out.println("Modes are equal"); 
    }
}
}
