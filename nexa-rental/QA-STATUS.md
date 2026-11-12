# NEXA Rental Profit Manager — QA audit

Audit date: 2026-11-12
Branch: `nexa-rental-foundation`

## Implemented in the current working build
- Property and unit creation, editing and deletion.
- Reservation and expense creation, editing and deletion.
- Basic month selector with a list of reservations intersecting the selected month.
- Date-filtered management report with booked nights, average stay, ADR and estimated RevPAR.
- Dashboard and reports grouped by property currency; shared/unassigned expenses have an explicit currency field and default to EUR for older records.
- CSV import with manual column mapping, name matching and basic duplicate detection.
- JSON backup/restore and reservation CSV export.
- Five initial language dictionaries (IT/EN/ES/FR/DE), plus translated labels for the new calendar/report functions.
- Static QA script and GitHub Actions workflow are present.

## Execution status
The latest source changes have been committed, but no successful GitHub Actions run has been confirmed in the available connector results. Static JavaScript parsing, browser interaction, calculations, import fixtures and device tests must therefore be treated as **not yet verified**.

## Remaining blockers before Etsy sale
1. The calendar is a month-filtered reservation list, not a full visual availability calendar; owner blocks and availability rules are absent.
2. Period reports are manually date-filtered. There are no automatic monthly/annual/five-year summaries or period/platform/property comparison screens.
3. Shared expenses can be recorded with a currency but are not allocated across units or properties. Do not use unassigned shared expenses for per-property profitability.
4. RevPAR is an estimate based on the number of units multiplied by the selected period length (or 365 days when no full range is selected); it does not account for blocked/unavailable nights.
5. CSV import remains generic. Real Airbnb/Booking.com/Vrbo export fixtures have not been tested; source-specific fields and formats may need manual mapping.
6. UI localization is incomplete: some form options, status values, category names, validation prompts and operational messages remain hard-coded or partially translated.
7. Data remains in browser localStorage. There is no account, cloud backup, or multi-device synchronization.
8. No real Android installation test or iOS device test has been completed. iOS is untested.
9. No browser-based functional test or verified automated QA run has been recorded.

## Release decision
**NOT READY FOR PAID ETSY RELEASE.** The build has gained core editing, calendar-list and reporting functions, but the remaining limitations and unverified tests are material. It must not be advertised as a fully tested professional property-management platform. It is not tax software and does not provide tax advice.
