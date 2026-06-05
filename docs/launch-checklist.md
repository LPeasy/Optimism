# Launch Checklist

## Static Page

- [x] Confirm `CONTACT_EMAIL` in `script.js` points to the approved public-launch Gmail inbox.
- [x] Confirm `WORKSHEET_PDF` in `script.js` points to the optional fillable AI Workflow Intake prep worksheet.
- [x] Confirm `LEAVE_BEHIND_PDF` in `script.js` points to the workflow software brief.
- [x] Confirm `FORM_ENDPOINT` in `script.js` points to the backend-free FormSubmit AJAX receiver.
- [x] Confirm `POSTAL_ADDRESS` in `script.js` is the approved business mailing address.
- [x] Point `BOOKING_LINK` to the Google Calendar appointment schedule booking-page URL.
- [ ] Confirm all navigation links scroll to correct sections.
- [x] Confirm `Book call` and `Book a fit call` open the Google Calendar booking page.
- [ ] Confirm primary CTA scrolls to the intake form.
- [x] Confirm mobile layout has no horizontal overflow.

## Gmail-Only Intake

- [x] Create the one-page fillable `AI Workflow Intake Worksheet v1` prep PDF.
- [x] Create the `Optimism Workflow Software Brief v1` leave-behind PDF.
- [x] Wire the page form around business context, current tools, current AI use, AI challenge, workflow candidate, desired result, control gap, timeline, budget readiness, and offer focus.
- [x] Hide the worksheet and sales/proof brief until after a successful intake submission.
- [x] Submit the first live FormSubmit activation test from the page.
- [x] Activate the FormSubmit endpoint from the Gmail activation email.
- [x] Submit a test intake request from the page.
- [x] Confirm the receiver sends the intake to `CONTACT_EMAIL`.
- [x] Confirm the generated receiver payload includes the worksheet URL, sales brief URL, and intake answers.
- [x] Send the test request only from a controlled test account.
- [x] Confirm the request is visible in Gmail.
- [x] Create Gmail label: `Optimism/Website Intake`.
- [x] Apply `Optimism/Website Intake` to current `AI Workflow Intake` test messages.
- [x] Mark current `AI Workflow Intake` test messages important.
- [x] Create the Gmail web filter for future messages: from `submissions@formsubmit.co`, subject `AI Workflow Intake`, apply `Optimism/Website Intake`, mark important, never send to spam.
- [ ] Record real inbound requests in the CRM tracker before follow-up.
- [ ] Suppress any contact that opts out or says no.

## Business Email

- [x] Table custom-domain and Google Workspace setup for the current showtime pass.
- [ ] Keep the current Gmail fallback in `CONTACT_EMAIL` until a business sender is chosen later.
- [ ] Before the next outbound outreach batch, revisit custom-domain sender, aliases, SPF, DKIM, and DMARC.

## Google Calendar Scheduler

- [x] Create a Google Calendar appointment schedule from a computer.
- [x] Use title `Optimism Workflow Fit Call`.
- [x] Set duration, availability, minimum lead time, buffer time, and maximum bookings per day.
- [x] Choose Google Meet as the meeting location.
- [x] Add booking form field: `What workflow are you trying to improve?`
- [ ] Require email verification if the account tier supports it.
- [x] Copy the booking page URL and paste it into `BOOKING_LINK` in `script.js`.
- [x] Confirm `Book call` and `Book a fit call` open the Google Calendar booking page.

## Compliance And Deliverability

- [ ] Add the approved business postal address to every commercial email footer.
- [ ] Include a clear opt-out line in every commercial email.
- [ ] Honor opt-outs before any follow-up draft or send.
- [ ] Keep sender identity accurate and consistent.
- [ ] Do not use HubSpot enrollment, scoring, or automated sequence logic for the current funnel.

## Pre-Launch Test

- [x] Start a local preview.
- [x] Submit the form with all fields completed.
- [x] Confirm required-field validation works.
- [x] Confirm generated receiver payload contains name, email, company, role, business summary, tools used, AI use, AI challenge, workflow candidate, workflow type, desired result, concern, timeline, budget readiness, offer focus, consent, worksheet PDF URL, sales brief URL, source, and lead score.
- [x] Confirm footer displays the approved postal address.
- [x] Confirm no HubSpot script loads in the browser.
- [x] After publishing, submit one public-URL smoke test to confirm the activated FormSubmit endpoint accepts the production page URL.
