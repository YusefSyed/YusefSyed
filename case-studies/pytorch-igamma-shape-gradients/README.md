# PyTorch incomplete-gamma shape gradients: validation supplement

This is an unofficial, AI-assisted contribution and author-run validation record for [PyTorch PR 196390](https://github.com/pytorch/pytorch/pull/196390). The PR was open and unmerged when checked September 8, 2026. These results are not upstream CI, maintainer acceptance, an all-domain numerical proof, or a performance benchmark.

## What was checked

The framework runner selects 581 inputs from the 687-row frozen corpus: 509 numerical cases, 60 domain cases and 12 bounded-zero cases. Both regularized incomplete-gamma shape derivatives are evaluated on each input, giving 1,162 outputs per run. The three recorded source-build runs are macOS CPU, Linux CPU and NVIDIA RTX A4000 CUDA: **3,486 output comparisons, with zero recorded corpus failures**. These are repeated checks across environments, not 3,486 unique inputs.

The 106 remaining rows cover standalone arithmetic/classification checks. The older 687-check standalone kernel experiment is separate and is not added to this count. Higher-order differentiation, MPS/XPU, other GPU architectures, complete upstream CI and global accuracy are outside this evidence.

## Reproduce

Build the public [PR head](https://github.com/pytorch/pytorch/commit/4fa63375b8e42dda6fd323b1c152434a31c04ecf) using PyTorch's [source-build instructions](https://github.com/pytorch/pytorch#from-source). Use a CPU build for CPU tests and a CUDA-enabled build on a supported NVIDIA device for GPU tests. With that build importable as `torch`, run the following from this supplement's directory:

```sh
python validation/validate_igamma_integration.py --device cpu --cases validation/cases.json --output cpu-results.json
python validation/validate_igamma_integration.py --device cuda --cases validation/cases.json --output cuda-results.json
```

The runner's command-line arguments and output contract are documented in its source. It requires Python's standard library and the source-built PyTorch; GPU validation aborts if CUDA is unavailable rather than silently falling back. The corpus is supplied beside the runner as `validation/cases.json`.

The PR also contains focused framework regressions in `test/test_igamma_autograd.py`. The supplemental corpus and captured receipts here are outside the PR commit and should not be confused with its checked-in tests.

## Patch identity and recorded receipts

Builds preceded the final contribution commit, so the runtime reports the base commit `2e2b1371931ea2a080c423ee3bc15c4fc59787a6`. [Patch identity](validation/patch-identity.json) records per-file SHA-256 matches between the tested local/remote sources and public PR head `4fa63375b8e42dda6fd323b1c152434a31c04ecf`.

- [Summary](validation/summary.json)
- [Exact frozen input/reference corpus](validation/cases.json)
- [Runner](validation/validate_igamma_integration.py)
- [macOS CPU outputs](validation/results/macos-cpu.json)
- [Linux CPU outputs](validation/results/linux-cpu.json)
- [RTX A4000 CUDA outputs](validation/results/rtx-a4000-cuda.json)

Absolute installation paths were removed from each public result's `torch_file` field. Numerical inputs, references, returned values, tolerances and comparison results are retained. Scheduler scripts, account names, machine storage paths, private logs and credentials are not included. The [summary](validation/summary.json) hashes identify these sanitized copies.

The outputs are author-run records, not an independent third-party replication. This supplement makes the method and numerical evidence inspectable without implying endorsement by PyTorch.
