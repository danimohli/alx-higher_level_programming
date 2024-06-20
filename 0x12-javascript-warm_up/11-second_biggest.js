#!/usr/bin/node

const argv = process.argv.slice(2);

const nums = argv.map(arg => parseInt(arg, 10));

function findSecondBiggest (nums) {
  if (nums.length <= 1) {
    return 0;
  }
  const uniqueNums = [...new Set(nums)].sort((a, b) => b - a);
  return uniqueNums.length > 1 ? uniqueNums[1] : 0;
}
console.log(findSecondBiggest(nums));
