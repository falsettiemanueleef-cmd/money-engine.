# NEXA Rental Profit Manager — working build

## Included
- Properties and units: create, edit and delete.
- Reservations and expenses: create, edit and delete.
- Monthly reservation list.
- Dashboard and date-filtered management report with booked nights, average stay, ADR and estimated RevPAR.
- CSV import with manual column mapping and basic duplicate checks.
- Reservation CSV export and JSON backup/restore.
- Italian, English, Spanish, French and German language selector.

## Important operating notes
- Data is stored only in the current browser on the current device. Export a JSON backup regularly. Clearing browser data can erase records.
- The app does not sync between devices and has no user account or cloud backup.
- Use the same currency for comparable records. Property-linked expenses use the property's currency; unassigned/shared expenses use their selected currency (EUR by default for older records). Shared expenses are not automatically split between properties or units.
- Reports use reservation check-in dates for the selected period. RevPAR is estimated from unit count × period days and does not subtract owner blocks or unavailable nights.
- CSV mapping is generic and has not been certified against all real Airbnb, Booking.com or Vrbo exports. Review imported rows and totals carefully.
- Do not enter guest personal data.
- Some labels and option values may remain in Italian or English when another language is selected.
- No physical iOS test has been completed. Android installation and offline behavior also require a real-device test.
- This is a management aid, not tax/accounting software or tax advice.

## Current release status
Working build for internal testing only. Not approved for paid sale until functional, import, calculation, localization and device testing are completed.
