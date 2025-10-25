// 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

// 每行的元素从左到右升序排列。
// 每列的元素从上到下升序排列。

function searchMatrix(matrix, target) {
    if (matrix.length === 0) return false; // 空矩阵直接返回false
    const m = matrix.length; // 行数
    const n = matrix[0].length; // 列数
    
    let row = 0; // 从第一行开始
    let col = n - 1; // 从最后一列（右上角）开始
    
    while (row < m && col >= 0) {
        const current = matrix[row][col];
        if (current === target) {
            return true; // 找到目标
        } else if (current > target) {
            col--; // 目标更小，左移一列
        } else {
            row++; // 目标更大，下移一行
        }
    }
    
    return false; // 遍历完未找到
}

function a(matrix,target){
    if(matrix.length === 0) return false;
    let m = matrix.length;
    let n = matrix[0].length;

    let row = 0;
    let col = n - 1;

    while(row < m && col >= 0){
        let current = matrix[row][col];
        if(current == target){
            return true;
        }else if(current > target){
            col--;
        }else{
            row++;
        }
    }
    return false;
}

let matrix = [[1,2,3],[4,5,6],[7,8,9]];
let target = 5
console.log(a(matrix,target))