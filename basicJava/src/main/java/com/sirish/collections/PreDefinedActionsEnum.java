package com.sirish.collections;

public enum PreDefinedActionsEnum
{
	DisableOneTimeBoot(1),
	EnableOneTimeBoot (new String[] {"bootTarget"},2),
	PowerOnServer ("PowerOnServer", new String[] {"WaitForPowerOn"},3),
	WaitForPowerOn(4),
	WaitForDiscoveryComplete(5),
	WaitForPostComplete(6),
	RestartServer(7),
	WaitForRestartComplete(8),
	ResetManagementProcessor(9),
	UpdateLEDState (new String[] {"indicatorLedState"},10),
	PowerOffServer ("PowerOffServer", new String[] {"WaitForPowerOff"},11),
	ForcePowerOffServer ("ForcePowerOffServer", new String[] {"WaitForPowerOff"},12),
	WaitForPowerOff(13),
	None(14);

    private final String mainAction;
    private final String[] postActions;
    private final String[] mandatoryParams;
    private final int index;

    PreDefinedActionsEnum(final String mainAction, final String[] postActions,int index)
    {
        this.mainAction = mainAction;
        this.postActions = postActions;
        this.mandatoryParams = new String[0];
        this.index = index;
    }

    PreDefinedActionsEnum(final String[] mandatoryParams,int index)
    {
        this.mainAction = this.toString();
        this.postActions = new String[0];
        this.mandatoryParams = mandatoryParams;
        this.index = index;
    }

    PreDefinedActionsEnum(int index)
    {
        this.mainAction = this.toString();
        this.postActions = new String[0];
        this.mandatoryParams = new String[0];
        this.index = index;
    }

    /**
     * @return the mainAction
     */
    public String getMainAction()
    {
        return mainAction;
    }

    /**
     * @return the postActions
     */
    public String[] getPostActions()
    {
        return postActions;
    }

    /**
     * @return the mandatoryParams
     */
    public String[] getMandatoryParams()
    {
        return mandatoryParams;
    }
    
    /**
     * @return the index
     */
    public int getIndex() 
    {
        return index;
      }
}

