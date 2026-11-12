# NEXA Rental Profit Manager

A mobile-first, installable web application (PWA) for managing short-term rental portfolios. The app is designed for Android and iOS browsers, with a local-first data model and exportable reports.

## Product principles

- Complete portfolio management, not a stripped-down demo.
- Full UI localization: Italian, English, Spanish, French, German.
- Mobile-first layouts and accessible controls.
- Import reservation and expense data from user-exported CSV files; no claim of automatic Airbnb/Booking.com API synchronization.
- Explicit separation of reservation-derived fees and manually entered expenses to prevent double counting.
- Transparent net-profit calculations and audit-friendly source records.
- Privacy by design: collect only operational data required by the user.
- No tax advice or fiscal-compliance claims.

## Current phase

Foundation and specification. No production-ready or tested release is claimed yet. The next implementation stages are data model, calculation engine, CSV staging/import, dashboard, reports, and end-to-end validation.

## Scope and decisions

See:
- [Product specification](docs/product-spec.md)
- [Data model and calculation rules](docs/data-model.md)
- [Acceptance checklist](docs/acceptance-checklist.md)

## Compatibility

Target: current mobile browsers on Android and iOS with PWA installation where supported. iOS device testing is not claimed unless performed on a real iOS device.
