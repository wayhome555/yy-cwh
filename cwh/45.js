/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const map = new Map();

    for(let str of strs){
        let key = str.split('').sort().join('');

        if(!map.has(key)){
            map.set(key,[str]);
        }else{
            map.get(key).push(str);
        }
    }

    return [...map.values()]
};