/**
* Problem: If (x1, y1) represent bottom left corner and (x2, y2) represent the top right corner of a
* Rectangle. We are given the list of rectangles. Determine the maximum number of intersecting rectangles.
* Two rectangles are called to be intersecting when any point of rectangle r1 lies in rectangle r2 or
* vice-versa.
**/


import java.lang.Math;
import java.util.*;


class Point{
	int x;
	int y;
	Point(int x, int y) {
		this.x = x;
		this.y = y;
	}
}

class Rectange{
	Point p1;
	Point p2;
	Rectange(Point p1, Point p2) {
		this.p1 = p1;
		this.p2 = p2;
	}

	Rectange(int x1, int y1, int x2, int y2) {
		this.p1 = new Point(x1, y1);
		this.p2 = new Point(x2, y2);
	}
	/**
	* Determine if a point is in the Rectangle
	**/
	boolean contains_point(Point p) {
		return (p.x >= this.p1.x && p.x <= this.p2.x) && (p.y >= this.p1.y && p.y <= this.p2.y);
	}
}

public class IntersectingRectangles {
	public static void main(String[] args) {
		// {x1, y1, x2, y2}
		Rectange[] rectangles = {
			new Rectange(0,0,2,2),
			new Rectange(1,1,4,5),
			new Rectange(6,6,8,8),
			new Rectange(7,7,12,13),
			new Rectange(9,9,14,15)
		};

		int[][] cr = rectanges_to_adjacency_matrix(rectangles);

		int max = max_connected_size(cr);
		System.out.println(max);
	}

	/**
	* This method creates a adjacency matrix for given rectangles.
	* If r1 and r4 are intersecting then matrix[1][4] is 1
	* If r1 and r4 are not intersecting then matrix[1][4] is 0
	* This matrix is representing a connected GRAPH where is matrix[1][4] is 1
	* means there is an edge from Node 1 to Node 4
	**/
	public static int[][] rectanges_to_adjacency_matrix(Rectange[] rectangles) {
		int total_rectangles = rectangles.length;
		int[][] matrix = new int[total_rectangles][total_rectangles];

		for(int i=0; i<total_rectangles; i++) {
			for(int j=0; j<total_rectangles; j++){
				if(i==j)
					matrix[i][j] = 0;
				else{
					boolean is_intersected = is_intersecting(rectangles[i], rectangles[j]);
					matrix[i][j] = is_intersected ? 1 : 0;
				}
			}
		}
		return matrix;
	}

	/**
	* Returns true if Rectangle r2 is intersecting with rectangle r1
	* Else returns false
	**/
	public static boolean is_intersecting(Rectange r1, Rectange r2) {
		return r1.contains_point(r2.p1) || r1.contains_point(r2.p2);
	}

	/**
	* This method determines the maximum connected graph for given adjacency matrix.
	**/
	public static int max_connected_size(int[][] mn) {
		int M = mn.length;
		int N = mn[0].length;

		int max = 0;
		for(int i=0; i<M; i++) {
			for(int j=0; j<N; j++) {
				if(mn[i][j] == 1) {
					int count = connected_size(mn, M, N, i, j);
					max = Math.max(count, max);
				}
			}
		}
		return max+1;
	}

	/**
	* This method determines the size of connected graph where starting node is (i,j).
	* This can also be done by using DFS.
	**/
	public static int connected_size(int[][] mn, int M, int N, int i, int j) {
		if(i<0 || i == M || j<0 || j == N || mn[i][j] < 1)
			return 0;

		mn[i][j] = -1;

		int count = 1;
		for(int k=0; k<M; k++) {
			count += connected_size(mn, M, N, k, j) ;
		}
		for(int k=0; k<N; k++) {
			count += connected_size(mn, M, N, i, k) ;
		}
		return count;
	}
}