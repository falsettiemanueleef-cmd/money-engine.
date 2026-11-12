# NEXA Rental Profit Manager — QA audit

Audit date: 2026-11-12
Branch: `nexa-rental-foundation`

## Repository checks completed
- Confirmed that the app HTML, PWA manifest, service worker, and app guide exist on the branch.
- Inspected the current source code and identified the limitations below.
- Added `qa-check.mjs` for JavaScript syntax, manifest JSON, translation-key parity, and duplicate static HTML ID checks.
- Added a GitHub Actions workflow to run those static checks on pushes to this branch.

## Execution status
The GitHub connector returned no workflow run or commit status for the latest QA commit. Therefore the automated checks are configured but **not confirmed as executed or passed**. No real browser/device session was available in this verification pass.

## Findings that block a sales-ready release
1. No full edit/update flow for existing reservations, expenses, properties, or units.
2. No advanced calendar, monthly/annual/five-year reporting, ADR, RevPAR, average stay, or period/platform/property comparisons.
3. Shared expenses are not allocated across units/properties.
4. Dashboard totals combine amounts without separating currencies; mixed-currency totals can be misleading.
5. Occupancy is a rough all-time calculation using 365 days per unit; it does not account for availability, owner blocks, date ranges, or overlapping reservations and can exceed 100%.
6. CSV import is generic, not validated against real Airbnb/Booking.com/Vrbo exports, does not detect duplicate imports, and can silently assign unmatched rows to the first property/unit. Quoted multiline CSV fields are not supported reliably.
7. CSV import does not map cleaning charges, payout, reservation status, or all source-specific fields.
8. Some UI strings and select options remain hard-coded rather than translated; matching dictionary keys alone does not prove complete localization.
9. Data is stored only in browser localStorage. There is no account, cloud backup, or multi-device synchronization.
10. No real Android installation test or iOS device test has been completed.

## Release decision
**NOT READY FOR SALE.** The static QA harness is now in the repository, but its execution has not been confirmed. Functional, import-fixture, calculation, accessibility, and real-device testing remain required. This app is not tax software and does not provide tax advice.
