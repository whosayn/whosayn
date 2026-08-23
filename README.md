# Hussein Faara

<p align="center">
  <img src="./assets/systems-pipeline.svg" alt="Animated systems pipeline showing source graph, build graph, cache, compiler, scheduler, and artifacts" width="100%">
</p>

<p align="center">
  <a href="https://github.com/whosayn?tab=repositories"><img alt="repos" src="https://img.shields.io/badge/focus-systems%20%26%20infrastructure-0969da"></a>
  <a href="https://github.com/rdkit/rdkit"><img alt="rdkit" src="https://img.shields.io/badge/open%20source-RDKit-1f883d"></a>
  <img alt="langs" src="https://img.shields.io/badge/C%2B%2B-Python-8250df">
  <img alt="interests" src="https://img.shields.io/badge/build%20systems-performance%20engineering-d1242f">
  <img alt="interests" src="https://img.shields.io/badge/scientific%20computing-developer%20platforms-f59e0b">
</p>

<h3 align="center">I make expensive software workflows boring.</h3>

<p align="center">
  I work on infrastructure-heavy problems where <b>performance, portability, and developer experience</b> all matter:
  build graphs, caches, schedulers, parsers, native/Python boundaries, and scientific software.
</p>

---

## Visual map

```mermaid
flowchart LR
    A[Source graph] --> B[Build graph]
    B --> C[Compiler cache]
    C --> D[Compilation]
    D --> E[Test / CI scheduler]
    E --> F[Artifacts]
    F --> G[Scientists / Developers]

    H[Parser diagnostics] --> G
    I[Scientific data structures] --> G
    J[Native/Python interfaces] --> G
    K[Distributed infrastructure] --> G
```

<p align="center">
  <sub>My favorite engineering problems usually live somewhere in this graph.</sub>
</p>

---

## OSS pulse

<p align="center">
  <img src="./assets/oss-pulse.svg" alt="GitHub contribution pulse for the last 12 months" width="100%">
</p>

---

## What I like building

<table>
  <tr>
    <td valign="top" width="33%">
      <h3>⚙️ Build & CI</h3>
      <p>Dependency graphs, caching, distributed builds, reproducible environments, packaging, and CI systems that reduce wasted work.</p>
    </td>
    <td valign="top" width="33%">
      <h3>🚀 Performance</h3>
      <p>Latency reduction, memory efficiency, throughput tuning, data structures, parser performance, and removing hidden bottlenecks.</p>
    </td>
    <td valign="top" width="33%">
      <h3>🧪 Scientific software</h3>
      <p>Cheminformatics, molecular representations, native/Python interfaces, graph algorithms, and infrastructure for computation-heavy workflows.</p>
    </td>
  </tr>
</table>

---

## Selected engineering work

<table>
  <tr>
    <td valign="top" width="50%">
      <h3>🧪 RDKit</h3>
      <p>Contributor to the C++ core of <a href="https://github.com/rdkit/rdkit">RDKit</a>, a widely used cheminformatics toolkit.</p>
      <ul>
        <li><b>ccache integration work</b> to speed up iterative development and reduce rebuild cost</li>
        <li><b>#8675</b> fixed parse error handling for invalid characters</li>
        <li><b>#6906</b> addressed unnecessary vector copying in <code>PositionVariationOp::getVariationCounts()</code></li>
        <li><b>#8742</b> proposed efficient extraction of small subgraphs from very large molecules</li>
        <li><b>#8612</b> improved parser diagnostics by identifying the precise offending character/token</li>
      </ul>
      <p><b>Why it matters:</b> correctness, performance, build acceleration, and API design are much stronger signals than generic cleanup.</p>
    </td>
    <td valign="top" width="50%">
      <h3>🛡️ sourceguard</h3>
      <p><a href="https://github.com/whosayn/sourceguard">sourceguard</a> is a developer-tooling project for keeping prohibited source patterns out of new changes.</p>
      <p><b>Idea:</b> enforcement belongs as close as possible to the developer feedback loop.</p>
      <hr>
      <h3>🧬 rdkit_smiles</h3>
      <p><a href="https://github.com/whosayn/rdkit_smiles">rdkit_smiles</a> explores lexing, grammar, parsing, and molecular graph construction in C++.</p>
      <p><b>Why I like it:</b> it sits at the intersection of language tooling, graph structure, and scientific computing.</p>
    </td>
  </tr>
</table>

---

## Things I enjoy debugging

```text
slow build
   │
   ├─ duplicated work? ───────────────► cache it
   ├─ bad dependency graph? ──────────► fix the graph
   ├─ poor scheduling? ───────────────► move the bottleneck
   ├─ serialization / I/O? ───────────► measure bytes, not vibes
   ├─ cross-platform divergence? ─────► remove special cases
   └─ nobody knows why it's slow? ────► instrument first
```

---

## Current rabbit holes

<p>
  <img src="https://img.shields.io/badge/remote%20build%20caching-1f6feb?style=for-the-badge" alt="remote build caching">
  <img src="https://img.shields.io/badge/distributed%20CI-238636?style=for-the-badge" alt="distributed CI">
  <img src="https://img.shields.io/badge/C%2B%2B%20performance-a371f7?style=for-the-badge" alt="C++ performance">
  <img src="https://img.shields.io/badge/Rust%20build%20tooling-db6d28?style=for-the-badge" alt="Rust build tooling">
  <img src="https://img.shields.io/badge/Go%20backends-0969da?style=for-the-badge" alt="Go backends">
  <img src="https://img.shields.io/badge/scientific%20computing-8250df?style=for-the-badge" alt="scientific computing">
  <img src="https://img.shields.io/badge/storage%20systems-bd561d?style=for-the-badge" alt="storage systems">
  <img src="https://img.shields.io/badge/developer%20platforms-d1242f?style=for-the-badge" alt="developer platforms">
</p>

---

## A few principles

<table>
  <tr>
    <td valign="top" width="25%"><b>Build platforms, not patches</b><br><sub>solve the recurring problem once</sub></td>
    <td valign="top" width="25%"><b>Measure first</b><br><sub>profile before optimizing</sub></td>
    <td valign="top" width="25%"><b>Reduce hidden work</b><br><sub>cache, simplify, and make bottlenecks visible</sub></td>
    <td valign="top" width="25%"><b>Make it boring</b><br><sub>good infrastructure fades into the background</sub></td>
  </tr>
</table>

---

<details>
  <summary><b>More GitHub archaeology</b></summary>
  <br>
  <ul>
    <li><a href="https://github.com/whosayn/check-old-commit-date">check-old-commit-date</a> — pre-commit tooling around stale commit timestamps</li>
    <li>experiments in developer tooling, parsing, and systems-oriented utilities</li>
    <li>ongoing interest in infrastructure that compounds engineer productivity</li>
  </ul>
</details>

---

<p align="center">
  <sub>
    Preferred metric: <code>before → after</code>, not “feels faster”.
    &nbsp;•&nbsp;
    <a href="https://husseinfaara.com">website</a>
  </sub>
</p>
