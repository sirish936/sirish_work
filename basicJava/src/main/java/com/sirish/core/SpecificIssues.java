package com.sirish.core;

import java.util.ArrayList;
import java.util.List;

public class SpecificIssues {

	public void getAllSiteLogins(final String providerDisplayName) {

		final List<String> siteLoginList = getSiteLogins(providerDisplayName);
		final List<String> siteLogin = new ArrayList<String>();

		for (final String sl : siteLoginList) {

			final String siteLoginStausMsg = getProviderAccStatus(sl);
			if (siteLoginStausMsg != null) {
				siteLogin.add(sl);
			}
		}

	}

	private List<String> getSiteLogins(final String displayName) {
		// TODO Auto-generated method stub
		return null;
	}

	private String getProviderAccStatus(final String providerAcc) {
		// TODO Auto-generated method stub
		return null;
	}

}
