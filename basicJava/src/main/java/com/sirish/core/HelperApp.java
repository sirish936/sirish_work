package com.sirish.core;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class HelperApp {

	public void getProviderCategory(final String providerCategory) {

		final List<String> listProviders = getProviderByCategory(providerCategory);

		final Map<String, List<String>> listFailedSiteLogin = new HashMap<String, List<String>>();
		List<String> siteLogin = new ArrayList<String>();

		for (final String provider : listProviders) {

			siteLogin = getFailedSiteLogin(provider);
			listFailedSiteLogin.put(provider, siteLogin);

		}
	}

	public void getProviderByDate(final String startingDate, final String endingDate) {

		final List<String> listProviders = getAllProvider();

		final Map<String, List<String>> listFailedSiteLogin = new HashMap<String, List<String>>();
		List<String> siteLogin = new ArrayList<String>();

		for (final String provider : listProviders) {

			siteLogin = getFailedSiteLogin(provider);

			listFailedSiteLogin.put(provider, siteLogin);

		}
	}

	private List<String> getAllProvider() {
		// TODO Auto-generated method stub
		return null;
	}

	private List<String> getFailedSiteLogin(final String provider) {
		// TODO Auto-generated method stub
		final List<String> listSiteLogin = getSiteLogins(provider);
		final List<String> providerAccs = new ArrayList<String>();

		for (final String providerAcc : listSiteLogin) {

			final String siteLoginStausMsg = getProviderAccStatus(providerAcc);
			if (siteLoginStausMsg != null) {
				providerAccs.add(providerAcc);
			}
		}

		return null;
	}

	private String getProviderAccStatus(final String providerAcc) {
		// TODO Auto-generated method stub
		return null;
	}

	private List<String> getSiteLogins(final String provider) {
		// TODO Auto-generated method stub
		return null;
	}

	private List<String> getProviderByCategory(final String providerCategory) {
		// TODO Auto-generated method stub
		return null;
	}

}
