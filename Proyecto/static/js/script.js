console.log("Plataforma de Estructuras de Datos iniciada correctamente");

const autoTimers = {};

/* -------------------------
   Ejemplos de pasos por algoritmo
   Puedes editar los arrays para mostrar más pasos o datos reales
   ------------------------- */

/* Bubble Sort */
window.bubbleSteps = [
  { array:[5,3,8,1], log:"Inicio: [5,3,8,1]" },
  { array:[3,5,8,1], log:"Comparar 5 y 3 → intercambiar" },
  { array:[3,5,1,8], log:"Comparar 8 y 1 → intercambiar" },
  { array:[3,1,5,8], log:"Segunda pasada: intercambiar 5 y 1" },
  { array:[1,3,5,8], log:"Ordenado" }
];
window.bubbleIndex = 0;

/* Selection Sort */
window.selectionSteps = [
  { array:[5,3,8,1], log:"Inicio: [5,3,8,1]" },
  { array:[1,3,8,5], log:"Seleccionar mínimo (1) e intercambiar con 5" },
  { array:[1,3,8,5], log:"Segunda iteración: mínimo 3 ya en su lugar" },
  { array:[1,3,5,8], log:"Intercambiar 8 y 5" },
  { array:[1,3,5,8], log:"Ordenado" }
];
window.selectionIndex = 0;

/* Insertion Sort */
window.insertionSteps = [
  { array:[5,3,8,1], log:"Inicio: [5,3,8,1]" },
  { array:[3,5,8,1], log:"Insertar 3 antes de 5" },
  { array:[3,5,8,1], log:"Insertar 8 (ya en su lugar)" },
  { array:[1,3,5,8], log:"Insertar 1 al inicio" },
  { array:[1,3,5,8], log:"Ordenado" }
];
window.insertionIndex = 0;

/* Merge Sort (pasos simplificados) */
window.mergeSteps = [
  { array:[5,3,8,1], log:"Inicio: [5,3,8,1]" },
  { array:[[5,3],[8,1]], log:"Dividir en [5,3] y [8,1]" },
  { array:[[3,5],[1,8]], log:"Ordenar subarrays" },
  { array:[1,3,5,8], log:"Merge final → [1,3,5,8]" }
];
window.mergeIndex = 0;

/* Quick Sort (pasos simplificados) */
window.quickSteps = [
  { array:[5,3,8,1], log:"Inicio: elegir pivot = 1" },
  { array:[1,3,8,5], log:"Partición: mover pivot a la izquierda" },
  { array:[1,3,5,8], log:"Recursión y orden final" }
];
window.quickIndex = 0;

/* BFS (ejemplo de recorrido en grafo pequeño) */
window.bfsSteps = [
  { array:['cola: [A]'], log:"Inicio en A; encolar A" },
  { array:['cola: [B,C]'], log:"Visitar A → encolar B,C" },
  { array:['cola: [C,D]'], log:"Visitar B → encolar D" },
  { array:['cola: [D]'], log:"Visitar C" },
  { array:['cola: []'], log:"Visitar D → recorrido completo: A,B,C,D" }
];
window.bfsIndex = 0;

/* Torres de Hanoi (ejemplo con 3 discos) */
window.hanoiSteps = [
  { array:['A:[3,2,1]','B:[]','C:[]'], log:"Inicio: todos los discos en A" },
  { array:['A:[3,2]','B:[]','C:[1]'], log:"Mover disco 1 de A a C" },
  { array:['A:[3]','B:[2]','C:[1]'], log:"Mover disco 2 de A a B" },
  { array:['A:[3]','B:[2,1]','C:[]'], log:"Mover disco 1 de C a B" },
  { array:['A:[]','B:[2,1]','C:[3]'], log:"... pasos hasta completar" }
];
window.hanoiIndex = 0;

/* Kruskal (ejemplo simplificado) */
window.kruskalSteps = [
  { array:['(A-B:1)','(B-C:2)','(A-C:3)'], log:"Aristas ordenadas por peso" },
  { array:['(A-B:1)'], log:"Agregar (A-B) al AGM" },
  { array:['(A-B:1)','(B-C:2)'], log:"Agregar (B-C) al AGM" },
  { array:['(A-B:1)','(B-C:2)'], log:"Siguiente arista crea ciclo → ignorar" },
  { array:['(A-B:1)','(B-C:2)'], log:"AGM completado" }
];
window.kruskalIndex = 0;

