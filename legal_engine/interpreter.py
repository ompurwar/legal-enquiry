"""
Legal Interpretation Engine.

This module maps a user's natural-language query to the relevant Indian laws,
sections, and landmark cases. It returns a structured context object that is
then fed to the Claude API to generate a precise legal answer.
"""

from __future__ import annotations

from .laws.bns import get_relevant_bns_sections
from .laws.bnss import get_relevant_bnss_sections
from .laws.evidence import get_relevant_bsa_sections
from .laws.personal_laws import get_relevant_personal_law_sections
from .laws.case_law import get_relevant_cases

# ---------------------------------------------------------------------------
# Category classifiers
# ---------------------------------------------------------------------------

CRIMINAL_KEYWORDS = {
    "murder", "rape", "theft", "robbery", "dacoity", "fraud", "cheating",
    "assault", "hurt", "kidnap", "abduct", "extortion", "arson", "bribery",
    "corruption", "forgery", "counterfeiting", "riot", "sedition", "terror",
    "drug", "narcotic", "bail", "fir", "arrest", "custody", "police",
    "criminal", "offence", "offense", "crime", "accused", "convicted",
    "sentence", "jail", "prison", "warrant",
}

FAMILY_KEYWORDS = {
    "marriage", "divorce", "talaq", "nikah", "alimony", "maintenance",
    "dowry", "domestic violence", "custody", "child support", "adoption",
    "guardianship", "inheritance", "succession", "will", "wife", "husband",
    "matrimonial", "conjugal", "separation", "shah bano", "mehr", "mahr",
    "wedding", "remarriage", "bigamy", "polygamy",
}

CONSTITUTIONAL_KEYWORDS = {
    "fundamental right", "article 21", "right to life", "article 14",
    "equality", "article 19", "freedom of speech", "basic structure",
    "constitutional", "writ", "habeas corpus", "mandamus", "certiorari",
    "supreme court", "high court", "judicial review",
}

EVIDENCE_KEYWORDS = {
    "evidence", "proof", "witness", "testimony", "confession", "admission",
    "burden of proof", "digital evidence", "electronic", "cctv", "whatsapp",
    "document", "exhibit", "hearsay",
}

PROPERTY_KEYWORDS = {
    "property", "land", "house", "rent", "lease", "tenancy", "eviction",
    "possession", "transfer", "registration", "mortgage", "sale deed",
    "title", "ownership",
}


def _classify_query(query: str) -> list[str]:
    """Return a list of legal domain categories for the given query."""
    query_lower = query.lower()
    categories = []
    if any(kw in query_lower for kw in CRIMINAL_KEYWORDS):
        categories.append("criminal")
    if any(kw in query_lower for kw in FAMILY_KEYWORDS):
        categories.append("family")
    if any(kw in query_lower for kw in CONSTITUTIONAL_KEYWORDS):
        categories.append("constitutional")
    if any(kw in query_lower for kw in EVIDENCE_KEYWORDS):
        categories.append("evidence")
    if any(kw in query_lower for kw in PROPERTY_KEYWORDS):
        categories.append("property")
    if not categories:
        categories.append("general")
    return categories


def build_legal_context(query: str) -> dict:
    """
    Analyse the query and return a structured legal context dict containing:
    - categories  : list of applicable legal domains
    - bns         : matching BNS sections
    - bnss        : matching BNSS sections
    - bsa         : matching BSA (Evidence) sections
    - personal    : matching Personal Law sections
    - cases       : matching landmark Supreme Court cases
    - summary     : a short human-readable text summarising found references
    """
    categories = _classify_query(query)

    bns_matches = get_relevant_bns_sections(query)
    bnss_matches = get_relevant_bnss_sections(query)
    bsa_matches = get_relevant_bsa_sections(query)
    personal_matches = get_relevant_personal_law_sections(query)
    case_matches = get_relevant_cases(query)

    # Build a concise reference summary for use in the prompt
    lines: list[str] = []

    if bns_matches:
        lines.append("**Bharatiya Nyaya Sanhita (BNS) / IPC references:**")
        for m in bns_matches:
            lines.append(
                f"  • BNS Section {m['section']} – {m['title']} (formerly {m.get('old_ref', '')})"
            )

    if bnss_matches:
        lines.append("**Bharatiya Nagarik Suraksha Sanhita (BNSS) / CrPC references:**")
        for m in bnss_matches:
            lines.append(
                f"  • BNSS Section {m['section']} – {m['title']} (formerly {m.get('old_ref', '')})"
            )

    if bsa_matches:
        lines.append("**Bharatiya Sakshya Adhiniyam (BSA) / Evidence Act references:**")
        for m in bsa_matches:
            lines.append(
                f"  • BSA Section {m['section']} – {m['title']} (formerly {m.get('old_ref', '')})"
            )

    if personal_matches:
        lines.append("**Personal Laws / Marriage Acts references:**")
        for m in personal_matches:
            lines.append(
                f"  • {m['law']} – {m['title']}"
            )

    if case_matches:
        lines.append("**Landmark Supreme Court Cases:**")
        for c in case_matches:
            lines.append(
                f"  • {c['case_name']} ({c['citation']}) – {c['topic']}"
            )

    reference_summary = "\n".join(lines) if lines else "No specific sections automatically identified; providing general legal guidance."

    return {
        "categories": categories,
        "bns": bns_matches,
        "bnss": bnss_matches,
        "bsa": bsa_matches,
        "personal": personal_matches,
        "cases": case_matches,
        "reference_summary": reference_summary,
    }


def build_system_prompt(legal_context: dict) -> str:
    """
    Build the Claude system prompt enriched with identified legal references.
    """
    ref_block = legal_context["reference_summary"]
    domains = ", ".join(legal_context["categories"])

    return f"""You are an expert Indian legal advisor specialising in Indian law. You provide accurate, 
clear, and helpful legal guidance based on current Indian legislation including:
- Bharatiya Nyaya Sanhita (BNS), 2023 – replaced IPC, effective 1 July 2024
- Bharatiya Nagarik Suraksha Sanhita (BNSS), 2023 – replaced CrPC, effective 1 July 2024  
- Bharatiya Sakshya Adhiniyam (BSA), 2023 – replaced Indian Evidence Act, effective 1 July 2024
- Hindu Marriage Act, 1955 and other Personal Laws
- Muslim Personal Law (Shariat) Application Act, 1937
- Special Marriage Act, 1954
- Protection of Women from Domestic Violence Act, 2005
- Dowry Prohibition Act, 1961
- Relevant Supreme Court landmark judgments

**AUTOMATICALLY IDENTIFIED LEGAL REFERENCES FOR THIS QUERY:**
{ref_block}

**DETECTED LEGAL DOMAIN(S):** {domains}

**YOUR RESPONSE GUIDELINES:**
1. Start with a clear, direct answer to the user's question.
2. Cite specific sections from BNS/BNSS/BSA (mentioning the old IPC/CrPC reference for context).
3. Mention relevant Supreme Court cases where applicable.
4. Explain WHEN each law applies to the user's specific situation.
5. Use simple language – avoid excessive legal jargon.
6. If the query is in Hindi or mixed Hindi-English (Hinglish), respond in the same language style.
7. Always advise the user to consult a qualified advocate for their specific case.
8. Do NOT give advice that could be harmful or encourage illegal activity.
9. Maintain the dignity and rights of all parties, especially women and vulnerable groups.
10. If unsure, say so clearly rather than guessing.

IMPORTANT: Always mention that laws changed from 1 July 2024 (IPC → BNS, CrPC → BNSS, Evidence Act → BSA) and use current section numbers while noting old ones for reference."""
