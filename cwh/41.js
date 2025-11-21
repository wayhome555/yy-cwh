// 给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地 对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

// 我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

// 必须在不使用库内置的 sort 函数的情况下解决这个问题。

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    return nums.sort((a,b) => a-b)
};

[2,0,1] [2,0,1] [0,1,1] 
var sortColors = function(nums) {
    let p0 = 0, p1 = 0;// 1 1 
    for (let i = 0; i < nums.length; i++) {
        const x = nums[i]; //0
        nums[i] = 2;
        if (x <= 1) {
            nums[p1++] = 1;
        }
        if (x === 0) {
            nums[p0++] = 0;
        }
    }
};


(nums) => {
    let p0 = 0,p1 = 0;

    for(let i=0;i<nums.length;i++){
        let x = nums[i];
        nums[i] = 2;
        if(x<=1){
            nums[p1++] = 1;
        }
        if(x===0){
            nums[p0++] = 0;
        }
    }
}