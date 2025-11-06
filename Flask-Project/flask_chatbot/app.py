from flask import Flask, render_template, request, redirect, url_for, session
import random
from datetime import datetime
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # For session management

# Data Science focused responses
responses = {
    'greetings': [
        "Hello! How can I help you with data science today?",
        "Hi there! Ready to discuss some data science concepts?",
        "Hey! What would you like to know about ML or data science?"
    ],
    'ml_algorithms': [
        "Popular ML algorithms include Linear Regression, Logistic Regression, Decision Trees, Random Forest, SVM, K-Means, and Neural Networks. Which one interests you?",
        "There are supervised algorithms (regression, classification) and unsupervised algorithms (clustering, dimensionality reduction). What would you like to explore?",
    ],
    'python': [
        "Python is excellent for data science! Key libraries include NumPy, Pandas, Scikit-learn, TensorFlow, and Matplotlib.",
        "For data science in Python, I recommend mastering Pandas for data manipulation and Scikit-learn for ML models.",
    ],
    'statistics': [
        "Statistics fundamentals include mean, median, mode, variance, standard deviation, probability distributions, hypothesis testing, and correlation.",
        "Understanding statistics is crucial for data science. Key concepts: descriptive stats, inferential stats, and probability theory.",
    ],
    'default': [
        "That's an interesting question! Could you provide more details?",
        "I'm here to help! Can you elaborate on that?",
        "Tell me more about what you'd like to know.",
    ]
}

def get_bot_response(user_message):
    """Generate bot response based on user message"""
    message_lower = user_message.lower()
    
    if any(word in message_lower for word in ['hi', 'hello', 'hey', 'namaste']):
        return random.choice(responses['greetings'])
    elif any(word in message_lower for word in ['algorithm', 'machine learning', 'ml', 'model', 'classification', 'regression']):
        return random.choice(responses['ml_algorithms'])
    elif any(word in message_lower for word in ['python', 'pandas', 'numpy', 'sklearn', 'library']):
        return random.choice(responses['python'])
    elif any(word in message_lower for word in ['statistics', 'stats', 'probability', 'distribution', 'hypothesis']):
        return random.choice(responses['statistics'])
    elif any(word in message_lower for word in ['feature', 'scaling', 'normalization', 'encoding']):
        return "Feature engineering includes scaling (StandardScaler, MinMaxScaler), encoding (One-Hot, Label), and feature selection (PCA, SelectKBest)."
    elif any(word in message_lower for word in ['preprocessing', 'cleaning', 'missing', 'null']):
        return "Data preprocessing involves handling missing values (imputation, deletion), removing duplicates, outlier detection, and data transformation."
    elif any(word in message_lower for word in ['evaluation', 'metric', 'accuracy', 'precision', 'recall']):
        return "Key metrics: Accuracy, Precision, Recall, F1-Score for classification. MSE, RMSE, R² for regression. Also consider confusion matrix and ROC-AUC."
    elif 'flask' in message_lower:
        return "Flask is a lightweight Python web framework. Perfect for building APIs and web applications. Key concepts: routes, templates, request/response handling."
    else:
        return random.choice(responses['default'])

@app.route('/')
def index():
    """Home page - initialize chat"""
    if 'chat_history' not in session:
        session['chat_history'] = []
    return render_template('index.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    """Handle chat page and messages"""
    if 'chat_history' not in session:
        session['chat_history'] = []
    
    if request.method == 'POST':
        user_message = request.form.get('message', '').strip()
        
        if user_message:
            # Get bot response
            bot_response = get_bot_response(user_message)
            
            # Add to chat history
            session['chat_history'].append({
                'user': user_message,
                'bot': bot_response,
                'timestamp': datetime.now().strftime('%I:%M %p')
            })
            session.modified = True
        
        return redirect(url_for('chat'))
    
    return render_template('chat.html', chat_history=session.get('chat_history', []))

@app.route('/clear')
def clear():
    """Clear chat history"""
    session['chat_history'] = []
    return redirect(url_for('chat'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
