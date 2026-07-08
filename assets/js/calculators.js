(function () {
  "use strict";

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
