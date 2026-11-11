# Hussein Faara

**Senior Software Engineer · C++ / Python · Systems & infrastructure**

I build the tools teams use to ship native software: reproducible C++ and Python builds, shared storage APIs, and faster critical paths.

[Portfolio](https://husseinfaara.com/) · [GitHub](https://github.com/whosayn) · [Email](mailto:faarahussein@gmail.com)

## What moved after the changes

| Measurement | Before | After |
| --- | ---: | ---: |
| Clean build time (normalized) | 100 | **22** |
| Logging latency (normalized) | 100 | **80** |
| Internal database count | 10 | **1** |

The first two rows use the original value as 100. [Project context](https://husseinfaara.com/)

## What I built

### Reproducible releases for native software

I built reproducible packaging and release workflows with Pixi and rattler-build for Linux, macOS, and Windows, with x86-64 and ARM targets.

### Ten databases, one storage API

I designed a C++ API across multiple storage engines and brought ten internal databases onto one foundation shared by applications.

### 20% lower logging latency

I profiled a logging path shared by C++ and Python, found network overhead, and removed it. Logging latency fell 20%.

## Open source

- **[RDKit](https://github.com/rdkit/rdkit/issues/8742).** Proposed a C++ API for building a new molecular graph from selected atoms.
- **[RDKit](https://github.com/rdkit/rdkit/issues/8612).** Proposed pointing SMARTS parse errors at the exact invalid token.
- **[rdkit_smiles](https://github.com/whosayn/rdkit_smiles).** Explores how C++ turns SMILES notation into a molecular graph.
- **[sourceguard](https://github.com/whosayn/sourceguard).** Checks code changes for prohibited patterns so teams can catch them earlier.

## Where I go deep

- **Developer infrastructure.** Resolve dependencies, cut rebuild work, and ship repeatable native packages.
- **C++ systems & performance.** Profile C++ and Python across native boundaries, parsers, and memory-intensive paths.
- **Storage & distributed compute.** Design shared APIs, reduce serialization costs, and coordinate compute-heavy work.
- **Technical leadership.** Own architecture and set standards for tools that other engineers rely on.

[Email me about a senior systems or infrastructure role](mailto:faarahussein@gmail.com)
