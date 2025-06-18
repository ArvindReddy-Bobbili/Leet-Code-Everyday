/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if(t.length != s.length)
    {
        return false;
    }
    const count = new Map();
    for(let i=0; i<t.length; i++)
        {
            const c1 = s[i]
            const c2 = t[i]
            count.set(c1, (count.get(c1) || 0) + 1);
            count.set(c2, (count.get(c2) || 0) - 1);
        }
    for (const v of count.values()) {
        if (v !== 0) return false;
    }
    // now that every count was zero:
    return true;
    
    
    };