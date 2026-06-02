# Launch Checklist

## Static Page

- [ ] Replace `BOOKING_LINK` in `script.js`.
- [ ] Replace `HUBSPOT_PORTAL_ID` in `script.js`.
- [ ] Replace `HUBSPOT_FORM_ID` in `script.js`.
- [ ] Replace `POSTAL_ADDRESS` in `script.js`.
- [ ] Confirm all navigation links scroll to correct sections.
- [ ] Confirm `Book call` opens the scheduling URL.
- [ ] Confirm primary CTA scrolls to the checklist form.
- [ ] Confirm mobile layout has no horizontal overflow.

## HubSpot

- [ ] Create all required contact properties.
- [ ] Create `Optimism - AI Workflow Risk Checklist` form.
- [ ] Create active list `optimism-funnel-signup`.
- [ ] Create workflow `Optimism - 10 Email Funnel`.
- [ ] Load all 10 emails.
- [ ] Confirm Email 1 sends immediately.
- [ ] Configure lead scoring.
- [ ] Configure hot-lead task creation.
- [ ] Configure stop rules.

## Compliance And Deliverability

- [ ] Add business postal address to every email footer.
- [ ] Add unsubscribe token to every email footer.
- [ ] Authenticate sending domain with SPF.
- [ ] Authenticate sending domain with DKIM.
- [ ] Configure DMARC.
- [ ] Confirm consent checkbox language appears on the form.
- [ ] Confirm unsubscribed contacts are suppressed.

## Pre-Launch Test

- [ ] Submit a test lead.
- [ ] Confirm contact is created or updated in HubSpot.
- [ ] Confirm hidden fields save correctly.
- [ ] Confirm lead enters `optimism-funnel-signup`.
- [ ] Confirm lead score starts at `10`.
- [ ] Confirm Email 1 is sent.
- [ ] Click booking link and confirm score adds `20`.
- [ ] Set lead score to `50+` and confirm task creation.
- [ ] Mark consultation booked and confirm workflow unenrollment.

