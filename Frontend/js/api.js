/**
 * api.js
 * ------
 * All fetch() calls to the Pathfinder FastAPI backend live here.
 *
 * If the backend is unreachable every function falls back to
 * built-in local data automatically — the quiz always works.
 *
 * To use the live backend:
 *   cd Backend && uvicorn main:app --reload
 */

const BASE_URL = "http://127.0.0.1:8000";

// ─────────────────────────────────────────────────────────────────────────────
// FALLBACK DATA  (identical to the backend)
// ─────────────────────────────────────────────────────────────────────────────

const FALLBACK_QUESTIONS = [
  { id:1,  text:"Do you enjoy breaking down complex problems step by step to find a logical solution?",        options:["Yes","Sometimes","No"], trait:0 },
  { id:2,  text:"Do you feel comfortable working with numbers, statistics, or spreadsheets?",                  options:["Yes","Sometimes","No"], trait:1 },
  { id:3,  text:"Are you drawn to creative work — design, art, writing, or visual storytelling?",              options:["Yes","Sometimes","No"], trait:2 },
  { id:4,  text:"Do you genuinely enjoy helping, teaching, or mentoring other people?",                        options:["Yes","Sometimes","No"], trait:3 },
  { id:5,  text:"Do you love building or fixing things — software, hardware, or complex systems?",             options:["Yes","Sometimes","No"], trait:4 },
  { id:6,  text:"Are you interested in how businesses, markets, and organisations operate?",                   options:["Yes","Sometimes","No"], trait:5 },
  { id:7,  text:"Do you enjoy presenting ideas, writing persuasively, or speaking in front of others?",        options:["Yes","Sometimes","No"], trait:6 },
  { id:8,  text:"Do you like taking charge — organising teams, setting goals, and driving projects forward?",  options:["Yes","Sometimes","No"], trait:7 },
  { id:9,  text:"Are you fascinated by how the natural or physical world works — science, biology, or engineering?", options:["Yes","Sometimes","No"], trait:8 },
  { id:10, text:"Do you take pride in precision and accuracy — noticing errors that others might miss?",        options:["Yes","Sometimes","No"], trait:9 },
  { id:11, text:"Do you do your best work alone, preferring deep focus over constant team interaction?",        options:["Yes","Sometimes","No"], trait:10 },
  { id:12, text:"Are you motivated by making a real difference to people's lives or to society as a whole?",   options:["Yes","Sometimes","No"], trait:11 },
];

// Trait indices:
//  0=ANALYTICAL  1=DATA        2=CREATIVE    3=SOCIAL
//  4=TECHNICAL   5=BUSINESS    6=COMMUNICATION 7=LEADERSHIP
//  8=SCIENTIFIC  9=DETAIL     10=INDEPENDENT 11=EMPATHETIC

