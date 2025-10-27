// 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

// 子数组是数组中的一个连续部分。

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let cur = nums[0];
    let max = nums[0];
    for(let i=1;i<nums.length;i++){
        cur = Math.max(nums[i],nums[i]+cur);
        max = Math.max(max,cur)
    }
    return max;
};

nums = [-2,1,-3,4,-1,2,1,-5,4]
console.log(maxSubArray(nums))