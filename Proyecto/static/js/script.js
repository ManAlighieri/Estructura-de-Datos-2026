console.log("Plataforma de Estructuras de Datos iniciada correctamente");

const autoTimers = {};
const NS = 'http://www.w3.org/2000/svg';

/* ═══════════════════════════════════════════════
   SORTING — generador de pasos reales
═══════════════════════════════════════════════ */
const DEFAULT_ARR = [38, 27, 43, 3, 9, 82, 10, 56];

function bubbleGen(input) {
  const a = [...input], steps = [];
  const n = a.length;
  for (let i = 0; i < n - 1; i++) {
    for (let j = 0; j < n - i - 1; j++) {
      steps.push({ arr: [...a], hi: { [j]: 'cmp', [j+1]: 'cmp' }, log: `Comparando <b>${a[j]}</b> y <b>${a[j+1]}</b>` });
      if (a[j] > a[j+1]) {
        [a[j], a[j+1]] = [a[j+1], a[j]];
        steps.push({ arr: [...a], hi: { [j]: 'swap', [j+1]: 'swap' }, log: `Intercambiando → <b>${a[j]}</b> y <b>${a[j+1]}</b>` });
      }
    }
  }
  steps.push({ arr: [...a], hi: {}, log: '<b style="color:#3fb950">✔ Ordenado</b>', done: true });
  return steps;
}

function selectionGen(input) {
  const a = [...input], steps = [];
  const n = a.length;
  for (let i = 0; i < n - 1; i++) {
    let min = i;
    for (let j = i + 1; j < n; j++) {
      steps.push({ arr: [...a], hi: { [i]: 'sorted', [j]: 'cmp', [min]: 'swap' }, log: `Buscando mínimo: <b>${a[j]}</b> vs actual <b>${a[min]}</b>` });
      if (a[j] < a[min]) min = j;
    }
    if (min !== i) {
      [a[i], a[min]] = [a[min], a[i]];
      steps.push({ arr: [...a], hi: { [i]: 'swap', [min]: 'swap' }, log: `Colocando <b>${a[i]}</b> en posición ${i}` });
    }
  }
  steps.push({ arr: [...a], hi: {}, log: '<b style="color:#3fb950">✔ Ordenado</b>', done: true });
  return steps;
}

function insertionGen(input) {
  const a = [...input], steps = [];
  for (let i = 1; i < a.length; i++) {
    let j = i;
    while (j > 0 && a[j-1] > a[j]) {
      steps.push({ arr: [...a], hi: { [j]: 'cmp', [j-1]: 'cmp' }, log: `Insertando <b>${a[j]}</b>: <b>${a[j-1]}</b> > <b>${a[j]}</b>, desplazando` });
      [a[j], a[j-1]] = [a[j-1], a[j]];
      j--;
    }
    steps.push({ arr: [...a], hi: { [j]: 'sorted' }, log: `<b>${a[j]}</b> insertado en posición ${j}` });
  }
  steps.push({ arr: [...a], hi: {}, log: '<b style="color:#3fb950">✔ Ordenado</b>', done: true });
  return steps;
}

function mergeGen(input) {
  const steps = [];
  function merge(a, l, m, r) {
    const L = a.slice(l, m+1), R = a.slice(m+1, r+1);
    let i = 0, j = 0, k = l;
    while (i < L.length && j < R.length) {
      steps.push({ arr: [...a], hi: { [l+i]: 'cmp', [m+1+j]: 'cmp' }, log: `Comparando <b>${L[i]}</b> y <b>${R[j]}</b>` });
      if (L[i] <= R[j]) a[k++] = L[i++]; else a[k++] = R[j++];
      steps.push({ arr: [...a], hi: { [k-1]: 'swap' }, log: `Colocando <b>${a[k-1]}</b> en posición ${k-1}` });
    }
    while (i < L.length) { a[k++] = L[i++]; }
    while (j < R.length) { a[k++] = R[j++]; }
  }
  function msort(a, l, r) {
    if (l >= r) return;
    const m = Math.floor((l+r)/2);
    steps.push({ arr: [...a], hi: { [l]: 'cmp', [r]: 'cmp' }, log: `Dividiendo subarray [${l}..${r}], mitad en ${m}` });
    msort(a, l, m); msort(a, m+1, r);
    merge(a, l, m, r);
  }
  const a = [...input];
  msort(a, 0, a.length - 1);
  steps.push({ arr: [...a], hi: {}, log: '<b style="color:#3fb950">✔ Ordenado</b>', done: true });
  return steps;
}

function quickGen(input) {
  const steps = [];
  function partition(a, l, r) {
    const pivot = a[r]; let i = l - 1;
    for (let j = l; j < r; j++) {
      steps.push({ arr: [...a], hi: { [j]: 'cmp', [r]: 'swap' }, log: `Comparando <b>${a[j]}</b> con pivote <b>${pivot}</b>` });
      if (a[j] <= pivot) { i++; [a[i], a[j]] = [a[j], a[i]]; }
    }
    [a[i+1], a[r]] = [a[r], a[i+1]];
    steps.push({ arr: [...a], hi: { [i+1]: 'sorted' }, log: `Pivote <b>${pivot}</b> en posición final ${i+1}` });
    return i + 1;
  }
  function qs(a, l, r) {
    if (l >= r) return;
    const p = partition(a, l, r);
    qs(a, l, p-1); qs(a, p+1, r);
  }
  const a = [...input];
  qs(a, 0, a.length - 1);
  steps.push({ arr: [...a], hi: {}, log: '<b style="color:#3fb950">✔ Ordenado</b>', done: true });
  return steps;
}