const FALLBACK_CAREERS = [
  { name:"Software Engineer",
    profile:[0.8,0.3,0.2,0.1,1.0,0.2,0.2,0.2,0.3,0.6,0.7,0.1],
    description:"You love building things from scratch. Whether it's a mobile app, a web platform, or a backend system, you thrive on turning logical thinking and technical skill into working software." },
  { name:"Data Scientist",
    profile:[0.9,1.0,0.1,0.1,0.6,0.2,0.2,0.1,0.7,0.7,0.8,0.1],
    description:"You are driven by a hunger to find patterns in data. You combine statistical thinking, programming, and domain curiosity to build models that answer questions no one else thought to ask." },
  { name:"Cybersecurity Analyst",
    profile:[0.9,0.4,0.1,0.1,0.9,0.2,0.2,0.2,0.5,1.0,0.8,0.2],
    description:"You think like an attacker so you can defend like a pro. Detail-oriented and endlessly curious about how systems can be broken — and fixed — you are the guardian of the digital world." },
  { name:"DevOps Engineer",
    profile:[0.8,0.4,0.1,0.2,1.0,0.3,0.3,0.4,0.3,0.9,0.6,0.1],
    description:"You sit at the crossroads of development and operations. You automate, optimise, and keep complex infrastructure running smoothly — turning chaos into reliable, repeatable systems." },
  { name:"Machine Learning Engineer",
    profile:[1.0,0.9,0.1,0.1,0.9,0.1,0.1,0.1,0.8,0.7,0.9,0.1],
    description:"You build the engines that power AI. Sitting between research and production, you design, train, and deploy models that learn — turning cutting-edge ideas into real-world products." },
  { name:"UX / UI Designer",
    profile:[0.4,0.2,1.0,0.7,0.4,0.2,0.6,0.3,0.1,0.8,0.5,0.6],
    description:"You have a sharp eye for aesthetics and deep empathy for users. You craft digital experiences that are both beautiful and effortless to use — sitting at the crossroads of art and technology." },
  { name:"Graphic Designer",
    profile:[0.2,0.1,1.0,0.3,0.3,0.2,0.5,0.2,0.1,0.8,0.7,0.3],
    description:"You communicate through visuals. Typography, colour, composition — these are your tools. You bring ideas to life in ways that words alone never could." },
  { name:"Content Creator / Writer",
    profile:[0.3,0.1,0.9,0.4,0.1,0.3,1.0,0.2,0.2,0.6,0.7,0.4],
    description:"You tell stories that move people. Whether it's articles, scripts, social media, or long-form journalism, you have a gift for turning ideas into compelling words." },
  { name:"Product Manager",
    profile:[0.6,0.5,0.5,0.6,0.4,0.8,0.8,0.8,0.2,0.5,0.3,0.5],
    description:"You are the glue between business, design, and engineering. You define what gets built and why, balancing user needs, commercial goals, and technical constraints to ship products people love." },
  { name:"Business Analyst",
    profile:[0.8,0.7,0.2,0.4,0.4,0.9,0.6,0.4,0.2,0.8,0.4,0.3],
    description:"You bridge the gap between business needs and technical solutions. You map processes, spot inefficiencies, and translate messy real-world problems into clear requirements." },
  { name:"Entrepreneur / Startup Founder",
    profile:[0.6,0.4,0.7,0.5,0.4,1.0,0.8,1.0,0.3,0.4,0.5,0.5],
    description:"You spot opportunities others miss and have the courage to chase them. Resilient, resourceful, and comfortable with risk, you build companies from nothing — driven by a vision." },
  { name:"Marketing Manager",
    profile:[0.4,0.5,0.8,0.6,0.2,0.8,1.0,0.6,0.1,0.5,0.3,0.4],
    description:"You understand people and know how to reach them. You blend creativity with data-driven thinking to craft campaigns that grow brands and win customers." },
  { name:"Financial Analyst",
    profile:[0.9,1.0,0.1,0.2,0.3,0.9,0.5,0.3,0.2,0.9,0.7,0.1],
    description:"Numbers are your language. You evaluate investments, model financial scenarios, and advise on strategy — giving decision-makers the clarity they need to grow wealth and manage risk." },
  { name:"Project Manager",
    profile:[0.5,0.4,0.2,0.7,0.3,0.7,0.7,1.0,0.1,0.8,0.2,0.4],
    description:"You bring order to complexity. Juggling timelines, budgets, and people, you keep teams aligned and projects on track — turning ambitious goals into delivered results." },
  { name:"Data Analyst",
    profile:[0.5,0.9,0.2,0.5,0.2,0.9,0.8,0.3,0.2,0.7,0.3,0.2],
    description:"You turn raw numbers into stories that drive action. Sitting inside a business, you answer the questions that matter — why did sales drop? which campaign worked? — with evidence, not guesswork." },
  { name:"Human Resources Manager",
    profile:[0.4,0.3,0.4,1.0,0.1,0.6,0.8,0.7,0.1,0.5,0.2,0.9],
    description:"People are your passion. You recruit, develop, and look after the humans that make organisations work — creating cultures where everyone can do their best work and grow." },
  { name:"Educator / Teacher",
    profile:[0.5,0.2,0.6,1.0,0.2,0.2,0.9,0.5,0.5,0.5,0.3,1.0],
    description:"You light up when you help someone understand something new. Patient, articulate, and deeply committed to others' growth, you shape how the next generation thinks." },
  { name:"Healthcare Professional (Nurse / Paramedic)",
    profile:[0.5,0.3,0.2,0.9,0.3,0.1,0.7,0.4,0.8,0.9,0.2,1.0],
    description:"You are driven by care. Whether at a bedside or on the front line, you combine clinical skill with human compassion to support people through their most vulnerable moments." },
  { name:"Research Scientist",
    profile:[0.9,0.8,0.3,0.3,0.5,0.1,0.5,0.2,1.0,0.9,0.9,0.4],
    description:"You push the boundaries of what is known. Methodical, curious, and deeply rigorous, you design experiments and gather evidence that expands humanity's understanding of the world." },
  { name:"Environmental / Sustainability Consultant",
    profile:[0.6,0.5,0.4,0.7,0.3,0.6,0.7,0.5,0.9,0.6,0.4,1.0],
    description:"You are passionate about protecting the planet. You advise organisations on reducing their environmental footprint — combining scientific knowledge, strategic thinking, and a genuine drive for a better world." },
];

