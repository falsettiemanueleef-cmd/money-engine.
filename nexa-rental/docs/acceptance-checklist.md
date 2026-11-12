# Acceptance checklist

A release is not commercially ready until each applicable item is verified and the evidence is recorded.

## Calculations
- [ ] Nights and date boundaries tested across month/year changes and leap years.
- [ ] Occupancy denominator correctly handles unit availability and date filters.
- [ ] Overlapping reservations are flagged.
- [ ] Cancelled reservations follow the documented policy.
- [ ] Gross revenue, commission, payout, cleaning, taxes, and expenses are not double counted.
- [ ] Shared-expense allocations reconcile to the source amount.
- [ ] Decimal arithmetic and currency rounding are tested.
- [ ] Period comparisons use equivalent ranges.

## CSV import
- [ ] Header detection and manual mapping work on mobile.
- [ ] Preview shows accepted, rejected, and warning rows before commit.
- [ ] Duplicate detection is explainable and reviewable.
- [ ] Import can be cancelled without partial writes.
- [ ] Re-import behavior is tested.
- [ ] Personal guest data columns are excluded by default.
- [ ] At least one real sample export per supported source is tested when legally and practically available.

## Localization
- [ ] Italian, English, Spanish, French, and German cover every visible UI string.
- [ ] Dates, numbers, currencies, plural forms, and validation messages are localized.
- [ ] Long translations fit mobile layouts.
- [ ] No mixed-language screens remain.

## Mobile and resilience
- [ ] Layout tested at narrow Android viewport.
- [ ] Touch targets and keyboard flows are usable.
- [ ] PWA manifest and service worker verified over HTTPS.
- [ ] Offline behavior is documented and tested.
- [ ] Backup export and restore tested.
- [ ] Data-loss risks are disclosed.
- [ ] iOS behavior is documented separately; do not claim physical iOS testing unless performed.

## Commercial readiness
- [ ] Privacy notice and data-handling description reviewed.
- [ ] Product screenshots and user guide reflect the actual build.
- [ ] No tax/accounting advice claims.
- [ ] Known limitations are disclosed.
- [ ] No sales or public release until owner approval.
