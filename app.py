from flask import Flask, render_template, request
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)


app = Flask(__name__)


# ==============================
# LOAD DATASET
# ==============================

data = pd.read_csv("placement_data.csv")


# ==============================
# INPUT FEATURES
# ==============================

X = data[
    [
        "cgpa",
        "aptitude",
        "communication",
        "projects",
        "internships"
    ]
]


# ==============================
# TARGET
# ==============================

y = data["placement"]


# ==============================
# TRAIN TEST SPLIT
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# ==============================
# RANDOM FOREST MODEL
# ==============================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


model.fit(X_train, y_train)


# ==============================
# MODEL EVALUATION
# ==============================

y_prediction = model.predict(X_test)


accuracy = accuracy_score(
    y_test,
    y_prediction
)


precision = precision_score(
    y_test,
    y_prediction,
    zero_division=0
)


recall = recall_score(
    y_test,
    y_prediction,
    zero_division=0
)


f1 = f1_score(
    y_test,
    y_prediction,
    zero_division=0
)


cm = confusion_matrix(
    y_test,
    y_prediction
)


tn, fp, fn, tp = cm.ravel()


# ==============================
# JOB SKILLS
# ==============================

job_skills = {

    "Data Scientist": [
        "Python",
        "SQL",
        "Statistics",
        "Machine Learning",
        "Pandas",
        "NumPy"
    ],

    "Data Analyst": [
        "Python",
        "SQL",
        "Excel",
        "Power BI",
        "Statistics"
    ],

    "Python Developer": [
        "Python",
        "OOP",
        "Django",
        "SQL",
        "Git"
    ],

    "Web Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Git"
    ]
}


# ==============================
# HOME PAGE
# ==============================

@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    probability = None

    recommended_skills = []

    recommended_jobs = []

    student_details = None


    # ==============================
    # WHEN FORM IS SUBMITTED
    # ==============================

    if request.method == "POST":

        cgpa = float(
            request.form["cgpa"]
        )

        aptitude = float(
            request.form["aptitude"]
        )

        communication = float(
            request.form["communication"]
        )

        projects = int(
            request.form["projects"]
        )

        internships = int(
            request.form["internships"]
        )


        # ==============================
        # STUDENT DETAILS
        # ==============================

        student_details = {

            "CGPA": cgpa,

            "Aptitude Score": aptitude,

            "Communication Score": communication,

            "Projects": projects,

            "Internships": internships
        }


        # ==============================
        # STUDENT DATA
        # ==============================

        student = [[

            cgpa,

            aptitude,

            communication,

            projects,

            internships

        ]]


        # ==============================
        # PLACEMENT PREDICTION
        # ==============================

        prediction = model.predict(
            student
        )[0]


        probability = (
            model.predict_proba(student)[0][1]
            * 100
        )


        if prediction == 1:

            result = "LIKELY TO BE PLACED"

        else:

            result = "NOT LIKELY TO BE PLACED"


        # ==============================
        # TARGET JOB
        # ==============================

        target_job = request.form[
            "target_job"
        ]


        # ==============================
        # STUDENT SKILLS
        # ==============================

        student_skills = [

            skill.strip().lower()

            for skill in request.form[
                "student_skills"
            ].split(",")

        ]


        # ==============================
        # SKILL GAP ANALYSIS
        # ==============================

        required_skills = job_skills[
            target_job
        ]


        for skill in required_skills:

            if skill.lower() not in student_skills:

                recommended_skills.append(
                    skill
                )


        # ==============================
        # JOB RECOMMENDATION
        # ==============================

        job_scores = {}


        for job, skills in job_skills.items():

            matched_skills = 0


            for skill in skills:

                if skill.lower() in student_skills:

                    matched_skills += 1


            score = (
                matched_skills
                / len(skills)
                * 100
            )


            job_scores[job] = score


        # ==============================
        # SORT JOBS
        # ==============================

        recommended_jobs = sorted(

            job_scores.items(),

            key=lambda x: x[1],

            reverse=True

        )


    # ==============================
    # SEND DATA TO HTML
    # ==============================

    return render_template(

        "index.html",

        result=result,

        probability=probability,

        recommended_skills=recommended_skills,

        recommended_jobs=recommended_jobs,

        student_details=student_details,

        accuracy=accuracy,

        precision=precision,

        recall=recall,

        f1=f1,

        tn=tn,

        fp=fp,

        fn=fn,

        tp=tp

    )


# ==============================
# START FLASK
# ==============================

if __name__ == "__main__":

    print(
        "AI Placement System Starting..."
    )

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )