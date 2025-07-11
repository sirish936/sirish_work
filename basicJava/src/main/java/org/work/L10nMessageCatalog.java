package org.work;

import java.io.File;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLClassLoader;
import java.security.PrivilegedAction;
import java.util.Locale;
import java.util.Set;

import org.springframework.context.support.ResourceBundleMessageSource;

/**
 * Simple wrapper around Spring's ResourceBundleMessageSource to retrieve
 * locale specific display messages. This class is intended to be the one
 * class everyone uses to get localized messages.
 */
public class L10nMessageCatalog
{
    private final ResourceBundleMessageSource messageSource;
    Set<String> partnerMessageKeys = null;
    String basename = null;

    public L10nMessageCatalog(final String basename)
    {
        messageSource = new ResourceBundleMessageSource();
        messageSource.setBasename(basename);
        this.basename = basename;
    }

    public void setAlwaysUseMessageFormat(final boolean alwaysUseMessageFormat)
    {
        messageSource.setAlwaysUseMessageFormat(alwaysUseMessageFormat);
    }

    public String getMessage(final String code, final Object[] args, final String defaultMessage, final Locale locale)
    {
        String msg_key = code;
        final String msg = BrandingMessageCatalog.getMessage(messageSource.getMessage(msg_key, args, defaultMessage, locale));
        return msg;
    }

}