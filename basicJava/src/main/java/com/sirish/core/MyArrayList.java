package com.sirish.core;

import java.util.Arrays;

public class MyArrayList {

	public Object[] myArray;
	int arraySize = 0;

	public MyArrayList() {
		myArray = new Object[10];
	}

	void add(final Object obj) {

		if (myArray.length - arraySize <= 2) {
			myArray = Arrays.copyOf(myArray, myArray.length * 2);// dynamically increasing My ArrayList size
		}
		myArray[arraySize++] = obj;
	}

	public Object get(final int index) {

		if (index < arraySize) {
			return myArray[index];
		} else {
			throw new ArrayIndexOutOfBoundsException();
		}
	}

	void remove(final int index) {

		if (index < arraySize) {

			int tmp = index;
			myArray[index] = null;

			while (tmp < arraySize) {
				myArray[tmp] = myArray[tmp + 1];
				myArray[tmp + 1] = null;
				tmp++;
			}
			arraySize--;
		} else {
			throw new ArrayIndexOutOfBoundsException();
		}
	}

	public int size() {
		return arraySize;
	}

	public static void main(final String[] args) {

		final MyArrayList myArrayList = new MyArrayList();

		// adding elements to Array
		myArrayList.add(1);
		myArrayList.add(2);
		myArrayList.add(3);
		myArrayList.add(4);
		myArrayList.add(5);

		// retrieving element from Array
		System.out.println(" Element at Index:" + myArrayList.get(2));

		// removing element from Array
		myArrayList.remove(2);

		// getting size of Array
		System.out.println(" My ArraySize:" + myArrayList.size());

	}
}
