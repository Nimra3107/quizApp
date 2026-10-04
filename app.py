from flask import Flask, render_template

app = Flask(__name__)


# =========================
# QUIZ QUESTIONS
# =========================

questions = [

    {
        "question": "Which plant tissue transports water and minerals from roots to the aerial parts?",
        "options": ["Phloem", "Xylem", "Epidermis", "Cambium"],
        "answer": "Xylem"
    },

    {
        "question": "Which tissue transports sugars and other organic nutrients throughout the plant?",
        "options": ["Xylem", "Collenchyma", "Phloem", "Sclerenchyma"],
        "answer": "Phloem"
    },

    {
        "question": "Which structure is primarily responsible for gas exchange in leaves?",
        "options": ["Root hairs", "Stomata", "Xylem vessels", "Trichomes"],
        "answer": "Stomata"
    },

    {
        "question": "Which cells control the opening and closing of stomata?",
        "options": [
            "Epidermal cells",
            "Guard cells",
            "Companion cells",
            "Mesophyll cells"
        ],
        "answer": "Guard cells"
    },

    {
        "question": "Which part of the root absorbs most water and mineral ions from the soil?",
        "options": [
            "Root cap",
            "Root hairs",
            "Root apical meristem",
            "Endodermis"
        ],
        "answer": "Root hairs"
    },

    {
        "question": "What is the main function of the root cap?",
        "options": [
            "Photosynthesis",
            "Absorption of sugars",
            "Protection of the root tip",
            "Transport of water"
        ],
        "answer": "Protection of the root tip"
    },

    {
        "question": "Which tissue is mainly responsible for photosynthesis in a typical leaf?",
        "options": [
            "Mesophyll",
            "Phloem",
            "Pericycle",
            "Cork"
        ],
        "answer": "Mesophyll"
    },

    {
        "question": "Which type of mesophyll is usually located directly beneath the upper epidermis?",
        "options": [
            "Spongy mesophyll",
            "Palisade mesophyll",
            "Vascular cambium",
            "Collenchyma"
        ],
        "answer": "Palisade mesophyll"
    },

    {
        "question": "What is the primary function of the cuticle on a leaf?",
        "options": [
            "Increase mineral absorption",
            "Reduce water loss",
            "Transport sugars",
            "Produce pollen"
        ],
        "answer": "Reduce water loss"
    },

    {
        "question": "Which organelle is the main site of photosynthesis in plant cells?",
        "options": [
            "Mitochondrion",
            "Ribosome",
            "Chloroplast",
            "Nucleus"
        ],
        "answer": "Chloroplast"
    },

    {
        "question": "Which meristem is mainly responsible for increasing the length of roots and shoots?",
        "options": [
            "Lateral meristem",
            "Apical meristem",
            "Cork cambium",
            "Vascular cambium"
        ],
        "answer": "Apical meristem"
    },

    {
        "question": "Which meristem contributes primarily to an increase in plant thickness or girth?",
        "options": [
            "Apical meristem",
            "Lateral meristem",
            "Protoderm",
            "Ground meristem"
        ],
        "answer": "Lateral meristem"
    },

    {
        "question": "Which tissue provides flexible support to young and growing plant parts?",
        "options": [
            "Sclerenchyma",
            "Collenchyma",
            "Xylem",
            "Phloem"
        ],
        "answer": "Collenchyma"
    },

    {
        "question": "Which tissue provides strong mechanical support and has thick, lignified cell walls?",
        "options": [
            "Parenchyma",
            "Collenchyma",
            "Sclerenchyma",
            "Epidermis"
        ],
        "answer": "Sclerenchyma"
    },

    {
        "question": "What is the main function of phloem companion cells?",
        "options": [
            "Conduct water",
            "Control stomatal opening",
            "Support and maintain sieve tube elements",
            "Absorb water"
        ],
        "answer": "Support and maintain sieve tube elements"
    },

    {
        "question": "Which process causes water to move upward through the xylem due largely to evaporation from leaves?",
        "options": [
            "Transpiration pull",
            "Fermentation",
            "Glycolysis",
            "Translocation"
        ],
        "answer": "Transpiration pull"
    },

    {
        "question": "Which flower part produces pollen grains?",
        "options": [
            "Stigma",
            "Ovary",
            "Anther",
            "Sepal"
        ],
        "answer": "Anther"
    },

    {
        "question": "Which floral structure receives pollen during pollination?",
        "options": [
            "Anther",
            "Stigma",
            "Ovule",
            "Filament"
        ],
        "answer": "Stigma"
    },

    {
        "question": "Which structure develops into a seed after fertilization?",
        "options": [
            "Ovary wall",
            "Ovule",
            "Stigma",
            "Petal"
        ],
        "answer": "Ovule"
    },

    {
        "question": "Which structure develops into a fruit after fertilization in a typical flowering plant?",
        "options": [
            "Ovule",
            "Anther",
            "Ovary",
            "Stigma"
        ],
        "answer": "Ovary"
    }
]


# =========================
# HOME PAGE
# =========================

@app.route("/")
def home():
    return render_template(
        "index.html",
        questions=questions
    )


# =========================
# QUIZ PAGE
# =========================

@app.route("/quiz")
def quiz():
    return render_template(
        "quiz.html",
        questions=questions
    )


# =========================
# RUN FLASK
# =========================

if __name__ == "__main__":
    app.run(debug=True)
