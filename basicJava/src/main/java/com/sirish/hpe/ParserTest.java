package com.sirish.hpe;

public class ParserTest {
	
	Multimap<String, Collection<String>> parse(final String uefiDevicePath)
    {

        final Multimap<String, Collection<String>> parsedUefiDevicePath = ArrayListMultimap.create();

        final Pattern pattern = Pattern.compile("(\\w+)\\((.*?)\\)");
        // TODO need to add support for local storage efi path, which does not
        // follow the normal Key(value) format

        final Matcher matcher = pattern.matcher(uefiDevicePath);
        while (matcher.find())
        {
            final String key = matcher.group(1);
            final String val = matcher.group(2);

            final Collection<String> valueCollection = new ArrayList<String>();
            if (val.contains(","))
            {
                final String[] values = val.split(",");
                for (final String currentValue : values)
                {
                    if (currentValue != null)
                    {
                        valueCollection.add(currentValue);
                    }
                }
            }
            else if (!val.isEmpty())
            {
                valueCollection.add(val);
            }
            if (!valueCollection.isEmpty())
            {
                parsedUefiDevicePath.put(key, valueCollection);
            }

        }
        return parsedUefiDevicePath;
    }

}
