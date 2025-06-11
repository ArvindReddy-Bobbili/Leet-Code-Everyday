/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  const seen = new Set();
  for (const f of nums) {
    if (seen.has(f)) {
      return true;
    } else {
      seen.add(f);
    }
  }
  return false;
};
