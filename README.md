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

## Contact

**Athul Prem**

For scientific discussion, collaboration, or suggestions related to this project, please contact Athul Prem through the GitHub account associated with this repository.
