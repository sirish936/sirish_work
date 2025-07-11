package org.work;


import java.util.Map;
import java.util.regex.Pattern;

import org.apache.commons.lang.text.StrSubstitutor;

public final class BrandingMessageCatalog
{

    static final String BRANDING_PLACEHOLDER_PREFIX = "$[";
    static final String BRANDING_PLACEHOLDER_SUFFIX = "]";
    static final String BRANDING_PLACEHOLDER_REGEX = "\\$\\[[^]]+\\]";
    static final Pattern PATTERN = Pattern.compile(BRANDING_PLACEHOLDER_REGEX);

    private BrandingMessageCatalog()
    {
    }

    public static String getMessage(final String message)
    {
        if (message == null)
        {
            return null;
        }
        String formattedMessage = message;

        if (PATTERN.matcher(message).find())
        {
            formattedMessage = replace(message, BrandingDictionary.getDictionary());
        }
        return formattedMessage;
    }

    private static String replace(final String message, final Map<String, String> brandingMap)
    {
        final StrSubstitutor strSubstitutor = new StrSubstitutor(brandingMap, BRANDING_PLACEHOLDER_PREFIX,
                BRANDING_PLACEHOLDER_SUFFIX);
        return strSubstitutor.replace(message);
    }
}