function countingGen(input) {
  const steps = [];
  const a = [...input];
  const maxV = Math.max(...a);
  const count = new Array(maxV + 1).fill(0);
  steps.push({ arr: [...a], hi: {}, log: `Array original. Máximo = ${maxV}` });
  a.forEach((v, i) => {
    count[v]++;
    steps.push({ arr: [...a], hi: { [i]: 'cmp' }, log: `Contando <b>${v}</b> → count[${v}] = ${count[v]}` });
  });
  for (let i = 1; i <= maxV; i++) count[i] += count[i-1];
  steps.push({ arr: [...a], hi: {}, log: `Acumulando conteos para posiciones finales` });
  const output = new Array(a.length);
  for (let i = a.length - 1; i >= 0; i--) {
    output[count[a[i]] - 1] = a[i];
    count[a[i]]--;
    steps.push({ arr: [...output.map(v => v === undefined ? 0 : v)], hi: { [count[a[i]]]: 'swap' }, log: `Colocando <b>${a[i]}</b> en posición ${count[a[i]]}` });
  }
  steps.push({ arr: [...output], hi: {}, log: '<b style="color:#3fb950">✔ Ordenado</b>', done: true });
  return steps;
}

function rquickGen(input) {
  const steps = [];
  function partition(a, l, r) {
    const ri = l + Math.floor(Math.random() * (r - l + 1));
    [a[ri], a[r]] = [a[r], a[ri]];
    const pivot = a[r]; let i = l - 1;
    steps.push({ arr: [...a], hi: { [r]: 'swap' }, log: `Pivote aleatorio elegido: <b>${pivot}</b>` });
    for (let j = l; j < r; j++) {
      steps.push({ arr: [...a], hi: { [j]: 'cmp', [r]: 'swap' }, log: `Comparando <b>${a[j]}</b> con pivote <b>${pivot}</b>` });
      if (a[j] <= pivot) { i++; [a[i], a[j]] = [a[j], a[i]]; }
    }
    [a[i+1], a[r]] = [a[r], a[i+1]];
    steps.push({ arr: [...a], hi: { [i+1]: 'sorted' }, log: `Pivote <b>${pivot}</b> en posición final ${i+1}` });
    return i + 1;
  }
  function qs(a, l, r) {
    if (l >= r) return;
    const p = partition(a, l, r);
    qs(a, l, p-1); qs(a, p+1, r);
  }
  const a = [...input];
  qs(a, 0, a.length - 1);
  steps.push({ arr: [...a], hi: {}, log: '<b style="color:#3fb950">✔ Ordenado</b>', done: true });
  return steps;
}

/* ═══════════════════════════════════════════════
   BFS — pasos reales con grafo
═══════════════════════════════════════════════ */
const BFS_GRAPH = { A:['B','C'], B:['D','E'], C:['F','G'], D:[], E:[], F:[], G:[] };

function bfsGen() {
  const steps = [];
  const vis = new Set(['A']), q = ['A'], visited = [];
  steps.push({ q: [...q], vis: new Set(vis), cur: null, log: 'Inicio: nodo <b>A</b> en cola' });
  while (q.length) {
    const node = q.shift();
    visited.push(node);
    steps.push({ q: [...q], vis: new Set(vis), cur: node, log: `Visitando <b>${node}</b> — recorrido: [${visited.join(', ')}]` });
    for (const nx of BFS_GRAPH[node]) {
      if (!vis.has(nx)) {
        vis.add(nx); q.push(nx);
        steps.push({ q: [...q], vis: new Set(vis), cur: node, next: nx, log: `Descubriendo <b>${nx}</b> desde <b>${node}</b> → cola: [${q.join(', ')}]` });
      }
    }
  }
  steps.push({ q: [], vis: new Set(vis), cur: null, log: `<b style="color:#3fb950">✔ BFS completo:</b> ${visited.join(' → ')}`, done: true });
  return steps;
}

/* ═══════════════════════════════════════════════
   HANOI — pasos reales
═══════════════════════════════════════════════ */
function hanoiGen(n = 3) {
  const steps = [];
  const torres = { A: [], B: [], C: [] };
  for (let i = n; i >= 1; i--) torres.A.push(i);
  steps.push({ torres: JSON.parse(JSON.stringify(torres)), log: `Inicio: ${n} discos en A` });
  function mover(h, orig, dest, aux) {
    if (h === 0) return;
    mover(h-1, orig, aux, dest);
    const disco = torres[orig].pop();
    torres[dest].push(disco);
    steps.push({ torres: JSON.parse(JSON.stringify(torres)), log: `Mover disco <b>${disco}</b> de <b>${orig}</b> → <b>${dest}</b>` });
    mover(h-1, aux, dest, orig);
  }
  mover(n, 'A', 'C', 'B');
  steps.push({ torres: JSON.parse(JSON.stringify(torres)), log: `<b style="color:#3fb950">✔ Completado en ${Math.pow(2,n)-1} movimientos</b>`, done: true });
  return steps;
}

/* ═══════════════════════════════════════════════
   KRUSKAL — pasos reales
═══════════════════════════════════════════════ */
const KRUSKAL_EDGES = [[1,'A','B'],[2,'A','C'],[3,'B','C'],[4,'B','D'],[5,'C','D'],[6,'C','E'],[7,'D','E']];

