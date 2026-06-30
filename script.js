const CONFIG = {
  CONTACT_EMAIL: "lawtonperret96@gmail.com",
  WORKSHEET_PDF: "assets/ai-workflow-fit-worksheet-v1.pdf",
  LEAVE_BEHIND_PDF: "assets/optimism-ai-workflow-setup-brief-v1.pdf",
  FORM_ENDPOINT: "https://formsubmit.co/ajax/bc798d040aeefaf78c24be24823c8867",
  BOOKING_LINK: "https://calendar.google.com/calendar/u/0/appointments/schedules/AcZssZ2dqa5JcpExEoYPi5aPzILSfjcMrg64iFwFj3I3nDGNhPyYU6X4eZz817pbKwzU8_lEPSedoell",
  POSTAL_ADDRESS: "959 Prudential Drive, Jacksonville, FL 32207"
};

const placeholders = new Set([
  "CONTACT_EMAIL",
  "WORKSHEET_PDF",
  "LEAVE_BEHIND_PDF",
  "FORM_ENDPOINT",
  "BOOKING_LINK",
  "POSTAL_ADDRESS"
]);

const attributionKeys = ["utm_source", "utm_medium", "utm_campaign", "utm_content"];
const payloadFieldNames = [
  "capture_type",
  "name",
  "email",
  "company",
  "role",
  "business_summary",
  "tools_used",
  "current_ai_use",
  "current_ai_challenge",
  "workflow_candidate",
  "workflow_type",
  "desired_result",
  "biggest_ai_concern",
  "implementation_timeline",
  "budget_readiness",
  "offer_focus",
  "consent",
  "lead_score",
  "optimism_funnel_signup"
];

function isPlaceholder(value) {
  return !value || placeholders.has(value);
}

function hasValue(key) {
  return !isPlaceholder(CONFIG[key]);
}

function absoluteAssetUrl(path) {
  return new URL(path, window.location.href).href;
}

function worksheetPdfUrl() {
  return hasValue("WORKSHEET_PDF") ? absoluteAssetUrl(CONFIG.WORKSHEET_PDF) : "";
}

function leaveBehindPdfUrl() {
  return hasValue("LEAVE_BEHIND_PDF") ? absoluteAssetUrl(CONFIG.LEAVE_BEHIND_PDF) : "";
}

function bookingUrl() {
  return hasValue("BOOKING_LINK") ? CONFIG.BOOKING_LINK : "";
}

function campaignAttribution() {
  const params = new URLSearchParams(window.location.search);
  return attributionKeys.reduce((values, key) => {
    values[key] = params.get(key)?.trim() || "";
    return values;
  }, {});
}

function campaignLeadSource(form) {
  const attribution = campaignAttribution();
  if (attribution.utm_source.toLowerCase() === "linkedin" && attribution.utm_medium.toLowerCase() === "organic") {
    return "linkedin_organic";
  }
  return attribution.utm_source || formValue(form, "lead_source") || "optimism_landing_page";
}

function applyCampaignAttribution() {
  const attribution = campaignAttribution();
  attributionKeys.forEach((key) => {
    document.querySelectorAll(`[name='${key}']`).forEach((field) => {
      field.value = attribution[key];
    });
  });

  document.querySelectorAll("[name='source_page_url']").forEach((field) => {
    field.value = window.location.href;
  });

  document.querySelectorAll("[name='lead_source']").forEach((field) => {
    if (attribution.utm_source.toLowerCase() === "linkedin" && attribution.utm_medium.toLowerCase() === "organic") {
      field.value = "linkedin_organic";
    }
  });
}

function applyWorksheetLinks() {
  const ready = hasValue("WORKSHEET_PDF");
  document.querySelectorAll("[data-worksheet-pdf]").forEach((link) => {
    if (ready) {
      link.setAttribute("href", CONFIG.WORKSHEET_PDF);
      link.setAttribute("target", "_blank");
      link.setAttribute("rel", "noopener");
    } else {
      link.setAttribute("href", "#intake-form");
      link.removeAttribute("target");
      link.removeAttribute("rel");
    }
  });
}

