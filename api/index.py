from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# ❌ code me hardcode mat rakho
# ✅ Vercel Environment Variable use karo
JWT = os.getenv("JWT_TOKEN")

@app.route("/")
def home():
    return "API running on Vercel 🚀"

@app.route("/user-details", methods=["GET"])
def user_details():
    user_id = request.args.get("user")

    if not user_id:
        return jsonify({
            "success": False,
            "error": "Missing user ID"
        }), 400

    url = f"https://funstat.info/api/v1/users/{user_id}/stats_min"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {JWT}"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code != 200:
            return jsonify({
                "success": False,
                "status": response.status_code,
                "message": "Failed to fetch user info"
            }), 500

        return jsonify({
            "success": True,
            "data": response.json()
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

# ⚠️ Vercel ke liye REQUIRED
app = app