function kruskalGen() {
  const steps = [];
  const sorted = [...KRUSKAL_EDGES].sort((a,b) => a[0]-b[0]);
  const parent = {};
  ['A','B','C','D','E'].forEach(n => parent[n] = n);
  function find(x) { return parent[x] === x ? x : find(parent[x]); }
  function union(x, y) { parent[find(x)] = find(y); }
  const mst = [], rejected = [];
  steps.push({ mst: [], rej: [], cur: null, log: `Aristas ordenadas por peso: ${sorted.map(e=>`(${e[1]}-${e[2]}:${e[0]})`).join(', ')}` });
  for (const [w, u, v] of sorted) {
    if (find(u) !== find(v)) {
      union(u, v); mst.push([w,u,v]);
      steps.push({ mst: [...mst], rej: [...rejected], cur: [u,v], log: `Agregar <b>(${u}-${v})</b> peso ${w} → sin ciclo ✔` });
    } else {
      rejected.push([w,u,v]);
      steps.push({ mst: [...mst], rej: [...rejected], cur: [u,v], log: `Rechazar <b>(${u}-${v})</b> peso ${w} → formaría ciclo ✖` });
    }
    if (mst.length === 4) break;
  }
  steps.push({ mst: [...mst], rej: [...rejected], cur: null, log: `<b style="color:#3fb950">✔ AGM completo — costo: ${mst.reduce((s,e)=>s+e[0],0)}</b>`, done: true });
  return steps;
}

/* ═══════════════════════════════════════════════
   PRIM — pasos reales
═══════════════════════════════════════════════ */
const PRIM_GRAPH = { A:[['B',1],['C',4]], B:[['A',1],['C',2],['D',5]], C:[['A',4],['B',2],['D',1]], D:[['B',5],['C',1]] };

function primGen() {
  const steps = [];
  const vis = new Set(['A']), mst = [];
  steps.push({ vis: new Set(vis), mst: [], cur: null, log: 'Inicio desde nodo <b>A</b>' });
  while (vis.size < Object.keys(PRIM_GRAPH).length) {
    let best = null, bw = Infinity, bu = null;
    vis.forEach(u => {
      PRIM_GRAPH[u].forEach(([v, w]) => { if (!vis.has(v) && w < bw) { bw = w; best = v; bu = u; } });
    });
    if (!best) break;
    vis.add(best); mst.push([bu, best, bw]);
    steps.push({ vis: new Set(vis), mst: [...mst], cur: [bu, best], log: `Agregar nodo <b>${best}</b> desde <b>${bu}</b> (peso ${bw})` });
  }
  steps.push({ vis: new Set(vis), mst: [...mst], cur: null, log: `<b style="color:#3fb950">✔ AGM completo — costo: ${mst.reduce((s,e)=>s+e[2],0)}</b>`, done: true });
  return steps;
}

/* ═══════════════════════════════════════════════
   RENDER — barras SVG para sorts
═══════════════════════════════════════════════ */
function barColor(state) {
  if (state === 'cmp')    return '#e3b341';
  if (state === 'swap')   return '#f85149';
  if (state === 'sorted') return '#3fb950';
  return '#58a6ff';
}

function renderBars(containerId, arr, hi) {
  let svg = document.getElementById(containerId + '-svg');
  if (!svg) {
    svg = document.createElementNS(NS, 'svg');
    svg.setAttribute('id', containerId + '-svg');
    svg.setAttribute('width', '100%');
    svg.setAttribute('height', '200');
    svg.style.display = 'block';
    svg.style.overflow = 'visible';
    svg.style.marginBottom = '12px';
    const container = document.getElementById(containerId + '-array');
    if (container) container.parentElement.insertBefore(svg, container);
  }
  const W = svg.parentElement.clientWidth || 600;
  const H = 180;
  svg.setAttribute('height', H + 24);
  svg.innerHTML = '';
  const n = arr.length;
  const bw = Math.floor((W - (n-1)*4) / n);
  const maxV = Math.max(...arr);
  arr.forEach((v, i) => {
    const bh = Math.round((v / maxV) * (H - 10));
    const x = i * (bw + 4);
    const y = H - bh;
    const state = hi && hi[i] ? hi[i] : 'idle';
    const rect = document.createElementNS(NS, 'rect');
    rect.setAttribute('x', x); rect.setAttribute('y', y);
    rect.setAttribute('width', bw); rect.setAttribute('height', bh);
    rect.setAttribute('fill', barColor(state));
    rect.setAttribute('rx', '3');
    svg.appendChild(rect);
    const txt = document.createElementNS(NS, 'text');
    txt.setAttribute('x', x + bw/2); txt.setAttribute('y', H + 16);
    txt.setAttribute('text-anchor', 'middle');
    txt.setAttribute('font-size', '11');
    txt.setAttribute('font-family', 'IBM Plex Mono,monospace');
    txt.setAttribute('fill', '#8b949e');
    txt.textContent = v;
    svg.appendChild(txt);
  });
}

/* ═══════════════════════════════════════════════
   RENDER — BFS con grafo SVG
═══════════════════════════════════════════════ */
const BFS_POS = { A:[300,40], B:[160,130], C:[440,130], D:[80,230], E:[240,230], F:[360,230], G:[520,230] };

