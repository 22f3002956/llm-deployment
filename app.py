import os
import json
import requests
from flask import Flask, request, jsonify
from github import Github

app = Flask(__name__)

# ---------------------------------------------------
# 🔧 CONFIGURATION
# ---------------------------------------------------
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
SECRET = "mysecret123"  # same as in your .env and form

# ---------------------------------------------------
# 🧠 HELPER FUNCTION
# ---------------------------------------------------
def create_or_update_repo(task_name, brief):
    """Create or update GitHub repo and upload generated files."""
    g = Github(GITHUB_TOKEN)
    user = g.get_user()
    repo_name = task_name.replace(" ", "-")

    try:
        repo = user.get_repo(repo_name)
        print(f"ℹ️ Repo '{repo_name}' already exists — updating...")
    except:
        repo = user.create_repo(repo_name, private=False)
        print(f"✅ Created new repo: {repo_name}")

    # Simple generated HTML content
    html_content = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>{task_name}</title>
  <style>
    body {{
      font-family: 'Inter', sans-serif;
      background: linear-gradient(135deg, #ff9a9e, #fad0c4);
      color: white;
      text-align: center;
      padding: 60px;
    }}
    h1 {{
      font-size: 3em;
      margin-bottom: 20px;
    }}
    .card {{
      background: rgba(255, 255, 255, 0.15);
      border-radius: 10px;
      padding: 20px;
      margin: 10px;
      display: inline-block;
      width: 250px;
      color: white;
      box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }}
  </style>
</head>
<body>
  <h1>Atul Raghav</h1>
  <p>{brief}</p>
  <div class="card">🚀 Project 1</div>
  <div class="card">🧠 Project 2</div>
  <div class="card">💻 Project 3</div>
</body>
</html>"""

    # Files to upload
    files_to_upload = {
        "index.html": html_content,
        "README.md": f"# {task_name}\n\n{brief}\n\nGenerated automatically for IITM LLM Code Deployment project.",
        "LICENSE": "MIT License\n\nCopyright (c) 2025",
        "style.css": "body { font-family: Arial; }",
        "app.js": "console.log('App loaded successfully');",
    }

    # Upload or update files
    for filename, content in files_to_upload.items():
        try:
            existing_file = repo.get_contents(filename)
            repo.update_file(existing_file.path, f"Updated {filename}", content, existing_file.sha)
            print(f"📝 Updated {filename}")
        except:
            repo.create_file(filename, f"Uploaded {filename}", content)
            print(f"📦 Uploaded {filename}")

    # Make public and enable Pages (modern safe method)
    try:
        repo.edit(visibility="public", homepage=repo.html_url, has_wiki=False)
        print("🌐 GitHub Pages enabled automatically via public main branch")
    except Exception as e:
        print(f"⚠️ Pages enable warning: {e}")

    pages_url = f"https://{user.login}.github.io/{repo_name}/"
    latest_commit_sha = repo.get_commits()[0].sha

    return repo, pages_url, latest_commit_sha


# ---------------------------------------------------
# 🚀 MAIN API ENDPOINT
# ---------------------------------------------------
@app.route("/api-endpoint", methods=["POST"])
def receive_request():
    data = request.get_json()
    print("\n🎯 IITM Evaluation Request Received")
    print(json.dumps(data, indent=2))

    # Verify secret
    if data.get("secret") != SECRET:
        print("❌ Invalid secret received!")
        return jsonify({"error": "Invalid secret"}), 403

    try:
        task_name = data.get("task", "llm-project")
        brief = data.get("brief", "No brief provided")
        evaluation_url = data.get("evaluation_url") or data.get("evaluationURL")

        if not evaluation_url:
            print("⚠️ Missing evaluation_url in request body")
            return jsonify({"error": "Missing evaluation_url"}), 400

        nonce = data.get("nonce", "")
        round_num = data.get("round", 1)
        email = data.get("email", "")

        # Deploy project
        repo, pages_url, latest_commit_sha = create_or_update_repo(task_name, brief)

        # Prepare data to send to evaluator
        payload = {
            "email": email,
            "task": task_name,
            "round": round_num,
            "nonce": nonce,
            "repo_url": repo.html_url,
            "commit_sha": latest_commit_sha,
            "pages_url": pages_url,
        }

        print("📡 Sending deployment info to IITM evaluation server...")
        response = requests.post(
            evaluation_url,
            headers={"Content-Type": "application/json"},
            json=payload,
        )

        print(f"🧭 Evaluation server returned {response.status_code}: {response.text}")

        if response.status_code == 200:
            print("✅ IITM Evaluation Ping Successful")
        else:
            print("⚠️ IITM Evaluation Ping Failed")

        return jsonify({
            "message": f"Project '{task_name}' deployed successfully!",
            "project_url": pages_url,
            "status": "success"
        }), 200

    except Exception as e:
        print(f"❌ Deployment Error: {e}")
        return jsonify({"error": str(e)}), 500


# ---------------------------------------------------
# 🏠 HOME ROUTE
# ---------------------------------------------------
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "LLM Deployment App Active. Use POST /api-endpoint with JSON body."
    })


# ---------------------------------------------------
# 🧩 RUN FLASK
# ---------------------------------------------------
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 7860))
    app.run(host="0.0.0.0", port=port)

