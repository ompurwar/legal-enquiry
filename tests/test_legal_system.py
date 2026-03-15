"""
Tests for the Legal Advisory System.
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from legal_engine.laws.bns import get_relevant_bns_sections
from legal_engine.laws.bnss import get_relevant_bnss_sections
from legal_engine.laws.evidence import get_relevant_bsa_sections
from legal_engine.laws.personal_laws import get_relevant_personal_law_sections
from legal_engine.laws.case_law import get_relevant_cases
from legal_engine.interpreter import build_legal_context, build_system_prompt


# ─── BNS tests ───────────────────────────────────────────────────────────────

class TestBNS:
    def test_murder_keyword(self):
        results = get_relevant_bns_sections("murder case")
        assert any(r["section"] == "103" for r in results)

    def test_rape_keyword(self):
        results = get_relevant_bns_sections("rape victim")
        assert any(r["section"] == "63" for r in results)

    def test_dowry_death_keyword(self):
        results = get_relevant_bns_sections("dowry death case")
        assert any(r["section"] == "84" for r in results)

    def test_domestic_violence_498a(self):
        results = get_relevant_bns_sections("husband cruelty 498a")
        assert any(r["section"] == "85" for r in results)

    def test_cheating_fraud(self):
        results = get_relevant_bns_sections("cheating and fraud")
        assert any(r["section"] == "318" for r in results)

    def test_no_match(self):
        results = get_relevant_bns_sections("how to bake a cake")
        assert results == []

    def test_defamation(self):
        results = get_relevant_bns_sections("defamation case slander")
        assert any(r["section"] == "356" for r in results)


# ─── BNSS tests ──────────────────────────────────────────────────────────────

class TestBNSS:
    def test_fir_keyword(self):
        results = get_relevant_bnss_sections("how to file an FIR")
        assert any(r["section"] == "173" for r in results)

    def test_maintenance_125(self):
        results = get_relevant_bnss_sections("wife maintenance alimony")
        assert any(r["section"] == "480" for r in results)

    def test_bail(self):
        results = get_relevant_bnss_sections("apply for bail bailable offence")
        assert any(r["section"] == "223" for r in results)

    def test_arrest_24_hours(self):
        results = get_relevant_bnss_sections("detained in custody 24 hours")
        assert any(r["section"] == "57" for r in results)

    def test_no_match(self):
        results = get_relevant_bnss_sections("photosynthesis in plants")
        assert results == []


# ─── BSA / Evidence tests ────────────────────────────────────────────────────

class TestBSA:
    def test_electronic_evidence(self):
        results = get_relevant_bsa_sections("WhatsApp messages as digital evidence")
        assert any(r["section"] == "68" for r in results)

    def test_confession_to_police(self):
        results = get_relevant_bsa_sections("confession to police")
        assert any(r["section"] == "25" for r in results)

    def test_burden_of_proof(self):
        results = get_relevant_bsa_sections("burden of proof in court")
        assert any(r["section"] == "57" for r in results)

    def test_rape_consent_presumption(self):
        results = get_relevant_bsa_sections("rape evidence consent")
        assert any(r["section"] == "113" for r in results)

    def test_no_match(self):
        results = get_relevant_bsa_sections("stock market investment tips")
        assert results == []


# ─── Personal Laws tests ─────────────────────────────────────────────────────

class TestPersonalLaws:
    def test_hindu_divorce(self):
        results = get_relevant_personal_law_sections("hindu divorce grounds")
        assert any(r["law"] == "Hindu Marriage Act" for r in results)

    def test_muslim_nikah(self):
        results = get_relevant_personal_law_sections("nikah muslim marriage")
        assert any(r["law"] == "Muslim Personal Law" for r in results)

    def test_muslim_talaq(self):
        results = get_relevant_personal_law_sections("triple talaq divorce")
        assert any(r["law"] == "Muslim Personal Law" for r in results)

    def test_shah_bano_context(self):
        results = get_relevant_personal_law_sections("muslim alimony section 125")
        assert any(r["law"] == "Muslim Personal Law" for r in results)

    def test_special_marriage(self):
        results = get_relevant_personal_law_sections("court marriage inter-religion")
        assert any(r["law"] == "Special Marriage Act" for r in results)

    def test_domestic_violence(self):
        results = get_relevant_personal_law_sections("domestic violence protection order")
        assert any(r["law"] == "Domestic Violence Act" for r in results)

    def test_dowry_demand(self):
        results = get_relevant_personal_law_sections("dowry demand in-laws")
        assert any(r["law"] == "Dowry Prohibition Act" for r in results)

    def test_mehr(self):
        results = get_relevant_personal_law_sections("mahr dower muslim bride")
        assert any(r["law"] == "Muslim Personal Law" for r in results)

    def test_no_match(self):
        results = get_relevant_personal_law_sections("climate change policy")
        assert results == []


# ─── Case Law tests ──────────────────────────────────────────────────────────

class TestCaseLaw:
    def test_shah_bano_case(self):
        results = get_relevant_cases("shah bano maintenance case")
        assert any(c["case_name"] == "Mohd. Ahmed Khan v. Shah Bano Begum" for c in results)

    def test_shayara_bano_triple_talaq(self):
        results = get_relevant_cases("triple talaq unconstitutional shayara bano")
        assert any(c["case_name"] == "Shayara Bano v. Union of India" for c in results)

    def test_vishaka_sexual_harassment(self):
        results = get_relevant_cases("vishaka sexual harassment workplace")
        assert any(c["case_name"] == "Vishaka v. State of Rajasthan" for c in results)

    def test_danial_latifi(self):
        results = get_relevant_cases("muslim maintenance beyond iddat danial latifi")
        assert any(c["case_name"] == "Danial Latifi v. Union of India" for c in results)

    def test_basic_structure(self):
        results = get_relevant_cases("basic structure constitutional amendment")
        assert any(c["case_name"] == "Kesavananda Bharati v. State of Kerala" for c in results)

    def test_nirbhaya(self):
        results = get_relevant_cases("nirbhaya gang rape death penalty")
        assert any("Mukesh" in c["case_name"] for c in results)

    def test_no_match(self):
        results = get_relevant_cases("how to cook biryani")
        assert results == []


# ─── Interpreter tests ───────────────────────────────────────────────────────

class TestInterpreter:
    def test_build_context_criminal(self):
        ctx = build_legal_context("I was arrested without a warrant, can they do that?")
        assert "criminal" in ctx["categories"]

    def test_build_context_family(self):
        ctx = build_legal_context("My husband wants a divorce after 10 years of marriage")
        assert "family" in ctx["categories"]

    def test_build_context_has_keys(self):
        ctx = build_legal_context("maintenance alimony for wife")
        assert all(k in ctx for k in ["categories", "bns", "bnss", "bsa", "personal", "cases", "reference_summary"])

    def test_build_context_shah_bano(self):
        ctx = build_legal_context("Muslim divorced woman seeking maintenance – shah bano case")
        assert any(c["case_name"] == "Mohd. Ahmed Khan v. Shah Bano Begum" for c in ctx["cases"])
        assert "family" in ctx["categories"]

    def test_build_system_prompt_contains_refs(self):
        ctx = build_legal_context("FIR for theft")
        prompt = build_system_prompt(ctx)
        assert "BNS" in prompt or "BNSS" in prompt
        assert "Indian legal advisor" in prompt

    def test_build_system_prompt_non_empty(self):
        ctx = build_legal_context("general legal advice")
        prompt = build_system_prompt(ctx)
        assert len(prompt) > 100

    def test_reference_summary_present(self):
        ctx = build_legal_context("dowry harassment cruelty wife")
        assert ctx["reference_summary"] != ""

    def test_multiple_domains(self):
        ctx = build_legal_context("WhatsApp evidence in theft case burden of proof")
        assert "criminal" in ctx["categories"]
        assert "evidence" in ctx["categories"]


# ─── Flask app tests ─────────────────────────────────────────────────────────

class TestFlaskApp:
    @pytest.fixture(autouse=True)
    def setup(self):
        os.environ.setdefault("FLASK_SECRET_KEY", "test-secret")
        import app as flask_app
        flask_app.app.config["TESTING"] = True
        self.client = flask_app.app.test_client()

    def test_index_returns_200(self):
        response = self.client.get("/")
        assert response.status_code == 200
        assert b"Kanoon Mitra" in response.data

    def test_health_endpoint(self):
        response = self.client.get("/api/health")
        assert response.status_code == 200
        data = response.get_json()
        assert data["status"] == "ok"

    def test_search_laws_no_query(self):
        response = self.client.get("/api/laws/search")
        assert response.status_code == 400

    def test_search_laws_with_query(self):
        response = self.client.get("/api/laws/search?q=murder+case")
        assert response.status_code == 200
        data = response.get_json()
        assert "bns" in data
        assert any(s["section"] == "103" for s in data["bns"])

    def test_chat_empty_message(self):
        response = self.client.post(
            "/api/chat",
            json={"message": "", "history": []},
        )
        assert response.status_code == 400

    def test_chat_demo_mode(self):
        """Without a real API key the app returns a demo response."""
        from unittest.mock import patch
        import app as flask_app

        with patch.object(flask_app, "_ANTHROPIC_KEY", ""), \
             patch.object(flask_app, "_claude_client", None):
            response = self.client.post(
                "/api/chat",
                json={"message": "What is the punishment for theft in India?", "history": []},
            )
        assert response.status_code == 200
        data = response.get_json()
        assert "reply" in data
        assert "legal_refs" in data
        assert len(data["reply"]) > 0
