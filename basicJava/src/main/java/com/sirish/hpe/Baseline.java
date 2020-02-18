package com.sirish.hpe;

public class Baseline {
	
	public String baselineName;
	public String getBaselineName() {
		return baselineName;
	}

	public void setBaselineName(String baselineName) {
		this.baselineName = baselineName;
	}

	public String getBaselieUri() {
		return baselieUri;
	}

	public void setBaselieUri(String baselieUri) {
		this.baselieUri = baselieUri;
	}

	public BaselineMetaData getBaselineMetaData() {
		return baselineMetaData;
	}

	public void setBaselineMetaData(BaselineMetaData baselineMetaData) {
		this.baselineMetaData = baselineMetaData;
	}

	public String baselieUri;
	
	public BaselineMetaData baselineMetaData;

}
