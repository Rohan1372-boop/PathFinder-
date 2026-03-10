/**
 * main.js
 * -------
 * Shared utilities used across all pages.
 * Currently handles the "Start Quiz" button on index.html.
 */

document.addEventListener("DOMContentLoaded", () => {
  // ── Home page CTA ────────────────────────────────────────────────────────
  const startBtn = document.getElementById("start-btn");
  if (startBtn) {
    startBtn.addEventListener("click", () => {
      window.location.href = "quiz.html";
    });
  }
});