# Energies 2026 — illustrative operational subcooled data sample

Piasecka, M.; Piasecki, A. *A Unified Experimental Database and Group-Aware Pilot Machine Learning for Flow Boiling in Rectangular Minichannels*. Energies 2026, 19, 4483. https://doi.org/10.3390/en19194483

## Content

- `energies_2026_subcooled_illustrative_sample.csv` — 120 unchanged point-level records selected from an archival pilot regression subset for operational **subcooled** conditions. The original source rows and numeric values are preserved.
- `Table_S1_Data_Dictionary.xlsx` — supplied data dictionary; it covers the wider published database and can contain entries not present in this reduced subset.
- `sample_manifest.json` — frozen input file hash, actual columns, counts, selection rule and limitations.
- `SHA256SUMS.txt` — integrity checks for these public files.

## Scope and limitations

This is a small **illustrative** sample, NOT a statistically representative subset of the full database of 64,385,791 point-level records / 449 source files, and NOT a reproduction dataset for the five-split Random Forest study. It is selected only from the operational subcooled, pilot-eligible records. It does not contain the saturated or ambiguous branches and is not suited to benchmarking QC rejection, reconstructing population proportions or validating machine-learning performance.

The measured and reconstructed fields retain their original column names and values, including `alpha_W_m2K`. Nu was not present in this source and has not been fabricated or reconstructed. The file `source_file` is a provenance identifier. No experimental observations or physical quantities were synthesised. No coefficient has been recalculated. A tiny subset cannot reproduce the published figures or summary performance.

For the full database, supporting methodological details and access conditions, consult the publication.
