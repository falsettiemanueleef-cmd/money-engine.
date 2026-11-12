# NEXA Rental Profit Manager — QA audit

Audit date: 2026-11-12
Branch: `nexa-rental-foundation`

## Implemented in the current working build
- Property and unit creation, editing and deletion.
- Reservation and expense creation, editing and deletion.
- Month-filtered reservation list.
- Currency-separated dashboard and date-filtered report with booked nights, average stay, ADR, estimated RevPAR, and monthly, annual, property and channel breakdown tables.
- Revenue, commissions, expenses and operating result shown separately.
- Reservation CSV import with manual column mapping, property/unit matching, basic duplicate detection, date/amount validation and overlap rejection.
- Reservation CSV export, expense CSV export and JSON backup/restore.
- IT/EN/ES/FR/DE language selector; several previously hard-coded status, channel and expense category labels have been localized.
- Static QA script and GitHub Actions workflow, with additional source assertions.

## Execution status
Latest changes are committed, but a successful GitHub Actions run has **not** been confirmed in the available results. The connector's commit-run lookup only returned pull-request-triggered runs and showed none. Static JavaScript parsing, browser interaction, calculations, import fixtures and device tests must therefore be treated as **not yet verified**.

## Remaining blockers before Etsy sale
1. The calendar is a month-filtered reservation list, not a full visual availability calendar; owner blocks and availability rules are absent.
2. Reports are manually date-filtered and include month/year/property/channel breakdowns, but there is no dedicated comparison of two separately selected date ranges or a five-year preset.
3. Shared expenses can be recorded with a currency but are not allocated across units or properties. Do not use unassigned shared expenses for per-property profitability.
4. RevPAR is an estimate based on unit count × period length (or 365 days when no range is selected); unavailable nights and owner blocks are not subtracted.
5. CSV import is generic. Real Airbnb/Booking.com/Vrbo export fixtures have not been tested; source-specific formats may need manual mapping.
6. UI localization remains incomplete: some prompts, validation messages, labels and operational messages remain hard-coded or partially translated.
7. Data remains in browser localStorage. There is no account, cloud backup or multi-device synchronization.
8. No real Android installation test or iOS device test has been completed. iOS is untested.
9. No browser-based functional test or verified automated QA run has been recorded.
10. The repository is public; the source code is not protected as a paid download. No Etsy-ready ZIP/release package or access-control mechanism has been prepared.

## Release decision
**NOT READY FOR PAID ETSY RELEASE.** Core management functions have been expanded, but the remaining limitations and unverified tests are material. Do not advertise this as a fully tested professional property-management platform. It is not tax software and does not provide tax advice.
