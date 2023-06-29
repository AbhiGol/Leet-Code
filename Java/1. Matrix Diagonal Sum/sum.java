
public class sum {
    public static void main(String[] args) {
        int[][] matrix = {
                { 1, 2, 3 },
                { 4, 5, 6 },
                { 7, 8, 9 }
        };

        int diagonalSum = calculateDiagonalSum(matrix);
        System.out.println("Diagonal sum: " + diagonalSum);
    }

    public static int calculateDiagonalSum(int[][] matrix) {
        int sum = 0;
        int rows = matrix.length;
        int cols = matrix[0].length;

        if (rows != cols) {
            System.out.println("The matrix is not square.");
            return 0;
        }

        for (int i = 0; i < rows; i++) {
            sum += matrix[i][i];
        }

        return sum;
    }
}
