"""
Bharatiya Sakshya Adhiniyam (BSA), 2023
Replaced the Indian Evidence Act, 1872.
Effective from 1 July 2024.
"""

BSA_SECTIONS = {
    "2": {
        "title": "Definitions – Facts, Evidence, Proved, Disproved",
        "description": (
            "Evidence means and includes: (1) all statements which the Court permits or requires to be made before it by witnesses, in relation to matters of fact under inquiry—such statements are called oral evidence; (2) all documents including electronic records produced for the inspection of the Court—such documents are called documentary evidence."
        ),
        "old_ref": "Evidence Act Section 3",
        "keywords": ["evidence", "proof", "facts", "witness statement", "documentary evidence"],
    },
    "8": {
        "title": "Admissions",
        "description": "An admission is a statement, oral or documentary or contained in electronic form, which suggests any inference as to any fact in issue or relevant fact, and which is made by any of the persons, and under the circumstances, hereinafter mentioned.",
        "old_ref": "Evidence Act Section 17",
        "keywords": ["admission", "confession", "statement", "acknowledgement"],
    },
    "22": {
        "title": "Confessions caused by inducement, threat or promise",
        "description": "A confession made by an accused person is irrelevant in a criminal proceeding if the making of the confession appears to the Court to have been caused by any inducement, threat or promise having reference to the charge against the accused person.",
        "old_ref": "Evidence Act Section 24",
        "keywords": ["confession under duress", "forced confession", "threat confession", "coerced confession"],
    },
    "25": {
        "title": "Confession to police officer",
        "description": "No confession made to a police officer shall be proved as against a person accused of any offence.",
        "old_ref": "Evidence Act Section 25",
        "keywords": ["police confession", "confession to police", "police statement"],
    },
    "57": {
        "title": "Burden of proof",
        "description": "Whoever desires any Court to give judgment as to any legal right or liability dependent on the existence of facts which he asserts, must prove that those facts exist. When a person is bound to prove the existence of any fact, it is said that the burden of proof lies on that person.",
        "old_ref": "Evidence Act Section 101",
        "keywords": ["burden of proof", "onus probandi", "prove facts", "evidence burden"],
    },
    "63": {
        "title": "Presumption of innocence",
        "description": "The burden of proof in a criminal case lies on the prosecution. The accused is presumed innocent until proved guilty beyond reasonable doubt.",
        "old_ref": "Evidence Act Section 101 read with CrPC",
        "keywords": ["presumption of innocence", "innocent until proven guilty", "beyond reasonable doubt"],
    },
    "68": {
        "title": "Electronic records and digital evidence",
        "description": "All statements made by a person before a Magistrate or by way of a statement recorded by a police officer shall be admissible in evidence. Electronic records produced for the inspection of the Court shall be treated as documentary evidence and are admissible subject to conditions of authenticity.",
        "old_ref": "Evidence Act Section 65B",
        "keywords": ["electronic evidence", "digital evidence", "WhatsApp messages", "email evidence", "CCTV footage", "phone records"],
    },
    "111": {
        "title": "Evidence of character in civil cases",
        "description": "In civil cases the fact that the character of any person concerned is such as to render probable or improbable any conduct imputed to him is irrelevant, except in so far as such character appears from facts otherwise relevant.",
        "old_ref": "Evidence Act Section 52",
        "keywords": ["character evidence", "civil case character", "reputation evidence"],
    },
    "113": {
        "title": "Rape cases – presumption as to absence of consent",
        "description": "In a prosecution for rape, where sexual intercourse by the accused is proved and the question is whether it was without the consent of the woman alleged to have been raped, and she states in her evidence that she did not consent, the Court shall presume that she did not consent.",
        "old_ref": "Evidence Act Section 114A",
        "keywords": ["rape evidence", "consent in rape", "rape presumption", "sexual assault evidence"],
    },
}

EVIDENCE_ACT_TO_BSA_MAP = {
    "3": "2",
    "17": "8",
    "24": "22",
    "25": "25",
    "52": "111",
    "65B": "68",
    "101": "57",
    "114A": "113",
}


def get_relevant_bsa_sections(query: str) -> list[dict]:
    """Return BSA sections relevant to a user's query."""
    query_lower = query.lower()
    matches = []
    for section_num, section_data in BSA_SECTIONS.items():
        for keyword in section_data["keywords"]:
            if keyword in query_lower:
                matches.append({"section": section_num, **section_data})
                break
    return matches
