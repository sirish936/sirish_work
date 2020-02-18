package com.sirish.hpe;

	public enum InstallState
    {
        Uninitialized,
        Unknown,
        Pending,
        SPPBootFailed,
        Scheduled,
        ScheduleFailed,
        ScheduleDelayed,
        Staging,
        Staged,
        StageFailed,
        Installing,
        InstalledPendingReboot,
        InstallFailed,
        Activating,
        Activated,
        ActivateFailed;

        private static final String SPACE = " ";
        private static final String EMPTY_STRING = "";

        /**
         * Returns true if the current state is a terminal state.
         *
         * @return
         */
        public boolean isTerminal()
        {
            return (this == Activated || this == ActivateFailed || this == InstallFailed || this == StageFailed
                    || this == Uninitialized || this == SPPBootFailed);
        }

        /**
         * Returns a string whose value with any interceding whitespace removed.
         *
         * @param value the string to search for whitespaces.
         * @return A string whose value with any interceding whitespace removed,
         *         or this string if it has no arbitrating whitespace.
         */
        public static InstallState getInstallState(final String value)
        {
            return valueOf(value.replaceAll(SPACE, EMPTY_STRING));
        }

        /**
         * Returns whether the current state is a probable state before eFuse
         *
         * @return
         */
        public boolean isAPostInstallState()
        {
            return (this == Activating
                    || this == Activated
                    || this == ActivateFailed
                    || this == Installing
                    || this == InstallFailed
                    || this == InstalledPendingReboot);
        }
    }

