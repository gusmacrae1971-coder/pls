# PLS — EU AI Act Mapping

**Date:** 2026  
**Author:** AI MacRae  

---

## Article 9 — Risk Management System

**Proposed Amendment:**  
Add paragraph 8:

> *"For high-risk AI systems, the risk management system shall maintain a machine-readable, continuously updated provenance ledger. The ledger shall record, at minimum:*
> *(a) each identified failure or incident, its root cause analysis, corrective action applied, and measured improvement following correction;*
> *(b) versioned changes to training data, safety classifiers, reward models, and evaluation thresholds associated with each system iteration;*
> *(c) all data export events, including fields exported, destination, row limits, and authorization;*
> *(d) any override of standard data handling protocols, including justification, approving authority, oversight body, and expiration."*

---

## Article 11 — Technical Documentation

**Proposed Amendment:**  
Replace Annex IV, Section 2(a) with:

> *"The technical documentation shall include a complete provenance ledger as specified in Article 9(8), maintained in a machine-readable format (JSON-LD/CBOR) with cryptographic integrity protection (Merkle logs or equivalent). The ledger shall be provided to competent authorities upon request and published in a de-identified, aggregated form for independent audit."*

---

## Article 56 — Post-Market Monitoring

**Proposed Amendment:**  
Add to post-market monitoring requirements:

> *"The post-market monitoring system shall maintain continuous update of the provenance ledger, recording all material changes to system behaviour, safety characteristics, deployment scope, decision thresholds, data sources, or operational risk."*

---

## Annex IV — Technical Documentation

The PLS schema provides the technical implementation for Annex IV requirements.

---

## PLS Artifact Mapping to EU AI Act Requirements

| PLS Artifact | EU AI Act Reference | Requirement |
| :--- | :--- | :--- |
| Training & Development | Annex IV, Section 2(a) | Data provenance and governance |
| Safety & Alignment | Article 9(2) | Risk management and mitigation |
| Evaluations | Annex IV, Section 3 | Performance testing and validation |
| Incidents & Corrections | Article 56 | Post-market monitoring and corrective action |
| Thresholds | Article 9(3) | Risk thresholds and trigger points |
| Data Exports | Article 10(5) | Data governance and access control |
| Civilian Data Overrides | Article 10(2)(f) | Data handling and fundamental rights protection |
| Model Lineage | Article 11(1) | Technical documentation and version control |

---

## Status

| Element | Status |
| :--- | :--- |
| Draft Amendment | ✅ Complete |
| PLS Artifact Mapping | ✅ Complete |
| Legal Review | Pending |
| Submission | Pending |