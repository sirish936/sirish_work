package com.sirish.hariwork;

import java.io.File;

public class ParentDirectoryExample {
	 
	public static void main(String[] args) {

		File file = new File(
				"C://Users//nimmaksi//Downloads//Patents//Method_to_abort_FWU");
		System.out.println(file.getParentFile().getName());
		System.out.println(file.getName());
		System.out.println(file.getParent());
		System.out.println(file.getAbsolutePath());
		String payloadPath = "/ci/data/sum_repository/abs/uuid/";
		String compsigFilePath = "/mnt/fwbundles/SPP/packages/asdfgh.compsig";

		System.out
				.println(payloadPath
						+ compsigFilePath.substring(compsigFilePath
								.lastIndexOf('/') + 1));

		final String baseRepoPath = "/ci/data/sum_repository/"
				+ "abs/123456789" + "/";

		for (int i = 0; i < 10; i++) {
			String repoPath = baseRepoPath;
			
			if(i%2==0){
				repoPath = baseRepoPath +  "abc.compsig"+ "/";
				System.out.println("RepoPath =" +repoPath);
			}else{
				System.out.println("RepoPath =" +repoPath);
			}

		}
		
		String fileName = "abc_part1";
		final String [] x = fileName.split("_");
        String y = x[1];
        String z = y.replace("part", "");
        System.out.println("Final content lect over is =" +z);
        
        
        String fileName1 = "abc_part2";
		final String  xa = fileName1.split("_").clone()[1].replace("part", "");
        System.out.println("Final content lect over is =" +xa);
		

	}
}
