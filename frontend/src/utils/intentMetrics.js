const normalizeText = (value) =>
  String(value || "")
    .toLowerCase()
    .replace(/[_-]+/g, " ")
    .replace(/\s+/g, " ")
    .trim();

export const isSilentIntent = (intent) =>
  normalizeText(intent).includes("silent");

export const isFrontDeskIntent = (intent) =>
  normalizeText(intent).includes("front desk");

export const isAppointmentIntent = (intent) => {
  const text = normalizeText(intent);
  return (
    text.includes("appointment") ||
    text.includes("reschedule") ||
    text.includes("cancel") ||
    text.includes("modify")
  );
};

export const getIntentBucket = (intent) => {
  const text = normalizeText(intent);

  if (!text) return "Unknown";
  if (text.includes("silent")) return "Silent Calls";
  if (text.includes("front desk")) return "Front Desk";
  if (text.includes("billing") || text.includes("insurance")) {
    return "Billing / Insurance";
  }
  if (text.includes("medication") || text.includes("refill")) {
    return "Medication / Refill";
  }
  if (
    text.includes("appointment") ||
    text.includes("reschedule") ||
    text.includes("cancel") ||
    text.includes("modify")
  ) {
    return "Appointments";
  }
  if (text.includes("general information")) return "General Information";
  if (text.includes("general inquiry") || text.includes("inquiry")) {
    return "General Inquiry";
  }

  return "Other";
};

