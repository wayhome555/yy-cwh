// 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    if(!matrix.length) return [];

    let res = [];
    let [t,b,l,r] = [0,matrix.length-1,0,matrix[0].length-1]
    while(t <= b && l <= r){
        for(let i=l;i<=r;i++) res.push(matrix[t][i]);
        t++;
        for(let i=t;i<=b;i++) res.push(matrix[i][r]);
        r--;

        if(t <= b) for(let i=r;i>=l;i--) res.push(matrix[b][i]);
        b--;
        if(l <= r) for(let i=b;i>=t;i--) res.push(matrix[i][l]);
        l++;
    }
    return res;
};

let matrix = [[1,2,3],[4,5,6],[7,8,9]]

console.log(spiralOrder(matrix))