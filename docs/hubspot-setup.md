# HubSpot Setup

## Required Contact Properties

Create these custom properties before publishing the form.

| Property label | Internal name | Type | Values |
|---|---|---|---|
| Optimism Funnel Signup | `optimism_funnel_signup` | single checkbox | checked/unchecked |
| Workflow Type | `workflow_type` | dropdown | finance or sales operations; proposal or grant package; research memo; board or management report; compliance evidence review; other recurring workflow |
| Biggest AI Concern | `biggest_ai_concern` | dropdown | data boundaries; output quality; human approval; tool access; staff adoption; unclear workflow fit |
| Implementation Timeline | `implementation_timeline` | dropdown | now; next 30 days; next 90 days; later |
| Lead Source | `lead_source` | single-line text | set to `optimism_landing_page` |
| Lead Score | `lead_score` | number | starts at `10` |
| Consultation Booked | `consultation_booked` | single checkbox | checked/unchecked |
| Active Opportunity | `active_opportunity` | single checkbox | checked/unchecked |
| Replied With Workflow | `replied_with_workflow` | single checkbox | checked/unchecked |

## Form

Create a HubSpot form named:

```text
Optimism - AI Workflow Risk Checklist
```

Include these visible fields:

- name
- email
- company
- role
- workflow type
- biggest AI concern
- implementation timeline
- consent checkbox

Set hidden fields:

- `lead_source = optimism_landing_page`
- `lead_score = 10`
- `optimism_funnel_signup = true`

After the form exists, replace these values in `script.js`:

```js
HUBSPOT_PORTAL_ID: "HUBSPOT_PORTAL_ID",
HUBSPOT_FORM_ID: "HUBSPOT_FORM_ID"
```

## Active List

Create an active list named:

```text
optimism-funnel-signup
```

Membership criteria:

```text
optimism_funnel_signup is true
```

Recommended exclusion criteria:

- unsubscribed from marketing email
- `consultation_booked` is true
- `active_opportunity` is true

## Email Workflow

Create workflow:

```text
Optimism - 10 Email Funnel
```

Enrollment trigger:

```text
List membership: optimism-funnel-signup
```

Send cadence:

| Email | Delay after enrollment |
|---:|---|
| 1 | immediately |
| 2 | 1 day |
| 3 | 3 days |
| 4 | 5 days |
| 5 | 8 days |
| 6 | 12 days |
| 7 | 16 days |
| 8 | 21 days |
| 9 | 28 days |
| 10 | 35 days |

Use the email copy in:

```text
funnel/10-email-sequence.md
```

Replace every `{{booking_link}}` token with `BOOKING_LINK` after the real scheduling URL exists.

## Lead Scoring

Configure scoring:

| Signal | Score |
|---|---:|
| signup | +10 |
| opens multiple emails | +5 |
| clicks booking link | +20 |
| replies with workflow | +40 |
| books call | +100 |

Hot lead threshold:

```text
lead_score >= 50
```

When a lead becomes hot, create task:

```text
Follow up: {{company}} AI workflow interest
```

Task note:

```text
Review workflow_type, biggest_ai_concern, implementation_timeline, clicked emails, and book consult.
```

## Stop Rules

Unenroll contact if any condition becomes true:

- `consultation_booked` is true
- `replied_with_workflow` is true
- contact unsubscribes
- `active_opportunity` is true

## Email Footer

Every email must include:

```text
Optimism
POSTAL_ADDRESS
You are receiving this because you requested Optimism resources or updates.
Unsubscribe: HubSpot unsubscribe token
```

Do not launch until `POSTAL_ADDRESS` is replaced with a compliant business mailing address.

