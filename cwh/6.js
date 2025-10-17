// 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
// 请注意 ，必须在不复制数组的情况下原地对数组进行操作。

// 示例 1:
// 输入: nums = [0,1,0,3,12]
// 输出: [1,3,12,0,0]

// 示例 2:
// 输入: nums = [0]
// 输出: [0]

var moveZeroes = function(nums) {
    let n=0;

    for(let i=0;i<nums.length;i++){
        if(nums[i]!==0){
            nums[n]=nums[i]
            n++;
        }
    }

    for(let i=n;i<nums.length;i++){
        nums[i]=0;
    }

    return nums;
};

console.log(moveZeroes([0,1,0,3,12]))