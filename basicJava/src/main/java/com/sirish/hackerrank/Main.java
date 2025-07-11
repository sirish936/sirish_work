package com.sirish.hackerrank;

import java.util.HashSet;
import java.util.Set;

public class Main {
    public static void main(String[] args) {
        Set<String> ipAddresses = new HashSet<>();
        
        // Adding all IP addresses from 10.0.0.1 to 10.0.3.254 to the HashSet
        for (int i = 0; i <= 3; i++) {
            for (int j = 0; j <= 255; j++) {
                String ipAddress = "10.0." + i + "." + j;
                ipAddresses.add(ipAddress);
            }
        }
        
        // Print the HashSet elements
        System.out.println(ipAddresses);
        
        // Optionally, you can check the size of the HashSet
        System.out.println("Number of IP addresses: " + ipAddresses.size());
    }
}

