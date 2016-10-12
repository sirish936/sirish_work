package com.sirish.work;

import org.junit.Assert;
import org.junit.Test;

public class TestDatePredictor {

	@Test
	public void testGetYearPredictor() {

		PredictYearFor predictYearFor = null;
		DatePredictor datePredictor = new DatePredictor();

		PredictDates pd1 = new PredictDates();
		pd1.setStmtDate("20/12/2015");
		pd1.setDueDate("20/01");
		predictYearFor = datePredictor.getYearPredictor(pd1);
		Assert.assertEquals(PredictYearFor.DUE_DATE, predictYearFor);

		PredictDates pd2 = new PredictDates();
		pd2.setStmtDate("20/12");
		pd2.setDueDate("20/01/2015");
		predictYearFor = datePredictor.getYearPredictor(pd2);
		Assert.assertEquals(PredictYearFor.STATEMENT_DATE, predictYearFor);

		PredictDates pd3 = new PredictDates();
		pd3.setStmtDate("20/12");
		pd3.setDueDate("20/01");
		predictYearFor = datePredictor.getYearPredictor(pd3);
		Assert.assertEquals(PredictYearFor.STATEMENT_DATE_AND_DUE_DATE, predictYearFor);

		PredictDates pd4 = new PredictDates();
		pd4.setStmtDate("2015/05/07");
		pd4.setDueDate("20/01");
		predictYearFor = datePredictor.getYearPredictor(pd4);
		Assert.assertEquals(PredictYearFor.DUE_DATE, predictYearFor);

		PredictDates pd5 = new PredictDates();
		pd5.setStmtDate("2015-05-07");
		pd5.setDueDate("20/01");
		predictYearFor = datePredictor.getYearPredictor(pd5);
		Assert.assertEquals(PredictYearFor.DUE_DATE, predictYearFor);

		PredictDates pd6 = new PredictDates();
		pd6.setStmtDate("20 Dec,2015");
		pd6.setDueDate("20/01");
		predictYearFor = datePredictor.getYearPredictor(pd6);
		Assert.assertEquals(PredictYearFor.DUE_DATE, predictYearFor);

		PredictDates pd7 = new PredictDates();
		pd7.setStmtDate("20 Jan");
		pd7.setDueDate("20 Dec, 2015");
		predictYearFor = datePredictor.getYearPredictor(pd7);
		Assert.assertEquals(PredictYearFor.STATEMENT_DATE, predictYearFor);

		PredictDates pd8 = new PredictDates();
		pd8.setStmtDate("Jan 20");
		pd8.setDueDate("20th Dec, 2015");
		predictYearFor = datePredictor.getYearPredictor(pd8);
		Assert.assertEquals(PredictYearFor.STATEMENT_DATE, predictYearFor);

		PredictDates pd9 = new PredictDates();
		pd9.setStmtDate("Jan 20");
		pd9.setDueDate("20 January");
		predictYearFor = datePredictor.getYearPredictor(pd9);
		Assert.assertEquals(PredictYearFor.STATEMENT_DATE_AND_DUE_DATE, predictYearFor);

		PredictDates pd10 = new PredictDates();
		pd10.setStmtDate("January 30");
		pd10.setDueDate("30 March");
		predictYearFor = datePredictor.getYearPredictor(pd10);
		Assert.assertEquals(PredictYearFor.STATEMENT_DATE_AND_DUE_DATE, predictYearFor);

	}
}