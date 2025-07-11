package com.sirish.core;

import java.util.ArrayList;
import java.util.List;

public class LargestSumCycle {

	private static int[] edges;
	private static boolean[] visited;
	private static int[] nodeValues;
	private static int largestSumCycle;

	public static int findLargestSumCycle(int[] edgeArray) {
		edges = edgeArray;
		int numCells = edges.length;

        visited = new boolean[numCells];
        nodeValues = new int[numCells];
        largestSumCycle = -1;

        for (int i = 0; i < numCells; i++) {
        	if (!visited[i]) {
        		dfs(i, new ArrayList<>());
        	}
        }
        return largestSumCycle;
}

	private static void dfs(int start, List<Integer> path) {
		visited[start] = true;
		path.add(start);

		int next = edges[start];
		if (next != -1) {
			if (!visited[next]) {
				dfs(next, path);
			} else {
				// Cycle found
				int cycleSum = calculateCycleSum(path, next);
				largestSumCycle = Math.max(largestSumCycle, cycleSum);
			}
		}
		
		path.remove(path.size()-1);
}

	private static int calculateCycleSum(List<Integer> path, int next) {
		int cycleSum = 0;
		boolean cycleStarted = false;
		for (int node : path) {
			if (!cycleStarted) {
				if (node == next) {
					cycleStarted = true;
					cycleSum += node;
				}
			} else {
				cycleSum += node;
			}
		}
		return cycleSum;
}

	public static void main(String[] args) {
		int[] edgeArray = {4, 4, 14, 13, 8, 88, 0, 8, 149, 15, 11, -1, 10, 15, 22, 22, 22, 22, 22, 21};
		int largestSum = findLargestSumCycle(edgeArray);
		System.out.println(largestSum);
}
}
