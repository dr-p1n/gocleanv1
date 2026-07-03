(function () {
  "use strict";

  function initTabs() {
    var tabs = Array.prototype.slice.call(document.querySelectorAll(".tab"));
    var panels = Array.prototype.slice.call(document.querySelectorAll(".tab-panel"));
    if (!tabs.length || !panels.length) return;

    var mobilePanel = document.querySelector(".mobile-nav-panel");
    var mobileToggle = document.querySelector(".mobile-nav-toggle");

    function activate(id) {
      tabs.forEach(function (tab) {
        tab.setAttribute("aria-selected", String(tab.dataset.tab === id));
      });
      panels.forEach(function (panel) {
        panel.hidden = panel.dataset.panel !== id;
      });
    }

    tabs.forEach(function (tab) {
      tab.addEventListener("click", function () {
        activate(tab.dataset.tab);
      });
    });

    var explorer = document.getElementById("explorer");
    document.querySelectorAll("[data-tab-link]").forEach(function (link) {
      link.addEventListener("click", function (e) {
        e.preventDefault();
        activate(link.dataset.tabLink);
        if (mobilePanel && mobilePanel.classList.contains("open")) {
          mobilePanel.classList.remove("open");
          if (mobileToggle) mobileToggle.setAttribute("aria-expanded", "false");
        }
        if (explorer) explorer.scrollIntoView({ behavior: "smooth", block: "start" });
      });
    });
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

    function bandFor(gapCount) {
      if (gapCount === 0) return "low";
      if (gapCount <= 2) return "moderate";
      return "high";
    }

    function update() {
      var answers = questions.map(function (q) {
        var pressed = q.querySelector('.choice-toggle button[aria-pressed="true"]');
        return pressed ? pressed.dataset.answer : null;
      });

      if (answers.indexOf(null) !== -1) {
        emptyState.hidden = false;
        doneState.hidden = true;
        return;
      }

      var gaps = questions.filter(function (q, i) {
        return answers[i] === "no";
      });
      var band = bandFor(gaps.length);

      bands.forEach(function (el) {
        el.hidden = el.dataset.band !== band;
      });

      if (gapsList) {
        gapsList.innerHTML = "";
        gaps.forEach(function (q) {
          var li = document.createElement("li");
          li.textContent = q.dataset.gapLabel;
          gapsList.appendChild(li);
        });
        gapsBox.hidden = gaps.length === 0;
      }

      emptyState.hidden = true;
      doneState.hidden = false;
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
  }

  document.addEventListener("DOMContentLoaded", function () {
    initTabs();
    initScorecard("risk-audit");

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
