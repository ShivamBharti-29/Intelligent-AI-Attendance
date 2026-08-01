import streamlit as st
import pandas as pd
from datetime import datetime

from src.pipelines.voice_pipeline import process_bulk_audio
from src.database.config import supabase
from src.components.dialog_attendance_results import show_attendance_result

# Voice similarity threshold
VOICE_THRESHOLD = 0.65


@st.dialog("Voice Attendance")
def voice_attendance_dialog(selected_subject_id):

    # Clear previous results when dialog opens
    if "voice_attendance_results" not in st.session_state:
        st.session_state.voice_attendance_results = None

    st.write(
        "🎤 Record the classroom audio while students say **'I am present'** one by one."
    )

    audio_data = st.audio_input("Record classroom audio")

    if st.button(
        "Analyze Audio",
        type="primary",
        width="stretch",
        icon=":material/mic:"
    ):

        # Ensure audio exists
        if audio_data is None:
            st.warning("Please record classroom audio before analyzing.")
            return

        with st.spinner("Processing audio..."):

            # Fetch enrolled students
            enrolled_res = (
                supabase.table("subject_students")
                .select("*, students(*)")
                .eq("subject_id", selected_subject_id)
                .execute()
            )

            enrolled_students = enrolled_res.data

            if not enrolled_students:
                st.warning("No students are enrolled in this course.")
                return

            # Build candidate dictionary
            candidates_dict = {
                student["students"]["student_id"]: student["students"]["voice_embedding"]
                for student in enrolled_students
                if student["students"].get("voice_embedding")
            }

            if not candidates_dict:
                st.error("No enrolled students have registered voice profiles.")
                return

            # Read audio bytes
            audio_bytes = audio_data.read()

            # Process voice recognition
            detected_scores = process_bulk_audio(audio_bytes, candidates_dict)

            results = []
            attendance_to_log = []

            current_timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

            for node in enrolled_students:

                student = node["students"]

                score = float(detected_scores.get(student["student_id"], 0.0))

                is_present = bool(score >= VOICE_THRESHOLD)

                results.append(
                    {
                        "Name": student["name"],
                        "ID": student["student_id"],
                        "Score": round(score, 3),
                        "Status": "✅ Present" if is_present else "❌ Absent",
                    }
                )

                attendance_to_log.append(
                    {
                        "student_id": int(student["student_id"]),
                        "subject_id": int(selected_subject_id),
                        "timestamp": current_timestamp,
                        "is_present": is_present,
                    }
                )

            st.session_state.voice_attendance_results = (
                pd.DataFrame(results),
                attendance_to_log,
            )

    # Display results
    if st.session_state.get("voice_attendance_results"):

        st.divider()

        df_results, logs = st.session_state.voice_attendance_results

        show_attendance_result(df_results, logs)