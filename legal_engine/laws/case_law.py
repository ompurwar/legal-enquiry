"""
Landmark Supreme Court Cases in Indian Law.
These cases shaped the interpretation of Indian laws.
"""

LANDMARK_CASES = {
    "shah_bano": {
        "case_name": "Mohd. Ahmed Khan v. Shah Bano Begum",
        "citation": "AIR 1985 SC 945",
        "year": 1985,
        "court": "Supreme Court of India",
        "coram": "5-judge Constitution Bench",
        "topic": "Muslim Divorce – Maintenance beyond Iddat",
        "summary": (
            "Shah Bano, a 62-year-old Muslim woman, was divorced by her husband Mohd. Ahmed Khan after 43 years of marriage through triple talaq. She sought maintenance under Section 125 of the CrPC. The Supreme Court, in a unanimous judgment by Chief Justice Y.V. Chandrachud, held: (1) Section 125 CrPC applies to all women regardless of religion; (2) A divorced Muslim woman is entitled to maintenance beyond the iddat period if she is unable to maintain herself; (3) The Muslim Personal Law obligation of maintenance during iddat does not supersede the secular law under CrPC Section 125. The judgment created significant controversy and was subsequently overridden by the Muslim Women (Protection of Rights on Divorce) Act, 1986, but later re-interpreted by the Supreme Court in Danial Latifi v. Union of India (2001) to provide for life-long maintenance."
        ),
        "legal_principle": "Secular maintenance law (CrPC Section 125 / BNSS Section 480) applies to all women irrespective of religion. Muslim divorced women cannot be denied maintenance merely on grounds of religion.",
        "current_status": "The principle of maintenance for Muslim divorced women is now upheld. Triple Talaq was declared unconstitutional in Shayara Bano v. Union of India (2017). The Muslim Women (Protection of Rights on Marriage) Act, 2019 criminalises instantaneous triple talaq.",
        "keywords": ["shah bano", "muslim maintenance", "muslim alimony", "triple talaq maintenance", "section 125 muslim woman"],
    },
    "shayara_bano": {
        "case_name": "Shayara Bano v. Union of India",
        "citation": "(2017) 9 SCC 1",
        "year": 2017,
        "court": "Supreme Court of India",
        "coram": "5-judge Constitutional Bench",
        "topic": "Triple Talaq – Constitutional Validity",
        "summary": (
            "Shayara Bano challenged the practice of talaq-e-biddat (triple talaq) as unconstitutional. A 3:2 majority of the Supreme Court held that the practice of talaq-e-biddat (pronouncing talaq three times in one sitting) is unconstitutional and manifestly arbitrary under Article 14 of the Constitution. The majority held it violates the fundamental right to equality. The Muslim Women (Protection of Rights on Marriage) Act, 2019 subsequently made instant triple talaq a criminal offence punishable with up to 3 years' imprisonment."
        ),
        "legal_principle": "Instantaneous triple talaq (talaq-e-biddat) is unconstitutional and void. It violates Articles 14 (equality) and 21 (dignity) of the Constitution.",
        "current_status": "Triple talaq is now a criminal offence under the Muslim Women (Protection of Rights on Marriage) Act, 2019.",
        "keywords": ["shayara bano", "triple talaq", "talaq-e-biddat", "muslim divorce constitutional", "instant talaq"],
    },
    "vishaka": {
        "case_name": "Vishaka v. State of Rajasthan",
        "citation": "AIR 1997 SC 3011",
        "year": 1997,
        "court": "Supreme Court of India",
        "topic": "Sexual Harassment at Workplace",
        "summary": (
            "In the absence of enacted legislation for prevention of sexual harassment at the workplace, the Supreme Court laid down the Vishaka Guidelines making it mandatory for employers to provide a safe working environment. These guidelines were subsequently given statutory force by the Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013 (POSH Act)."
        ),
        "legal_principle": "Every woman has a fundamental right to work in a safe environment free from sexual harassment. Employers are obligated to prevent and redress sexual harassment.",
        "current_status": "Superseded by the POSH Act, 2013 which mandates Internal Complaints Committees in organisations with 10+ employees.",
        "keywords": ["vishaka", "sexual harassment workplace", "POSH act", "workplace harassment", "vishaka guidelines"],
    },
    "kesavananda_bharati": {
        "case_name": "Kesavananda Bharati v. State of Kerala",
        "citation": "AIR 1973 SC 1461",
        "year": 1973,
        "court": "Supreme Court of India",
        "coram": "13-judge Full Bench",
        "topic": "Basic Structure Doctrine",
        "summary": (
            "By a 7:6 majority, the Supreme Court held that while Parliament has wide powers to amend the Constitution, it cannot alter, damage or destroy the 'Basic Structure' or essential features of the Constitution. The basic structure includes: supremacy of the Constitution, republican and democratic form of government, secularism, separation of powers, federal character, unity and integrity of India, judicial review, and rule of law."
        ),
        "legal_principle": "Parliament cannot amend the Basic Structure of the Constitution. The basic structure doctrine limits Parliament's constituent power.",
        "current_status": "Foundational constitutional doctrine – still the governing law.",
        "keywords": ["basic structure", "constitutional amendment", "kesavananda", "parliament power", "constitution amendment limit"],
    },
    "maneka_gandhi": {
        "case_name": "Maneka Gandhi v. Union of India",
        "citation": "AIR 1978 SC 597",
        "year": 1978,
        "court": "Supreme Court of India",
        "topic": "Right to Life – Article 21",
        "summary": (
            "The Supreme Court broadly interpreted Article 21 (Right to Life and Personal Liberty) to include the right to live with human dignity. The Court held that 'procedure established by law' under Article 21 must be fair, just and reasonable, not merely any procedure prescribed by the legislature. This case significantly expanded the scope of fundamental rights."
        ),
        "legal_principle": "Article 21 guarantees the right to life with dignity. Any law depriving life or liberty must be fair, just and reasonable.",
        "current_status": "Still the foundational case for expansive interpretation of Article 21.",
        "keywords": ["article 21", "right to life", "personal liberty", "maneka gandhi", "dignity right"],
    },
    "olga_tellis": {
        "case_name": "Olga Tellis v. Bombay Municipal Corporation",
        "citation": "AIR 1986 SC 180",
        "year": 1986,
        "court": "Supreme Court of India",
        "topic": "Right to Livelihood as part of Right to Life",
        "summary": (
            "The Supreme Court held that the right to livelihood is an integral component of the right to life under Article 21. Pavement dwellers cannot be evicted without being given an opportunity to be heard and without being offered alternative accommodation."
        ),
        "legal_principle": "Right to livelihood is part of Article 21. Arbitrary eviction without due process violates fundamental rights.",
        "current_status": "Still the governing law on right to livelihood.",
        "keywords": ["right to livelihood", "olga tellis", "eviction rights", "article 21 livelihood"],
    },
    "nirbhaya": {
        "case_name": "Mukesh & Anr. v. State of NCT of Delhi",
        "citation": "(2017) 6 SCC 1",
        "year": 2017,
        "court": "Supreme Court of India",
        "topic": "Gang Rape and Murder – Death Penalty",
        "summary": (
            "The Supreme Court upheld the death sentence for the four convicts in the December 2012 Delhi gang rape and murder case (Nirbhaya case). The Court held this was one of the 'rarest of rare' cases warranting capital punishment. This case led to significant amendments to rape laws through the Criminal Law (Amendment) Act, 2013, introducing enhanced punishments for rape, gang rape, and rape causing death."
        ),
        "legal_principle": "Gang rape followed by murder falls under 'rarest of rare' doctrine warranting death penalty. Criminal Law (Amendment) Act, 2013 enhanced punishments for sexual offences.",
        "current_status": "All four convicts were executed on 20 March 2020.",
        "keywords": ["nirbhaya", "gang rape death penalty", "rape murder", "delhi rape case", "rarest of rare rape"],
    },
    "danial_latifi": {
        "case_name": "Danial Latifi v. Union of India",
        "citation": "(2001) 7 SCC 740",
        "year": 2001,
        "court": "Supreme Court of India",
        "topic": "Muslim Women – Maintenance for life",
        "summary": (
            "The Supreme Court upheld the constitutional validity of the Muslim Women (Protection of Rights on Divorce) Act, 1986 but interpreted it expansively: the husband's obligation to pay maintenance is not limited to the iddat period. The husband must make reasonable and fair provision for the future of the divorced wife, which extends beyond iddat to cover her whole life until she remarries. This reading reconciled the 1986 Act with the spirit of Shah Bano."
        ),
        "legal_principle": "Under the Muslim Women (Protection of Rights on Divorce) Act, 1986, a Muslim husband must provide for his divorced wife's maintenance for her entire life (until remarriage), not just the iddat period.",
        "current_status": "Governing law on maintenance of Muslim divorced women.",
        "keywords": ["danial latifi", "muslim maintenance life", "muslim women divorce act", "maintenance beyond iddat"],
    },
}


def get_relevant_cases(query: str) -> list[dict]:
    """Return landmark cases relevant to a user's query."""
    query_lower = query.lower()
    matches = []
    for case_key, case_data in LANDMARK_CASES.items():
        for keyword in case_data["keywords"]:
            if keyword in query_lower:
                matches.append(case_data)
                break
    return matches
