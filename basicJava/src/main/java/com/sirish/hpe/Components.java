package com.sirish.hpe;

public class Components {
	String componentName;
	public String getComponentName() {
		return componentName;
	}
	public void setComponentName(String componentName) {
		this.componentName = componentName;
	}
	public String getComponentGuid() {
		return ComponentGuid;
	}
	public void setComponentGuid(String componentGuid) {
		ComponentGuid = componentGuid;
	}
	public int getComponentVersion() {
		return componentVersion;
	}
	public void setComponentVersion(int componentVersion) {
		this.componentVersion = componentVersion;
	}
	String ComponentGuid;
	int componentVersion;
	

}
