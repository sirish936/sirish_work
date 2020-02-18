package com.sirish.hpe;

public enum ServerSecurityState
{

    PRODUCTION ("Production", false),
    FIPS ("FIPS", true),
    HIGHSECURITY ("HighSecurity", true),
    CAC ("CAC", true),
    WIPE ("Wipe", false),
    SUITEB ("SuiteB/CNSA", true),
    UNSUPPORTED ("Unsupported", false),
    CNSA ("CNSA", true),
    FACTORY ("Factory", false);

    final boolean value;
    final String name;

    private ServerSecurityState(final String name, final boolean value)
    {
        this.name = name;
        this.value = value;
    }

    public boolean isHighSecurityMode()
    {
        return this.value;
    }

    public String getName()
    {
        return this.name;
    }

    /**
     * This method will get the security state for a String value.
     *
     * @param securityState
     * @return
     */
    
}
