(function () {
  "use strict";

  function initChoiceAudit(rootId) {
    var root = document.getElementById(rootId);
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

  document.addEventListener("DOMContentLoaded", function () {
    initChoiceAudit("risk-audit");
    initChoiceAudit("biocleaning-audit");

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
