// 给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。

// 示例 1:
// 输入: s = "abcabcbb"
// 输出: 3 
// 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。注意 "bca" 和 "cab" 也是正确答案。

// 示例 2:
// 输入: s = "bbbbb"
// 输出: 1
// 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

// 示例 3:
// 输入: s = "pwwkew"
// 输出: 3
// 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。

// 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

// var lengthOfLongestSubstring = function(s) {
//     let start = 0;
//     let max = 0;
//     let hash = new Set();

//     for(let i=0;i<s.length;i++){

//         while(hash.has(s[i])){
//             hash.delete(s[start])
//             start++
//         }

//         hash.add(s[i])

//         max = Math.max(max,i-start+1)

//     }
    
//     return max;
// };

//abcabcbb abc

function longestSubstringWithoutRepeating(s) {
    let start = 0; // 当前窗口的起始索引
    let max = 0; // 最长子串的长度
    let hash = new Set(); // 存储当前窗口的字符
    let maxStart = 0; // 最长子串的起始索引
    let maxEnd = 0; // 最长子串的结束索引

    for (let i = 0; i < s.length; i++) {
        // 若当前字符在窗口中，移动左指针直到移除重复字符
        while (hash.has(s[i])) {
            hash.delete(s[start]);
            start++;
        }
        // 将当前字符加入窗口
        hash.add(s[i]);

        // 计算当前窗口长度，若更长则更新最长子串的边界
        const currentLen = i - start + 1;
        if (currentLen > max) {
            max = currentLen;
            maxStart = start; // 更新最长子串的起始索引
            maxEnd = i; // 更新最长子串的结束索引（当前右指针位置）
        }
    }

    // 根据最长子串的边界截取结果（substring 左闭右开，所以 end+1）
    return s.substring(maxStart, maxEnd + 1);
}

console.log(longestSubstringWithoutRepeating('pwwkew'))


function a(s){
    let start = 0;
    let max = 0;
    let hash = new Set();

    for(let i=0;i<s.length;i++){

        while(hash.has(s[i])){
            hash.delete(s[start])
            start++
        }

        hash.add(s[i])

        max = Math.max(max,i-start+1)
    }
    return max;
}

console.log(a('pwwkew'))


function b(s){
    let start = 0;
    let max = 0;
    let hash = new Set();
    let maxStart = 0;
    let maxEnd = 0;

    for(let i=0;i<s.length;i++){

        while(hash.has(s[i])){
            hash.delete(s[start])
            start++;
        }

        hash.add(s[i])

        let current = i - start + 1;

        if(current>max){
            max = current
            maxStart = start
            maxEnd = i
        }
    }

    return s.substring(maxStart,maxEnd+1)
}

console.log(b('pwwkew'))