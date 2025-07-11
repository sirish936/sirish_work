package com.sirish.test.utils;

import java.util.Set;
import java.util.TreeSet;

import org.junit.Assert;
import org.junit.Test;

import com.sirish.collections.ActionsComparator;
import com.sirish.collections.PreDefinedActionsEnum;

public class ActionsComparatorTest {
	@Test
	public void testActionsComparator() {
		Set actionsSet = new TreeSet<PreDefinedActionsEnum>(new ActionsComparator());
		actionsSet.add(PreDefinedActionsEnum.WaitForPostComplete);
		actionsSet.add(PreDefinedActionsEnum.EnableOneTimeBoot);
		actionsSet.add(PreDefinedActionsEnum.ResetManagementProcessor);
		actionsSet.add(PreDefinedActionsEnum.WaitForDiscoveryComplete);
		actionsSet.add(PreDefinedActionsEnum.None);
		actionsSet.add(PreDefinedActionsEnum.WaitForRestartComplete);
		actionsSet.add(PreDefinedActionsEnum.PowerOnServer);
		Assert.assertEquals(((PreDefinedActionsEnum) actionsSet.stream().findFirst().get()).getIndex(), 2);

	}
}
