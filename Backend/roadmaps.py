"""
roadmaps.py
-----------
10-step learning roadmap for every career defined in career_logic.py.
Called by GET /api/roadmap/{career}.
"""

ROADMAPS: dict[str, list[str]] = {

    # ── Tech / Engineering ───────────────────────────────────────────────────

    "Software Engineer": [
        "Master the fundamentals of a first language — Python or JavaScript",
        "Learn data structures and algorithms (arrays, trees, sorting, searching)",
        "Understand version control with Git and GitHub",
        "Build your first full-stack project (frontend + backend + database)",
        "Study object-oriented and functional programming patterns",
        "Learn SQL and at least one NoSQL database",
        "Understand REST APIs, HTTP, and basic system design",
        "Write unit and integration tests — practise Test-Driven Development",
        "Deploy applications to the cloud (AWS, GCP, or Azure)",
        "Contribute to open-source projects and build a strong GitHub portfolio",
    ],
    "Data Scientist": [
        "Learn Python programming fundamentals and the scientific stack",
        "Master statistics: distributions, hypothesis testing, Bayesian thinking",
        "Explore data wrangling with pandas and NumPy",
        "Learn data visualisation with Matplotlib and Seaborn",
        "Study machine learning fundamentals with scikit-learn",
        "Dive into deep learning with TensorFlow or PyTorch",
        "Practice SQL for querying and joining large datasets",
        "Build and document end-to-end ML projects from raw data to insight",
        "Learn MLOps: model versioning, deployment, and monitoring",
        "Publish projects on GitHub and compete on Kaggle to build reputation",
    ],
    "Cybersecurity Analyst": [
        "Build a solid foundation in networking — TCP/IP, DNS, HTTP, firewalls",
        "Learn Linux fundamentals and confident command-line usage",
        "Study core security principles: CIA triad, encryption, authentication",
        "Learn Python or Bash scripting for security automation",
        "Get hands-on with ethical hacking tools: Kali Linux, Nmap, Burp Suite",
        "Study common attack vectors: SQL injection, XSS, phishing, MITM",
        "Learn SIEM tools and practise log analysis",
        "Set up a home lab and tackle Capture-the-Flag (CTF) challenges",
        "Earn a recognised certification: CompTIA Security+, CEH, or OSCP",
        "Apply for a SOC Analyst or junior Penetration Tester role",
    ],
    "DevOps Engineer": [
        "Master Linux administration and shell scripting",
        "Learn at least one programming language well (Python or Go)",
        "Understand version control workflows: branching strategies, pull requests",
        "Study containerisation with Docker and orchestration with Kubernetes",
        "Learn CI/CD pipelines using GitHub Actions, Jenkins, or GitLab CI",
        "Master infrastructure-as-code with Terraform or Ansible",
        "Understand cloud platforms: AWS, GCP, or Azure fundamentals",
        "Study monitoring, logging, and alerting with Prometheus and Grafana",
        "Learn site reliability engineering (SRE) principles and SLOs",
        "Earn a cloud certification (AWS Solutions Architect or GCP Professional)",
    ],
    "Machine Learning Engineer": [
        "Master Python and the scientific stack: NumPy, pandas, scikit-learn",
        "Study linear algebra, calculus, and probability in depth",
        "Build and train neural networks from scratch before using frameworks",
        "Deep-dive into TensorFlow and/or PyTorch",
        "Study advanced topics: transformers, computer vision, reinforcement learning",
        "Learn software engineering best practices for ML: testing, versioning, logging",
        "Understand MLOps tooling: MLflow, DVC, Weights & Biases",
        "Deploy models as REST APIs using FastAPI or Flask",
        "Study distributed training and GPU optimisation",
        "Contribute to ML research or open-source projects and publish findings",
    ],

    # ── Design / Creative ────────────────────────────────────────────────────

    "UX / UI Designer": [
        "Learn core design principles: colour theory, typography, visual hierarchy",
        "Master Figma — the industry-standard design and prototyping tool",
        "Study user research methods: interviews, surveys, usability testing",
        "Learn information architecture and user flow mapping",
        "Create wireframes and interactive prototypes for real product ideas",
        "Conduct usability tests and iterate rapidly on feedback",
        "Study accessibility standards (WCAG) and inclusive design principles",
        "Learn basic HTML and CSS so you can collaborate fluently with engineers",
        "Build a portfolio of 3–5 in-depth case studies showing your process",
        "Apply for junior UX roles, freelance projects, or design internships",
    ],
    "Graphic Designer": [
        "Study the fundamentals: colour, typography, layout, and composition",
        "Master the Adobe Creative Suite — especially Illustrator and Photoshop",
        "Learn Figma for digital and UI design work",
        "Study branding and identity design: logos, style guides, visual systems",
        "Practise print design: posters, brochures, packaging",
        "Learn motion graphics basics with After Effects",
        "Build a diverse portfolio showcasing a range of styles and media",
        "Understand client briefs and professional feedback workflows",
        "Freelance on small projects to build real-world experience",
        "Grow your presence on Behance, Dribbble, and Instagram",
    ],
    "Content Creator / Writer": [
        "Write every day — practise clarity, conciseness, and voice",
        "Study narrative structure, storytelling, and persuasive writing",
        "Learn SEO fundamentals: keywords, on-page optimisation, search intent",
        "Master one content format deeply: long-form, video scripts, or social media",
        "Study copywriting frameworks: AIDA, PAS, and headline formulas",
        "Learn basic analytics: Google Analytics, social media insights",
        "Build a personal blog or YouTube channel to develop your audience",
        "Understand content strategy: editorial calendars, audience personas, funnels",
        "Pitch to publications or brands to get commissioned work",
        "Grow your platform and build a portfolio of published work with results",
    ],

    # ── Business / Management ────────────────────────────────────────────────

    "Product Manager": [
        "Learn the end-to-end product lifecycle from discovery to launch",
        "Master agile frameworks: Scrum sprints, Kanban, and retrospectives",
        "Study user research: customer interviews, Jobs-to-Be-Done, empathy mapping",
        "Learn prioritisation frameworks: RICE, MoSCoW, and opportunity scoring",
        "Practise writing clear Product Requirement Documents (PRDs)",
        "Learn data analysis and A/B testing to measure product decisions",
        "Develop stakeholder management and executive communication skills",
        "Understand basic UX design and engineering workflows",
        "Shadow or assist an experienced PM on a real product team",
        "Build and ship a side project end-to-end to prove your PM instincts",
    ],
    "Business Analyst": [
        "Learn core BA concepts: requirements, use cases, process modelling",
        "Master stakeholder interviews and facilitated workshops",
        "Study process modelling: BPMN flowcharts and swimlane diagrams",
        "Learn SQL to query databases and validate data independently",
        "Practise writing Business Requirement Documents (BRDs) and user stories",
        "Study agile and waterfall project methodologies",
        "Understand ERP systems (SAP, Oracle) and CRM platforms (Salesforce)",
        "Develop strong data visualisation and reporting skills (Tableau, Power BI)",
        "Earn a BA certification: CBAP, PMI-PBA, or BCS Business Analysis",
        "Work on a real project — even as a volunteer or intern — to build evidence",
    ],
    "Entrepreneur / Startup Founder": [
        "Read widely: startups, business models, technology trends, and psychology",
        "Identify a real problem you care deeply about solving",
        "Learn the basics of business model design and the Lean Startup method",
        "Build a minimum viable product (MVP) as fast as possible",
        "Talk to 100 potential customers before writing a single line of code",
        "Learn digital marketing, SEO, and growth loops to acquire users",
        "Study fundraising basics: pitch decks, term sheets, and investor relations",
        "Build your network — find co-founders, advisors, and early customers",
        "Learn basic financial literacy: P&L, cash flow, unit economics",
        "Launch publicly, gather feedback relentlessly, and iterate fast",
    ],
    "Marketing Manager": [
        "Learn the fundamentals of marketing: the 4 Ps, segmentation, positioning",
        "Master digital marketing channels: SEO, paid search, email, and social",
        "Learn Google Analytics and data-driven decision making",
        "Study copywriting and persuasive communication",
        "Understand branding, brand voice, and visual identity",
        "Run your first real marketing campaign — even on a tiny budget",
        "Learn about customer journeys, funnels, and conversion optimisation",
        "Study marketing automation tools: HubSpot, Mailchimp, Klaviyo",
        "Earn a recognised certification: Google, Meta, or HubSpot",
        "Build a portfolio of campaigns with clear ROI metrics to show employers",
    ],
    "Financial Analyst": [
        "Master Microsoft Excel: financial modelling, pivot tables, VLOOKUP",
        "Study financial statements: income statement, balance sheet, cash flow",
        "Learn valuation techniques: DCF, comparable company analysis, precedent transactions",
        "Study accounting fundamentals and the principles behind financial reporting",
        "Learn Python or SQL for financial data analysis at scale",
        "Understand investment vehicles: equities, bonds, derivatives, alternatives",
        "Study macroeconomics and how monetary policy affects markets",
        "Build a financial model for a real publicly-traded company",
        "Earn the CFA (Chartered Financial Analyst) Level 1 as a foundational credential",
        "Apply for analyst roles at banks, investment firms, or corporate finance teams",
    ],
    "Project Manager": [
        "Learn project management fundamentals: scope, time, cost, and quality",
        "Study agile methodologies: Scrum, Kanban, SAFe",
        "Master a PM tool: Jira, Asana, Monday.com, or MS Project",
        "Study risk management: identification, assessment, and mitigation strategies",
        "Learn how to create and maintain project schedules and Gantt charts",
        "Develop strong communication skills for stakeholder reporting and escalation",
        "Study change management and how to bring teams through uncertainty",
        "Earn the CAPM certification (entry-level) then work toward PMP",
        "Practise running stand-ups, retrospectives, and sprint reviews",
        "Deliver a real end-to-end project on time and on budget to build evidence",
    ],

    # ── People / Social ──────────────────────────────────────────────────────

    "Data Analyst": [
        "Learn SQL — the single most important skill for a data analyst",
        "Master Excel or Google Sheets for data manipulation and pivot tables",
        "Learn Python or R for analysis beyond what spreadsheets can handle",
        "Study data visualisation tools: Tableau or Microsoft Power BI",
        "Understand core statistics: mean, median, variance, hypothesis testing",
        "Practise cleaning and transforming real-world messy datasets",
        "Build at least three dashboards that tell a clear, actionable story",
        "Study the business domain you want to work in (marketing, finance, ops)",
        "Complete an end-to-end project and publish it on GitHub or Tableau Public",
        "Earn the Google Data Analytics Certificate as a strong entry-level credential",
    ],
    "Human Resources Manager": [
        "Study the fundamentals of employment law in your region",
        "Learn recruitment and talent acquisition best practices",
        "Understand performance management frameworks and review processes",
        "Study learning and development (L&D): training design and delivery",
        "Learn compensation and benefits design and benchmarking",
        "Master an HRIS platform: Workday, BambooHR, or SAP SuccessFactors",
        "Study organisational culture, employee engagement, and wellbeing",
        "Develop strong conflict resolution and mediation skills",
        "Earn a CIPD (UK) or SHRM (US) professional HR qualification",
        "Build experience across multiple HR disciplines before specialising",
    ],
    "Educator / Teacher": [
        "Identify the subject and age group you are most passionate about teaching",
        "Study pedagogy: how people learn, Bloom's Taxonomy, and learning styles",
        "Learn lesson planning: clear objectives, activities, and assessments",
        "Develop classroom management skills and the ability to read a room",
        "Learn to differentiate instruction for diverse learners",
        "Study educational technology: interactive tools, LMS platforms",
        "Earn a recognised teaching qualification (PGCE, QTS, or equivalent)",
        "Practise public speaking and confident, clear explanation daily",
        "Seek mentorship from experienced educators and observe their classes",
        "Reflect consistently on your practice and never stop learning yourself",
    ],
    "Healthcare Professional (Nurse / Paramedic)": [
        "Complete a relevant undergraduate degree: Nursing, Paramedicine, or Allied Health",
        "Master anatomy, physiology, and pathophysiology as your scientific foundation",
        "Develop clinical skills: assessment, triage, medication administration",
        "Study pharmacology: drug classes, dosing, interactions, and contraindications",
        "Learn first aid and emergency response protocols to a professional standard",
        "Complete supervised clinical placements in diverse healthcare settings",
        "Develop therapeutic communication skills and bedside manner",
        "Study medical ethics, patient rights, and professional accountability",
        "Register with the relevant professional body (NMC, HCPC, or equivalent)",
        "Continue professional development through specialisation and postgraduate study",
    ],

    # ── Science / Research ───────────────────────────────────────────────────

    "Research Scientist": [
        "Build an excellent undergraduate degree in your chosen scientific discipline",
        "Develop rigorous statistical and data analysis skills",
        "Learn scientific writing: research papers, grant proposals, and literature reviews",
        "Master laboratory or computational techniques specific to your field",
        "Complete a PhD or equivalent deep research experience",
        "Publish peer-reviewed papers and present at academic conferences",
        "Build a network of collaborators inside and outside your institution",
        "Learn research project management and how to supervise junior researchers",
        "Pursue postdoctoral research to develop an independent research agenda",
        "Apply for faculty positions, research fellowships, or industry R&D roles",
    ],
    "Environmental / Sustainability Consultant": [
        "Earn a degree in Environmental Science, Ecology, or Sustainable Development",
        "Learn environmental legislation and regulatory frameworks in your region",
        "Study Environmental Impact Assessment (EIA) methodology",
        "Develop strong data analysis skills for carbon accounting and footprinting",
        "Learn GIS (Geographic Information Systems) for spatial environmental analysis",
        "Study corporate sustainability frameworks: ESG, GRI, Science-Based Targets",
        "Earn a relevant professional qualification (IEMA Associate or Full Membership)",
        "Build experience through placements with consultancies, NGOs, or government",
        "Develop stakeholder engagement and report-writing skills",
        "Stay ahead of climate policy, clean technology, and sustainability innovation",
    ],
}


def get_roadmap(career: str) -> dict | None:
    """
    Return the roadmap dict for a given career name, or None if not found.
    Case-insensitive lookup.
    """
    for key, steps in ROADMAPS.items():
        if key.lower() == career.lower():
            return {"career": key, "roadmap": steps}
    return None