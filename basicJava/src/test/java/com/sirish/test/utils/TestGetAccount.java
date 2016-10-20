package com.sirish.test.utils;
//package com.sirish.work;
//
//import static org.mockito.Mockito.mock;
//
//import java.math.BigDecimal;
//import java.util.Date;
//import java.util.List;
//
//import org.junit.Before;
//import org.junit.Test;
//
//import com.fiport.business.AccountIdentifier;
//import com.fiport.business.manager.IUserManager;
//import com.fiport.business.util.provider.IAccountNumberMatcher;
//import com.fiport.downloader.DownloadScrapedData;
//import com.fiport.mongo.Account;
//import com.fiport.mongo.AccountDAL;
//import com.fiport.mongo.Provider;
//import com.fiport.mongo.ProviderAccount;
//
//public class TestGetAccount extends TesterBase {
//
//	private IUserManager userManager;
//	ProviderAccount providerAccount;
//	private Provider provider;
//	private AccountDAL accountDao;
//	Account acc1, acc2, acc3;
//	DownloadScrapedData downloadScrapedData;
//
//	IAccountNumberMatcher accNumberMatcher;
//
//	String accountNumber, accountName, accountType, currentBalance;
//	Date currentBalanceDate;
//	BigDecimal creditLimit;
//	Long intuitAccountId;
//	List<Account> accList;
//	IAccountNumberMatcher accNumMatcher;
//
//	@Before
//	public void setup() throws Exception {
//
//		userManager = mock(IUserManager.class);
//		providerAccount = new ProviderAccount();
//		provider = new Provider();
//		accountDao = mock(AccountDAL.class);
//		downloadScrapedData = new DownloadScrapedData();
//		accNumMatcher = mock(IAccountNumberMatcher.class);
//
//	}
//
//	@Test
//	public void testGetAccount() throws Exception {
//
//		provider.setName("Airtel");
//
//		currentBalanceDate = new Date();
//		accountNumber = "123";
//		accountName = "Airtel Prepaid";
//		accountType = "UTILITY";
//		creditLimit = new BigDecimal(5000);
//		currentBalance = "500";
//		intuitAccountId = new Long(12345);
//
//		accList.add(acc1);
//		accList.add(acc2);
//		accList.add(acc3);
//
//		final AccountIdentifier accidentifier = new AccountIdentifier(userManager, accountDao, accNumberMatcher);
//
//		accidentifier.getAccountByDownloadScrapedDataDetails(accountNumber, accountName, accountType, creditLimit, currentBalance, intuitAccountId,
//				currentBalanceDate, providerAccount.getId(), provider);
//
//		// final DownloadScrapedDataUpdator scrapedDataUpdator = new DownloadScrapedDataUpdator(userManager, accountDao);
//		// final Method m = scrapedDataUpdator.getClass().getDeclaredMethod("getAccount(provider,downloadScrapedData)");
//		// m.setAccessible(true);
//		//
//		// m.invoke(scrapedDataUpdator);
//
//	}
// }
