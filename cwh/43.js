// 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。

// 在「杨辉三角」中，每个数是它左上方和右上方的数的和。

// 示例 1:

// 输入: numRows = 5
// 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
// 示例 2:

// 输入: numRows = 1
// 输出: [[1]]
 

/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
    if(numRows === 0) return [];

    const dp = new Array(numRows);
    dp[0] = [1];

    for(let i = 1;i<numRows;i++){
        dp[i] = new Array(i+1);

        dp[i][0] = 1;
        dp[i][i] = 1;

        for(let j=1;j<i;j++){
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        }
    }

    return dp;
};

console.log(generate(5))