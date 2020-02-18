package com.sirish.io;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.Map;

public class FileDataRead {

	public static void main(String[] args) throws IOException {
		String line = null;
		BufferedWriter wr = null;
		BufferedReader reader = null;
		final StringBuffer portalInfo = new StringBuffer();
		final Map<String, String> portalInfoMap = new HashMap<String, String>();
		try {
			reader = new BufferedReader(new InputStreamReader(
					new FileInputStream(args[0])));
			wr = new BufferedWriter(new OutputStreamWriter(
					new FileOutputStream(args[1])));
			while ((line = reader.readLine()) != null) {
				// wr.write(line);
				if(!line.contains("="))
                {
                    continue;
                }
				portalInfo.append(line);
				portalInfo.append(";");
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} finally {
			wr.close();
			reader.close();
		}
		if(portalInfo != null )
        {
            String portalData[] = portalInfo.toString().split(";");
            for(String data : portalData)
            {
                String portal[] = data.split("=");
               
                    portalInfoMap.put(portal[0], portal[1]);
                
               
            }
        }
		System.out.println(portalInfo);
		System.out.println(portalInfoMap);
	}
}
