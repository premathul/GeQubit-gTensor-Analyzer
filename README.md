# GeQubit-gTensor-Analyzer

GeQubit-gTensor-Analyzer is a focused research toolkit for analyzing anisotropic effective (g)-tensors in semiconductor spin qubits, with particular emphasis on Ge/SiGe hole-spin systems. In these devices the spin response can depend strongly on magnetic-field orientation, and the tensor structure can change with gate voltage, confinement, strain, or numerical discretization. A rigorous analysis therefore requires more than reporting three diagonal values. It requires principal-axis reconstruction, angular response, tensor comparison, uncertainty propagation, and physically meaningful distance measures between calculations.

For a magnetic-field direction (mathbf n), the observable effective (g)-factor is
[
g_{mathrm{eff}}(mathbf n)=|mathbf gmathbf n|
=
sqrt{mathbf n^T Gmathbf n},
qquad G=g^Tg.
]
The symmetric positive-semidefinite matrix (G) is especially useful because it directly determines the Zeeman magnitude. The eigenvectors of (G) define principal field directions and the square roots of its eigenvalues give the principal effective (g)-values. This repository therefore treats (G) as a central object and provides utilities for validating positive-semidefiniteness, extracting principal axes, scanning the sphere, and comparing independently obtained tensors.

The project is intended for use in mesh-convergence studies, device comparisons, gate-susceptibility analysis, and uncertainty estimation. It can be used to compare a baseline and fine-mesh result, quantify rotation of principal axes, or estimate the spread in (g_{mathrm{eff}}) arising from an ensemble of perturbed tensors. Future versions will add fitting of (g)-tensors from angular spectroscopy and covariance-aware uncertainty propagation.

Installation is performed with
```bash
git clone https://github.com/premathul/GeQubit-gTensor-Analyzer.git
cd GeQubit-gTensor-Analyzer
python -m pip install -e .
```.
The package is intentionally independent of any specific device solver, so tensors from QTCAD, k·p calculations, experiment, or synthetic models can all be analyzed in the same framework.

## Runnable scientific baseline

The fitting problem is linear in the six independent components of the symmetric matrix G = gᵀg, since g_eff(n)² = nᵀG n for a unit field direction n. The script normalizes supplied directions, rejects rank-deficient angular sampling, solves a least-squares system, and diagonalizes the fitted matrix. The square roots of nonnegative eigenvalues are principal effective g magnitudes; the eigenvectors give their axes up to sign. Angular measurements of the energy splitting alone cannot reconstruct the unique signed 3×3 g tensor, because distinct tensors can share the same G.

Install `numpy` and supply a CSV with columns `bx,by,bz,g_eff`, for example rows `1,0,0,1.2`, `0,1,0,0.8`, and additional noncoplanar directions until at least six linearly independent quadratic constraints are present. Run `python src/main.py measurements.csv`. Inspect the displayed squared-g residual and positive-semidefinite warning. For scientific inference, record measurement uncertainty, angular alignment errors, gate bias, field magnitude, and mesh settings; propagate these uncertainties before claiming principal-axis precision.

## Validation and scope

The calculations in `src/main.py` are transparent baseline models intended for reproducibility and extension. Inputs and assumptions should be reported alongside outputs; numerical agreement with a plotted trace alone does not validate a material-specific prediction. New physical terms should be accompanied by dimensional checks and independent limiting-case comparisons.

## Contact

**Athul Prem** — [GitHub profile](https://github.com/premathul). For scientific discussion or collaboration, open an issue in this repository or reach out through my GitHub profile.
