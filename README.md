# pls
# Provenance Ledger Standard (PLS)

**A Governance Specification for High-Impact AI Systems**

**Author:** AI MacRae  
**Status:** Draft — Public Review  
**Version:** 0.1  
**Date:** 2026

---

## Guiding Principle

> **The shift is not from "trust us" to "trust someone else." It is from "tell us" to "show us."**

---

## Purpose

The Provenance Ledger Standard defines the **minimum machine-readable record** that high-impact AI systems must maintain as a condition of deployment. It is the control plane for AI accountability.

---

## Core Artifacts

1. **Training & Development** — datasets, preprocessing, training config
2. **Safety & Alignment** — classifiers, reward models, RLHF iterations
3. **Evaluations** — benchmarks, red-team reports, adversarial tests
4. **Incidents & Corrections** — failure → root cause → action → improvement
5. **Thresholds** — operational tripwires as immutable governance events
6. **Data Exports** — fields exported, destinations, authorization
7. **Civilian Data Overrides** — receipts for privacy-bypass/access-elevation with justification, authority, expiration
8. **Model Lineage & Version Provenance** — model identifier, parent model, deployment/retirement dates, rollback history, compatibility

---

## Regulatory Mapping

This standard is submitted as a proposed amendment to:
- **EU AI Act, Article 9(8)** — Risk Management System provenance obligations
- **EU AI Act, Article 11** — Technical Documentation requirements

---

## Conformance

A system is PLS-compliant if it:
1. Produces all mandatory ledger artifacts
2. Maintains cryptographic integrity of records
3. Supports independent audit
4. Preserves ledger continuity across version updates
5. Documents all material post-deployment changes

---

## Repository Structure

