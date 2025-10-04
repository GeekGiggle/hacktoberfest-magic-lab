/**
 * SpellMap: find best matching key from known list for a given typo/variant.
 * Very small fuzzy logic: normalized tokens + Levenshtein distance.
 */
function normalize(s){
  return String(s).trim().toLowerCase().replace(/[^a-z0-9]/g,'');
}
function levenshtein(a,b){
  if(!a) return b.length;
  if(!b) return a.length;
  const row = Array(b.length+1).fill(0).map((_,i)=>i);
  for(let i=1;i<=a.length;i++){
    let prev = i;
    for(let j=1;j<=b.length;j++){
      const cur = Math.min(
        row[j]+1,
        prev+1,
        row[j-1] + (a[i-1]===b[j-1]?0:1)
      );
      row[j-1] = prev;
      prev = cur;
      if(j===b.length) row[j]=prev;
    }
  }
  return row[b.length];
}
function bestMatch(input, candidates){
  const n = normalize(input);
  let best = {cand:null, score: Infinity};
  for(const c of candidates){
    const s = levenshtein(n, normalize(c));
    if(s < best.score){ best = {cand:c, score:s}; }
  }
  return best;
}

module.exports = {bestMatch, levenshtein, normalize};
