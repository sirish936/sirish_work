package com.sirish.collections;

import java.util.Comparator;

public class ActionsComparator implements Comparator<PreDefinedActionsEnum>
{
    /*
     * @see java.util.Comparator#compare(java.lang.Object, java.lang.Object)
     */
    @Override
    public int compare(final PreDefinedActionsEnum o1, final PreDefinedActionsEnum o2)
    {
        // TODO Auto-generated method stub
    	      int returnValue = 0;
    	      if (o1.getIndex() > o2.getIndex()) {
    	          returnValue = 1;
    	      } else if (o1.getIndex() < o2.getIndex()) {
    	          returnValue = -1;
    	      }
    	      return returnValue;
    	  }
    }


