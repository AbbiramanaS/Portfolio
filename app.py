# ============================================================
#   ABBIRAMANA S — Portfolio Website
#   Flask Application
#   Author  : Abbiramana S
#   Role    : Programmer Trainee @ SRM Tech
#   Email   : abbiramana@gmail.com
#   GitHub  : https://github.com/AbbiramanaS
#   LinkedIn: https://linkedin.com/in/abbiramanas/
# ============================================================

from flask import Flask, render_template

# ── App Initialisation ────────────────────────────────────────
app = Flask(__name__)


# ── Profile Data ──────────────────────────────────────────────
#    All content rendered into index.html via Jinja2 template.
#    Update any field here and the website updates automatically.

PROFILE = {

    # ── Personal ──────────────────────────────────────────────
    "name"       : "Abbiramana S",
    "tagline"    : "Data Analyst · AI Engineer · Programmer Trainee",
    "location"   : "Salem, Tamil Nadu, India",
    "email"      : "abbiramana@gmail.com",
    "phone"      : "+91 7397089551",
    "linkedin"   : "https://linkedin.com/in/abbiramanas/",
    "github"     : "https://github.com/AbbiramanaS",

    # ── Bio ───────────────────────────────────────────────────
    "bio": (
        "Detail-oriented Data Analyst and AI Engineer skilled in data cleaning, "
        "statistical analysis, data visualization, and predictive modeling. "
        "Experienced with Python, SQL, Power BI, and Tableau for deriving "
        "actionable insights. Strong foundation in machine learning workflows, "
        "data pipelines, and analytics automation. Currently working as a "
        "Programmer Trainee at SRM Tech, applying AI/ML knowledge to real-world "
        "software development challenges."
    ),

    # ── Stats ─────────────────────────────────────────────────
    "stats": [
        {"number": "4+",  "label": "Years of Study"},
        {"number": "7+",  "label": "Certifications"},
        {"number": "1",   "label": "Publication"},
        {"number": "3",   "label": "Internships"},
    ],

    # ── Education ─────────────────────────────────────────────
    "education": [
        {
            "degree"     : "B.Tech — Artificial Intelligence & Data Science",
            "institution": "Nehru Institute of Engineering and Technology",
            "location"   : "Coimbatore, Tamil Nadu",
            "period"     : "2021 – 2025",
            "grade"      : "CGPA: 7.54 / 10",
            "board"      : "",
        },
        {
            "degree"     : "Senior Secondary (Class XII)",
            "institution": "Jaivins Academy",
            "location"   : "Attur, Salem, Tamil Nadu",
            "period"     : "2020 – 2021",
            "grade"      : "68%",
            "board"      : "CBSE",
        },
        {
            "degree"     : "Secondary (Class X)",
            "institution": "Sri Vidya Mandir Senior Secondary School",
            "location"   : "Salem, Tamil Nadu",
            "period"     : "2018 – 2019",
            "grade"      : "53%",
            "board"      : "CBSE",
        },
    ],

    # ── Experience ────────────────────────────────────────────
    "experience": [
        {
            "role"    : "Programmer Trainee",
            "company" : "SRM Tech",
            "location": "Tamil Nadu",
            "period"  : "2025 — Present",
            "type"    : "Full-Time · Current",
            "points"  : [
                "Applying AI/ML knowledge in real-world software development.",
                "Working on data-driven programming tasks within the SRM Tech ecosystem.",
                "Contributing to internal tools and automation workflows.",
            ],
        },
        {
            "role"    : "Data Science Job Simulation",
            "company" : "BCG · Forage",
            "location": "Remote",
            "period"  : "September 2025",
            "type"    : "Virtual Simulation",
            "points"  : [
                "Analysed business datasets using Python (Pandas, NumPy, Seaborn).",
                "Built data visualisations and recommendation models for client scenarios.",
                "Derived strategic insights from complex enterprise data.",
            ],
        },
        {
            "role"    : "Cloud Computing Intern",
            "company" : "Novitech R&D Pvt. Ltd",
            "location": "Coimbatore",
            "period"  : "July 2023",
            "type"    : "Internship",
            "points"  : [
                "Explored cloud models, IoT integration, and AI data management.",
                "Gained hands-on experience with cloud infrastructure for AI workloads.",
            ],
        },
        {
            "role"    : "Data Analysis Intern",
            "company" : "Techvolt Pvt Ltd",
            "location": "Coimbatore",
            "period"  : "Feb – Mar 2023",
            "type"    : "Internship",
            "points"  : [
                "Cleaned and processed large datasets using Pandas and NumPy.",
                "Applied ML models to analyse data patterns and optimise performance.",
            ],
        },
    ],

    # ── Skills ────────────────────────────────────────────────
    "skills": [
        {
            "icon"    : "🐍",
            "category": "Languages",
            "tags"    : ["Python", "Java (Basics)", "C (Basics)", "SQL"],
        },
        {
            "icon"    : "🤖",
            "category": "ML Frameworks",
            "tags"    : ["TensorFlow", "Keras", "scikit-learn", "OpenCV", "YOLO", "CNN"],
        },
        {
            "icon"    : "📊",
            "category": "Data & Analytics",
            "tags"    : ["Pandas", "NumPy", "Seaborn", "Power BI", "Tableau"],
        },
        {
            "icon"    : "🛠️",
            "category": "Tools & Platforms",
            "tags"    : ["Docker", "GitHub", "IBM Watson", "Raspberry Pi"],
        },
        {
            "icon"    : "🧠",
            "category": "AI Concepts",
            "tags"    : ["Machine Learning", "Deep Learning", "Computer Vision",
                         "Data Pipelines", "Reinforcement Learning (Basic)"],
        },
        {
            "icon"    : "☁️",
            "category": "Cloud & IoT",
            "tags"    : ["AWS", "Cloud Computing", "IoT Integration", "Edge ML"],
        },
    ],

    # ── Projects ──────────────────────────────────────────────
    "projects": [
        {
            "title"      : "AI-Powered Smart Visual Aid for the Blind",
            "badge"      : "📄 Published · IJARESM Vol. 5, Issue 13 — May 2025",
            "description": (
                "Developed a Python & OpenCV system using CNN and YOLO for real-time "
                "object and face detection, designed to assist visually impaired users. "
                "Integrated audio feedback and IoT modules for autonomous, wearable "
                "real-time interaction. Containerised with Docker for portable deployment "
                "on Raspberry Pi hardware."
            ),
            "tools"      : ["Python", "OpenCV", "CNN", "YOLO", "Raspberry Pi",
                            "Docker", "IoT", "Audio Feedback"],
            "publication": '"AI-Powered Smart Visual Aid for Blind" — IJARESM, Vol. 5, Issue 13 (May 2025)',
        },
    ],

    # ── Certifications ────────────────────────────────────────
    "certifications": [
        {"name": "Data Analytics Process Automation (AI & ML)", "issuer": "Google for Developers", "icon": "🌐"},
        {"name": "Data Science Master",                          "issuer": "ALTAIR",                "icon": "📊"},
        {"name": "AI and ML",                                    "issuer": "Amazon Web Services",   "icon": "☁️"},
        {"name": "Networking Cloud",                             "issuer": "JUNIPER",               "icon": "🌐"},
        {"name": "Foundation of Cloud IoT Edge ML (2025)",       "issuer": "NPTEL",                 "icon": "🤖"},
        {"name": "Machine Learning (2024)",                      "issuer": "NPTEL",                 "icon": "🧠"},
        {"name": "Python for Data Science (2023)",               "issuer": "NPTEL",                 "icon": "🐍"},
    ],

    # ── Languages ─────────────────────────────────────────────
    "languages": ["Tamil", "English"],
}


# ── Routes ────────────────────────────────────────────────────

@app.route("/")
def index():
    """Render the main portfolio page."""
    return render_template("index.html", p=PROFILE)


# ── Entry Point ───────────────────────────────────────────────

if __name__ == "__main__":
    app.run(debug=True, port=5000)
