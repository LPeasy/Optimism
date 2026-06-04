# Gmail-Only Funnel Setup

Status: active current path as of 2026-06-04.

## Decision

Do not wire the landing page to HubSpot for now. The site stays static. Website intake submissions post to a backend-free FormSubmit receiver that routes into `CONTACT_EMAIL`, then Gmail labels, CRM tracker rows, and manual reply checks control the funnel.

## Current Website Configuration

Set these values in `script.js`:

```js
CONTACT_EMAIL: "lawtonperret96@gmail.com",
WORKSHEET_PDF: "assets/ai-workflow-fit-worksheet-v1.pdf",
LEAVE_BEHIND_PDF: "assets/optimism-ai-workflow-setup-brief-v1.pdf",
FORM_ENDPOINT: "https://formsubmit.co/ajax/bc798d040aeefaf78c24be24823c8867",
BOOKING_LINK: "https://calendar.google.com/calendar/u/0/appointments/schedules/AcZssZ2dqa5JcpExEoYPi5aPzILSfjcMrg64iFwFj3I3nDGNhPyYU6X4eZz817pbKwzU8_lEPSedoell",
POSTAL_ADDRESS: "959 Prudential Drive, Jacksonville, FL 32207"
```

`CONTACT_EMAIL` is approved for the current public launch. Replace it with the custom-domain sender after the business email setup is complete.

`WORKSHEET_PDF` points to the optional fillable one-page prep worksheet. The worksheet helps the respondent identify business context, current AI friction, the workflow they would improve first, desired outcome, control gaps, and call fit. The website form remains the canonical intake record.

`LEAVE_BEHIND_PDF` points to the sales/proof brief. It explains the offer, GOV gate, ExampleCo synthetic demo, proof metrics, and next step. It is not an intake form.

`FORM_ENDPOINT` uses FormSubmit's activated AJAX receiver token. The initial activation email was received and the endpoint was activated on 2026-06-04.

Activation evidence: controlled submission `Optimism FormSubmit Activation Test` reached Gmail with all intake fields after activation. After publishing, run one public-URL smoke test because the activation flow was completed from the local preview URL.

`BOOKING_LINK` is active. Booking CTAs open the Google Calendar appointment schedule.

Custom-domain and Google Workspace setup is tabled for the current showtime pass. Do not block landing-page readiness on that task. Revisit it before the next outbound outreach batch.

## Google Calendar Scheduler

Use Google Calendar appointment schedules as the lightweight scheduler. Current active schedule: `Optimism Workflow Fit Call`.

Recommended setup:

- Created one appointment schedule named `Optimism Workflow Fit Call`.
- Duration is 20 minutes.
- Availability is weekdays, 9:00 AM to 5:00 PM.
- Minimum lead time is 24 hours, buffer time is 15 minutes, and maximum bookings per day is 2.
- Location is Google Meet.
- Custom booking form question: `What workflow are you trying to improve?`
- If available on the account tier, require email verification to reduce spam bookings.
- Booking page URL is pasted into `BOOKING_LINK` in `script.js`.

Google Calendar can work alone as the scheduler. Gmail still controls the outreach and reply workflow. The site should not use HubSpot for booking, scoring, or enrollment while this path is active.

## Recommended Business Email Path

Best fit: buy or use a custom domain and run it through Google Workspace Business Starter.

Why this path:

- It keeps Gmail as the daily inbox.
- It gives Optimism a real sender such as `lawton@your-domain.com`.
- A single user can also have no-cost aliases such as `hello@your-domain.com`, `founder@your-domain.com`, or `intake@your-domain.com`.
- It avoids the deliverability weakness of forwarding-only services that cannot send authenticated outbound mail.

Official references checked on 2026-06-04:

- Google Workspace pricing and Starter features: `https://workspace.google.com/pricing.html`
- Google Workspace aliases: `https://support.google.com/a/answer/33327`
- Gmail send-as settings: `https://support.google.com/mail/answer/22370`

## Alternatives

Stopgap: keep the current Gmail account, update the display name to `Lawton Perret | Optimism`, and use the existing Gmail labels. This costs nothing but still exposes a consumer Gmail address.

Cheap inbound-only: use Cloudflare Email Routing to forward `hello@your-domain.com` into Gmail. This is not enough for outreach because Cloudflare Email Routing forwards inbound mail only and does not provide outbound SMTP.

Non-Gmail hosted email: Zoho Mail or Proton Mail can host custom-domain email. These can be credible, but they move operations away from the Gmail-first system unless forwarding and SMTP are added.

## Gmail Operating Rules

- Gmail label: `Optimism/Website Intake`.
- Daily weekday rule: check the intake label once per business day.
- Intake handling rule: add qualified website intake leads to the CRM tracker before any follow-up.
- Search and triage replies under `Optimism/Cold Outreach`.
- Use response labels for `Needs Reply`, `Call Interest`, `Referral Route`, `Opt Out`, and `Bounce Bad Route`.
- Expect intake submissions from FormSubmit after the endpoint is activated.
- Record qualified inbound website intake submissions in the CRM tracker before follow-up.
- Review the intake answers before proposing a Workflow Fit Call; the form is meant to help the respondent identify their needs, not just request a download.
- Stop follow-up if a reply, booked call, opt-out, no, active opportunity, procurement route, legal route, vendor-registration route, or bad route appears.
- Draft replies only with explicit approval. Do not auto-send.

## Custom-Domain Setup Checklist

1. Choose the domain and email pattern.
2. Create the Google Workspace user, likely `lawton@...`.
3. Add aliases for public-facing addresses, likely `hello@...` and `intake@...`.
4. Configure SPF, DKIM, and DMARC before sending outreach.
5. In Gmail, set the business address as the default `From` and reply-to address.
6. Send tests to Gmail and Outlook recipients.
7. Update `CONTACT_EMAIL` in `script.js`.
8. Create the Google Calendar appointment schedule under the same business identity if possible.
9. Update `BOOKING_LINK` in `script.js` with the booking page URL.
10. Update future outreach templates. Do not rewrite historical sent-message records.

## Compliance Notes

Commercial email still needs accurate sender identity, a valid physical postal address, and a clear opt-out mechanism. Keep the postal address and opt-out line in outreach signatures until a better compliance address and unsubscribe flow are chosen.
