package com.sirish.hpe;

public enum SubResourceName {

	Memory("memory"), Processors("processors");

	private final String id;

	private SubResourceName(final String id) {
		this.id = id;
	}

	public String getId() {
		return id;
	}

	@Override
	public String toString() {
		return getId();
	}
}
