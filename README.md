# Optimism Landing Page

Static GitHub Pages landing page for Optimism's `AI Workflow Risk Checklist`.

## Purpose

Convert interested visitors into HubSpot contacts tagged for the Optimism email funnel and, when qualified, into booked Workflow Fit Calls.

## Local Preview

From this folder:

```powershell
python -m http.server 4173
```

Open:

```text
http://localhost:4173
```

The page is intentionally launch-blocked until these values are replaced in `script.js`:

- `BOOKING_LINK`
- `HUBSPOT_PORTAL_ID`
- `HUBSPOT_FORM_ID`
- `POSTAL_ADDRESS`

## GitHub Pages

This repo includes `.github/workflows/pages.yml`. After pushing to GitHub:

1. Open repository settings.
2. Go to `Pages`.
3. Set source to `GitHub Actions`.
4. Run the workflow or push to `main`.

The workflow uploads the static repo root as the Pages artifact.

## HubSpot Funnel

Use `docs/hubspot-setup.md` to create:

- HubSpot form
- `optimism-funnel-signup` active list
- required contact properties
- 10-email sequence workflow
- lead scoring
- stop rules

The funnel source copy lives in `funnel/`.

## Visual Reference

The approved concept reference is stored at:

```text
docs/landing-page-concept.png
```

Implementation intentionally changes the hero copy to:

```text
Modern Workflows,
Transparent Designs,
Human Relationships.
Click to see if we can help you grow ->
```

