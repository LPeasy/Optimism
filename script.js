const CONFIG = {
  BOOKING_LINK: "BOOKING_LINK",
  HUBSPOT_PORTAL_ID: "HUBSPOT_PORTAL_ID",
  HUBSPOT_FORM_ID: "HUBSPOT_FORM_ID",
  POSTAL_ADDRESS: "POSTAL_ADDRESS"
};

const placeholders = new Set([
  "BOOKING_LINK",
  "HUBSPOT_PORTAL_ID",
  "HUBSPOT_FORM_ID",
  "POSTAL_ADDRESS"
]);

function isPlaceholder(value) {
  return !value || placeholders.has(value);
}

function applyBookingLinks() {
  const ready = !isPlaceholder(CONFIG.BOOKING_LINK);
  document.querySelectorAll("[data-booking-link]").forEach((link) => {
    link.setAttribute("href", ready ? CONFIG.BOOKING_LINK : "#setup-required");
    link.toggleAttribute("target", ready);
    if (ready) {
      link.setAttribute("rel", "noopener");
    } else {
      link.removeAttribute("rel");
    }
  });
}

function applyPostalAddress() {
  const addressTarget = document.getElementById("postal-address");
  if (!addressTarget) return;
  addressTarget.textContent = isPlaceholder(CONFIG.POSTAL_ADDRESS)
    ? "POSTAL_ADDRESS"
    : CONFIG.POSTAL_ADDRESS;
}

function updateSetupWarning() {
  const warning = document.getElementById("setup-required");
  if (!warning) return;
  const missing = Object.entries(CONFIG)
    .filter(([, value]) => isPlaceholder(value))
    .map(([key]) => key);

  if (missing.length === 0) {
    warning.classList.add("is-ready");
    warning.textContent = "Launch values are configured. HubSpot form capture is active.";
  } else {
    warning.classList.remove("is-ready");
    warning.innerHTML = `Launch blocked until ${missing
      .map((key) => `<code>${key}</code>`)
      .join(", ")} ${missing.length === 1 ? "is" : "are"} replaced.`;
  }
}

function loadHubSpotForm() {
  const hasHubSpotConfig =
    !isPlaceholder(CONFIG.HUBSPOT_PORTAL_ID) &&
    !isPlaceholder(CONFIG.HUBSPOT_FORM_ID);
  const target = document.getElementById("hubspot-form-target");
  const fallback = document.getElementById("fallback-lead-form");

  if (!hasHubSpotConfig || !target || !fallback) {
    return;
  }

  target.hidden = false;
  fallback.hidden = true;

  const script = document.createElement("script");
  script.src = "https://js.hsforms.net/forms/embed/v2.js";
  script.async = true;
  script.onload = () => {
    if (!window.hbspt?.forms) return;
    window.hbspt.forms.create({
      region: "na1",
      portalId: CONFIG.HUBSPOT_PORTAL_ID,
      formId: CONFIG.HUBSPOT_FORM_ID,
      target: "#hubspot-form-target",
      onFormReady: ($form) => {
        const form = $form?.[0] || document.querySelector("#hubspot-form-target form");
        if (!form) return;
        const hiddenFields = {
          lead_source: "optimism_landing_page",
          lead_score: "10",
          optimism_funnel_signup: "true"
        };
        Object.entries(hiddenFields).forEach(([name, value]) => {
          let input = form.querySelector(`input[name="${name}"]`);
          if (!input) {
            input = document.createElement("input");
            input.type = "hidden";
            input.name = name;
            form.appendChild(input);
          }
          input.value = value;
        });
      }
    });
  };
  document.head.appendChild(script);
}

function wireFallbackForm() {
  const form = document.getElementById("fallback-lead-form");
  const status = document.getElementById("form-status");
  if (!form || !status) return;

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    status.textContent =
      "This preview form is launch-blocked. Add HubSpot portal/form IDs before collecting leads.";
  });
}

applyBookingLinks();
applyPostalAddress();
updateSetupWarning();
loadHubSpotForm();
wireFallbackForm();
