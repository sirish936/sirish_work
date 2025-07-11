package com.sirish.hpe;

import java.util.List;

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
	
	public List<Components> compList;
	public List<Components> getCompList() {
		return compList;
	}

	public void setCompList(List<Components> compList) {
		this.compList = compList;
	}

}