function renderBFS(containerId, state) {
  let svg = document.getElementById(containerId + '-svg');
  if (!svg) {
    svg = document.createElementNS(NS, 'svg');
    svg.setAttribute('id', containerId + '-svg');
    svg.setAttribute('width', '100%');
    svg.setAttribute('height', '280');
    svg.style.display = 'block';
    svg.style.overflow = 'visible';
    svg.style.marginBottom = '12px';
    const container = document.getElementById(containerId + '-array');
    if (container) container.parentElement.insertBefore(svg, container);
  }
  svg.innerHTML = '';
  Object.entries(BFS_GRAPH).forEach(([n, nbrs]) => {
    nbrs.forEach(nb => {
      const l = document.createElementNS(NS, 'line');
      l.setAttribute('x1', BFS_POS[n][0]); l.setAttribute('y1', BFS_POS[n][1]);
      l.setAttribute('x2', BFS_POS[nb][0]); l.setAttribute('y2', BFS_POS[nb][1]);
      l.setAttribute('stroke', state && state.next === nb && state.cur === n ? '#58a6ff' : '#30363d');
      l.setAttribute('stroke-width', '2');
      svg.appendChild(l);
    });
  });
  Object.keys(BFS_GRAPH).forEach(n => {
    const [x, y] = BFS_POS[n];
    const g = document.createElementNS(NS, 'g');
    g.setAttribute('transform', `translate(${x},${y})`);
    const c = document.createElementNS(NS, 'circle');
    c.setAttribute('r', '22');
    let fill = '#161b22', stroke = '#444c56';
    if (state) {
      if (state.cur === n)                      { fill = '#1c2e4a'; stroke = '#58a6ff'; }
      else if (state.vis && state.vis.has(n))   { fill = '#0d2016'; stroke = '#3fb950'; }
      if (state.q && state.q.includes(n))       { fill = '#1e1c0a'; stroke = '#e3b341'; }
    }
    c.setAttribute('fill', fill); c.setAttribute('stroke', stroke); c.setAttribute('stroke-width', '2');
    const t = document.createElementNS(NS, 'text');
    t.setAttribute('text-anchor', 'middle'); t.setAttribute('dominant-baseline', 'central');
    t.setAttribute('font-size', '13'); t.setAttribute('font-family', 'IBM Plex Mono,monospace');
    t.setAttribute('fill', state && state.cur === n ? '#58a6ff' : state && state.vis && state.vis.has(n) ? '#3fb950' : '#e6edf3');
    t.setAttribute('font-weight', '500'); t.textContent = n;
    g.appendChild(c); g.appendChild(t);
    svg.appendChild(g);
  });
  const arrDiv = document.getElementById(containerId + '-array');
  if (arrDiv) arrDiv.innerHTML = '';
}

/* ═══════════════════════════════════════════════
   RENDER — Hanoi SVG
═══════════════════════════════════════════════ */
const HANOI_COLORS = ['#f85149','#e3b341','#58a6ff','#3fb950','#bc8cff'];

function renderHanoi(containerId, torres) {
  let svg = document.getElementById(containerId + '-svg');
  if (!svg) {
    svg = document.createElementNS(NS, 'svg');
    svg.setAttribute('id', containerId + '-svg');
    svg.setAttribute('width', '100%');
    svg.setAttribute('height', '220');
    svg.style.display = 'block';
    svg.style.overflow = 'visible';
    svg.style.marginBottom = '12px';
    const container = document.getElementById(containerId + '-array');
    if (container) container.parentElement.insertBefore(svg, container);
  }
  const W = svg.parentElement.clientWidth || 600;
  const H = 200;
  svg.setAttribute('height', H + 10);
  svg.innerHTML = '';
  const postes = { A: W/6, B: W/2, C: W*5/6 };
  Object.entries(postes).forEach(([name, x]) => {
    const r = document.createElementNS(NS, 'rect');
    r.setAttribute('x', x-3); r.setAttribute('y', 30);
    r.setAttribute('width', 6); r.setAttribute('height', 150);
    r.setAttribute('fill', '#30363d'); r.setAttribute('rx', '3');
    svg.appendChild(r);
    const base = document.createElementNS(NS, 'rect');
    base.setAttribute('x', x-50); base.setAttribute('y', 178);
    base.setAttribute('width', 100); base.setAttribute('height', 8);
    base.setAttribute('fill', '#30363d'); base.setAttribute('rx', '3');
    svg.appendChild(base);
    const t = document.createElementNS(NS, 'text');
    t.setAttribute('x', x); t.setAttribute('y', H + 8);
    t.setAttribute('text-anchor', 'middle');
    t.setAttribute('font-size', '13'); t.setAttribute('font-family', 'IBM Plex Mono,monospace');
    t.setAttribute('fill', '#8b949e'); t.textContent = name;
    svg.appendChild(t);
  });
  Object.entries(torres).forEach(([name, stack]) => {
    const x = postes[name];
    stack.forEach((d, i) => {
      const w = 20 + d * 18;
      const bx = x - w/2, by = 178 - (i+1)*22;
      const rect = document.createElementNS(NS, 'rect');
      rect.setAttribute('x', bx); rect.setAttribute('y', by);
      rect.setAttribute('width', w); rect.setAttribute('height', 18);
      rect.setAttribute('fill', HANOI_COLORS[(d-1) % HANOI_COLORS.length]);
      rect.setAttribute('rx', '4');
      svg.appendChild(rect);
      const t = document.createElementNS(NS, 'text');
      t.setAttribute('x', x); t.setAttribute('y', by + 12);
      t.setAttribute('text-anchor', 'middle');
      t.setAttribute('font-size', '11'); t.setAttribute('font-family', 'IBM Plex Mono,monospace');
      t.setAttribute('fill', '#0d1117'); t.textContent = d;
      svg.appendChild(t);
    });
  });
  const arrDiv = document.getElementById(containerId + '-array');
  if (arrDiv) arrDiv.innerHTML = '';
}

