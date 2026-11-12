# NEXA Rental Profit Manager — working build

## Included
- Properties and units: create, edit and delete.
- Reservations and expenses: create, edit and delete.
- Monthly reservation list.
- Dashboard grouped by property currency.
- Date-filtered management report with booked nights, average stay, ADR and estimated RevPAR, plus revenue, commission, expense and operating-result totals.
- CSV import with manual column mapping, property/unit matching, basic duplicate detection and overlap rejection.
- Reservation CSV export, expense CSV export and JSON backup/restore.
- Italian, English, Spanish, French and German language selector; selected labels, categories and status values are localized.

## Important operating notes
- Data is stored only in the current browser on the current device. Export a JSON backup regularly. Clearing browser data can erase records.
- The app does not sync between devices and has no user account or cloud backup.
- Use the same currency for comparable records. Property-linked expenses use the property's currency; unassigned/shared expenses use their selected currency (EUR by default for older records). Shared expenses are not automatically split between properties or units.
- Reports include reservations by check-in date in the selected range and expenses by expense date. Select both dates or leave both empty.
- ADR and RevPAR use accommodation revenue only, excluding cleaning charges. RevPAR is estimated from unit count × selected period days (or 365 days when no range is selected); owner blocks and unavailable nights are not subtracted.
- CSV mapping is generic and has not been certified against all real Airbnb, Booking.com or Vrbo exports. Review imported rows and totals carefully.
- Do not enter guest personal data.
- Some labels, prompts and operational messages may remain in Italian or English when another language is selected.
- No physical iOS test has been completed. Android installation and offline behavior also require a real-device test.
- This is a management aid, not tax/accounting software or tax advice.

## Current release status
Working build for internal testing only. Not approved for paid sale until functional, import, calculation, localization and device testing are completed.
