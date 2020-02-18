package com.sirish.hpe;

public class BaselineMetaData {
	public String baseId;
	public String getBaseId() {
		return baseId;
	}
	public void setBaseId(String baseId) {
		this.baseId = baseId;
	}
	public boolean isBaselineReleased() {
		return baselineReleased;
	}
	public void setBaselineReleased(boolean baselineReleased) {
		this.baselineReleased = baselineReleased;
	}
	public boolean baselineReleased;
}