function applyLeaveBehindLinks() {
  const ready = hasValue("LEAVE_BEHIND_PDF");
  document.querySelectorAll("[data-leavebehind-pdf]").forEach((link) => {
    if (ready) {
      link.setAttribute("href", CONFIG.LEAVE_BEHIND_PDF);
      link.setAttribute("target", "_blank");
      link.setAttribute("rel", "noopener");
    } else {
      link.setAttribute("href", "#intake-form");
      link.removeAttribute("target");
      link.removeAttribute("rel");
    }
  });
}

function applyBookingLinks() {
  const ready = hasValue("BOOKING_LINK");
  document.querySelectorAll("[data-booking-link]").forEach((link) => {
    link.setAttribute("href", ready ? CONFIG.BOOKING_LINK : "#intake-form");
    if (ready) {
      link.setAttribute("target", "_blank");
      link.setAttribute("rel", "noopener");
    } else {
      link.removeAttribute("target");
      link.removeAttribute("rel");
    }
  });
}

function applyPostalAddress() {
  const addressTarget = document.getElementById("postal-address");
  if (!addressTarget) return;
  addressTarget.textContent = hasValue("POSTAL_ADDRESS")
    ? CONFIG.POSTAL_ADDRESS
    : "POSTAL_ADDRESS";
}

function updateSetupWarning() {
  const warning = document.getElementById("setup-required");
  if (!warning) return;

  const requiredMissing = ["CONTACT_EMAIL", "WORKSHEET_PDF", "LEAVE_BEHIND_PDF", "FORM_ENDPOINT", "POSTAL_ADDRESS"].filter(
    (key) => !hasValue(key)
  );

  if (requiredMissing.length === 0) {
    warning.hidden = true;
    warning.classList.add("is-ready");
    warning.textContent = hasValue("BOOKING_LINK")
      ? "Website intake receiver, post-submit assets, and booking links are configured."
      : "Website intake receiver and post-submit assets are configured. Booking links route to this form until a scheduling URL is added.";
    return;
  }

  warning.hidden = false;
  warning.classList.remove("is-ready");
  warning.innerHTML = `Launch blocked until ${requiredMissing
    .map((key) => `<code>${key}</code>`)
    .join(", ")} ${requiredMissing.length === 1 ? "is" : "are"} replaced.`;
}

function formValue(form, name) {
  const field = form.elements[name];
  if (!field) return "";
  if (field.type === "checkbox") return field.checked ? "yes" : "no";
  return field.value.trim();
}

function captureType(form) {
  return formValue(form, "capture_type") || "workflow_full_intake";
}

function captureSubjectPrefix(form) {
  return captureType(form) === "workflow_quick_capture"
    ? "AI Workflow Quick Capture"
    : "AI Workflow Intake";
}

function buildIntakeEmail(form) {
  const name = formValue(form, "name");
  const company = formValue(form, "company");
  const attribution = campaignAttribution();
  const leadSource = campaignLeadSource(form);
  const subject = `${captureSubjectPrefix(form)} - ${company || name || "Optimism lead"}`;
  return {
    subject,
    body: [
    `New ${captureSubjectPrefix(form)}`,
    "",
    `Capture type: ${captureType(form)}`,
    `Name: ${name}`,
    `Email: ${formValue(form, "email")}`,
    `Company: ${company}`,
    `Role: ${formValue(form, "role")}`,
    `Business or team summary: ${formValue(form, "business_summary")}`,
    `Tools already used: ${formValue(form, "tools_used")}`,
    `Current AI use: ${formValue(form, "current_ai_use")}`,
    `Current AI challenge or need: ${formValue(form, "current_ai_challenge")}`,
    `Workflow to improve first: ${formValue(form, "workflow_candidate")}`,
    `Workflow type: ${formValue(form, "workflow_type")}`,
    `Desired result: ${formValue(form, "desired_result")}`,
    `Biggest control gap or AI concern: ${formValue(form, "biggest_ai_concern")}`,
    `Implementation timeline: ${formValue(form, "implementation_timeline")}`,
    `Budget readiness: ${formValue(form, "budget_readiness")}`,
    `Offer focus: ${formValue(form, "offer_focus")}`,
    `Consent: ${formValue(form, "consent")}`,
    `Lead source: ${leadSource}`,
    `UTM source: ${attribution.utm_source}`,
    `UTM medium: ${attribution.utm_medium}`,
    `UTM campaign: ${attribution.utm_campaign}`,
    `UTM content: ${attribution.utm_content}`,
    `Source page URL: ${window.location.href}`,
    "",
    "Post-submit assets",
    `Optional worksheet: ${worksheetPdfUrl()}`,
    `Sales brief: ${leaveBehindPdfUrl()}`,
    `Booking link: ${bookingUrl()}`,
    "",
    `Source: ${leadSource}`,
    `Lead score: ${formValue(form, "lead_score")}`,
    "Funnel: gmail_only"
    ].join("\n")
  };
}

