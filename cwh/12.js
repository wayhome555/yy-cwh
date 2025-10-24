// 给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。


var setZeroes = function(matrix) {
    let m = [];
    let n = [];

    for(let i=0;i<matrix.length;i++){
        for(let j=0;j<matrix[i].length;j++){
            if(matrix[i][j] === 0){
                m.push(i);
                n.push(j);
            }
        }
    }

    console.log(m,n)

    for(let i=0;i<matrix.length;i++){
        for(let j=0;j<matrix[i].length;j++){
            if(m.includes(i) || n.includes(j)){
                matrix[i][j] = 0;
            }
        }
    }
    
};

let matrix = [[1,1,1],[1,0,1],[1,1,1]];

console.log(setZeroes(matrix))