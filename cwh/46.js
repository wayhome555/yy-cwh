/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    if (nums.length === 0) return 0;

    let a = [...new Set(nums)].sort((a,b) => a-b);
    let b = 1;
    let c = 1;

    console.log(a.length)

    for(let i=1;i<a.length;i++){
        
        if(a[i] == a[i-1]+1){
            b++;
        }
        else{
            c = Math.max(c,b);
            b=1;
        }
    }

    c = Math.max(c, b);
    return c;
};