function buildMailtoFallback(form) {
  const email = buildIntakeEmail(form);
  return `mailto:${encodeURIComponent(CONFIG.CONTACT_EMAIL)}?subject=${encodeURIComponent(
    email.subject
  )}&body=${encodeURIComponent(email.body)}`;
}

function buildReceiverPayload(form) {
  const email = buildIntakeEmail(form);
  const attribution = campaignAttribution();
  const payload = {
    _subject: email.subject,
    _template: "table",
    _captcha: "false",
    _url: window.location.href,
    worksheet_pdf: worksheetPdfUrl(),
    leavebehind_pdf: leaveBehindPdfUrl(),
    booking_link: bookingUrl(),
    lead_source: campaignLeadSource(form),
    utm_source: attribution.utm_source,
    utm_medium: attribution.utm_medium,
    utm_campaign: attribution.utm_campaign,
    utm_content: attribution.utm_content,
    source_page_url: window.location.href,
    message: email.body
  };

  payloadFieldNames.forEach((name) => {
    payload[name] = formValue(form, name);
  });

  return payload;
}

function showPostSubmitPanel() {
  const panel = document.getElementById("post-submit-panel");
  if (!panel) return;
  panel.hidden = false;
}

async function submitIntake(form) {
  const response = await fetch(CONFIG.FORM_ENDPOINT, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json"
    },
    body: JSON.stringify(buildReceiverPayload(form))
  });

  const result = await response.json().catch(() => ({}));
  if (!response.ok || result.success === false) {
    throw new Error(result.message || "The intake receiver did not accept the submission.");
  }
  return result;
}

function wireLeadForm(form) {
  const status = form.querySelector(".form-status");
  const submitButton = form.querySelector("[type='submit']");
  if (!status) return;
  form.addEventListener("submit", async (event) => {
    event.preventDefault();

    if (!form.checkValidity()) {
      form.reportValidity();
      status.textContent = "Complete the required fields before sending.";
      return;
    }

    if (formValue(form, "_honey")) {
      status.textContent = "Submission received.";
      form.reset();
      applyCampaignAttribution();
      return;
    }

    if (!hasValue("FORM_ENDPOINT")) {
      status.innerHTML = `The intake receiver is not configured. <a href="${buildMailtoFallback(form)}">Send by email instead.</a>`;
      return;
    }

    status.textContent = "Sending your intake summary.";
    if (submitButton) submitButton.disabled = true;

    try {
      await submitIntake(form);
      status.textContent = "Intake received. The brief, worksheet, and booking link are below.";
      showPostSubmitPanel();
      form.reset();
      applyCampaignAttribution();
    } catch (error) {
      status.innerHTML = `The intake receiver could not complete the submission. <a href="${buildMailtoFallback(form)}">Send by email instead.</a>`;
    } finally {
      if (submitButton) submitButton.disabled = false;
    }
  });
}

function wireLeadForms() {
  document.querySelectorAll("[data-lead-form], .lead-form").forEach((form) => {
    wireLeadForm(form);
  });
}

applyWorksheetLinks();
applyLeaveBehindLinks();
applyBookingLinks();
applyPostalAddress();
applyCampaignAttribution();
updateSetupWarning();
wireLeadForms();
