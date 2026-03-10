/**
 * result.js
 * ---------
 * Drives the result page (result.html):
 *  1. Reads the career result from localStorage
 *  2. Displays career title and description
 *  3. Fetches the learning roadmap from the backend
 *  4. Renders the roadmap as an animated step-by-step list
 */

document.addEventListener("DOMContentLoaded", async () => {
  const careerTitle   = document.getElementById("career-title");
  const careerDesc    = document.getElementById("career-description");
  const roadmapList   = document.getElementById("roadmap-list");
  const roadmapSection = document.getElementById("roadmap-section");
  const retakeBtn     = document.getElementById("retake-btn");
  const errorBanner   = document.getElementById("error-banner");
  const loadingSpinner = document.getElementById("roadmap-loading");

  // ── 1. Read result from localStorage ───────────────────────────────────────
  const raw = localStorage.getItem("pathfinder_result");

  if (!raw) {
    careerTitle.textContent = "No result found";
    careerDesc.textContent  =
      "It looks like you haven't taken the quiz yet. Please go back and complete it.";
    retakeBtn.classList.remove("hidden");
    return;
  }

  let result;
  try {
    result = JSON.parse(raw);
  } catch {
    careerTitle.textContent = "Error reading result";
    careerDesc.textContent  = "Something went wrong. Please retake the quiz.";
    retakeBtn.classList.remove("hidden");
    return;
  }

  // ── 2. Display career ───────────────────────────────────────────────────────
  careerTitle.textContent = result.career;
  careerDesc.textContent  = result.description;

  // Retake button always visible
  retakeBtn.classList.remove("hidden");
  retakeBtn.addEventListener("click", () => {
    localStorage.removeItem("pathfinder_result");
    window.location.href = "quiz.html";
  });

  // ── 3. Fetch roadmap ────────────────────────────────────────────────────────
  roadmapSection.classList.remove("hidden");
  loadingSpinner.classList.remove("hidden");

  try {
    const data = await getRoadmap(result.career);
    loadingSpinner.classList.add("hidden");
    renderRoadmap(data.roadmap, roadmapList);
  } catch (err) {
    loadingSpinner.classList.add("hidden");
    showError(errorBanner, "Could not load roadmap: " + err.message);
  }
});

// ── Render roadmap steps ───────────────────────────────────────────────────────
function renderRoadmap(steps, container) {
  container.innerHTML = "";

  steps.forEach((step, i) => {
    const li = document.createElement("li");
    li.classList.add("roadmap-step");
    li.style.animationDelay = `${i * 80}ms`;

    const num = document.createElement("span");
    num.classList.add("step-number");
    num.textContent = i + 1;

    const text = document.createElement("span");
    text.classList.add("step-text");
    // Strip "Step N –" prefix from text since we show the number badge
    text.textContent = step.replace(/^Step \d+\s*[–-]\s*/i, "");

    li.appendChild(num);
    li.appendChild(text);
    container.appendChild(li);
  });
}

// ── Error helper ──────────────────────────────────────────────────────────────
function showError(banner, message) {
  banner.textContent = message;
  banner.classList.remove("hidden");
}