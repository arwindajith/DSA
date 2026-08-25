---
name: pdsa-algorithms
description: "Use when working on this repository's Python data structures, graph algorithms, heaps, sorting algorithms, search trees, or algorithm exercises. Preserve the educational style, verify algorithm invariants, and run focused Python checks."
---

# PDSA Algorithms

## Repository Scope

This repository contains standalone Python implementations for data structures and algorithms:

- `data structures/`: union-find
- `graphs/`: BFS, DFS traversal, shortest paths, all-pairs shortest paths, and minimum spanning tree algorithms
- `heap/`: min-heap and max-heap implementations
- `sorting/`: insertion, selection, merge, quick, heap, and related sorting implementations
- `practice/`: exercises and alternate implementations
- `tree/`: binary search trees and AVL trees

There is no package-level application or test framework. Treat each Python file as a small, independently understandable exercise.

## Working Conventions

- Preserve the simple, instructional implementation style and existing public class and method names unless a change is explicitly requested.
- Prefer standard-library Python only. Do not add dependencies for core algorithms.
- Keep changes focused on the requested algorithm or data structure; avoid broad refactors across duplicate implementations.
- Respect existing filename spelling, including names such as `Djikstra_SSP.py` and `Insertion _sort.py`.
- Use descriptive variable names and short comments only where the algorithm's invariant or a non-obvious step needs clarification.
- Preserve the repository's current representation choices, such as sentinel or empty tree nodes, unless the task requires changing the representation.

## Correctness Checks

Before editing, identify the algorithm invariant and its edge cases. After editing, run the narrowest useful check:

```powershell
python -m py_compile "path\to\changed_file.py"
python "path\to\changed_file.py"
```

For data structures, check empty input, one-element input, duplicate values, already ordered or reverse-ordered input, and boundary operations. For graph algorithms, check disconnected graphs, unreachable vertices, zero-weight edges, and negative edges only where supported. For trees and heaps, verify ordering, height or heap properties, and traversal output after mutations.

When practical, use a short inline assertion script or a temporary test command rather than adding a test framework solely for one exercise. Do not treat a whole-repository compile as a clean signal when unrelated files are incomplete; report pre-existing failures separately from failures in the changed file.

## Algorithm-Specific Guidance

- Sorting functions should return or mutate data consistently with the surrounding implementation; verify both the result and whether the input was changed.
- Traversals should visit each reachable vertex or node once and maintain the documented traversal order.
- Shortest-path algorithms should make unreachable results explicit and should not silently apply assumptions from a different algorithm, such as non-negative weights for Dijkstra's algorithm.
- Union-find should maintain correct parent representatives and apply path compression or union balancing when those operations are part of the implementation.
- AVL operations must preserve binary-search ordering, update heights after rotations, and keep every balance factor within `-1`, `0`, or `1`.

## Change Review

Before finishing, inspect the focused diff and confirm:

- no unrelated files were modified;
- public names and example usage remain compatible;
- empty and boundary cases are handled;
- the changed file compiles and its focused behavior check passes;
- any repository-wide failures are clearly identified as pre-existing or unrelated.
