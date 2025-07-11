package com.sirish.strings;

public class HelloWorld1{

    public static void main(String []args){
       String filename = "firmware-ilo5-2_10-1_1_x86_64_part1.compsig";
       String resourceId =  "firmware-ilo5-2_10-1_1_x86_64_part1";
       String LAST_UNDERSCORE_REGEX = "_(?!.*_)";
       if (resourceId.split(LAST_UNDERSCORE_REGEX)[1].contains("_part"))
                   {
                       resourceId = filename.split(LAST_UNDERSCORE_REGEX)[0];
                       System.out.println(resourceId);
                   }
                   if (filename.contains("_part*"))
                   {
                       
                       System.out.println("resourceId");
                   }
       
    }
     
                   
       
    
}
