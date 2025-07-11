package org.work;

//(C) Copyright 2012-2019 Hewlett Packard Enterprise Development LP


import java.util.Locale;

import org.springframework.web.client.HttpStatusCodeException;



public class ErrorMessageFactory
{
 public static final String LINE_SEPARATOR = System.getProperty("line.separator");

 public static final ErrorMessage createBestErrorMessage(final Throwable exception, final Locale locale)
 {
     if (exception instanceof ErrorMessageException)
     {
         return createErrorMessage((ErrorMessageException) exception, locale);
     }
     if (exception instanceof HttpStatusCodeException)
     {
         return createErrorMessageFromClient((HttpStatusCodeException) exception);
     }
     return createErrorMessageFromThrowable(exception);
 }

 public static final ErrorMessage createErrorMessage(final ErrorMessageException exception, final Locale locale)
 {
     final String message = exception.getLocalizedMessage(locale);
     final String details = exception.getLocalizedDetails(locale);
     final String fullRecommendedActions = exception.getLocalizedRecommendedActions(locale);
     final String[] recommendedActions = (fullRecommendedActions == null ? new String[0] : fullRecommendedActions.split("\\n"));

     final ErrorMessage errorMessage = new ErrorMessage();
     errorMessage.setErrorCode(exception.getErrorCode());
     errorMessage.setMessage(message);
     errorMessage.setDetails(details);
     errorMessage.setRecommendedActions(recommendedActions);
     errorMessage.setErrorSource(exception.getErrorSource());
     errorMessage.setData(exception.getData());
     errorMessage.setMessageParameters(exception.getMessageParameters());

     for (final ErrorMessageException nestedError : exception.getNestedErrors())
     {
         final ErrorMessage nestedErrorMessage = createErrorMessage(nestedError, locale);
         errorMessage.addNestedError(nestedErrorMessage);
     }

     return errorMessage;
 }

 public static final ErrorMessage createErrorMessageFromThrowable(final Throwable exception)
 {
     final ErrorMessage errorMessage = new ErrorMessage();
     errorMessage.setMessage(exception.getLocalizedMessage());
     errorMessage.setRecommendedActions(new String[0]);
     return errorMessage;
 }

 public static final ErrorMessage createErrorMessage(String resourceBundle, String messageKey, String recommendedActionsKey, Locale locale)
 {
     final ErrorMessage errorMessage = new ErrorMessage();
     errorMessage.setMessage(getMessage(resourceBundle, messageKey, null, locale));
     errorMessage.setRecommendedActions(new String[] {getMessage(resourceBundle, recommendedActionsKey, null, locale)});
     return errorMessage;
 }
 public static final ErrorMessage createErrorMessageFromClient(final HttpStatusCodeException exception)
 {
     try
     {
         return (ObjectMapperFacade.readValue(exception.getResponseBodyAsString(), ErrorMessage.class));
     }
     catch (final Exception e)
     {
     }
     return createErrorMessageFromThrowable(exception);
 }

 public static final String getMessage(final String resourceBundle, final String code, final Object[] args, final Locale locale)
 {
     if (resourceBundle == null)
     {
         return "";
     }
     final L10nMessageCatalog catalog = new L10nMessageCatalog(resourceBundle);
     return getMessage(catalog, code, args, locale);

 }

 /**
  * Returns error message
  *
  * @param catalog
  * @param code
  * @param args
  * @param locale
  * @return error message
  */
 public static final String getMessage(
         final L10nMessageCatalog catalog,
         final String code,
         final Object[] args,
         final Locale locale)
 {
     if (catalog == null || code == null)
     {
         return "";
     }
     return catalog.getMessage(code, args, locale);
 }
}