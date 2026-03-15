"""
Legal Advisory System – Main Flask Application
===============================================
An AI-powered Indian legal advisor bot backed by Anthropic Claude.

Run:
    pip install -r requirements.txt
    cp .env.example .env         # fill in ANTHROPIC_API_KEY
    python app.py
"""

from __future__ import annotations

import os
import json
from flask import Flask, render_template, request, jsonify, session
from flask_cors import CORS
from dotenv import load_dotenv
import anthropic

from legal_engine import build_legal_context, build_system_prompt

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev-secret-change-in-production")
CORS(app)

# ---------------------------------------------------------------------------
# Anthropic client
# ---------------------------------------------------------------------------

_ANTHROPIC_KEY = os.getenv("ANTHROPIC_API_KEY", "")
_claude_client: anthropic.Anthropic | None = None


def get_claude_client() -> anthropic.Anthropic:
    """Lazily initialise and return the Anthropic client."""
    global _claude_client
    if _claude_client is None:
        if not _ANTHROPIC_KEY:
            raise RuntimeError(
                "ANTHROPIC_API_KEY is not set. "
                "Copy .env.example to .env and fill in your API key."
            )
        _claude_client = anthropic.Anthropic(api_key=_ANTHROPIC_KEY)
    return _claude_client


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    """Serve the chat UI."""
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    """
    POST /api/chat
    Body: { "message": "<user query>", "history": [ {"role": "user"|"assistant", "content": "..."}, ... ] }
    Returns: { "reply": "<advisor response>", "legal_refs": { ... } }
    """
    data = request.get_json(force=True) or {}
    user_message: str = (data.get("message") or "").strip()
    history: list[dict] = data.get("history") or []

    if not user_message:
        return jsonify({"error": "Message cannot be empty"}), 400

    # Build legal context from the interpretation engine
    legal_context = build_legal_context(user_message)
    system_prompt = build_system_prompt(legal_context)

    # Build messages list for Claude (keep last 10 turns for context)
    messages = [
        {"role": m["role"], "content": m["content"]}
        for m in history[-10:]
        if m.get("role") in ("user", "assistant") and m.get("content")
    ]
    messages.append({"role": "user", "content": user_message})

    try:
        client = get_claude_client()
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=2048,
            system=system_prompt,
            messages=messages,
        )
        reply_text = response.content[0].text
    except RuntimeError as exc:
        # API key not configured – return a demo response
        reply_text = _demo_response(user_message, legal_context)
    except anthropic.APIError as exc:
        app.logger.error("Anthropic API error: %s", exc)
        return jsonify({"error": f"AI service error: {exc}"}), 502

    # Prepare a lightweight legal refs summary for the front-end
    legal_refs = {
        "domains": legal_context["categories"],
        "bns_sections": [
            {"section": m["section"], "title": m["title"]}
            for m in legal_context["bns"]
        ],
        "bnss_sections": [
            {"section": m["section"], "title": m["title"]}
            for m in legal_context["bnss"]
        ],
        "bsa_sections": [
            {"section": m["section"], "title": m["title"]}
            for m in legal_context["bsa"]
        ],
        "personal_law": [
            {"law": m["law"], "section": m["section"], "title": m["title"]}
            for m in legal_context["personal"]
        ],
        "cases": [
            {"name": c["case_name"], "citation": c["citation"], "year": c["year"]}
            for c in legal_context["cases"]
        ],
    }

    return jsonify({"reply": reply_text, "legal_refs": legal_refs})


@app.route("/api/laws/search", methods=["GET"])
def search_laws():
    """
    GET /api/laws/search?q=<query>
    Returns structured legal references for the query without calling Claude.
    """
    query = (request.args.get("q") or "").strip()
    if not query:
        return jsonify({"error": "Query parameter 'q' is required"}), 400

    legal_context = build_legal_context(query)
    return jsonify({
        "query": query,
        "domains": legal_context["categories"],
        "bns": legal_context["bns"],
        "bnss": legal_context["bnss"],
        "bsa": legal_context["bsa"],
        "personal_laws": legal_context["personal"],
        "cases": legal_context["cases"],
        "reference_summary": legal_context["reference_summary"],
    })


@app.route("/api/health")
def health():
    """Health-check endpoint."""
    return jsonify({
        "status": "ok",
        "api_key_configured": bool(_ANTHROPIC_KEY),
    })


# ---------------------------------------------------------------------------
# Demo response (used when API key is absent, e.g., in CI)
# ---------------------------------------------------------------------------

def _demo_response(query: str, legal_context: dict) -> str:
    """Return a canned demo response using only the interpretation engine data."""
    ref = legal_context["reference_summary"]
    domains = ", ".join(legal_context["categories"])
    return (
        f"**[DEMO MODE – Configure ANTHROPIC_API_KEY for AI responses]**\n\n"
        f"Your query covers the following legal domain(s): **{domains}**.\n\n"
        f"Based on the interpretation engine, here are the applicable Indian laws:\n\n"
        f"{ref}\n\n"
        f"Please consult a qualified advocate for advice specific to your situation."
    )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    debug = os.getenv("FLASK_ENV", "development") == "development"
    app.run(host="0.0.0.0", port=port, debug=debug)