/* ═══════════════════════════════════════════════
   RENDER — Kruskal / Prim texto
═══════════════════════════════════════════════ */
function renderGraphText(containerId, state, type) {
  const arrDiv = document.getElementById(containerId + '-array');
  if (!arrDiv) return;
  arrDiv.innerHTML = '';
  if (!state) return;
  if (type === 'kruskal') {
    (state.mst || []).forEach(([w,u,v]) => {
      const el = document.createElement('div');
      el.innerHTML = `<span style="color:#3fb950">(${u}-${v}: ${w})</span>`;
      el.style.padding = '6px 10px';
      arrDiv.appendChild(el);
    });
    (state.rej || []).forEach(([w,u,v]) => {
      const el = document.createElement('div');
      el.innerHTML = `<span style="color:#f85149;text-decoration:line-through">(${u}-${v}: ${w})</span>`;
      el.style.padding = '6px 10px';
      arrDiv.appendChild(el);
    });
  }
  if (type === 'prim') {
    const visEl = document.createElement('div');
    visEl.innerHTML = `<span style="color:#3fb950">V={${[...state.vis].join(',')}}</span>`;
    visEl.style.padding = '6px 10px';
    arrDiv.appendChild(visEl);
    (state.mst || []).forEach(([u,v,w]) => {
      const el = document.createElement('div');
      el.innerHTML = `<span style="color:#58a6ff">(${u}-${v}: ${w})</span>`;
      el.style.padding = '6px 10px';
      arrDiv.appendChild(el);
    });
  }
}

/* ═══════════════════════════════════════════════
   ESTADO GLOBAL de cada algoritmo
═══════════════════════════════════════════════ */
const STATE = {};

function initAlgo(name, steps) {
  STATE[name] = { steps, idx: 0 };
  renderStep(name);
}

function renderStep(name) {
  const s = STATE[name];
  if (!s) return;
  const step = s.steps[s.idx];
  const logDiv = document.getElementById(name + '-log');
  if (logDiv) logDiv.innerHTML = step.log || '';

  if (['bubble','selection','insertion','merge','quick'].includes(name)) {
    renderBars(name, step.arr, step.hi);
    const arrDiv = document.getElementById(name + '-array');
    if (arrDiv) arrDiv.innerHTML = '';
  }
  if (name === 'bfs')     renderBFS(name, step);
  if (name === 'hanoi')   renderHanoi(name, step.torres);
  if (name === 'kruskal') renderGraphText(name, step, 'kruskal');
  if (name === 'prim')    renderGraphText(name, step, 'prim');
}

function algoNext(name) {
  const s = STATE[name]; if (!s) return;
  if (s.idx < s.steps.length - 1) { s.idx++; renderStep(name); }
}
function algoPrev(name) {
  const s = STATE[name]; if (!s) return;
  if (s.idx > 0) { s.idx--; renderStep(name); }
}
function algoReset(name) {
  const s = STATE[name]; if (!s) return;
  stopAuto(name); s.idx = 0; renderStep(name);
}
function autoPlay(name, delay = 700) {
  stopAuto(name);
  autoTimers[name] = setInterval(() => {
    const s = STATE[name]; if (!s) return stopAuto(name);
    if (s.idx >= s.steps.length - 1) return stopAuto(name);
    algoNext(name);
  }, delay);
}
function stopAuto(name) {
  if (autoTimers[name]) { clearInterval(autoTimers[name]); delete autoTimers[name]; }
}

/* ═══════════════════════════════════════════════
   ABB
═══════════════════════════════════════════════ */
let raiz = null;

class Nodo {
  constructor(v) { this.v = v; this.izq = null; this.der = null; this.x = 0; this.y = 0; }
}

function insertar(nodo, v, log) {
  if (!nodo) return new Nodo(v);
  if (v < nodo.v) { log.push(`<b>${v}</b> &lt; <b>${nodo.v}</b> → izquierda`); nodo.izq = insertar(nodo.izq, v, log); }
  else if (v > nodo.v) { log.push(`<b>${v}</b> &gt; <b>${nodo.v}</b> → derecha`); nodo.der = insertar(nodo.der, v, log); }
  else log.push(`<b>${v}</b> ya existe`);
  return nodo;
}

function profundidad(nodo) { return nodo ? 1 + Math.max(profundidad(nodo.izq), profundidad(nodo.der)) : 0; }

function calcPos(nodo, x, y, gap) {
  if (!nodo) return;
  nodo.x = x; nodo.y = y;
  calcPos(nodo.izq, x - gap, y + 70, gap / 1.8);
  calcPos(nodo.der, x + gap, y + 70, gap / 1.8);
}

function dibujarABB(nuevo) {
  const svg = document.getElementById('abb-svg');
  if (!svg) return;
  const W = svg.parentElement.clientWidth || 640;
  const H = Math.max(220, profundidad(raiz) * 80 + 50);
  svg.setAttribute('height', H); svg.innerHTML = '';
  if (!raiz) return;
  calcPos(raiz, W/2, 40, W/4);
  function linea(x1,y1,x2,y2,isNew) {
    const l = document.createElementNS(NS,'line');
    l.setAttribute('x1',x1); l.setAttribute('y1',y1); l.setAttribute('x2',x2); l.setAttribute('y2',y2);
    l.setAttribute('stroke', isNew ? '#58a6ff' : '#30363d'); l.setAttribute('stroke-width', isNew ? '2' : '1.5');
    return l;
  }
  function aristas(n) {
    if (!n) return;
    if (n.izq) { svg.insertBefore(linea(n.x,n.y,n.izq.x,n.izq.y,n.izq.v===nuevo), svg.firstChild); aristas(n.izq); }
    if (n.der) { svg.insertBefore(linea(n.x,n.y,n.der.x,n.der.y,n.der.v===nuevo), svg.firstChild); aristas(n.der); }
  }
  function nodos(n) {
    if (!n) return;
    const isNew = n.v === nuevo, isRaiz = n === raiz;
    const g = document.createElementNS(NS,'g'); g.setAttribute('transform',`translate(${n.x},${n.y})`);
    const c = document.createElementNS(NS,'circle'); c.setAttribute('r','22');
    c.setAttribute('fill', isNew ? '#1c2e4a' : isRaiz ? '#1c2230' : '#161b22');
    c.setAttribute('stroke', isNew ? '#58a6ff' : '#444c56'); c.setAttribute('stroke-width', isNew ? '2' : '1');
    if (isNew) c.style.animation = 'pop .3s ease-out';
    const t = document.createElementNS(NS,'text');
    t.setAttribute('text-anchor','middle'); t.setAttribute('dominant-baseline','central');
    t.setAttribute('font-size','13'); t.setAttribute('font-family','IBM Plex Mono,monospace');
    t.setAttribute('fill', isNew ? '#58a6ff' : '#e6edf3'); t.setAttribute('font-weight','500'); t.textContent = n.v;
    g.appendChild(c); g.appendChild(t); svg.appendChild(g);
    nodos(n.izq); nodos(n.der);
  }
  aristas(raiz); nodos(raiz);
  const st = document.createElementNS(NS,'style');
  st.textContent = '@keyframes pop{from{transform:scale(0);opacity:0}to{transform:scale(1);opacity:1}}';
  svg.appendChild(st);
}

