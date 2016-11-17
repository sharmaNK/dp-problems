public class ArraySpiral {
	public static void main(String[] args) {
		int[][] mn = {
			{1, 2, 3},
			{4, 5, 6},
			{7, 8, 9},
			{10, 11, 12}
		};

		int m = mn.length;
		int n = mn[0].length;

		for(int i=0; i<m; i++) {
			for(int j=0; j<n; j++) {
				System.out.print(mn[i][j]+ " ");
			}
			i++;
			if(i < m) {
				for(int j=0; j<n; j++) {
					System.out.print(mn[i][n-j-1] + " ");
				}
			}
		}
	}
}
