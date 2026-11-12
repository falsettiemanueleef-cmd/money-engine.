# Data model and calculation safeguards

## Core entities

- Property: id, name, address label (optional), timezone, reporting currency, status.
- Unit: id, property_id, name, capacity (optional), status.
- Reservation: id, property_id, unit_id, channel, external_reference, guest_label (optional and non-identifying), arrival, departure, status, accommodation_gross, cleaning_fee_charged, taxes_collected, platform_commission, payout, currency, source_batch_id.
- Expense: id, date, category_id, amount, currency, description, scope_type, property_id, unit_id, allocation_rule, source_batch_id, linked_reservation_id (optional), duplicate_key.
- ExpenseAllocation: expense_id, property_id, unit_id, allocated_amount, allocation_basis.
- ImportBatch: id, source_type, filename, imported_at, row_count, accepted_count, rejected_count, mapping_profile.
- Category: id, localized_name_key, kind (revenue/expense), active.
- AvailabilityBlock: id, unit_id, start_date, end_date, reason.
- AuditEvent: id, entity_type, entity_id, action, timestamp, summary.

## Data integrity rules

1. Every reservation belongs to one property and one unit.
2. Departure must be later than arrival.
3. Monetary values are decimal-safe; never use binary floating-point for financial arithmetic.
4. Currency is stored with every monetary record.
5. A payout is not booked as new revenue if the underlying reservation revenue is already recognized.
6. Platform commission is represented once: either as a reservation deduction or as a linked expense, never both in net result.
7. Cleaning charged to the guest is revenue; cleaning paid to a cleaner is an expense. These are distinct events and must not be conflated.
8. Imported rows retain source batch metadata.
9. Duplicate detection is reviewable; uncertain matches are warnings, not silent deletions.
10. Shared expenses must reconcile: sum of allocations equals the original expense amount within the currency's minor-unit precision.

## Net result policy

For each reservation, the report must show accommodation revenue and separately itemized additional charges where supplied. Platform commission reduces operating result once. Expense records reduce operating result once. Payout is used for reconciliation only.

A configuration may choose whether guest-collected cleaning fees are included in revenue, but the corresponding cleaning supplier expense remains separate. The report must label this treatment.

## Date and occupancy policy

Use property-local dates for stays and availability. Occupied nights are counted per unit and date. Overlapping eligible reservations on the same unit must trigger a conflict warning and must not silently inflate occupancy. Availability blocks reduce available nights only when the selected metric configuration says owner-blocked dates are excluded.

## Privacy

Do not require guest full names, email addresses, phone numbers, identity documents, or payment card details. If a channel export contains personal data, discard those columns by default and explain the behavior before import.