function insertarValor() {
  const inp = document.getElementById('valInput'); if (!inp) return;
  const v = parseInt(inp.value); if (isNaN(v)) return;
  const log = [];
  if (!raiz) { log.push(`<b>${v}</b> es la raíz`); raiz = new Nodo(v); }
  else insertar(raiz, v, log);
  const abbLog = document.getElementById('abbLog');
  if (abbLog) abbLog.innerHTML = log.map((l,i) => `<span class="log-step">paso ${i+1}:</span> ${l}`).join('<br>');
  dibujarABB(v);
  inp.value = ''; inp.focus();
}

function resetArbol() {
  raiz = null; dibujarABB(null);
  const abbLog = document.getElementById('abbLog');
  if (abbLog) abbLog.innerHTML = 'Inserta un valor para comenzar.';
}

let seqTimer = null;
function cargarSecuencia(arr) {
  resetArbol(); if (seqTimer) clearInterval(seqTimer); let i = 0;
  seqTimer = setInterval(() => {
    if (i >= arr.length) { clearInterval(seqTimer); return; }
    const v = arr[i++], log = [];
    if (!raiz) { log.push(`<b>${v}</b> es la raíz`); raiz = new Nodo(v); }
    else insertar(raiz, v, log);
    const abbLog = document.getElementById('abbLog');
    if (abbLog) abbLog.innerHTML = log.map((l,j) => `<span class="log-step">paso ${j+1}:</span> ${l}`).join('<br>');
    dibujarABB(v);
  }, 900);
}

/* ═══════════════════════════════════════════════
   ASIENTOS
═══════════════════════════════════════════════ */
let asientosMatrix = Array.from({length:6}, () => new Array(6).fill(0));

function asientoRenderGrid() {
  const grid = document.getElementById('asientos-grid');
  if (!grid) return;
  let html = '<div style="display:grid;grid-template-columns:repeat(7,36px);gap:4px;font-family:IBM Plex Mono,monospace;font-size:11px;">';
  html += '<div style="color:#8b949e;text-align:center;"></div>';
  for (let c = 1; c <= 6; c++) html += `<div style="color:#8b949e;text-align:center;">${c}</div>`;
  for (let i = 0; i < 6; i++) {
    html += `<div style="color:#8b949e;text-align:center;line-height:36px;">${i+1}</div>`;
    for (let j = 0; j < 6; j++) {
      const ocupado = asientosMatrix[i][j] === 1;
      html += `<div style="width:36px;height:36px;border-radius:4px;border:1px solid ${ocupado?'rgba(248,81,73,.4)':'rgba(63,185,80,.4)'};background:${ocupado?'rgba(248,81,73,.1)':'rgba(63,185,80,.07)'};display:flex;align-items:center;justify-content:center;cursor:pointer;color:${ocupado?'#f85149':'#3fb950'}" onclick="asientoClick(${i+1},${j+1})">${ocupado?'✖':'✔'}</div>`;
    }
  }
  html += '</div>';
  html += `<div style="margin-top:10px;font-family:IBM Plex Mono,monospace;font-size:11px;color:#8b949e;">`;
  html += `<span style="color:#3fb950">✔ Libre</span> &nbsp; <span style="color:#f85149">✖ Reservado</span>`;
  const total = asientosMatrix.flat().filter(v=>v===1).length;
  html += ` &nbsp; Total reservados: <b style="color:#e6edf3">${total}</b></div>`;
  grid.innerHTML = html;
}

function asientoClick(i, j) {
  document.getElementById('asiento-fila').value = i;
  document.getElementById('asiento-col').value = j;
}

function asientoOp(op) {
  const i = parseInt(document.getElementById('asiento-fila').value);
  const j = parseInt(document.getElementById('asiento-col').value);
  const log = document.getElementById('asientos-log');
  if (isNaN(i) || isNaN(j) || i<1||i>6||j<1||j>6) {
    log.innerHTML = '<span style="color:#f85149">Ingresa fila y columna válidas (1-6)</span>'; return;
  }
  let msg = '';
  if (op === 'reservar') {
    if (asientosMatrix[i-1][j-1] === 1) msg = `<span style="color:#f85149">Rechazado: (${i},${j}) ya está reservado</span>`;
    else { asientosMatrix[i-1][j-1] = 1; msg = `<span style="color:#3fb950">Aceptado: (${i},${j}) reservado ✔</span>`; }
  } else if (op === 'liberar') {
    if (asientosMatrix[i-1][j-1] === 0) msg = `<span style="color:#f85149">Rechazado: (${i},${j}) ya está libre</span>`;
    else { asientosMatrix[i-1][j-1] = 0; msg = `<span style="color:#58a6ff">Aceptado: (${i},${j}) liberado</span>`; }
  } else if (op === 'consultar') {
    msg = asientosMatrix[i-1][j-1] === 1
      ? `<span style="color:#f85149">(${i},${j}) está reservado</span>`
      : `<span style="color:#3fb950">(${i},${j}) está libre</span>`;
  }
  log.innerHTML = msg;
  asientoRenderGrid();
}

