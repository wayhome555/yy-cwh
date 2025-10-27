// 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

// 示例 1：
// 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
// 输出：[[1,6],[8,10],[15,18]]
// 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

// 示例 2：
// 输入：intervals = [[1,4],[4,5]]
// 输出：[[1,5]]
// 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。

// 示例 3：
// 输入：intervals = [[4,7],[1,4]]
// 输出：[[1,7]]
// 解释：区间 [1,4] 和 [4,7] 可被视为重叠区间。

function a(intervals){
    if(!intervals) return [];

    intervals.sort((a,b)=>{return a[0]-b[0]})

    let merged = [intervals[0]];

    for(let i=1;i<intervals.length;i++){
        let cur = intervals[i];
        let curMerged = merged[merged.length-1];

        if(cur[0] <= curMerged[1]){
            curMerged[1] = Math.max(curMerged[1],cur[1])
        }else{
            merged.push(cur)
        }
    }

    return merged;
} 

let intervals = [[1,3],[2,6],[8,10],[15,18]];

console.log(a(intervals))