/* Prim (ejemplo simplificado) */
window.primSteps = [
  { array:['V={A}','E=[]'], log:"Iniciar en A" },
  { array:['V={A,B}','E=[(A-B:1)]'], log:"Agregar arista mínima desde A" },
  { array:['V={A,B,C}','E=[(A-B:1),(B-C:2)]'], log:"Agregar siguiente arista mínima" },
  { array:['V={A,B,C}','E=[(A-B:1),(B-C:2)]'], log:"AGM completado" }
];
window.primIndex = 0;

/* -------------------------
   Render y control genérico
   ------------------------- */

function renderAlgo(name, steps, index) {
  const arrDiv = document.getElementById(name + '-array');
  const logDiv = document.getElementById(name + '-log');
  if (!arrDiv || !logDiv) return;
  arrDiv.innerHTML = '';
  const step = steps[index] || steps[0];
  (step.array || []).forEach(item => {
    const el = document.createElement('div');
    el.textContent = item;
    arrDiv.appendChild(el);
  });
  logDiv.innerHTML = step.log;
}

function algoNext(name) {
  const steps = window[name + 'Steps'];
  const idxName = name + 'Index';
  if (!steps || typeof window[idxName] === 'undefined') return;
  if (window[idxName] < steps.length - 1) window[idxName]++;
  renderAlgo(name, steps, window[idxName]);
}
function algoPrev(name) {
  const steps = window[name + 'Steps'];
  const idxName = name + 'Index';
  if (!steps || typeof window[idxName] === 'undefined') return;
  if (window[idxName] > 0) window[idxName]--;
  renderAlgo(name, steps, window[idxName]);
}
function algoReset(name) {
  const steps = window[name + 'Steps'];
  const idxName = name + 'Index';
  if (!steps || typeof window[idxName] === 'undefined') return;
  window[idxName] = 0;
  renderAlgo(name, steps, window[idxName]);
}

/* autoplay helpers */
function autoPlay(name, delay = 700) {
  stopAuto(name);
  autoTimers[name] = setInterval(() => {
    const steps = window[name + 'Steps'];
    const idxName = name + 'Index';
    if (!steps || typeof window[idxName] === 'undefined') return stopAuto(name);
    if (window[idxName] >= steps.length - 1) return stopAuto(name);
    algoNext(name);
  }, delay);
}
function stopAuto(name) {
  if (autoTimers[name]) { clearInterval(autoTimers[name]); delete autoTimers[name]; }
}

/* Inicializar render si los contenedores existen */
document.addEventListener('DOMContentLoaded', () => {
  const algos = ['bubble','selection','insertion','merge','quick','bfs','hanoi','kruskal','prim'];
  algos.forEach(name => {
    const steps = window[name + 'Steps'];
    const idxName = name + 'Index';
    if (steps && typeof window[idxName] !== 'undefined') {
      renderAlgo(name, steps, window[idxName]);
    }
  });
});

/* -------------------------
   ABB: funciones de visualización
   (si ya están en archivo.html no hace falta duplicar;
    si prefieres centralizar, pega este bloque en script.js)
   ------------------------- */

let raiz = null;

class Nodo {
  constructor(v) { this.v = v; this.izq = null; this.der = null; this.x = 0; this.y = 0; }
}

function insertar(nodo, v, log) {
  if (!nodo) return new Nodo(v);
  if (v < nodo.v) {
    log.push(`${v} < ${nodo.v} → izquierda`);
    nodo.izq = insertar(nodo.izq, v, log);
  } else if (v > nodo.v) {
    log.push(`${v} > ${nodo.v} → derecha`);
    nodo.der = insertar(nodo.der, v, log);
  } else {
    log.push(`${v} ya existe`);
  }
  return nodo;
}

