// 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
// 题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
// 请 不要使用除法，且在 O(n) 时间复杂度内完成此题。

// 示例 1:
// 输入: nums = [1,2,3,4]
// 输出: [24,12,8,6]

// 示例 2:
// 输入: nums = [-1,1,0,-3,3]
// 输出: [0,0,9,0,0]

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    let cop = [];
    let sum = 1;
    for(let i=0;i<nums.length;i++){
        for(let j=0;j<nums.length;j++){
            if(j!=i){
                sum = sum*nums[j]
            }
        }
        cop[i] = sum;
        sum = 1;
    }
    return cop;
};

var a = function(nums) {
    let res = [];

    res[0] = 1;
    for(let i=1;i<nums.length;i++){
        res[i] = res[i-1] * nums[i-1]
    }

    rig = 1;
    for(let i=nums.length-1;i>=0;i--){
        res[i] = res[i]*rig;
        rig = rig*nums[i]
    }

    return res
};
nums = [1,2,3,4]
console.log(productExceptSelf(nums))