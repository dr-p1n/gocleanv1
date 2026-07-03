(function () {
  "use strict";

  function formatCurrency(value, locale) {
    return new Intl.NumberFormat(locale === "es" ? "es-PA" : "en-US", {
      style: "currency",
      currency: "USD",
      maximumFractionDigits: 0,
    }).format(value);
  }

  function bindRange(id, onChange) {
    var input = document.getElementById(id);
    if (!input) return null;
    var valueEl = document.querySelector('[data-value-for="' + id + '"]');
    input.addEventListener("input", function () {
      if (valueEl) valueEl.textContent = input.value;
      onChange();
    });
    return input;
  }

  function initRiskAudit() {
    var root = document.getElementById("risk-audit");
    if (!root) return;

    var buttons = root.querySelectorAll(".choice-toggle button");
    var states = root.querySelectorAll(".result-state");

    function showState(answer) {
      states.forEach(function (el) {
        el.hidden = el.dataset.state !== answer;
      });
      buttons.forEach(function (btn) {
        btn.setAttribute("aria-pressed", String(btn.dataset.answer === answer));
      });
    }

    buttons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        showState(btn.dataset.answer);
      });
    });
  }

  function initBiocleaningAudit(locale) {
    var root = document.getElementById("biocleaning-audit");
    if (!root) return;

    var resultEl = document.getElementById("biocleaning-audit-result");

    function recompute() {
      var units = Number(document.getElementById("bio-units").value);
      var cost = Number(document.getElementById("bio-cost").value);
      var percent = Number(document.getElementById("bio-percent").value);
      var total = units * cost * 12 * (percent / 100);
      resultEl.textContent = formatCurrency(total, locale);
    }

    bindRange("bio-units", recompute);
    bindRange("bio-cost", recompute);
    bindRange("bio-percent", recompute);
    recompute();
  }

  document.addEventListener("DOMContentLoaded", function () {
    var locale = document.documentElement.lang === "en" ? "en" : "es";
    initRiskAudit();
    initBiocleaningAudit(locale);

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
