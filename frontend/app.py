import streamlit as st
import requests

# Set page config FIRST
st.set_page_config(page_title="AI Customer Support", page_icon="🤖", layout="centered")

# Then custom CSS for cursor
st.markdown("""
    <style>
    /* Pointer cursor only for the selectbox */
    div[data-baseweb="select"] {
        cursor: pointer;
    }
    /* Keep text input normal */
    .stTextInput > div > div > input {
        cursor: text;
    }
    /* Button styling */
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        font-size: 16px;
        border: none;
        margin-top: 10px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "history" not in st.session_state:
    st.session_state.history = []

# Title and subheader
st.title("🤖 AI-Powered Customer Support Dashboard")
st.subheader("Enter your query below:")

# Predefined queries
queries = [
    "What is the status of my order?",
    "How can I track my shipment?",
    "How do I return a product?",
    "What are your shipping policies?",
    "Can I cancel my order?",
    "Where is my refund?"
]

# Intent mapping
intent_labels = {
    0: "Order Status Inquiry",
    1: "Refund Inquiry",
    2: "Product Return Inquiry",
    3: "Shipping Policy Inquiry",
    4: "Order Cancellation Request",
    5: "Shipment Tracking Inquiry"
}

# Selectbox to pick a query
query_selection = st.selectbox("Select a query from the list:", queries)

# Manual query typing
manual_query = st.text_input("Or type your query:")

# Use manual input if available
query = manual_query if manual_query else query_selection

# Submit button
submit = st.button("Submit")

# Clear history button
clear = st.button("Clear History")

# On submit
if submit:
    if query:
        try:
            with st.spinner('Analyzing your query...'):
                response = requests.post('http://127.0.0.1:5000/predict', json={'text': query})

                if response.status_code == 200:
                    result = response.json()

                    predicted_intent = intent_labels.get(result['intent'], f"Unknown Intent ({result['intent']})")
                    confidence = result['confidence']

                    # Display prediction
                    st.success(f"Predicted Intent: {predicted_intent}")
                    st.info(f"Confidence Score: {confidence:.2f}")

                    # Save to history
                    st.session_state.history.append({
                        "query": query,
                        "intent": predicted_intent,
                        "confidence": confidence
                    })
                else:
                    st.error(f"Error: Unable to get prediction (Status Code: {response.status_code})")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please select or type a query before submitting.")

# On clear
if clear:
    st.session_state.history = []
    st.success("History Cleared!")

# Divider
st.markdown("---")

# Query history
if st.session_state.history:
    st.subheader("📜 Query History")
    for i, record in enumerate(reversed(st.session_state.history), start=1):
        st.markdown(f"**{i}. Query:** {record['query']}")
        st.markdown(f"&nbsp;&nbsp;&nbsp;**Predicted Intent:** {record['intent']}")
        st.markdown(f"&nbsp;&nbsp;&nbsp;**Confidence:** {record['confidence']:.2f}")
        st.markdown("---")
else:
    st.info("No history yet. Submit a query to see it here!")
