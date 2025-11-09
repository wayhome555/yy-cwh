// 给你一个满足下述两条属性的 m x n 整数矩阵：

// 每行中的整数从左到右按非严格递增顺序排列。
// 每行的第一个整数大于前一行的最后一个整数。
// 给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。

/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    let flat = matrix.flat(Infinity);

    let right = flat.length - 1;
    let left = 0;

    while(left <= right){
        let mid = left + Math.floor((right-left)/2);

        if(flat[mid] === target) return true;
        else if(flat[mid] > target){
            right = mid -1;
        }else{
            left = mid +1;
        }
    }

    return false;
};

