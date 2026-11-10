# Hussein Faara

**Senior Software Engineer · C++ / Python · Systems & infrastructure**

I build developer infrastructure, shared storage, and performance-critical systems in C++ and Python.

[Portfolio](https://husseinfaara.com/) · [GitHub](https://github.com/whosayn) · [Email](mailto:faarahussein@gmail.com)

## Architecture decision: a shared storage API

**Context.** Several applications relied on different storage engines across ten internal databases.

**Decision.** Design a C++ storage abstraction that supports the engines behind a common interface.

**Outcome.** Consolidate the databases into one shared foundation.

## Selected engineering work

### Reproducible builds across platforms

Built packaging and distribution workflows for Linux, macOS, and Windows on x86-64 and ARM, using Pixi and rattler-build.

### A shared API for ten databases

Designed a C++ storage abstraction across multiple engines and consolidated ten internal databases into one foundation shared by applications.

### A shorter logging critical path

Profiled a shared logging path across C++ and Python and removed network bottlenecks. Latency improved by 20%.

## Open source

- **[RDKit](https://github.com/rdkit/rdkit/issues/8742).** Proposed extracting selected atoms as a new molecular graph.
- **[RDKit](https://github.com/rdkit/rdkit/issues/8612).** Proposed reporting the precise position of invalid SMARTS tokens.
- **[rdkit_smiles](https://github.com/whosayn/rdkit_smiles).** Explores lexing, parsing, and molecular graph construction.
- **[sourceguard](https://github.com/whosayn/sourceguard).** Checks new changes for prohibited source patterns.

## Core competencies

- **Developer infrastructure.** Build graphs, dependency resolution, caching, CI/CD, packaging.
- **C++ systems & performance.** Profiling, native/Python interfaces, parsers, memory, and throughput.
- **Storage & distributed compute.** Shared APIs, serialization, scheduling, and HPC workflows.
- **Technical leadership.** Architecture ownership, engineering standards, and developer enablement.

[Discuss a senior engineering role](mailto:faarahussein@gmail.com)
