/**
 Do not return anything, modify matrix in-place instead.
 */
function setZeroes(matrix: number[][]): void {
    for (let row=0; row < matrix.length; row++) {
        for (let col=0; col < matrix[0].length; col++) {
            if (matrix[row][col] == 0) continue

            // Same col
            for (let row2=0; row2 < matrix.length; row2++) {
                if (matrix[row2][col] == 0) {
                    matrix[row][col] = Infinity
                    break;
                }
            }

            if (matrix[row][col] == 0) continue;

            // Same row
            for (let col2=0; col2 < matrix[0].length; col2++) {
                if (matrix[row][col2] == 0) {
                    matrix[row][col] = Infinity
                    break;
                }
            }
        }
    }

    for (let row=0; row < matrix.length; row++) {
        for (let col=0; col < matrix[0].length; col++) {
            if (matrix[row][col] == Infinity) {
                matrix[row][col] = 0;
            }
        }
    }
};