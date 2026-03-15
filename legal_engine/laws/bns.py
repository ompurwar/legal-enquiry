"""
Bharatiya Nyaya Sanhita (BNS), 2023
Replaced the Indian Penal Code (IPC), 1860.
Effective from 1 July 2024.
"""

BNS_SECTIONS = {
    "103": {
        "title": "Murder",
        "description": "Whoever commits murder shall be punished with death or imprisonment for life, and shall also be liable to fine.",
        "old_ref": "IPC Section 302",
        "keywords": ["murder", "killing", "homicide", "death", "killed"],
    },
    "104": {
        "title": "Culpable homicide not amounting to murder",
        "description": "Whoever commits culpable homicide not amounting to murder shall be punished with imprisonment for life, or imprisonment for a term which may extend to ten years, and shall also be liable to fine.",
        "old_ref": "IPC Section 304",
        "keywords": ["culpable homicide", "manslaughter", "accidental death"],
    },
    "109": {
        "title": "Abetment of suicide",
        "description": "If any person commits suicide, whoever abets the commission of such suicide, shall be punished with imprisonment of either description for a term which may extend to ten years, and shall also be liable to fine.",
        "old_ref": "IPC Section 306",
        "keywords": ["suicide", "abetment", "self harm", "suicidal"],
    },
    "115": {
        "title": "Voluntarily causing grievous hurt",
        "description": "Whoever voluntarily causes grievous hurt shall be punished with imprisonment of either description for a term which may extend to seven years, and shall also be liable to fine.",
        "old_ref": "IPC Section 325",
        "keywords": ["grievous hurt", "serious injury", "bodily harm"],
    },
    "191": {
        "title": "Dacoity",
        "description": "When five or more persons conjointly commit or attempt to commit a robbery, or where the whole number of persons conjointly committing or attempting to commit a robbery, and persons present and aiding such commission or attempt, amount to five or more, every person so committing, attempting or aiding, is said to commit dacoity.",
        "old_ref": "IPC Section 391",
        "keywords": ["dacoity", "robbery", "gang robbery", "looting"],
    },
    "316": {
        "title": "Causing miscarriage",
        "description": "Whoever voluntarily causes a woman with child to miscarry shall be punished.",
        "old_ref": "IPC Section 312",
        "keywords": ["miscarriage", "abortion", "foetus"],
    },
    "351": {
        "title": "Criminal intimidation",
        "description": "Whoever threatens another with any injury to his person, reputation or property, or to the person or reputation of any one in whom that person is interested, with intent to cause alarm to that person, or to cause that person to do any act which he is not legally bound to do, or to omit to do any act which that person is legally entitled to do, commits criminal intimidation.",
        "old_ref": "IPC Section 503",
        "keywords": ["threat", "intimidation", "threatening", "coercion", "blackmail"],
    },
    "356": {
        "title": "Defamation",
        "description": "Whoever, by words either spoken or intended to be read, or by signs or by visible representations, makes or publishes any imputation concerning any person intending to harm, or knowing or having reason to believe that such imputation will harm, the reputation of such person, is said, except in the cases hereinafter excepted, to defame that person.",
        "old_ref": "IPC Section 499",
        "keywords": ["defamation", "slander", "libel", "reputation", "false statement"],
    },
    "63": {
        "title": "Rape",
        "description": "A man is said to commit rape if he has sexual intercourse with a woman without her consent or against her will.",
        "old_ref": "IPC Section 375",
        "keywords": ["rape", "sexual assault", "sexual violence", "non consensual"],
    },
    "64": {
        "title": "Punishment for rape",
        "description": "Whoever, except in the cases provided for in sub-section (2), commits rape, shall be punished with rigorous imprisonment for a term which shall not be less than ten years, but which may extend to imprisonment for life.",
        "old_ref": "IPC Section 376",
        "keywords": ["rape punishment", "sexual assault punishment"],
    },
    "85": {
        "title": "Husband or relative of husband subjecting woman to cruelty",
        "description": "Whoever, being the husband or the relative of the husband of a woman, subjects such woman to cruelty shall be punished with imprisonment for a term which may extend to three years and shall also be liable to fine.",
        "old_ref": "IPC Section 498A",
        "keywords": ["domestic violence", "cruelty", "wife", "husband", "dowry harassment", "498a"],
    },
    "84": {
        "title": "Dowry death",
        "description": "Where the death of a woman is caused by any burns or bodily injury or occurs under abnormal circumstances within seven years of marriage, and it is shown that soon before her death she was subjected to cruelty or harassment by her husband or any relative of her husband for, or in connection with, any demand for dowry, such death shall be called dowry death.",
        "old_ref": "IPC Section 304B",
        "keywords": ["dowry death", "dowry", "bride burning", "dowry harassment death"],
    },
    "303": {
        "title": "Theft",
        "description": "Whoever, intending to take dishonestly any moveable property out of the possession of any person without that person's consent, moves that property in order to such taking, is said to commit theft.",
        "old_ref": "IPC Section 378",
        "keywords": ["theft", "stealing", "pickpocket", "stolen"],
    },
    "318": {
        "title": "Cheating",
        "description": "Whoever, by deceiving any person, fraudulently or dishonestly induces the person so deceived to deliver any property to any person, or to consent that any person shall retain any property, or intentionally induces the person so deceived to do or omit to do anything which he would not do or omit if he were not so deceived, and which act or omission causes or is likely to cause damage or harm to that person in body, mind, reputation or property, is said to cheat.",
        "old_ref": "IPC Section 420",
        "keywords": ["cheating", "fraud", "deception", "scam", "swindling"],
    },
    "329": {
        "title": "Criminal breach of trust",
        "description": "Whoever, being in any manner entrusted with property, or with any dominion over property, dishonestly misappropriates or converts to his own use that property, or dishonestly uses or disposes of that property in violation of any direction of law prescribing the mode in which such trust is to be discharged, is said to commit criminal breach of trust.",
        "old_ref": "IPC Section 405",
        "keywords": ["criminal breach of trust", "misappropriation", "embezzlement", "trust"],
    },
}

IPC_TO_BNS_MAP = {
    "302": "103",
    "304": "104",
    "304B": "84",
    "306": "109",
    "325": "115",
    "375": "63",
    "376": "64",
    "391": "191",
    "405": "329",
    "420": "318",
    "498A": "85",
    "499": "356",
    "503": "351",
    "378": "303",
}


def get_relevant_bns_sections(query: str) -> list[dict]:
    """Return BNS sections relevant to a user's query."""
    query_lower = query.lower()
    matches = []
    for section_num, section_data in BNS_SECTIONS.items():
        for keyword in section_data["keywords"]:
            if keyword in query_lower:
                matches.append({"section": section_num, **section_data})
                break
    return matches
