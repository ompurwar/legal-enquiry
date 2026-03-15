"""
Bharatiya Nagarik Suraksha Sanhita (BNSS), 2023
Replaced the Code of Criminal Procedure (CrPC), 1973.
Effective from 1 July 2024.
"""

BNSS_SECTIONS = {
    "35": {
        "title": "Arrest without warrant",
        "description": "Any police officer may, without an order from a Magistrate and without a warrant, arrest any person who has been concerned in any cognisable offence, or against whom a reasonable complaint has been made, or credible information has been received, or a reasonable suspicion exists, of his having been so concerned.",
        "old_ref": "CrPC Section 41",
        "keywords": ["arrest", "detention", "police arrest", "arrested without warrant"],
    },
    "36": {
        "title": "Arrest on refusal to give name and residence",
        "description": "When any person who, in the presence of a police officer, has committed or has been accused of committing a non-cognisable offence refuses, on demand of such officer, to give his name and residence, or gives a name or residence which such officer has reason to believe to be false, he may be arrested by such officer.",
        "old_ref": "CrPC Section 42",
        "keywords": ["name refusal", "identity refusal", "non-cognisable arrest"],
    },
    "47": {
        "title": "No unnecessary restraint",
        "description": "The person arrested shall not be subjected to more restraint than is necessary to prevent his escape.",
        "old_ref": "CrPC Section 49",
        "keywords": ["unnecessary restraint", "police brutality", "excessive force during arrest"],
    },
    "52": {
        "title": "Rights of arrested person",
        "description": "Every person arrested shall have the right to meet an advocate of his choice during interrogation, though not throughout interrogation.",
        "old_ref": "CrPC Section 41D",
        "keywords": ["rights arrested person", "lawyer during interrogation", "advocate rights"],
    },
    "57": {
        "title": "Person arrested not to be detained more than twenty-four hours",
        "description": "No police officer shall detain in custody a person arrested without warrant for a longer period than under all the circumstances of the case is reasonable, and such period shall not, in the absence of a special order of a Magistrate under section 187, exceed twenty-four hours exclusive of the time necessary for the journey from the place of arrest to the Magistrate's Court.",
        "old_ref": "CrPC Section 57",
        "keywords": ["24 hours detention", "bail", "custody limit", "detain"],
    },
    "173": {
        "title": "Information in cognisable cases (FIR)",
        "description": "Every information relating to the commission of a cognisable offence shall be reduced to writing by the officer in charge of a police station if given orally, read over to the informant; and every such information shall be signed by the person giving it.",
        "old_ref": "CrPC Section 154",
        "keywords": ["fir", "first information report", "police complaint", "cognisable offence complaint"],
    },
    "223": {
        "title": "Bail in bailable offences",
        "description": "When any person other than a person accused of a non-bailable offence is arrested or detained without warrant by an officer in charge of a police station, or appears or is brought before a Court, and is prepared at any time while in the custody of such officer or at any stage of the proceedings before such Court to give bail, such person shall be released on bail.",
        "old_ref": "CrPC Section 436",
        "keywords": ["bail", "bailable offence", "release on bail"],
    },
    "480": {
        "title": "Order for maintenance of wives, children and parents",
        "description": "If any person having sufficient means neglects or refuses to maintain his wife, his legitimate or illegitimate minor children or his father or mother, unable to maintain themselves, a Magistrate of the first class may, upon proof of such neglect or refusal, order such person to make a monthly allowance for the maintenance of his wife or such child, father or mother.",
        "old_ref": "CrPC Section 125",
        "keywords": ["maintenance", "alimony", "wife maintenance", "child support", "parent maintenance", "section 125"],
    },
    "481": {
        "title": "Alteration in allowance",
        "description": "On proof of a change in the circumstances of any person, receiving, under section 480 a monthly allowance, or ordered under the same section to pay a monthly allowance to his wife, child, father or mother, the Magistrate may make such alteration in the allowance as he thinks fit.",
        "old_ref": "CrPC Section 127",
        "keywords": ["maintenance revision", "alimony revision", "change in maintenance"],
    },
}

CRPC_TO_BNSS_MAP = {
    "41": "35",
    "41D": "52",
    "42": "36",
    "49": "47",
    "57": "57",
    "125": "480",
    "127": "481",
    "154": "173",
    "436": "223",
}


def get_relevant_bnss_sections(query: str) -> list[dict]:
    """Return BNSS sections relevant to a user's query."""
    query_lower = query.lower()
    matches = []
    for section_num, section_data in BNSS_SECTIONS.items():
        for keyword in section_data["keywords"]:
            if keyword in query_lower:
                matches.append({"section": section_num, **section_data})
                break
    return matches
