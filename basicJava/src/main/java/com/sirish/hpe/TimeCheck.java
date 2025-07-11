package com.sirish.hpe;

import java.util.concurrent.TimeUnit;

public class TimeCheck {
	public static final long RAS_PROBE_TASK_COMPLETION_TIME_OUT_SEC = TimeUnit.MINUTES.toSeconds(1)
            + TimeUnit.SECONDS.toSeconds(30);
	public static void main(String[] args) {
		System.out.println("Time in seconds: "+ RAS_PROBE_TASK_COMPLETION_TIME_OUT_SEC);
	}
}