const FALLBACK_ROADMAPS = {
  "Software Engineer":["Master the fundamentals of a first language — Python or JavaScript","Learn data structures and algorithms (arrays, trees, sorting, searching)","Understand version control with Git and GitHub","Build your first full-stack project (frontend + backend + database)","Study object-oriented and functional programming patterns","Learn SQL and at least one NoSQL database","Understand REST APIs, HTTP, and basic system design","Write unit and integration tests — practise Test-Driven Development","Deploy applications to the cloud (AWS, GCP, or Azure)","Contribute to open-source projects and build a strong GitHub portfolio"],
  "Data Scientist":["Learn Python programming fundamentals and the scientific stack","Master statistics: distributions, hypothesis testing, Bayesian thinking","Explore data wrangling with pandas and NumPy","Learn data visualisation with Matplotlib and Seaborn","Study machine learning fundamentals with scikit-learn","Dive into deep learning with TensorFlow or PyTorch","Practice SQL for querying and joining large datasets","Build and document end-to-end ML projects from raw data to insight","Learn MLOps: model versioning, deployment, and monitoring","Publish projects on GitHub and compete on Kaggle to build reputation"],
  "Cybersecurity Analyst":["Build a solid foundation in networking — TCP/IP, DNS, HTTP, firewalls","Learn Linux fundamentals and confident command-line usage","Study core security principles: CIA triad, encryption, authentication","Learn Python or Bash scripting for security automation","Get hands-on with ethical hacking tools: Kali Linux, Nmap, Burp Suite","Study common attack vectors: SQL injection, XSS, phishing, MITM","Learn SIEM tools and practise log analysis","Set up a home lab and tackle Capture-the-Flag (CTF) challenges","Earn a recognised certification: CompTIA Security+, CEH, or OSCP","Apply for a SOC Analyst or junior Penetration Tester role"],
  "DevOps Engineer":["Master Linux administration and shell scripting","Learn at least one programming language well (Python or Go)","Understand version control workflows: branching strategies, pull requests","Study containerisation with Docker and orchestration with Kubernetes","Learn CI/CD pipelines using GitHub Actions, Jenkins, or GitLab CI","Master infrastructure-as-code with Terraform or Ansible","Understand cloud platforms: AWS, GCP, or Azure fundamentals","Study monitoring, logging, and alerting with Prometheus and Grafana","Learn site reliability engineering (SRE) principles and SLOs","Earn a cloud certification (AWS Solutions Architect or GCP Professional)"],
  "Machine Learning Engineer":["Master Python and the scientific stack: NumPy, pandas, scikit-learn","Study linear algebra, calculus, and probability in depth","Build and train neural networks from scratch before using frameworks","Deep-dive into TensorFlow and/or PyTorch","Study advanced topics: transformers, computer vision, reinforcement learning","Learn software engineering best practices for ML: testing, versioning, logging","Understand MLOps tooling: MLflow, DVC, Weights & Biases","Deploy models as REST APIs using FastAPI or Flask","Study distributed training and GPU optimisation","Contribute to ML research or open-source projects and publish findings"],
  "UX / UI Designer":["Learn core design principles: colour theory, typography, visual hierarchy","Master Figma — the industry-standard design and prototyping tool","Study user research methods: interviews, surveys, usability testing","Learn information architecture and user flow mapping","Create wireframes and interactive prototypes for real product ideas","Conduct usability tests and iterate rapidly on feedback","Study accessibility standards (WCAG) and inclusive design principles","Learn basic HTML and CSS so you can collaborate fluently with engineers","Build a portfolio of 3–5 in-depth case studies showing your process","Apply for junior UX roles, freelance projects, or design internships"],
  "Graphic Designer":["Study the fundamentals: colour, typography, layout, and composition","Master the Adobe Creative Suite — especially Illustrator and Photoshop","Learn Figma for digital and UI design work","Study branding and identity design: logos, style guides, visual systems","Practise print design: posters, brochures, packaging","Learn motion graphics basics with After Effects","Build a diverse portfolio showcasing a range of styles and media","Understand client briefs and professional feedback workflows","Freelance on small projects to build real-world experience","Grow your presence on Behance, Dribbble, and Instagram"],
  "Content Creator / Writer":["Write every day — practise clarity, conciseness, and voice","Study narrative structure, storytelling, and persuasive writing","Learn SEO fundamentals: keywords, on-page optimisation, search intent","Master one content format deeply: long-form, video scripts, or social media","Study copywriting frameworks: AIDA, PAS, and headline formulas","Learn basic analytics: Google Analytics, social media insights","Build a personal blog or YouTube channel to develop your audience","Understand content strategy: editorial calendars, audience personas, funnels","Pitch to publications or brands to get commissioned work","Grow your platform and build a portfolio of published work with results"],
  "Product Manager":["Learn the end-to-end product lifecycle from discovery to launch","Master agile frameworks: Scrum sprints, Kanban, and retrospectives","Study user research: customer interviews, Jobs-to-Be-Done, empathy mapping","Learn prioritisation frameworks: RICE, MoSCoW, and opportunity scoring","Practise writing clear Product Requirement Documents (PRDs)","Learn data analysis and A/B testing to measure product decisions","Develop stakeholder management and executive communication skills","Understand basic UX design and engineering workflows","Shadow or assist an experienced PM on a real product team","Build and ship a side project end-to-end to prove your PM instincts"],
  "Business Analyst":["Learn core BA concepts: requirements, use cases, process modelling","Master stakeholder interviews and facilitated workshops","Study process modelling: BPMN flowcharts and swimlane diagrams","Learn SQL to query databases and validate data independently","Practise writing Business Requirement Documents (BRDs) and user stories","Study agile and waterfall project methodologies","Understand ERP systems (SAP, Oracle) and CRM platforms (Salesforce)","Develop strong data visualisation and reporting skills (Tableau, Power BI)","Earn a BA certification: CBAP, PMI-PBA, or BCS Business Analysis","Work on a real project — even as a volunteer or intern — to build evidence"],
  "Entrepreneur / Startup Founder":["Read widely: startups, business models, technology trends, and psychology","Identify a real problem you care deeply about solving","Learn the basics of business model design and the Lean Startup method","Build a minimum viable product (MVP) as fast as possible","Talk to 100 potential customers before writing a single line of code","Learn digital marketing, SEO, and growth loops to acquire users","Study fundraising basics: pitch decks, term sheets, and investor relations","Build your network — find co-founders, advisors, and early customers","Learn basic financial literacy: P&L, cash flow, unit economics","Launch publicly, gather feedback relentlessly, and iterate fast"],
  "Marketing Manager":["Learn the fundamentals of marketing: the 4 Ps, segmentation, positioning","Master digital marketing channels: SEO, paid search, email, and social","Learn Google Analytics and data-driven decision making","Study copywriting and persuasive communication","Understand branding, brand voice, and visual identity","Run your first real marketing campaign — even on a tiny budget","Learn about customer journeys, funnels, and conversion optimisation","Study marketing automation tools: HubSpot, Mailchimp, Klaviyo","Earn a recognised certification: Google, Meta, or HubSpot","Build a portfolio of campaigns with clear ROI metrics to show employers"],
  "Financial Analyst":["Master Microsoft Excel: financial modelling, pivot tables, VLOOKUP","Study financial statements: income statement, balance sheet, cash flow","Learn valuation techniques: DCF, comparable company analysis, precedent transactions","Study accounting fundamentals and the principles behind financial reporting","Learn Python or SQL for financial data analysis at scale","Understand investment vehicles: equities, bonds, derivatives, alternatives","Study macroeconomics and how monetary policy affects markets","Build a financial model for a real publicly-traded company","Earn the CFA (Chartered Financial Analyst) Level 1 as a foundational credential","Apply for analyst roles at banks, investment firms, or corporate finance teams"],
  "Project Manager":["Learn project management fundamentals: scope, time, cost, and quality","Study agile methodologies: Scrum, Kanban, SAFe","Master a PM tool: Jira, Asana, Monday.com, or MS Project","Study risk management: identification, assessment, and mitigation strategies","Learn how to create and maintain project schedules and Gantt charts","Develop strong communication skills for stakeholder reporting and escalation","Study change management and how to bring teams through uncertainty","Earn the CAPM certification (entry-level) then work toward PMP","Practise running stand-ups, retrospectives, and sprint reviews","Deliver a real end-to-end project on time and on budget to build evidence"],
  "Data Analyst":["Learn SQL — the single most important skill for a data analyst","Master Excel or Google Sheets for data manipulation and pivot tables","Learn Python or R for analysis beyond what spreadsheets can handle","Study data visualisation tools: Tableau or Microsoft Power BI","Understand core statistics: mean, median, variance, hypothesis testing","Practise cleaning and transforming real-world messy datasets","Build at least three dashboards that tell a clear, actionable story","Study the business domain you want to work in (marketing, finance, ops)","Complete an end-to-end project and publish it on GitHub or Tableau Public","Earn the Google Data Analytics Certificate as a strong entry-level credential"],
  "Human Resources Manager":["Study the fundamentals of employment law in your region","Learn recruitment and talent acquisition best practices","Understand performance management frameworks and review processes","Study learning and development (L&D): training design and delivery","Learn compensation and benefits design and benchmarking","Master an HRIS platform: Workday, BambooHR, or SAP SuccessFactors","Study organisational culture, employee engagement, and wellbeing","Develop strong conflict resolution and mediation skills","Earn a CIPD (UK) or SHRM (US) professional HR qualification","Build experience across multiple HR disciplines before specialising"],
  "Educator / Teacher":["Identify the subject and age group you are most passionate about teaching","Study pedagogy: how people learn, Bloom's Taxonomy, and learning styles","Learn lesson planning: clear objectives, activities, and assessments","Develop classroom management skills and the ability to read a room","Learn to differentiate instruction for diverse learners","Study educational technology: interactive tools, LMS platforms","Earn a recognised teaching qualification (PGCE, QTS, or equivalent)","Practise public speaking and confident, clear explanation daily","Seek mentorship from experienced educators and observe their classes","Reflect consistently on your practice and never stop learning yourself"],
  "Healthcare Professional (Nurse / Paramedic)":["Complete a relevant undergraduate degree: Nursing, Paramedicine, or Allied Health","Master anatomy, physiology, and pathophysiology as your scientific foundation","Develop clinical skills: assessment, triage, medication administration","Study pharmacology: drug classes, dosing, interactions, and contraindications","Learn first aid and emergency response protocols to a professional standard","Complete supervised clinical placements in diverse healthcare settings","Develop therapeutic communication skills and bedside manner","Study medical ethics, patient rights, and professional accountability","Register with the relevant professional body (NMC, HCPC, or equivalent)","Continue professional development through specialisation and postgraduate study"],
  "Research Scientist":["Build an excellent undergraduate degree in your chosen scientific discipline","Develop rigorous statistical and data analysis skills","Learn scientific writing: research papers, grant proposals, and literature reviews","Master laboratory or computational techniques specific to your field","Complete a PhD or equivalent deep research experience","Publish peer-reviewed papers and present at academic conferences","Build a network of collaborators inside and outside your institution","Learn research project management and how to supervise junior researchers","Pursue postdoctoral research to develop an independent research agenda","Apply for faculty positions, research fellowships, or industry R&D roles"],
  "Environmental / Sustainability Consultant":["Earn a degree in Environmental Science, Ecology, or Sustainable Development","Learn environmental legislation and regulatory frameworks in your region","Study Environmental Impact Assessment (EIA) methodology","Develop strong data analysis skills for carbon accounting and footprinting","Learn GIS (Geographic Information Systems) for spatial environmental analysis","Study corporate sustainability frameworks: ESG, GRI, Science-Based Targets","Earn a relevant professional qualification (IEMA Associate or Full Membership)","Build experience through placements with consultancies, NGOs, or government","Develop stakeholder engagement and report-writing skills","Stay ahead of climate policy, clean technology, and sustainability innovation"],
};

