// 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

// 示例 1：
// 输入：nums = [1,2,3]
// 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

// 示例 2：
// 输入：nums = [0,1]
// 输出：[[0,1],[1,0]]

// 示例 3：
// 输入：nums = [1]
// 输出：[[1]]

function permuteUnique(nums) {
    const result = [];
    const len = nums.length;
    if (len === 0) return result;

    // 排序是去重的前提（让重复元素相邻）
    nums.sort((a, b) => a - b);
    const used = new Array(len).fill(false); // 标记元素是否已使用

    // 回溯函数：当前路径 path
    const backtrack = (path) => {
        // 终止条件：路径长度等于数组长度，找到一个完整排列
        if (path.length === len) {
            result.push([...path]); // 拷贝路径（避免引用问题）
            return;
        }

        for (let i = 0; i < len; i++) {
            // 跳过已使用的元素
            if (used[i]) continue;

            // 去重核心：若当前元素与前一个相同，且前一个未被使用，则跳过
            // 原因：前一个相同元素未被使用，说明它会在之后被选择，导致重复排列
            if (i > 0 && nums[i] === nums[i - 1] && !used[i - 1]) {
                continue;
            }

            // 选择当前元素
            path.push(nums[i]);
            used[i] = true;

            // 递归构建下一层路径
            backtrack(path);

            // 回溯：撤销选择（恢复状态）
            path.pop();
            used[i] = false;
        }
    };

    backtrack([]);
    return result;
}

function a(nums){
    let result = [];
    let len = nums.length;

    if(len === 0) return result;

    nums.sort((a,b)=>a-b);
    let used = Array(len).fill(false)

    const backtrack = function(path){
        if(path.length === len){
            result.push([...path])
            return
        }

        for(let i=0;i<len;i++){
            if(used[i]) continue;
            if(i>0 && nums[i]===nums[i-1] && !used[i-1]) continue;

            path.push(nums[i])
            used[i] = true

            backtrack(path)

            path.pop()
            used[i] = false
        }
    }

    backtrack([])
    return result
}

console.log(a([1,1,3]))