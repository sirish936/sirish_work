package com.sirish.hpe;

public enum DirectFlashOk
{
    TRUE (true),
    FALSE (false);
    private boolean value = false;

    private DirectFlashOk(final boolean value)
    {
        this.value = value;
    }

    public boolean getValue()
    {
        return this.value;
    }
}
