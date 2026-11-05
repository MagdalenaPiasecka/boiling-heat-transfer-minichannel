# Longitudinal infrared-temperature profile quality assessment — 64-feature Random Forest manifest

This supplementary documentation accompanies the *Applied Sciences* research article “Infrared Thermography-Based Thermal Diagnostics of Flow-Boiling Minichannels with Machine-Learning-Assisted Profile Quality Assessment” by Magdalena Piasecka and Artur Piasecki.

## Contents

- `feature_manifest_64.csv` — the ordered 64 input descriptors used by the final Random Forest benchmark, with feature names, groups, definitions, units, and missing-value processing stage. The ordering is the exact model-input order.
- `preprocessing_and_selection.md` — preprocessing and feature-selection decisions used in the reported benchmark.
- `SHA256SUMS.txt` — checksums of the public documentation files.

## Scope

This is **feature documentation**, not a release of the complete experimental dataset, trained model, or full executable processing pipeline. Temperature fields are expressed in degrees Celsius, physical coordinates in metres, and normalised features are dimensionless. `feature_manifest_64.csv` preserves the definitions and ordering of the locked analysis. Unit annotations are interpretive metadata compiled from feature names and definitions; they are not additional transformations.

The archive is a public documentation supplement to the research article, not a new model version. No model fitting, prediction, threshold selection, or recalculation of published metrics was performed to assemble it.

## Citation

Please cite the accompanying *Applied Sciences* article when using this descriptor specification. Final volume, article number and DOI should be added when assigned by the publisher.

## Data availability

The full experimental archives and analysis assets are held by the authors in institutional research storage, subject to the availability conditions stated in the article. They are not part of this public supplement.