function profundidad(nodo) {
  if (!nodo) return 0;
  return 1 + Math.max(profundidad(nodo.izq), profundidad(nodo.der));
}

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
  svg.setAttribute('height', H);
  svg.innerHTML = '';
  if (!raiz) return;
  calcPos(raiz, W / 2, 40, W / 4);

  const NS = 'http://www.w3.org/2000/svg';

  function linea(x1,y1,x2,y2,isNew) {
    const l = document.createElementNS(NS,'line');
    l.setAttribute('x1',x1); l.setAttribute('y1',y1);
    l.setAttribute('x2',x2); l.setAttribute('y2',y2);
    l.setAttribute('stroke', isNew ? '#58a6ff' : '#30363d');
    l.setAttribute('stroke-width', isNew ? '2' : '1.5');
    return l;
  }

  function aristas(nodo) {
    if (!nodo) return;
    if (nodo.izq) { svg.insertBefore(linea(nodo.x,nodo.y,nodo.izq.x,nodo.izq.y,nodo.izq.v===nuevo), svg.firstChild); aristas(nodo.izq); }
    if (nodo.der) { svg.insertBefore(linea(nodo.x,nodo.y,nodo.der.x,nodo.der.y,nodo.der.v===nuevo), svg.firstChild); aristas(nodo.der); }
  }

  function nodos(nodo) {
    if (!nodo) return;
    const isNew  = nodo.v === nuevo;
    const isRaiz = nodo === raiz;
    const g = document.createElementNS(NS,'g');
    g.setAttribute('transform',`translate(${nodo.x},${nodo.y})`);

    const c = document.createElementNS(NS,'circle');
    c.setAttribute('r','22');
    c.setAttribute('fill',  isNew ? '#1c2e4a' : isRaiz ? '#1c2230' : '#161b22');
    c.setAttribute('stroke', isNew ? '#58a6ff' : '#444c56');
    c.setAttribute('stroke-width', isNew ? '2' : '1');
    if (isNew) c.style.animation = 'pop .3s ease-out';

    const t = document.createElementNS(NS,'text');
    t.setAttribute('text-anchor','middle');
    t.setAttribute('dominant-baseline','central');
    t.setAttribute('font-size','13');
    t.setAttribute('font-family','IBM Plex Mono, monospace');
    t.setAttribute('fill', isNew ? '#58a6ff' : '#e6edf3');
    t.setAttribute('font-weight','500');
    t.textContent = nodo.v;

    g.appendChild(c); g.appendChild(t);
    svg.appendChild(g);
    nodos(nodo.izq); nodos(nodo.der);
  }

  aristas(raiz); nodos(raiz);
  const st = document.createElementNS(NS,'style');
  st.textContent = '@keyframes pop{from{transform:scale(0);opacity:0}to{transform:scale(1);opacity:1}}';
  svg.appendChild(st);
}

function insertarValorABB() {
  const inp = document.getElementById('valInput');
  if (!inp) return;
  const v = parseInt(inp.value);
  if (isNaN(v)) return;
  const log = [];
  if (!raiz) {
    log.push(`<b>${v}</b> es la raíz`);
    raiz = new Nodo(v);
  } else {
    insertar(raiz, v, log);
  }
  const abbLog = document.getElementById('abbLog');
  if (abbLog) abbLog.innerHTML = log.map((l,i) =>
    `<span class="log-step">paso ${i+1}:</span> ${l}`
  ).join('<br>');
  dibujarABB(v);
  inp.value = ''; inp.focus();
}

function resetArbolABB() {
  raiz = null; dibujarABB(null);
  const abbLog = document.getElementById('abbLog');
  if (abbLog) abbLog.innerHTML = 'Inserta un valor para comenzar.';
}

let seqTimer = null;
function cargarSecuenciaABB(arr) {
  resetArbolABB();
  if (seqTimer) clearInterval(seqTimer);
  let i = 0;
  seqTimer = setInterval(() => {
    if (i >= arr.length) { clearInterval(seqTimer); return; }
    const v = arr[i++];
    const log = [];
    if (!raiz) { log.push(`<b>${v}</b> es la raíz`); raiz = new Nodo(v); }
    else insertar(raiz, v, log);
    const abbLog = document.getElementById('abbLog');
    if (abbLog) abbLog.innerHTML = log.map((l,j) =>
      `<span class="log-step">paso ${j+1}:</span> ${l}`
    ).join('<br>');
    dibujarABB(v);
  }, 900);
}

/* Si centralizas ABB aquí, conecta los botones del HTML a estas funciones:
   - onclick="insertarValorABB()"
   - onclick="resetArbolABB()"
   - onclick="cargarSecuenciaABB([...])"
   Si prefieres mantener ABB en archivo.html, elimina este bloque duplicado.
*/
