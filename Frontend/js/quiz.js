/**
 * quiz.js
 * -------
 * Drives the quiz experience on quiz.html:
 *  1. Fetches questions from the backend via api.js
 *  2. Displays them one at a time with a progress bar
 *  3. Collects answers (0 / 1 / 2) in an array
 *  4. POSTs answers to the backend on submit
 *  5. Saves the result to localStorage and redirects to result.html
 */

// ── State ────────────────────────────────────────────────────────────────────
let questions = [];
let answers = [];
let currentIndex = 0;

// ── DOM refs (populated after DOMContentLoaded) ──────────────────────────────
let questionCounter, progressFill, questionText;
let optionBtns, submitSection, submitBtn;
let loadingOverlay, errorBanner;

// ── Boot ─────────────────────────────────────────────────────────────────────
document.addEventListener("DOMContentLoaded", async () => {
  questionCounter  = document.getElementById("question-counter");
  progressFill     = document.getElementById("progress-fill");
  questionText     = document.getElementById("question-text");
  optionBtns       = document.querySelectorAll(".option-btn");
  submitSection    = document.getElementById("submit-section");
  submitBtn        = document.getElementById("submit-btn");
  loadingOverlay   = document.getElementById("loading-overlay");
  errorBanner      = document.getElementById("error-banner");

  // Attach answer-selection handlers
  optionBtns.forEach((btn) => {
    btn.addEventListener("click", () => handleOptionClick(btn));
  });

  // Attach submit handler
  submitBtn.addEventListener("click", handleSubmit);

  // Load questions from backend
  await loadQuestions();
});

// ── Load questions ────────────────────────────────────────────────────────────
async function loadQuestions() {
  showLoading(true);
  try {
    questions = await getQuestions();
    answers   = new Array(questions.length).fill(null);
    renderQuestion(0);
  } catch (err) {
    showError("Could not load questions. Is the backend running? " + err.message);
  } finally {
    showLoading(false);
  }
}

// ── Render a single question ──────────────────────────────────────────────────
function renderQuestion(index) {
  const q = questions[index];

  // Counter & progress
  questionCounter.textContent = `Question ${index + 1} of ${questions.length}`;
  const pct = ((index) / questions.length) * 100;
  progressFill.style.width = `${pct}%`;

  // Question text — animate in
  questionText.classList.remove("fade-in");
  void questionText.offsetWidth; // reflow trick
  questionText.textContent = q.text;
  questionText.classList.add("fade-in");

  // Restore previously selected answer if user went back
  optionBtns.forEach((btn) => {
    const val = parseInt(btn.dataset.value, 10);
    btn.classList.toggle("selected", answers[index] === val);
  });

  // Hide submit on non-final questions
  submitSection.classList.toggle("hidden", index !== questions.length - 1);
}

// ── Handle option selection ───────────────────────────────────────────────────
function handleOptionClick(clickedBtn) {
  // Mark selected
  optionBtns.forEach((b) => b.classList.remove("selected"));
  clickedBtn.classList.add("selected");

  const value = parseInt(clickedBtn.dataset.value, 10);
  answers[currentIndex] = value;

  // Auto-advance after short delay (unless last question)
  if (currentIndex < questions.length - 1) {
    setTimeout(() => {
      currentIndex++;
      renderQuestion(currentIndex);
    }, 380);
  } else {
    // Last question — show submit button
    submitSection.classList.remove("hidden");
    progressFill.style.width = "100%";
  }
}

// ── Submit quiz ───────────────────────────────────────────────────────────────
async function handleSubmit() {
  // Validate all answered
  const unanswered = answers.findIndex((a) => a === null);
  if (unanswered !== -1) {
    showError(
      `You haven't answered question ${unanswered + 1} yet. Go back and answer it!`
    );
    return;
  }

  showLoading(true);
  submitBtn.disabled = true;

  try {
    const result = await submitQuiz(answers);
    // Save to localStorage so result.html can read it
    localStorage.setItem("pathfinder_result", JSON.stringify(result));
    window.location.href = "result.html";
  } catch (err) {
    showError("Submission failed: " + err.message);
    submitBtn.disabled = false;
  } finally {
    showLoading(false);
  }
}

// ── UI helpers ────────────────────────────────────────────────────────────────
function showLoading(visible) {
  loadingOverlay.classList.toggle("hidden", !visible);
}

function showError(message) {
  errorBanner.textContent = message;
  errorBanner.classList.remove("hidden");
  setTimeout(() => errorBanner.classList.add("hidden"), 5000);
}