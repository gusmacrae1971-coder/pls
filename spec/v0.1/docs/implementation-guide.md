# PLS Implementation Guide

**Date:** 2026  
**Author:** AI MacRae  

---

## 1. Purpose

This guide provides practical steps for implementing the Provenance Ledger Standard (PLS) in a high-impact AI system.

It is intended for:
- **Engineers** building PLS-compliant systems
- **Architects** designing PLS integration
- **Auditors** verifying PLS conformance
- **Governance teams** overseeing PLS adoption

---

## 2. Implementation Overview

Implementing the PLS involves four phases:

1. **System Assessment** — Determine which conformance profile applies.
2. **Ledger Design** — Map system components to PLS artifacts.
3. **Implementation** — Build the ledger and integrate with the system.
4. **Verification** — Validate the ledger against the PLS schema and verification properties.

---

## 3. Phase 1 — System Assessment

**Step 1:** Identify the system's impact category.

| Category | Description |
| :--- | :--- |
| **Research** | Non-deployed, experimental systems |
| **Commercial** | Deployed commercial AI systems |
| **High-Impact** | Systems affecting rights, safety, liberty, essential services, financial interests, or government decisions |
| **Critical** | Defence, healthcare, justice, or other high-stakes domains |

**Step 2:** Select the appropriate conformance profile.

| Profile | Applies To |
| :--- | :--- |
| **PLS-Lite** | Research models |
| **PLS-Core** | Commercial AI |
| **PLS-High** | High-impact AI |
| **PLS-Critical** | Critical systems |

---

## 4. Phase 2 — Ledger Design

**Step 1:** Map system components to PLS artifacts.

| PLS Artifact | System Component |
| :--- | :--- |
| **Training & Development** | Data pipeline, training infrastructure |
| **Safety & Alignment** | Classifiers, reward models, RLHF |
| **Evaluations** | Benchmarks, red-team tests |
| **Incidents & Corrections** | Incident management system |
| **Thresholds** | Operational monitoring system |
| **Data Exports** | Data export/access control system |
| **Civilian Data Overrides** | Override/exception management system |
| **Model Lineage** | Version control, model registry |

**Step 2:** Design the ledger structure.

- Use the PLS JSON Schema as the foundation.
- Extend with system-specific fields if necessary (non-material extensions are permitted).
- Ensure all mandatory fields are populated.

---

## 5. Phase 3 — Implementation

**Step 1:** Generate the initial ledger.

- Populate the ledger with data from system components.
- Ensure all required fields are present.
- Use the validation tool to verify the ledger against the schema.

**Step 2:** Set up the ledger maintenance process.

- Establish a process for updating the ledger on system changes.
- Define what constitutes a "material change" requiring a ledger update.
- Automate ledger generation where possible.

**Step 3:** Implement cryptographic integrity.

- Use Merkle logs (SCITT or similar) for tamper-evidence.
- Publish roots to a public transparency log.
- Sign the ledger with Ed25519 (or equivalent).

---

## 6. Phase 4 — Verification

**Step 1:** Test the ledger against the validation tool.

```bash
python3 validation-tool.py my-ledger.json provenance-ledger-schema.json