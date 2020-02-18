package com.sirish.hpe;

public enum UpgradeRequirement {
	CRITICAL("Critical"), RECOMMENDED("Recomended"), OPTIONAL("Optional");

	private String value;

	private UpgradeRequirement(final String value) {
		this.value = value;
	}
}