function asientoReset() {
  asientosMatrix = Array.from({length:6}, () => new Array(6).fill(0));
  asientoRenderGrid();
  const log = document.getElementById('asientos-log');
  if (log) log.innerHTML = 'Sala reiniciada.';
}

/* ═══════════════════════════════════════════════
   DEQUE
═══════════════════════════════════════════════ */
let dequeSaldos = [1000, 1000, 1000, 1000, 1000];
let dequeHistorial = [];

function dequeRender() {
  const vis = document.getElementById('deque-visual');
  if (!vis) return;
  vis.innerHTML = dequeSaldos.map((s, i) =>
    `<div style="padding:8px 14px;background:#1c2230;border:1px solid #30363d;border-radius:6px;font-family:IBM Plex Mono,monospace;font-size:13px;text-align:center;">
      <div style="color:#8b949e;font-size:10px;">cuenta ${i+1}</div>
      <div style="color:#3fb950;font-weight:500;">$${s}</div>
    </div>`
  ).join('');
}

function dequeOp(op) {
  const monto = parseInt(document.getElementById('deque-monto').value);
  const log = document.getElementById('deque-log');
  if (isNaN(monto) || monto <= 0) { log.innerHTML = '<span style="color:#f85149">Ingresa un monto válido</span>'; return; }
  if (!dequeSaldos.length) { log.innerHTML = '<span style="color:#f85149">Cola vacía</span>'; return; }
  if (op === 'retirar') {
    const anterior = dequeSaldos[0];
    dequeHistorial.push(anterior);
    dequeSaldos[0] = anterior - monto;
    dequeSaldos.push(dequeSaldos.shift());
    log.innerHTML = `Retiro de <b>$${monto}</b> — saldo anterior: <b>$${anterior}</b> → nuevo: <b style="color:#3fb950">$${dequeSaldos[dequeSaldos.length-1]}</b>`;
  } else if (op === 'depositar') {
    const anterior = dequeSaldos[dequeSaldos.length-1];
    dequeHistorial.push(anterior);
    dequeSaldos[dequeSaldos.length-1] = anterior + monto;
    log.innerHTML = `Depósito de <b>$${monto}</b> — saldo anterior: <b>$${anterior}</b> → nuevo: <b style="color:#3fb950">$${dequeSaldos[dequeSaldos.length-1]}</b>`;
  }
  dequeRender();
}

function dequeReset() {
  dequeSaldos = [1000, 1000, 1000, 1000, 1000];
  dequeHistorial = [];
  dequeRender();
  const log = document.getElementById('deque-log');
  if (log) log.innerHTML = 'Saldos reiniciados a $1000.';
}

/* ═══════════════════════════════════════════════
   COLA CIRCULAR
═══════════════════════════════════════════════ */
const COLA_CAP = 5;
let colaArr = new Array(COLA_CAP).fill(null);
let colaFrente = -1, colaFinal = -1;

function colaEsVacia() { return colaFrente === -1; }
function colaEsLlena() { return (colaFinal + 1) % COLA_CAP === colaFrente; }

function colaRender() {
  const vis = document.getElementById('cola-visual');
  if (!vis) return;
  let html = '<div style="display:flex;gap:6px;flex-wrap:wrap;margin-bottom:8px;">';
  for (let i = 0; i < COLA_CAP; i++) {
    const esFrente = i === colaFrente;
    const esFinal  = i === colaFinal;
    const tieneVal = colaArr[i] !== null;
    html += `<div style="width:56px;text-align:center;">
      <div style="padding:10px 4px;background:${tieneVal?'#1c2e4a':'#161b22'};border:1px solid ${tieneVal?'#58a6ff':'#30363d'};border-radius:6px;font-family:IBM Plex Mono,monospace;font-size:13px;color:${tieneVal?'#58a6ff':'#444c56'};">${tieneVal ? colaArr[i] : '—'}</div>
      <div style="font-family:IBM Plex Mono,monospace;font-size:9px;color:#8b949e;margin-top:3px;">[${i}]${esFrente?' F':''}${esFinal?' R':''}</div>
    </div>`;
  }
  html += '</div>';
  vis.innerHTML = html;
}

