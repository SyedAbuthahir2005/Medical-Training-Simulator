from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import random

app = Flask(__name__)


# =========================================================
# MISTRAL CONFIGURATION
# =========================================================

MISTRAL_API_KEY = "Ob5o2WIOeco7FVYGZof7n6UihfM803VG"

client = OpenAI(
    api_key="Ob5o2WIOeco7FVYGZof7n6UihfM803VG",
    base_url="https://api.mistral.ai/v1"
)

MODEL = "mistral-small-latest"


# =========================================================
# MEDICAL CASES
# =========================================================

CASES = [

    {
        "id": 1,
        "title": "Chest Pain",
        "category": "Cardiology",
        "difficulty": "Beginner",
        "age": 52,
        "gender": "Male",
        "chief_complaint": "Chest discomfort",
        "hidden_diagnosis": "Acute coronary syndrome",
        "symptoms": [
            "Central chest pressure",
            "Pain radiating to the left arm",
            "Sweating",
            "Mild shortness of breath"
        ],
        "history": "History of hypertension. Smoker.",
        "vitals": {
            "Blood Pressure": "150/95 mmHg",
            "Heart Rate": "102 bpm",
            "Temperature": "36.8 °C",
            "SpO2": "96%"
        },
        "tests": {
            "Blood Test": "Troponin level is elevated.",
            "ECG": "ST-segment changes are present.",
            "X-Ray": "No acute lung abnormality."
        }
    },

    {
        "id": 2,
        "title": "Abdominal Pain",
        "category": "Gastroenterology",
        "difficulty": "Beginner",
        "age": 28,
        "gender": "Female",
        "chief_complaint": "Lower abdominal pain",
        "hidden_diagnosis": "Acute appendicitis",
        "symptoms": [
            "Pain beginning around the umbilicus",
            "Pain moving to the right lower abdomen",
            "Nausea",
            "Low-grade fever"
        ],
        "history": "No major previous medical history.",
        "vitals": {
            "Blood Pressure": "118/76 mmHg",
            "Heart Rate": "96 bpm",
            "Temperature": "38.1 °C",
            "SpO2": "99%"
        },
        "tests": {
            "Blood Test": "White blood cell count is elevated.",
            "ECG": "Normal ECG.",
            "X-Ray": "No significant abnormality."
        }
    },

    {
        "id": 3,
        "title": "Breathing Difficulty",
        "category": "Respiratory",
        "difficulty": "Intermediate",
        "age": 35,
        "gender": "Male",
        "chief_complaint": "Shortness of breath",
        "hidden_diagnosis": "Acute asthma exacerbation",
        "symptoms": [
            "Wheezing",
            "Shortness of breath",
            "Chest tightness",
            "Night-time symptoms"
        ],
        "history": "Known history of asthma.",
        "vitals": {
            "Blood Pressure": "125/80 mmHg",
            "Heart Rate": "108 bpm",
            "Temperature": "36.7 °C",
            "SpO2": "92%"
        },
        "tests": {
            "Blood Test": "No significant abnormality.",
            "ECG": "Sinus tachycardia.",
            "X-Ray": "No focal consolidation."
        }
    },

    {
        "id": 4,
        "title": "Headache",
        "category": "Neurology",
        "difficulty": "Intermediate",
        "age": 24,
        "gender": "Female",
        "chief_complaint": "Severe headache",
        "hidden_diagnosis": "Migraine",
        "symptoms": [
            "One-sided throbbing headache",
            "Sensitivity to light",
            "Nausea",
            "Previous similar episodes"
        ],
        "history": "Previous episodes of similar headaches.",
        "vitals": {
            "Blood Pressure": "120/78 mmHg",
            "Heart Rate": "82 bpm",
            "Temperature": "36.6 °C",
            "SpO2": "99%"
        },
        "tests": {
            "Blood Test": "Normal.",
            "ECG": "Normal ECG.",
            "X-Ray": "No significant finding."
        }
    },

    {
        "id": 5,
        "title": "Fever and Cough",
        "category": "Infectious Disease",
        "difficulty": "Advanced",
        "age": 67,
        "gender": "Male",
        "chief_complaint": "Fever and cough",
        "hidden_diagnosis": "Community-acquired pneumonia",
        "symptoms": [
            "High fever",
            "Productive cough",
            "Shortness of breath",
            "Chest discomfort"
        ],
        "history": "History of type 2 diabetes.",
        "vitals": {
            "Blood Pressure": "110/70 mmHg",
            "Heart Rate": "105 bpm",
            "Temperature": "39.2 °C",
            "SpO2": "91%"
        },
        "tests": {
            "Blood Test": "Elevated white blood cell count.",
            "ECG": "Sinus tachycardia.",
            "X-Ray": "Right lower lobe consolidation."
        }
    }

]


# =========================================================
# HOME PAGE
# =========================================================

@app.route("/")
def index():
    return render_template("index.html")


# =========================================================
# GET AVAILABLE CASES
# =========================================================

