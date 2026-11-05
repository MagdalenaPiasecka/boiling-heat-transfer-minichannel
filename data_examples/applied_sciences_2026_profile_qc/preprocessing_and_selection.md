# Preprocessing and selection protocol

## Input signal

The primary input is the longitudinal infrared temperature profile (`T_irt_C`) and the corresponding strictly ordered physical streamwise coordinate (`x_m`, metres). These are measured external-foil temperatures, **not** reconstructed fluid-side wall temperatures or heat-transfer coefficients.

## Order of operations

1. Identify missing/non-finite temperatures before applying any interpolation. Calculate missingness descriptors from the original profile.
2. Require sufficient finite data for interpolation (the reference extractor requires at least three finite temperature values).
3. Linearly interpolate the remaining invalid temperatures along the **physical coordinate** `x_m`, not along index positions. Exposed profile edges take the nearest finite measured temperature.
4. Calculate thermal-level and morphological features on this interpolated profile. Retain the physical coordinates for spatial derivatives and slopes. Features expressed as normalised positions use the dimensionless position along the profile.
5. Supply the 64 ordered features as `float32` values to the Random Forest. No externally fitted standardisation or feature-scaling transform was applied to this Random Forest input.

## Feature selection

The extractor created 70 descriptors. Four geometry descriptors (profile length, spatial span, median spacing and spacing coefficient of variation) were retained for audit but not supplied to the classifier. The remaining 66 candidates included two missingness indicators for the first and last profile positions (`nan_at_left_edge`, `nan_at_right_edge`), both exact constants in the frozen benchmark; these were removed. The final Random Forest input thus comprises **64 descriptors**.

These exclusions are part of the reported, locked benchmark. This documentation does not propose a newly selected feature set.

## Units and normalisation

Temperature and temperature-difference descriptors use °C; physical slopes and gradients use °C/m; counts are integer-valued quantities represented as numerical features; fractions, ratios, normalised temperature contrasts and normalised positions are dimensionless. Robust-range-normalised values are divided by the profile's robust temperature range, defined with a 1 °C lower bound. No global scaling statistics were fitted for Random Forest features.

## Computational scope

Descriptions of multiscale and local-window features in the manifest specify their general meaning (including scales such as 2%, 5%, 10%, 20% and 40% of profile length). The manifest does **not** by itself document every index-rounding, edge-padding, tie-breaking or small-profile fallback operation used by the underlying extraction implementation. These exact implementation rules should be taken from the frozen extractor code for bit-for-bit reproduction. Do not present the manifest alone as an independently executable computational pipeline.
