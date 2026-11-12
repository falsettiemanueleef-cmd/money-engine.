# Product specification — NEXA Rental Profit Manager

## 1. Intended user and value

Owners and small operators of short-term rental properties who need a reliable view of revenue, costs, occupancy, and net operating performance across multiple units and booking channels.

## 2. Platforms and languages

- Primary delivery: responsive installable PWA.
- Android and iOS mobile browser support is a design target.
- Languages: Italian (it), English (en), Spanish (es), French (fr), German (de).
- All user-facing strings must be localized: navigation, forms, validation, empty states, import instructions, errors, confirmations, report labels, and help text.
- No untranslated hard-coded UI strings.

## 3. Functional modules

### Portfolio
- Create, edit, archive properties.
- Manage multiple units per property.
- Store property currency and timezone; portfolio reporting must disclose currency conversions if added in a future phase.

### Reservations and calendar
- Create, edit, cancel, and archive reservations.
- Fields: property/unit, channel, external booking reference (optional), arrival/departure, nights, gross booking amount, discounts, cleaning fee charged, platform commission, taxes/withholding where explicitly supplied, payout, status.
- Validate departure after arrival and derive nights consistently.
- Calendar views: month and agenda/list, with mobile-friendly navigation.

### Revenue and payouts
- Separate gross booking value, platform fees, cleaning charges, taxes/withholding, and payout.
- Support direct bookings and manual entries.
- Never infer tax treatment from a label; allow user-defined categories and disclaimers.

### Expenses
- Expense categories include cleaning, maintenance, utilities, supplies, insurance, property fees, travel/mileage, and custom categories.
- Support one-property, one-unit, and shared expenses.
- Shared expense allocation methods: equal split, by nights, by revenue, or custom percentage; store the allocation method and resulting allocations.
- Expense records include date, amount, currency, category, payee/description, allocation scope, and optional receipt reference.

### CSV import
- Import files exported by the user from Airbnb, Booking.com, Vrbo, and direct-booking tools when a compatible CSV is available.
- Use a staging preview: detect headers, allow field mapping, show parsed rows and validation warnings before committing.
- Provide duplicate detection using channel + external reference where available; fallback matching must be explicitly marked as heuristic.
- Store import batch ID and source filename for traceability.
- Never claim live API synchronization.
- Import reservation data separately from expense data unless the file mapping explicitly identifies expense rows.
- Prevent double counting: if platform commission or cleaning fee is already captured on a reservation, the same amount must not be added again as an expense without an explicit override.

### Analytics and dashboard
- Revenue, expenses, net operating result, occupancy, average length of stay, average daily rate, and revenue per available unit-night.
- Filters: date range, property, unit, booking channel.
- Monthly and annual summaries; five-year view where sufficient data exists.
- Period comparisons must compare equivalent date ranges and disclose missing/incomplete data.
- Exclude cancelled reservations from occupied nights and revenue unless user explicitly records retained cancellation income.

### Reports and exports
- Export filtered data to CSV.
- Export summary reports in a printable format.
- Export/restore a complete JSON backup.
- Provide a clear report methodology and included/excluded categories.

### Settings and help
- Language, currency display, timezone, custom categories, allocation preferences, backup/restore, privacy information.
- In-app guidance for importing common CSV layouts.

## 4. Calculation definitions

- Nights = departure date minus arrival date.
- Occupied nights = sum of nights for eligible reservations, avoiding overlap per unit.
- Occupancy = occupied unit-nights / available unit-nights for the selected period.
- Gross booking revenue = reservation gross amount before platform commission, with cleaning and taxes shown separately when the source supports the distinction.
- Net operating result = recognized operating revenue minus recognized operating expenses. Payout is a cash settlement measure, not additional revenue.
- ADR = eligible accommodation revenue / occupied nights.
- RevPAN = eligible accommodation revenue / available unit-nights.
- All metrics must document treatment of cleaning, taxes, refunds, cancellations, and owner-blocked dates.

## 5. Non-goals and limits

- Not accounting, tax filing, or legal advice.
- No automatic connection to Airbnb, Booking.com, Vrbo, bank accounts, or payment processors in the initial release.
- No scraping of private accounts.
- No guest passport, identity-document, or payment-card storage.
- No claim of native App Store / Play Store publication.

## 6. Commercial quality bar

The product is not ready for sale until core calculations, import mapping, duplicate handling, localization completeness, backup/restore, mobile usability, and documented limitations pass the acceptance checklist.
