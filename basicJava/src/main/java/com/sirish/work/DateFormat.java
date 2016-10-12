package com.sirish.work;

public enum DateFormat {

	YYYY_MM_DD_WITH_HYPHEN("yyyy-MM-dd"),
	YYYY_MM_DD_WITH_SLASH("yyyy/MM/dd"),
	
	MM_DD_YYYY_WITH_HYPHEN("MM-dd-yyyy"),
	MM_DD_YYYY_WITH_SLASH("MM/dd/yyyy"),
	
	MM_DD_YY_WITH_HYPHEN("MM-dd-yy"),
	MM_DD_YY_WITH_SLASH("MM/dd/yy"),
	
	MMM_DD_YYYY_WITH_SPACE("MMM dd, yyyy"),
	MMM_DD_YYYY_WITHOUT_SPACE("MMM dd,yyyy"),

	DD_MMM_YYYY_WITH_SPACE("dd MMM, yyyy"),
	DD_MMM_YYYY_WITHOUT_SPACE("dd MMM,yyyy"),

	MMM_DD_YY_WITH_SPACE("MMM dd, yy"),
	MMM_DD_YY_WITHOUT_SPACE("MMM dd,yy"),

	DD_MMM_YY_WITH_SPACE("dd MMM, yy"),
	DD_MMM_YY_WITHOUT_SPACE("dd MMM,yy"),

	DD_MMM("dd MMM"),
	MMM_DD("MMM dd"),
	
	MM_DD_WITH_HYHEN("MM-dd"),
	MM_DD_WITH_SLASH("MM/dd");
	
	
	String format;

	DateFormat(final String format) {
		this.format = format;
	}	

	@Override
	public String toString() {
		return format;
	}
}