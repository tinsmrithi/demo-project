# Sprint 42 — Technical Client Summary
**Period:** 2 – 16 January 2024
**Prepared for:** Smith
**Team:** J. Smith, R. Patel, A. Kim

---

## Delivery Overview

18 of 24 stories completed. 32 story points delivered against a 30-point rolling average — the team is above baseline velocity. 3 stories were intentionally descoped following a leadership-driven release date shift (Jan 10); this was not a capacity issue. 3 stories carry into Sprint 43, all on track to close within the first 3 days.

---

## Production Incident — NB-406: Invoice Rounding Bug

**Severity:** Low
**Discovered:** 11 January, 4:12 PM
**Resolved:** 11 January, 7:30 PM (same day, 3h 18m resolution time)

**What happened:**
Invoice totals were displaying incorrectly for invoices over $10,000. In some cases, the displayed total was off by $0.01.

**Root cause:**
Floating point precision error in `InvoiceFormatter.java` at line 203. A `double` type was used where `BigDecimal` is required for monetary calculations. `double` cannot represent all decimal fractions exactly in IEEE 754 binary format, causing rounding drift on large values.

**Fix applied:**
Replaced `double` with `BigDecimal` in the affected calculation. Fix deployed to production same day.

**Impact assessment:**
- 47 invoices affected — display only, no incorrect charges were processed
- No customer complaints received
- Finance team notified proactively before any queries arose
- Post-mortem waived by team agreement given low severity and same-day resolution

**Recommendation:**
A codebase-wide audit of `double` usage in financial calculation contexts is advisable to prevent recurrence. This is a known class of bug in Java financial code.

---

## Blocker — NB-405: Subcontractor Portal (3 Sprints Running)

**Blocked since:** Sprint 40
**Dependency:** ContractorLink API (third-party vendor)

**Technical context:**
The Subcontractor Portal requires integration with ContractorLink's auth endpoint. The team cannot begin implementation without the endpoint's authentication specification — specifically the OAuth flow, token structure, and error response schema. ContractorLink committed to delivering this documentation by 22 December. It has not been received.

**Escalation history:**
- 22 December: Documentation deadline missed, no delivery
- 5 January: R. Patel followed up — no substantive response
- 12 January: Second follow-up — response: "still in review"

**Current status:** Completely blocked. No development work can proceed without the API spec.

---

## What This Means for the Timeline

This is the most significant risk in the current release plan.

NB-405 is scoped for the **Q1 release**. Based on the current trajectory:

| Scenario | Outcome |
|---|---|
| API spec received before Sprint 43 start (by ~Jan 18) | Development begins immediately. Tight but potentially deliverable for Q1. |
| API spec received mid-Sprint 43 | Insufficient time for implementation, testing, and integration. Q1 release at risk. |
| No API spec received in Sprint 43 | Feature **misses Q1 release**. Earliest realistic delivery: Q2. |

The team has no further escalation leverage at their level. This requires **account-manager or leadership-level intervention with ContractorLink** to force a commitment with a hard deadline. Every day without the spec narrows the delivery window.

**Recommended action:** Escalate to ContractorLink account manager this week with a hard deadline of Jan 17. If not met, initiate contingency planning for Q1 scope — either descope the portal or identify an alternative integration path.

---

## Other Technical Notes

**NB-403 — API Rate Limiting (carry-over)**
Original estimate of 3 points was insufficient — actual complexity is closer to 5 points. The underestimate stemmed from not fully accounting for edge cases around burst handling and retry logic. Completing Jan 18. Story sizing for API-layer work should apply a complexity buffer going forward.

---

## Sprint 43 Technical Plan

**Capacity:** Reduced — R. Patel on leave 2 days. Target: 28 story points.

| Priority | Story | Notes |
|---|---|---|
| 1 | NB-414, NB-423 (carry-overs) | Close days 1–3 |
| 2 | NB-403 (API Rate Limiting) | Complete by Jan 18 |
| 3 | NB-407 (Role Permissions v2) | Reprioritised — full sprint effort |
| 4 | NB-408 (Notification Centre) | Reprioritised |
| 5 | NB-409 (Bulk Export) | Reprioritised |
| 6 | NB-405 (Subcontractor Portal) | Unblocked only if ContractorLink escalation succeeds |
| 7 | 3 backlog stories | TBD at sprint planning |

---

## Actions Required

| # | Action | Owner | Deadline |
|---|---|---|---|
| 1 | Escalate NB-405 to ContractorLink account manager | PM / Leadership | Jan 17 |
| 2 | Initiate Q1 contingency planning if no response by Jan 17 | PM | Jan 18 |
| 3 | Audit `double` usage in financial calculation code | Engineering | Sprint 43 |
| 4 | Apply complexity buffer to API-layer story estimates | Engineering | Sprint 43 planning |