// ─────────────────────────────────────────────────────────────────────────────
// LOCAL SCORING ENGINE  (mirrors career_logic.py — dot-product on trait vector)
// ─────────────────────────────────────────────────────────────────────────────
function _scoreLocally(answers) {
  const tv = answers.map(a => a === 0 ? 1.0 : a === 1 ? 0.5 : 0.0);
  let best = null, bestScore = -1;
  for (const career of FALLBACK_CAREERS) {
    const score = career.profile.reduce((sum, p, i) => sum + (tv[i] || 0) * p, 0);
    if (score > bestScore) { bestScore = score; best = career; }
  }
  return { career: best.name, description: best.description };
}

// ─────────────────────────────────────────────────────────────────────────────
// NETWORK HELPER — 3-second timeout, then fallback kicks in
// ─────────────────────────────────────────────────────────────────────────────
async function _fetchWithTimeout(url, options = {}, timeoutMs = 3000) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeoutMs);
  try {
    const res = await fetch(url, { ...options, signal: controller.signal });
    clearTimeout(timer);
    return res;
  } catch (err) {
    clearTimeout(timer);
    throw err;
  }
}

// ─────────────────────────────────────────────────────────────────────────────
// PUBLIC API FUNCTIONS
// ─────────────────────────────────────────────────────────────────────────────

