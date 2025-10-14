// 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

// 示例 1:
// 输入: s = "cbaebabacd", p = "abc"
// 输出: [0,6]
// 解释:
// 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
// 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。

//  示例 2:
// 输入: s = "abab", p = "ab"
// 输出: [0,1,2]
// 解释:
// 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
// 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
// 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。

var  findAnagrams = function(s, p) {
    const result = [];
    const sLen = s.length;
    const pLen = p.length;

    // 边界条件：若s比p短，直接返回空
    if (sLen < pLen) return result;

    // 计数数组：记录26个小写字母的频次差异
    const count = new Array(26).fill(0);

    // 1. 初始化计数：统计p的频次（+1）和s前pLen个字符的频次（-1）
    for (let i = 0; i < pLen; i++) {
        count[p.charCodeAt(i) - 97]++; // 'a'.charCodeAt(0) 是 97
        count[s.charCodeAt(i) - 97]--;
    }

    // 2. 检查初始窗口是否匹配（所有计数为0则是异位词）
    if (count.every(v => v === 0)) {
        result.push(0);
    }

    // 3. 滑动窗口：每次移动一位，更新计数并检查
    for (let i = 0; i < sLen - pLen; i++) {
        // 移除窗口左侧的字符（s[i]）
        const left = s.charCodeAt(i) - 97;
        count[left]++; // 左侧字符离开，计数+1（恢复p的计数影响）

        // 加入窗口右侧的新字符（s[i + pLen]）
        const right = s.charCodeAt(i + pLen) - 97;
        count[right]--; // 右侧字符进入，计数-1（抵消p的计数）

        // 检查当前窗口是否匹配
        if (count.every(v => v === 0)) {
            result.push(i + 1); // 起始索引为i+1
        }
    }

    return result;
}

function a(s,p){
    let result = [];
    let sLen = s.length;
    let pLen = p.length;

    if(pLen>sLen) return result;

    let arr =new Array(26).fill(0);

    for(let i=0;i<pLen;i++){
        arr[p.charCodeAt(i)-97]++;
        arr[s.charCodeAt(i)-97]--;
    }

    if(arr.every((item)=>(item===0))){
        result.push(0);
    }

    for(let i=0;i<sLen-pLen;i++){
        arr[s.charCodeAt(i)-97]++;
        arr[s.charCodeAt(i+pLen)-97]--;

        if(arr.every((item)=>(item===0))){
            result.push(i+1);
        }
    }
    return result
}

console.log(a("cbaebabacd","abc"))