/**
 * Go Services — Lead capture endpoint for the exposure scorecard.
 *
 * Receives a lead (name / email / company + scorecard result) from the website
 * and appends it to a Google Sheet. Fire-and-forget: the browser posts with
 * mode:'no-cors', so the response body is never read — but we still return JSON
 * for manual testing (open the /exec URL, or use doGet as a health check).
 *
 * Deploy: see README.md in this folder.
 */

// Optional: get an email each time a lead comes in. Leave "" to disable.
var NOTIFY_EMAIL = "hello@go-cleaning.com";

// Simple shared secret. Must match GAS_TOKEN in assets/js/calculators.js.
// Change this to any random string; blocks casual spam to the endpoint.
var SHARED_TOKEN = "gs_d66e9226d000ee67d956d26db8398073";

var HEADERS = [
  "Timestamp", "Source", "Name", "Email", "Company", "Phone",
  "Language", "Exposure band", "Gaps", "Page", "User agent"
];

function doPost(e) {
  try {
    var data = JSON.parse(e.postData.contents);

    if (SHARED_TOKEN && data.token !== SHARED_TOKEN) {
      return json({ ok: false, error: "unauthorized" });
    }

    var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheets()[0];
    if (sheet.getLastRow() === 0) {
      sheet.appendRow(HEADERS);
      sheet.getRange(1, 1, 1, HEADERS.length).setFontWeight("bold");
      sheet.setFrozenRows(1);
    }

    var gaps = Array.isArray(data.gaps) ? data.gaps.join("; ") : "";
    sheet.appendRow([
      new Date(),
      data.source || "",
      data.name || "",
      data.email || "",
      data.company || "",
      data.phone || "",
      data.lang || "",
      data.band || "",
      gaps,
      data.page || "",
      data.ua || ""
    ]);

    if (NOTIFY_EMAIL) {
      MailApp.sendEmail({
        to: NOTIFY_EMAIL,
        subject: "Nuevo lead — Scorecard (" + (data.band || "?") + " exposure)",
        body: [
          "Nombre:   " + (data.name || ""),
          "Email:    " + (data.email || ""),
          "Empresa:  " + (data.company || ""),
          "Teléfono: " + (data.phone || ""),
          "Idioma:   " + (data.lang || ""),
          "Banda:    " + (data.band || ""),
          "Brechas:  " + gaps,
          "Página:   " + (data.page || "")
        ].join("\n")
      });
    }

    return json({ ok: true });
  } catch (err) {
    return json({ ok: false, error: String(err) });
  }
}

function doGet() {
  return json({ ok: true, service: "go-services-lead-capture" });
}

function json(obj) {
  return ContentService
    .createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}