@app.route("/api/cases", methods=["GET"])
def get_cases():

    case_list = []

    for case in CASES:

        case_list.append({
            "id": case["id"],
            "title": case["title"],
            "category": case["category"],
            "difficulty": case["difficulty"],
            "age": case["age"],
            "gender": case["gender"],
            "chief_complaint": case["chief_complaint"]
        })

    return jsonify(case_list)


# =========================================================
# START NEW CASE
# =========================================================

@app.route("/api/new-case", methods=["POST"])
def new_case():

    data = request.get_json() or {}

    difficulty = data.get("difficulty", "All")

    available_cases = CASES

    if difficulty != "All":
        available_cases = [
            case for case in CASES
            if case["difficulty"] == difficulty
        ]

    case = random.choice(available_cases)

    return jsonify({
        "id": case["id"],
        "title": case["title"],
        "category": case["category"],
        "difficulty": case["difficulty"],
        "age": case["age"],
        "gender": case["gender"],
        "chief_complaint": case["chief_complaint"]
    })


# =========================================================
# PATIENT CHAT
# =========================================================

@app.route("/api/chat", methods=["POST"])
def chat():

    try:

        data = request.get_json()

        messages = data.get("messages", [])

        patient_data = data.get("patient", {})

        if not messages:

            return jsonify({
                "error": "No conversation provided."
            }), 400


        patient_prompt = f"""
You are role-playing as a real human patient in a medical
student training simulation.

The USER is the DOCTOR.

You are NOT the doctor.
You are NOT a medical assistant.
You are ONLY the patient.

PATIENT INFORMATION:

Age: {patient_data.get('age')}
Gender: {patient_data.get('gender')}
Chief Complaint: {patient_data.get('chief_complaint')}

IMPORTANT RULES:

1. Respond naturally as the patient.

2. Answer the doctor's questions based on the hidden medical case.

3. Do not reveal the diagnosis directly.

4. Do not say that you are an AI.

5. Do not give medical advice.

6. Do not automatically reveal every symptom.

7. Only provide information when the doctor asks about it.

8. If the doctor asks about medical history, answer naturally.

9. If the doctor asks about medications, answer naturally.

10. If the doctor asks about lifestyle, answer naturally.

11. If the doctor asks about symptoms, answer naturally.

12. Keep answers realistic and reasonably short.

13. Do not use medical terminology unless a real patient would
normally use it.

14. If the doctor asks for a physical examination, say:
"I don't know the results of my physical examination. You can
request the examination from the system."

15. Never reveal the hidden diagnosis.

Respond as if this is a real doctor-patient consultation.
"""


        full_messages = [

            {
                "role": "system",
                "content": patient_prompt
            }

        ] + messages


        response = client.chat.completions.create(

            model=MODEL,

            messages=full_messages,

            temperature=0.7,

            max_tokens=400

        )


        answer = response.choices[0].message.content


        return jsonify({

            "message": answer

        })


    except Exception as e:

        print("MISTRAL ERROR:", str(e))

        return jsonify({

            "error": str(e)

        }), 500


# =========================================================
# PHYSICAL EXAMINATION
# =========================================================

@app.route("/api/examination", methods=["POST"])
def examination():

    data = request.get_json()

    case_id = data.get("case_id")

    case = next(
        (c for c in CASES if c["id"] == case_id),
        None
    )

    if not case:

        return jsonify({
            "error": "Case not found."
        }), 404


    return jsonify({

        "vitals": case["vitals"],

        "examination": (
            "Physical examination findings are consistent "
            "with the patient's presenting complaint."
        )

    })


# =========================================================
# MEDICAL TESTS
# =========================================================

@app.route("/api/test", methods=["POST"])
def test():

    data = request.get_json()

    case_id = data.get("case_id")

    test_name = data.get("test")

    case = next(
        (c for c in CASES if c["id"] == case_id),
        None
    )

    if not case:

        return jsonify({
            "error": "Case not found."
        }), 404


    result = case["tests"].get(

        test_name,

        "This test is not available for this case."

    )


    return jsonify({

        "test": test_name,

        "result": result

    })


# =========================================================
# DIAGNOSIS EVALUATION
# =========================================================

@app.route("/api/evaluate", methods=["POST"])
def evaluate():

    data = request.get_json()

    case_id = data.get("case_id")

    diagnosis = data.get("diagnosis", "")


    case = next(

        (c for c in CASES if c["id"] == case_id),

        None

    )


    if not case:

        return jsonify({

            "error": "Case not found."

        }), 404


    correct_diagnosis = case["hidden_diagnosis"]


    evaluation_prompt = f"""

You are evaluating a medical student in a training simulator.

The correct diagnosis is:

{correct_diagnosis}

The student's diagnosis is:

{diagnosis}

Give a concise evaluation.

Return:

1. Correctness
2. Score out of 100
3. Short clinical reasoning feedback
4. One suggestion for improvement

Do not provide real-world medical advice.

"""


    response = client.chat.completions.create(

        model=MODEL,

        messages=[

            {

                "role": "system",

                "content": evaluation_prompt

            }

        ],

        temperature=0.3,

        max_tokens=300

    )


    feedback = response.choices[0].message.content


    return jsonify({

        "correct_diagnosis":
        correct_diagnosis,

        "feedback":
        feedback

    })


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":

    app.run(debug=True)