async function getQuestions() {
  try {
    const res = await _fetchWithTimeout(`${BASE_URL}/api/questions`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();
    console.log("✅ Questions loaded from backend");
    return data.questions;
  } catch (err) {
    console.warn("⚠️ Backend unreachable — using local questions.", err.message);
    return FALLBACK_QUESTIONS;
  }
}

async function submitQuiz(answers) {
  try {
    const res = await _fetchWithTimeout(`${BASE_URL}/api/submitQuiz`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ answers }),
    });
    if (!res.ok) {
      const err = await res.json().catch(() => ({}));
      throw new Error(err.detail || `HTTP ${res.status}`);
    }
    console.log("✅ Quiz submitted to backend");
    return res.json();
  } catch (err) {
    console.warn("⚠️ Backend unreachable — scoring locally.", err.message);
    return _scoreLocally(answers);
  }
}

async function getRoadmap(career) {
  try {
    const res = await _fetchWithTimeout(
      `${BASE_URL}/api/roadmap/${encodeURIComponent(career)}`
    );
    if (!res.ok) {
      const err = await res.json().catch(() => ({}));
      throw new Error(err.detail || `HTTP ${res.status}`);
    }
    console.log("✅ Roadmap loaded from backend");
    return res.json();
  } catch (err) {
    console.warn("⚠️ Backend unreachable — using local roadmap.", err.message);
    const key = Object.keys(FALLBACK_ROADMAPS).find(
      k => k.toLowerCase() === career.toLowerCase()
    );
    if (!key) throw new Error(`No roadmap found for: ${career}`);
    return { career: key, roadmap: FALLBACK_ROADMAPS[key] };
  }
}