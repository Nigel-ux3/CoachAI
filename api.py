
# File: api.py
from flask import Flask, request, jsonify
from agents.ceo_agent import CEOAgent

app = Flask(__name__)

# Create a dummy team (replace with your actual team)
team = {
    "Head Developer": "head_developer",
    "Financial Reporter": "financial_reporter",
    "Expense Manager": "expense_manager",
    # Add all other agents here...
}

# Create an instance of the AI CEO Agent
ceo_agent = CEOAgent(team)  # Pass the team argument

@app.route("/ceo", methods=["POST"])
def ceo_agent_api():
    # Get user input from the request
    data = request.json
    user_input = data.get("input")
    
    # Process the input using the AI CEO Agent
    response = ceo_agent.handle_task(user_input)
    
    # Return the response as JSON
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)