function colaOp(op) {
  const log = document.getElementById('cola-log');
  if (op === 'encolar') {
    const val = document.getElementById('cola-valor').value.trim();
    if (!val) { log.innerHTML = '<span style="color:#f85149">Ingresa un valor</span>'; return; }
    if (colaEsLlena()) { log.innerHTML = '<span style="color:#f85149">Cola llena</span>'; return; }
    if (colaEsVacia()) { colaFrente = 0; colaFinal = 0; }
    else colaFinal = (colaFinal + 1) % COLA_CAP;
    colaArr[colaFinal] = val;
    log.innerHTML = `<span style="color:#3fb950">Encolado: <b>${val}</b> en posición ${colaFinal}</span>`;
    document.getElementById('cola-valor').value = '';
  } else if (op === 'desencolar') {
    if (colaEsVacia()) { log.innerHTML = '<span style="color:#f85149">Cola vacía</span>'; return; }
    const val = colaArr[colaFrente];
    colaArr[colaFrente] = null;
    if (colaFrente === colaFinal) { colaFrente = -1; colaFinal = -1; }
    else colaFrente = (colaFrente + 1) % COLA_CAP;
    log.innerHTML = `<span style="color:#e3b341">Desencolado: <b>${val}</b></span>`;
  } else if (op === 'frente') {
    if (colaEsVacia()) log.innerHTML = '<span style="color:#f85149">Cola vacía</span>';
    else log.innerHTML = `Frente: <b style="color:#58a6ff">${colaArr[colaFrente]}</b>`;
  } else if (op === 'estado') {
    log.innerHTML = `Vacía: <b>${colaEsVacia()}</b> &nbsp; Llena: <b>${colaEsLlena()}</b> &nbsp; Capacidad: <b>${COLA_CAP}</b>`;
  }
  colaRender();
}

function colaReset() {
  colaArr = new Array(COLA_CAP).fill(null);
  colaFrente = -1; colaFinal = -1;
  colaRender();
  const log = document.getElementById('cola-log');
  if (log) log.innerHTML = 'Cola reiniciada.';
}

/* ═══════════════════════════════════════════════
   PILA
═══════════════════════════════════════════════ */
let pilaElementos = [];

function pilaRender() {
  const vis = document.getElementById('pila-visual');
  if (!vis) return;
  if (!pilaElementos.length) {
    vis.innerHTML = '<div style="padding:10px;font-family:IBM Plex Mono,monospace;font-size:12px;color:#444c56;border:1px dashed #30363d;border-radius:6px;text-align:center;">pila vacía</div>';
    return;
  }
  vis.innerHTML = [...pilaElementos].reverse().map((v, i) => {
    const isTop = i === 0;
    return `<div style="padding:10px 16px;background:${isTop?'#1c2e4a':'#161b22'};border:1px solid ${isTop?'#58a6ff':'#30363d'};border-radius:6px;font-family:IBM Plex Mono,monospace;font-size:13px;color:${isTop?'#58a6ff':'#e6edf3'};display:flex;align-items:center;justify-content:space-between;">
      <span>${v}</span>
      ${isTop ? '<span style="font-size:10px;color:#8b949e">← top</span>' : ''}
    </div>`;
  }).join('');
}

function pilaOp(op) {
  const log = document.getElementById('pila-log');
  if (op === 'push') {
    const val = document.getElementById('pila-valor').value.trim();
    if (!val) { log.innerHTML = '<span style="color:#f85149">Ingresa un valor</span>'; return; }
    pilaElementos.push(val);
    log.innerHTML = `<span style="color:#3fb950">Push: <b>${val}</b> → tamaño: ${pilaElementos.length}</span>`;
    document.getElementById('pila-valor').value = '';
  } else if (op === 'pop') {
    if (!pilaElementos.length) { log.innerHTML = '<span style="color:#f85149">Pila vacía</span>'; return; }
    const val = pilaElementos.pop();
    log.innerHTML = `<span style="color:#e3b341">Pop: <b>${val}</b> → tamaño: ${pilaElementos.length}</span>`;
  } else if (op === 'peek') {
    if (!pilaElementos.length) { log.innerHTML = '<span style="color:#f85149">Pila vacía</span>'; return; }
    log.innerHTML = `Peek: <b style="color:#58a6ff">${pilaElementos[pilaElementos.length-1]}</b>`;
  } else if (op === 'estado') {
    log.innerHTML = `Vacía: <b>${pilaElementos.length===0}</b> &nbsp; Tamaño: <b>${pilaElementos.length}</b>`;
  }
  pilaRender();
}

function pilaReset() {
  pilaElementos = [];
  pilaRender();
  const log = document.getElementById('pila-log');
  if (log) log.innerHTML = 'Pila reiniciada.';
}

/* ═══════════════════════════════════════════════
   INIT — al cargar la página
═══════════════════════════════════════════════ */
document.addEventListener('DOMContentLoaded', () => {
  const body = document.body;
  
  if (document.getElementById('asientos-grid')) asientoRenderGrid();
  if (document.getElementById('deque-visual'))  dequeRender();
  if (document.getElementById('cola-visual'))   colaRender();
  if (document.getElementById('pila-visual'))   pilaRender();
  if (document.getElementById('bubble-array'))    initAlgo('bubble',    bubbleGen(DEFAULT_ARR));
  if (document.getElementById('selection-array')) initAlgo('selection', selectionGen(DEFAULT_ARR));
  if (document.getElementById('insertion-array')) initAlgo('insertion', insertionGen(DEFAULT_ARR));
  if (document.getElementById('merge-array'))     initAlgo('merge',     mergeGen(DEFAULT_ARR));
  if (document.getElementById('quick-array'))     initAlgo('quick',     quickGen(DEFAULT_ARR));
  if (document.getElementById('bfs-array'))       initAlgo('bfs',       bfsGen());
  if (document.getElementById('hanoi-array'))     initAlgo('hanoi',     hanoiGen(3));
  if (document.getElementById('kruskal-array'))   initAlgo('kruskal',   kruskalGen());
  if (document.getElementById('prim-array'))      initAlgo('prim',      primGen());
  if (document.getElementById('counting-array')) initAlgo('counting', countingGen(DEFAULT_ARR));
  if (document.getElementById('rquick-array'))   initAlgo('rquick',   rquickGen(DEFAULT_ARR));

  const abbInp = document.getElementById('valInput');
  if (abbInp) abbInp.addEventListener('keydown', e => { if (e.key === 'Enter') insertarValor(); });
});