import streamlit as st
import requests
import datetime
import time

# Enhanced page configuration
st.set_page_config(
    page_title="✈️ AI Travel Planner | Your Personal Trip Assistant",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS for modern styling
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    .main {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom header styling */
    .hero-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        animation: fadeInUp 0.8s ease-out;
    }
    
    .hero-title {
        color: white;
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .hero-subtitle {
        color: rgba(255,255,255,0.9);
        font-size: 1.3rem;
        font-weight: 300;
        margin-bottom: 0;
    }
    
    /* Chat container styling */
    .chat-container {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
        border: 1px solid #e1e5e9;
    }
    
    .chat-header {
        color: #2c3e50;
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
        text-align: center;
        padding-bottom: 1rem;
        border-bottom: 2px solid #f8f9fa;
    }
    
    /* Enhanced form styling */
    .stTextInput > div > div > input {
        border-radius: 25px;
        border: 2px solid #e1e5e9;
        padding: 1rem 1.5rem;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        background: #f8f9fa;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        background: white;
    }
    
    .stFormSubmitButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.8rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .stFormSubmitButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }
    
    /* Response card styling */
    .response-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        color: white;
        animation: slideInUp 0.6s ease-out;
    }
    
    .response-header {
        display: flex;
        align-items: center;
        margin-bottom: 1.5rem;
        font-size: 1.8rem;
        font-weight: 700;
    }
    
    .response-content {
        background: rgba(255,255,255,0.1);
        border-radius: 15px;
        padding: 1.5rem;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    /* Loading animation */
    .loading-container {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 3rem;
    }
    
    .loading-spinner {
        width: 40px;
        height: 40px;
        border: 4px solid #f3f3f3;
        border-top: 4px solid #667eea;
        border-radius: 50%;
        animation: spin 1s linear infinite;
    }
    
    /* Animations */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes slideInUp {
        from {
            opacity: 0;
            transform: translateY(50px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* Feature cards */
    .feature-card {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        transition: transform 0.3s ease;
        border: 1px solid #e1e5e9;
        margin: 0.5rem;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }
    
    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    
    .feature-title {
        font-size: 1.2rem;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 0.5rem;
    }
    
    .feature-desc {
        color: #6c757d;
        font-size: 0.9rem;
        line-height: 1.5;
    }
    
    /* Error styling */
    .error-message {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a52 100%);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        border: none;
        animation: shake 0.5s ease-in-out;
    }
    
    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        25% { transform: translateX(-5px); }
        75% { transform: translateX(5px); }
    }
</style>
""", unsafe_allow_html=True)

# Hero Header
st.markdown("""
<div class="hero-header">
    <div class="hero-title">✈️ AI Travel Planner</div>
    <div class="hero-subtitle">Your Intelligent Trip Planning Assistant</div>
</div>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "loading" not in st.session_state:
    st.session_state.loading = False

# Features section
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🗺️</div>
        <div class="feature-title">Smart Itinerary</div>
        <div class="feature-desc">AI-powered trip planning with optimized routes</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">💰</div>
        <div class="feature-title">Budget Friendly</div>
        <div class="feature-desc">Find the best deals and budget options</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🏨</div>
        <div class="feature-title">Accommodation</div>
        <div class="feature-desc">Perfect stays for every budget and style</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🍽️</div>
        <div class="feature-title">Local Cuisine</div>
        <div class="feature-desc">Discover authentic local food experiences</div>
    </div>
    """, unsafe_allow_html=True)

# Chat Interface
st.markdown("""
<div class="chat-container">
    <div class="chat-header">
        💬 How can I help you plan your perfect trip?
    </div>
</div>
""", unsafe_allow_html=True)

# Enhanced form with better UX
with st.form(key="travel_query_form", clear_on_submit=True):
    col1, col2 = st.columns([4, 1])
    
    with col1:
        user_input = st.text_input(
            "", 
            placeholder="✨ e.g., Plan a romantic 7-day trip to Paris for two people with a $3000 budget",
            label_visibility="collapsed"
        )
    
    with col2:
        submit_button = st.form_submit_button("🚀 Plan Trip")

# Handle form submission
if submit_button and user_input.strip():
    try:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Show loading state
        with st.container():
            st.markdown("""
            <div class="loading-container">
                <div class="loading-spinner"></div>
                <span style="margin-left: 1rem; font-size: 1.1rem; color: #667eea;">
                    🤖 AI is crafting your perfect travel plan...
                </span>
            </div>
            """, unsafe_allow_html=True)
            
            # Simulate API call (replace with your actual API endpoint)
            BASE_URL = "http://localhost:8000" # Replace with your actual API URL
            payload = {"question": user_input}
            
            # Uncomment and modify this section for actual API call
            # response = requests.post(f"{BASE_URL}/query", json=payload)
            
            # For demo purposes, using a mock response
            time.sleep(2)  # Simulate processing time
            
            # Mock response - replace with actual API response
            mock_response = f"""
            ## 🌟 Your Personalized Travel Plan

            **Destination Analysis:** Based on your request "{user_input}", here's what I recommend:

            ### 📅 Itinerary Highlights
            - **Day 1-2:** Arrival and city exploration
            - **Day 3-4:** Main attractions and cultural sites  
            - **Day 5-6:** Adventure activities and local experiences
            - **Day 7:** Departure and last-minute shopping

            ### 🏨 Accommodation Suggestions
            - **Luxury Option:** Premium hotels with excellent amenities
            - **Mid-Range:** Comfortable hotels with good location
            - **Budget-Friendly:** Clean, safe hostels or guesthouses

            ### 🍽️ Culinary Experiences
            - Local street food tours
            - Fine dining restaurants
            - Cooking classes with locals

            ### 💡 Pro Tips
            - Book accommodations in advance
            - Try local transportation
            - Learn basic local phrases
            - Pack according to weather conditions

            *Happy travels! 🌍*
            """
            
        # Clear loading and show response
        st.markdown(f"""
        <div class="response-card">
            <div class="response-header">
                🎯 Your AI-Generated Travel Plan
            </div>
            <div class="response-content">
                {mock_response}
            </div>
            <div style="margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.2); font-size: 0.9rem; opacity: 0.8;">
                📅 Generated on {datetime.datetime.now().strftime('%B %d, %Y at %I:%M %p')} | 
                🤖 Powered by AI Travel Assistant
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": mock_response})
            
    except Exception as e:
        st.markdown(f"""
        <div class="error-message">
            ⚠️ Oops! Something went wrong: {str(e)}
            <br>Please try again or contact support if the issue persists.
        </div>
        """, unsafe_allow_html=True)

# Display chat history (if you want to show previous conversations)
if st.session_state.messages:
    with st.expander("📜 Chat History", expanded=False):
        for i, message in enumerate(st.session_state.messages):
            if message["role"] == "user":
                st.markdown(f"**🧑‍💻 You:** {message['content']}")
            else:
                st.markdown(f"**🤖 AI Assistant:** {message['content']}")
            if i < len(st.session_state.messages) - 1:
                st.markdown("---")

# Footer
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #6c757d; border-top: 1px solid #e1e5e9; margin-top: 3rem;">
    <p>✨ Made with ❤️ using Streamlit | © 2024 AI Travel Planner</p>
    <p style="font-size: 0.8rem;">Disclaimer: AI-generated travel plans should be verified for accuracy before booking.</p>
</div>
""", unsafe_allow_html=True)