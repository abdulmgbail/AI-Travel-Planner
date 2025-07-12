# 🌍 AI Travel Planner

An intelligent travel planning application built with Streamlit that uses AI to create personalized itineraries based on user preferences, travel dates, budget, and travel style. The app provides a beautiful, user-friendly interface for planning your perfect trip.

## ✨ Features

### Core Features

- **🤖 AI-Powered Itinerary Generation**: Create detailed travel plans using advanced AI
- **📅 Smart Date Selection**: Interactive date picker with trip duration calculation
- **💰 Budget Planning**: Multiple budget range options from budget to ultra-luxury
- **🎭 Travel Style Matching**: Customize plans based on adventure, relaxation, cultural, romantic, family-friendly, or business travel
- **📱 Responsive Design**: Beautiful, modern UI with gradient styling and interactive elements
- **📥 Multiple Export Options**: Download plans as text or JSON files

### Advanced Features

- **⚡ Real-time Validation**: Instant feedback on date selections and form inputs
- **🔍 Debug Mode**: Expandable request details for troubleshooting
- **💾 Session Management**: Remembers your last travel details
- **🎯 Smart Tips**: Helpful suggestions for better travel planning results
- **⏰ Timeout Handling**: Robust error handling for API requests

## 🏗️ Technology Stack

### Frontend

- **Framework**: Streamlit
- **Language**: Python
- **Styling**: Custom CSS with gradient designs
- **Components**: Streamlit native components with custom styling

### Backend

- **API**: FastAPI (running on localhost:8000)
- **Communication**: HTTP requests via Python requests library
- **Data Format**: JSON for API communication

### Key Libraries

- **streamlit**: Web app framework
- **requests**: HTTP library for API calls
- **datetime**: Date and time handling
- **json**: JSON data processing

## 📦 Installation

### Prerequisites

- Python 3.8+
- pip or conda
- FastAPI backend server (running on port 8000)

### Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/your-username/ai-travel-planner.git
cd ai-travel-planner
```

2. **Install dependencies**

```bash
pip install streamlit requests
```

3. **Start the backend server**

```bash
# Make sure your FastAPI server is running on localhost:8000
# The app expects a /query endpoint that accepts POST requests
```

4. **Run the Streamlit app**

```bash
streamlit run app.py
```

5. **Open in browser**

- The app will automatically open in your default browser
- Default URL: `http://localhost:8501`

## 🎯 Usage

### Planning a Trip

1. **Set Travel Dates**

   - Select departure date (today or future)
   - Choose return date (must be after departure)
   - View automatic trip duration calculation

2. **Configure Preferences**

   - Choose budget range: Budget ($) to Ultra-luxury ($$$$)
   - Select travel style: Adventure, Relaxation, Cultural, Romantic, Family-friendly, or Business

3. **Describe Your Trip**

   - Enter detailed description of your travel plans
   - Include destinations, interests, group size, special requirements
   - Follow the quick tips for better results

4. **Generate Plan**

   - Click "✨ Generate My Travel Plan"
   - Wait for AI processing (includes timeout handling)
   - Review your personalized itinerary

5. **Download & Save**
   - Download as text file for offline reading
   - Download as JSON for data processing
   - Plans are automatically timestamped

### Example Input

```
Plan a romantic trip to Paris for 2 people. We love art, fine dining, and historic sites.
We're interested in museums, local markets, and cozy cafes. Budget is mid-range.
```

## 🔧 API Integration

The app communicates with a FastAPI backend via the `/query` endpoint:

### Request Format

```json
{
  "question": "User's travel description",
  "start_date": "2024-07-15",
  "end_date": "2024-07-22",
  "budget_range": "Mid-range ($$)",
  "travel_style": "Romantic",
  "trip_duration": 7
}
```

### Response Format

```json
{
  "answer": "Generated travel plan text",
  "saved_file": "Optional file path",
  "travel_details": {
    "destination": "Paris",
    "duration": 7,
    "budget": "Mid-range"
  }
}
```

## 🎨 Design Features

### Visual Elements

- **Gradient Headers**: Modern purple-blue gradient design
- **Interactive Cards**: Elevated cards with hover effects
- **Color-coded Status**: Success (green), info (blue), error (red) messages
- **Responsive Layout**: Two-column layout with sidebar navigation

### User Experience

- **Form Validation**: Real-time date validation and error messages
- **Loading States**: Spinner animation during AI processing
- **Progress Feedback**: Clear status messages and error handling
- **Accessibility**: Proper contrast and semantic HTML structure

## 🚀 Deployment

### Local Development

```bash
# Run with auto-reload
streamlit run app.py --server.runOnSave true
```

### Production Deployment

```bash
# Using Streamlit Cloud, Heroku, or similar platforms
# Ensure environment variables are set for API endpoints
```

## 📁 File Structure

```
ai-travel-planner/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── backend/           # FastAPI backend (separate)
    ├── main.py        # FastAPI server
    └── requirements.txt
```

## 🔒 Environment Variables

```bash
# Create a .env file (if needed)
BASE_URL=http://localhost:8000
API_TIMEOUT=120
```

## 🛠️ Configuration

### Customizing the App

- **Colors**: Modify CSS gradients in the `st.markdown()` style section
- **API Endpoint**: Change `BASE_URL` variable
- **Timeout**: Adjust request timeout (default: 120 seconds)
- **Date Limits**: Modify max date range (default: 365 days)

### Adding Features

- **New Travel Styles**: Add options to the travel_style selectbox
- **Budget Ranges**: Extend budget_range options
- **Export Formats**: Add PDF or CSV export options

## 🐛 Troubleshooting

### Common Issues

1. **Backend Connection Error**: Ensure FastAPI server is running on port 8000
2. **Timeout Issues**: Increase timeout value for complex requests
3. **Date Validation**: Check that return date is after departure date
4. **Empty Response**: Verify API endpoint is correctly configured

### Debug Mode

- Use the "🔍 Debug: Request Details" expander to view API payloads
- Check browser console for JavaScript errors
- Monitor FastAPI logs for backend issues

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/) for the beautiful web interface
- AI integration via FastAPI backend
- Modern CSS design with gradient styling
- Responsive design principles

## 📞 Support

For issues and questions:

- Open an issue on GitHub
- Check the troubleshooting section
- Review the debug mode output

---

<div align="center">
  <p>🌍 <strong>AI Travel Planner</strong> | Making your travel dreams come true</p>
  <p>✈️ Safe travels and happy planning! ✈️</p>
</div>
