# Optimism Landing Page

Static GitHub Pages landing page for Optimism's backend-free workflow software intake funnel.

## Purpose

Convert interested owner-led businesses into FormSubmit-routed Gmail intake submissions and, when qualified, into booked Workflow Fit Calls for Human-First AI-Assisted Systems Design.

## Local Preview

From this folder:

```powershell
python -m http.server 4173
```

Open:

```text
http://localhost:4173
```

The page is intentionally simple: the website form is the canonical intake. It posts to a static FormSubmit receiver, then reveals the optional worksheet, workflow software brief, and booking link. These values live in `script.js`:

- `CONTACT_EMAIL` - required; approved Gmail inbox for current public launch.
- `WORKSHEET_PDF` - required; points to the fillable one-page AI Workflow Intake prep worksheet in `assets/ai-workflow-fit-worksheet-v1.pdf`.
- `LEAVE_BEHIND_PDF` - required; points to the workflow software leave-behind brief in `assets/optimism-ai-workflow-setup-brief-v1.pdf`.
- `FORM_ENDPOINT` - required; activated FormSubmit AJAX endpoint that routes submissions into Gmail.
- `POSTAL_ADDRESS` - required for commercial email footers.
- `BOOKING_LINK` - optional; use a Google Calendar appointment schedule booking-page URL when ready. When blank, booking CTAs route to the intake form.

## GitHub Pages

This repo includes `.github/workflows/pages.yml`. After pushing to GitHub:

1. Open repository settings.
2. Go to `Pages`.
3. Set source to `GitHub Actions`.
4. Run the workflow or push to `main`.

The workflow uploads the static repo root as the Pages artifact.

## Gmail-Only Funnel

Use `docs/gmail-only-setup.md` for the current operating path:

- static FormSubmit intake with mailto fallback
- optional fillable PDF prep worksheet
- workflow software leave-behind PDF
- Google Calendar appointment schedule as the booking link
- Gmail label and reply triage
- manual opt-out suppression
- custom-domain email migration notes

The old HubSpot setup notes remain in `docs/hubspot-setup.md` as a paused archive, not the current launch path. The funnel source copy still lives in `funnel/`.

## Visual Reference

The approved concept reference is stored at:

```text
docs/landing-page-concept.png
```

Implementation intentionally changes the hero copy to:

```text
Custom Workflow Software.
Human-First Systems.
AI Where It Helps.
```
