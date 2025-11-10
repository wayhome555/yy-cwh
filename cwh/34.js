// 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

// 如果数组中不存在目标值 target，返回 [-1, -1]。

// 你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    const first = (target)=>{
        let left = 0;
        let right = nums.length - 1;
        let res = -1;
        
        while(left <= right){
            let mid = left + Math.floor((right-left)/2);
            if(nums[mid] === target){
                res = mid;
                right = mid -1;
            }else if(nums[mid] > target){
                right = mid -1;
            }else{
                left = mid +1;
            }
        }
        return res;
    }

    const last = (target)=>{
        let left = 0;
        let right = nums.length -1;
        let res = -1;

        while(left <= right){
            let mid = left + Math.floor((right-left)/2);
            if(nums[mid] === target){
                res = mid;
                left = mid +1;
            }else if(nums[mid] > target){
                right = mid -1;
            }else{
                left = mid +1;
            }
        }
        return res;
    }

    if(first(target) === -1){
        return [-1,-1]
    }
    else return [first(target),last(target)]

};

console.log(searchRange([5,7,7,8,8,10],8))