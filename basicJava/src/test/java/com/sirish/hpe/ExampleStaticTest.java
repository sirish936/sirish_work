package com.sirish.hpe;

import static org.mockito.Mockito.mock;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.BlockJUnit4ClassRunner;
import org.mockito.MockedStatic;
import org.mockito.Mockito;
import org.work.ToDoService;

@RunWith(BlockJUnit4ClassRunner.class)
public class ExampleStaticTest {

	@Test
	public void testStatic()
	{
		try {
			ToDoService doService = Mockito.mock(ToDoService.class);
			MockedStatic<ExampleStatic> mockedStatic = Mockito.mockStatic(ExampleStatic.class);
			Mockito.when(ExampleStatic.test()).thenReturn(2);
			System.out.println("Result: " + ExampleStatic.test());
		}
		catch(Exception e) {
			
		}
	}
	
}
