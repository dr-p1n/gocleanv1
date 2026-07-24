(function () {
  "use strict";

  /* =========================================================================
   * Lead capture config — see apps-script/README.md
   * Set these two after deploying Code.gs as a Web app.
   * ========================================================================= */
  var GAS_ENDPOINT = "https://script.google.com/macros/s/AKfycbye9nmSosH9c0tB4lSNpzJrA552w4fzoym-PU_cDkxSdXspbcphhgFRqnUw4j06SO0yKg/exec";
  var GAS_TOKEN = "gs_d66e9226d000ee67d956d26db8398073"; // must match SHARED_TOKEN in Code.gs

  function lang() {
    return (document.documentElement.lang || "es").slice(0, 2) === "en"
      ? "en"
      : "es";
  }

  function escapeHtml(s) {
    return String(s == null ? "" : s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#39;");
  }

  var I18N = {
    es: {
      reportTitle: "Reporte de preparación para licitaciones",
      preparedFor: "Preparado para",
      date: "Fecha",
      exposure: "Nivel de exposición",
      gapsTitle: "Brechas detectadas",
      noGaps: "No se detectaron brechas en esta evaluación.",
      prioritiesTitle: "Prioridades sugeridas",
      priorities:
        "Solicita a tu proveedor evidencia auditable de cada punto anterior: certificaciones vigentes, protocolos documentados y reportería que tu equipo de compras pueda revisar. Cada brecha cerrada reduce tu riesgo en la próxima licitación o auditoría de cliente.",
      disclaimer:
        "Diagnóstico orientativo. Una auditoría en sitio confirma el nivel real de exposición de tu operación.",
      contact: "Contacto",
      print: "Imprimir / Guardar como PDF",
      fileName: "Reporte-Preparacion-GoServices",
      required: "Completa nombre, email, WhatsApp y empresa.",
      badEmail: "Ingresa un email válido.",
      success: "✓ Tu reporte se descargó. Te contactaremos pronto."
    },
    en: {
      reportTitle: "Tender-readiness report",
      preparedFor: "Prepared for",
      date: "Date",
      exposure: "Exposure level",
      gapsTitle: "Gaps detected",
      noGaps: "No gaps were detected in this assessment.",
      prioritiesTitle: "Suggested priorities",
      priorities:
        "Ask your vendor for auditable evidence of each point above: current certifications, documented protocols, and reporting your procurement team can review. Every gap you close lowers your risk in the next tender or client audit.",
      disclaimer:
        "For guidance only. An on-site audit confirms your operation's real exposure level.",
      contact: "Contact",
      print: "Print / Save as PDF",
      fileName: "Tender-Readiness-Report-GoServices",
      required: "Fill in name, email, WhatsApp and company.",
      badEmail: "Enter a valid email.",
      success: "✓ Your report was downloaded. We'll be in touch shortly."
    }
  };

  function buildReportHtml(ctx) {
    var t = I18N[ctx.lang];
    var title = ctx.reportTitle || t.reportTitle;
    var accent =
      ctx.band === "high"
        ? "#c0392b"
        : ctx.band === "moderate"
        ? "#a67a00"
        : "#2f7d4f";
    var gapsHtml = ctx.gaps.length
      ? "<ul>" +
        ctx.gaps
          .map(function (g) {
            var label = typeof g === "string" ? g : g.label;
            var outcome = g && g.outcome ? g.outcome : "";
            return (
              "<li><strong>" +
              escapeHtml(label) +
              "</strong>" +
              (outcome ? " — " + escapeHtml(outcome) : "") +
              "</li>"
            );
          })
          .join("") +
        "</ul>"
      : "<p class='muted'>" + escapeHtml(t.noGaps) + "</p>";

    return (
      "<!doctype html><html lang='" +
      ctx.lang +
      "'><head><meta charset='utf-8'>" +
      "<meta name='viewport' content='width=device-width, initial-scale=1'>" +
      "<title>" +
      escapeHtml(title) +
      " — Go Services</title><style>" +
      "*{box-sizing:border-box}body{margin:0;font-family:'Source Sans 3',-apple-system,Segoe UI,system-ui,sans-serif;color:#1e2a3a;background:#f0f1ee;padding:40px 24px}" +
      ".sheet{max-width:720px;margin:0 auto;background:#fff;border:1px solid rgba(30,42,58,.12);border-radius:12px;padding:40px}" +
      ".brand{font-weight:700;letter-spacing:.04em;font-size:14px;color:#1e2a3a}.brand span{color:#a67a00}" +
      "h1{font-size:24px;margin:18px 0 4px}.meta{font-size:13px;color:#55606e;margin:0 0 24px}" +
      ".band{display:inline-block;padding:6px 14px;border-radius:999px;color:#fff;font-weight:600;font-size:14px;background:" +
      accent +
      "}.band-msg{margin:14px 0 28px;font-size:15px;line-height:1.5}" +
      "h2{font-size:15px;text-transform:uppercase;letter-spacing:.05em;color:#55606e;margin:28px 0 10px}" +
      "ul{margin:0;padding-left:20px}li{margin:6px 0;line-height:1.4}" +
      ".muted{color:#55606e}p{line-height:1.55}" +
      ".foot{margin-top:32px;padding-top:20px;border-top:1px solid rgba(30,42,58,.12);font-size:13px;color:#55606e}" +
      ".disc{font-size:12px;color:#55606e;margin-top:16px}" +
      ".print{margin:24px auto 0;display:block;background:#f2b705;color:#1e2a3a;border:0;border-radius:8px;padding:12px 20px;font-weight:600;cursor:pointer}" +
      "@media print{body{background:#fff;padding:0}.sheet{border:0;max-width:none}.print{display:none}}" +
      "</style></head><body><div class='sheet'>" +
      "<div class='brand'>GO SERVICES <span>// PANAMA</span></div>" +
      "<h1>" +
      escapeHtml(title) +
      "</h1><p class='meta'>" +
      escapeHtml(t.preparedFor) +
      ": <strong>" +
      escapeHtml(ctx.company) +
      "</strong> — " +
      escapeHtml(ctx.name) +
      " · " +
      escapeHtml(t.date) +
      ": " +
      escapeHtml(ctx.dateStr) +
      "</p>" +
      "<h2>" +
      escapeHtml(t.exposure) +
      "</h2><span class='band'>" +
      escapeHtml(ctx.bandLabel) +
      "</span><p class='band-msg'>" +
      escapeHtml(ctx.bandMessage) +
      "</p>" +
      "<h2>" +
      escapeHtml(t.gapsTitle) +
      "</h2>" +
      gapsHtml +
      "<h2>" +
      escapeHtml(t.prioritiesTitle) +
      "</h2><p>" +
      escapeHtml(t.priorities) +
      "</p>" +
      "<div class='foot'><strong>" +
      escapeHtml(t.contact) +
      "</strong><br>WhatsApp: +507 6982-3165 · dabin.rivera@go-cleaning.com" +
      "<p class='disc'>" +
      escapeHtml(t.disclaimer) +
      "</p></div>" +
      "<button class='print' onclick='window.print()'>" +
      escapeHtml(t.print) +
      "</button>" +
      "</div></body></html>"
    );
  }

  function downloadReport(fileName, html) {
    var blob = new Blob([html], { type: "text/html;charset=utf-8" });
    var url = URL.createObjectURL(blob);
    var a = document.createElement("a");
    a.href = url;
    a.download = fileName + ".html";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    setTimeout(function () {
      URL.revokeObjectURL(url);
    }, 4000);
  }

  function submitLead(payload) {
    if (!GAS_ENDPOINT) return; // not configured yet — never blocks the report
    try {
      fetch(GAS_ENDPOINT, {
        method: "POST",
        mode: "no-cors",
        headers: { "Content-Type": "text/plain;charset=utf-8" },
        body: JSON.stringify(payload)
      }).catch(function () {});
    } catch (e) {
      /* fire and forget */
    }
  }

  function initScorecard(rootId) {
    var root = document.getElementById(rootId);
    if (!root) return;

    var questions = Array.prototype.slice.call(
      root.querySelectorAll(".scorecard-q")
    );
    var resultPanel = root.querySelector(".result-panel");
    if (!questions.length || !resultPanel) return;

    var emptyState = resultPanel.querySelector('.result-state[data-state="empty"]');
    var doneState = resultPanel.querySelector('.result-state[data-state="done"]');
    var bands = resultPanel.querySelectorAll(".scorecard-band");
    var gapsBox = resultPanel.querySelector(".scorecard-gaps");
    var gapsList = gapsBox ? gapsBox.querySelector("ul") : null;

    // Gate: contact form shown once all questions are answered, BEFORE results.
    // Results (band + gaps) are revealed only after the lead is captured.
    var leadForm = resultPanel.querySelector('form.lead-capture[data-state="gate"]');
    var leadError = leadForm ? leadForm.querySelector(".lead-error") : null;

    var current = { band: null, gaps: [] };
    var submitted = false;
    var lastReportHtml = null;

    function bandFor(gapCount) {
      if (gapCount === 0) return "low";
      if (gapCount <= 2) return "moderate";
      return "high";
    }

    function renderDone() {
      bands.forEach(function (el) {
        el.hidden = el.dataset.band !== current.band;
      });
      if (gapsList) {
        gapsList.innerHTML = "";
        current.gaps.forEach(function (g) {
          var li = document.createElement("li");
          var label = document.createElement("strong");
          label.textContent = g.label;
          li.appendChild(label);
          if (g.outcome) {
            var out = document.createElement("span");
            out.className = "gap-outcome";
            out.textContent = g.outcome;
            li.appendChild(out);
          }
          gapsList.appendChild(li);
        });
        gapsBox.hidden = current.gaps.length === 0;
      }
    }

    function update() {
      var answers = questions.map(function (q) {
        var pressed = q.querySelector('.choice-toggle button[aria-pressed="true"]');
        return pressed ? pressed.dataset.answer : null;
      });

      if (answers.indexOf(null) !== -1) {
        emptyState.hidden = false;
        if (leadForm) leadForm.hidden = true;
        doneState.hidden = true;
        return;
      }

      var gaps = questions.filter(function (q, i) {
        return answers[i] === "no";
      });
      current.band = bandFor(gaps.length);
      current.gaps = gaps.map(function (q) {
        return { label: q.dataset.gapLabel, outcome: q.dataset.outcome || "" };
      });

      emptyState.hidden = true;

      if (leadForm && !submitted) {
        // Hold the results back until the visitor gives contact info.
        leadForm.hidden = false;
        doneState.hidden = true;
      } else {
        if (leadForm) leadForm.hidden = true;
        doneState.hidden = false;
        renderDone();
      }
    }

    questions.forEach(function (q) {
      var buttons = q.querySelectorAll(".choice-toggle button");
      buttons.forEach(function (btn) {
        btn.addEventListener("click", function () {
          buttons.forEach(function (b) {
            b.setAttribute("aria-pressed", String(b === btn));
          });
          update();
        });
      });
    });

    // ---- Gated lead capture: submit sends the lead, then reveals results ----
    if (leadForm) {
      leadForm.addEventListener("submit", function (ev) {
        ev.preventDefault();
        var t = I18N[lang()];
        // Use form.elements: `form.name` is shadowed by the form's own name IDL attribute.
        var fields = leadForm.elements;
        var name = ((fields.name && fields.name.value) || "").trim();
        var email = ((fields.email && fields.email.value) || "").trim();
        var company = ((fields.company && fields.company.value) || "").trim();
        var phone = ((fields.phone && fields.phone.value) || "").trim();

        if (leadError) {
          leadError.hidden = true;
          leadError.textContent = "";
        }
        if (!name || !email || !company || !phone) {
          if (leadError) {
            leadError.textContent = t.required;
            leadError.hidden = false;
          }
          return;
        }
        if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
          if (leadError) {
            leadError.textContent = t.badEmail;
            leadError.hidden = false;
          }
          return;
        }

        var shownBand = resultPanel.querySelector(
          '.scorecard-band[data-band="' + current.band + '"]'
        );
        var bandLabel = shownBand
          ? shownBand.querySelector(".result-label").textContent.trim()
          : "";
        var bandMessage = shownBand
          ? shownBand.querySelector(".result-message").textContent.trim()
          : "";

        submitLead({
          token: GAS_TOKEN,
          source: leadForm.getAttribute("data-source") || rootId,
          name: name,
          email: email,
          company: company,
          phone: phone,
          lang: lang(),
          band: current.band,
          gaps: current.gaps.map(function (g) { return g.label; }),
          page: location.href,
          ua: navigator.userAgent
        });

        var html = buildReportHtml({
          lang: lang(),
          name: name,
          company: company,
          dateStr: new Date().toLocaleDateString(
            lang() === "en" ? "en-US" : "es-PA",
            { year: "numeric", month: "long", day: "numeric" }
          ),
          band: current.band,
          bandLabel: bandLabel,
          bandMessage: bandMessage,
          gaps: current.gaps,
          reportTitle: leadForm.getAttribute("data-report-title") || null
        });
        lastReportHtml = html;
        downloadReport(t.fileName, html);

        submitted = true;
        update();
      });
    }

    // Re-download button on the revealed results: re-saves the same branded
    // report without asking for the contact details again.
    var downloadBtn = resultPanel.querySelector(".scorecard-download");
    if (downloadBtn) {
      downloadBtn.addEventListener("click", function () {
        if (lastReportHtml) downloadReport(I18N[lang()].fileName, lastReportHtml);
      });
    }
  }

  function initCookieBanner() {
    try {
      if (localStorage.getItem("gs_cookie_ok")) return;
    } catch (e) {
      return;
    }
    var en = lang() === "en";
    var wrap = document.createElement("div");
    wrap.className = "cookie-banner";
    var p = document.createElement("p");
    p.appendChild(
      document.createTextNode(
        en
          ? "We use essential data to run this site and respond to your request. By continuing, you accept our "
          : "Usamos datos esenciales para operar este sitio y responder tu solicitud. Al continuar, aceptas nuestra "
      )
    );
    var a = document.createElement("a");
    a.href = en ? "/en/privacy" : "/es/privacidad";
    a.textContent = en ? "Privacy Policy" : "Política de Privacidad";
    p.appendChild(a);
    p.appendChild(document.createTextNode(en ? " (Law 81 of 2019)." : " (Ley 81 de 2019)."));
    var btn = document.createElement("button");
    btn.type = "button";
    btn.className = "cookie-accept";
    btn.textContent = en ? "Accept" : "Aceptar";
    btn.addEventListener("click", function () {
      try {
        localStorage.setItem("gs_cookie_ok", "1");
      } catch (e) {}
      if (wrap.parentNode) wrap.parentNode.removeChild(wrap);
    });
    wrap.appendChild(p);
    wrap.appendChild(btn);
    document.body.appendChild(wrap);
  }

  document.addEventListener("DOMContentLoaded", function () {
    initCookieBanner();
    initScorecard("risk-audit");
    initScorecard("eco-audit");

    // Flip cards: tap/click toggles the flip on touch devices (hover handles desktop)
    document.querySelectorAll(".flip-card").forEach(function (card) {
      card.addEventListener("click", function () {
        card.classList.toggle("flipped");
      });
    });

    var toggle = document.querySelector(".mobile-nav-toggle");
    var panel = document.querySelector(".mobile-nav-panel");
    if (toggle && panel) {
      toggle.addEventListener("click", function () {
        panel.classList.toggle("open");
        var expanded = panel.classList.contains("open");
        toggle.setAttribute("aria-expanded", String(expanded));
      });
    }
  });
})();
