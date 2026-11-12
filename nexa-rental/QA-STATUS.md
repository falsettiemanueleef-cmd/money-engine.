# NEXA Rental Profit Manager — QA audit

Audit date: 2026-11-12
Branch: `nexa-rental-foundation`

## Implemented in the current working build
- Property and unit creation, editing and deletion.
- Reservation and expense creation, editing and deletion.
- Month-filtered reservation list.
- Currency-separated dashboard and date-filtered report with booked nights, average stay, ADR, estimated RevPAR, and monthly, annual, property and channel breakdown tables.
- Revenue, commissions, expenses and operating result shown separately; property-level results use direct expenses only and explicitly exclude unallocated shared expenses.
- Reservation CSV import with manual column mapping, property/unit matching, basic duplicate detection, date/amount validation and overlap rejection.
- Reservation CSV export, expense CSV export and JSON backup/restore.
- IT/EN/ES/FR/DE language selector; several previously hard-coded status, channel and expense category labels have been localized.
- Static QA script and GitHub Actions workflow, with additional source assertions.

## Execution status
GitHub Actions run #37 (12 Nov 2026) completed the static QA and ZIP packaging steps successfully. The JavaScript parser, service-worker parser, manifest validation, translation-key parity and static feature assertions passed. The resulting ZIP was downloaded and its archive integrity and file list were independently checked. This is static validation only: browser interaction, calculation fixtures, real-world CSV imports and device tests remain **not yet verified**.

## Remaining blockers before Etsy sale
1. The calendar is a month-filtered reservation list, not a full visual availability calendar; owner blocks and availability rules are absent.
2. Reports are manually date-filtered and include month/year/property/channel breakdowns, but there is no dedicated comparison of two separately selected date ranges or a five-year preset.
3. Shared expenses can be recorded with a currency but are not allocated across units or properties. Do not use unassigned shared expenses for per-property profitability.
4. RevPAR is an estimate based on unit count × period length (or 365 days when no range is selected); unavailable nights and owner blocks are not subtracted.
5. CSV import is generic. Real Airbnb/Booking.com/Vrbo export fixtures have not been tested; source-specific formats may need manual mapping.
6. UI localization remains incomplete: some prompts, validation messages, labels and operational messages remain hard-coded or partially translated.
7. Data remains in browser localStorage. There is no account, cloud backup or multi-device synchronization.
8. No real Android installation test or iOS device test has been completed. iOS is untested.
9. No browser-based functional test, calculation fixture suite, real-world CSV fixture test, or Android/iOS device test has been recorded.
10. The repository is public; the source code is not protected as a paid download. A ZIP package has been assembled and integrity-checked, but it is a beta source kit, not a protected hosted application or a fully validated turnkey product.

## Release decision
**NOT READY FOR PAID ETSY RELEASE.** Core management functions have been expanded, but the remaining limitations and unverified tests are material. Do not advertise this as a fully tested professional property-management platform. It is not tax software and does not provide tax advice.
