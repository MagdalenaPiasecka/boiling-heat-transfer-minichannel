# Representative processed feature sample for infrared-thermography profile-quality assessment

## Associated publication

Magdalena Piasecka and Artur Piasecki, “Infrared Thermography-Based Thermal Diagnostics of Flow-Boiling Minichannels with Machine-Learning-Assisted Profile-Quality Assessment”, *Applied Sciences* (2026; accepted manuscript; insert DOI and bibliographic details after publication).

## Contents

`processed_profile_feature_sample.csv` is a small, **real extracted-feature subset** drawn from the frozen evaluation feature tables used in the study. It has 64 rows: 32 pairs of an unmodified extracted profile and a corresponding synthetically perturbed version. The sample contains 64 model-input descriptors in the **exact frozen model input order**, plus nine columns describing the sample, fluid, grid and perturbation label. The eight synthetic anomaly types are represented by four pairs each (two from FC-770 and two from NOVEC649). Rows are selected deterministically by ascending source profile ID within each anomaly-type/fluid combination. Original source filenames and internal profile IDs are not distributed.

This sample comes **only from the `external_grid` evaluation partition**, grid family 12 (nominal length 425). It is illustrative and balanced by anomaly type; it is **not a random or statistically representative sample** of all experimental profiles or all train/validation/test partitions. The file contains computed profile descriptors, **not raw or processed temperature-versus-position arrays**. Synthetic anomaly labels refer to computationally perturbed copies of experimental IR profiles; they do not identify confirmed physical flow anomalies.

## Column meanings

- `sample_id`: public unique row label.
- `profile_pair_id`: links the unmodified and perturbed descriptors of the same underlying measured profile, pseudonymised for this public sample.
- `fluid_id`: working-fluid identifier.
- `grid_family_id`, `nominal_x_count`: grid-family identifier and nominal number of sampled positions.
- `dataset_split`: original dataset partition (`external_grid` for every row in this sample).
- `profile_variant`: unmodified or synthetically perturbed profile.
- `synthetic_label`: 0 for unmodified, 1 for synthetically perturbed.
- `anomaly_type`: `clean` for unmodified data; otherwise the perturbation type.
- Remaining 64 columns: frozen Random Forest model descriptors, in the exact original order. See the public `feature_manifest_64.csv` for their definitions and units or normalisation.

## Preprocessing and interpretation

Missing-temperature descriptors are measured before interpolation. All other thermal and profile-shape descriptors are derived after linear interpolation over physical position, with nearest finite values used for exposed edges. The frozen 64-feature set excludes four geometry-audit descriptors and two constant edge-missingness flags. Some descriptors use internal, feature-specific normalisation; the Random Forest feature set does not require a separate universal scaling step. For the detailed preprocessing description and limitations, consult the manuscript and the accompanying public feature manifest.

Values are exported from the frozen feature table; this package does **not** retrain a model, recompute features or synthesize any new profile. Numerical formatting of the public CSV may differ from the original stored Parquet precision.

## Public reuse

This is a reproducibility and illustrative data sample, not a replacement for the full research database. The complete experimental archive, source-file metadata and analysis code are retained in the institutional research infrastructure and are subject to the availability conditions stated in the associated publication. Do not use this small, intentionally balanced sample to estimate model performance.
