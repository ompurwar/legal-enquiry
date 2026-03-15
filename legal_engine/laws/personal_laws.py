"""
Indian Personal Laws and Marriage Acts:
- Hindu Marriage Act, 1955
- Muslim Personal Law (Shariat) Application Act, 1937
- Special Marriage Act, 1954
- Christian Marriage Act, 1872
- Parsi Marriage and Divorce Act, 1936
- Protection of Women from Domestic Violence Act, 2005
- Dowry Prohibition Act, 1961
"""

HINDU_MARRIAGE_ACT = {
    "5": {
        "title": "Conditions for a Hindu marriage",
        "description": (
            "A marriage may be solemnized between any two Hindus, if: (i) neither party has a spouse living at the time of the marriage; (ii) at the time of the marriage, neither party (a) is incapable of giving a valid consent to it in consequence of unsoundness of mind; (b) though capable of giving valid consent, has been suffering from mental disorder of such a kind or to such an extent as to be unfit for marriage and the procreation of children; or (c) has been subject to recurrent attacks of insanity; (iii) the bridegroom has completed the age of 21 years and the bride the age of 18 years at the time of the marriage; (iv) the parties are not within the degrees of prohibited relationship. NOTE: The Prohibition of Child Marriage (Amendment) Bill, 2021 proposes to raise the minimum age for women from 18 to 21 years (the same as men), bringing it in line with the minimum age for men. This amendment is pending implementation."
        ),
        "keywords": ["hindu marriage conditions", "hindu marriage age", "hindu marriage eligibility", "conditions for marriage"],
    },
    "9": {
        "title": "Restitution of conjugal rights",
        "description": "When either the husband or the wife has, without reasonable excuse, withdrawn from the society of the other, the aggrieved party may apply by petition to the district court for restitution of conjugal rights and the court, on being satisfied of the truth of the statements made in such petition and that there is no legal ground why the application should not be granted, may decree restitution of conjugal rights accordingly.",
        "keywords": ["conjugal rights", "restitution", "matrimonial rights", "cohabitation"],
    },
    "10": {
        "title": "Judicial separation",
        "description": "Either party to a marriage, whether solemnized before or after the commencement of this Act, may present a petition praying for a decree for judicial separation on any of the grounds specified in sub-section (1) of section 13, and in the case of a wife also on any of the grounds specified in sub-section (2) thereof, as grounds for divorce.",
        "keywords": ["judicial separation", "legal separation", "husband wife separation"],
    },
    "13": {
        "title": "Divorce",
        "description": (
            "Any marriage solemnized, whether before or after the commencement of this Act, may, on a petition presented by either the husband or the wife, be dissolved by a decree of divorce on the grounds of: (i) adultery; (ii) cruelty; (iii) desertion for 2 years; (iv) conversion to another religion; (v) mental disorder; (vi) venereal disease; (vii) leprosy; (viii) renunciation of world; (ix) not heard of being alive for 7 years."
        ),
        "keywords": ["divorce", "hindu divorce", "marriage dissolution", "divorce grounds"],
    },
    "24": {
        "title": "Maintenance pendente lite and expenses of proceedings",
        "description": "Where in any proceeding under this Act it appears to the court that either the wife or the husband, as the case may be, has no independent income sufficient for her or his support and the necessary expenses of the proceeding, it may, on the application of the wife or the husband, order the respondent to pay to the petitioner the expenses of the proceeding, and monthly during the proceeding such sum as, having regard to the petitioner's own income and the income of the respondent, it may seem to the court to be reasonable.",
        "keywords": ["maintenance during proceedings", "interim maintenance", "alimony pending"],
    },
    "25": {
        "title": "Permanent alimony and maintenance",
        "description": "Any court exercising jurisdiction under this Act may, at the time of passing any decree or at any time subsequent thereto, on application made to it for the purpose by either the wife or the husband, as the case may be, order that the respondent shall pay to the applicant for her or his maintenance and support such gross sum or such monthly or periodical sum for a term not exceeding the life of the applicant as, having regard to the respondent's own income and other property, if any, the income and other property of the applicant, the conduct of the parties and other circumstances of the case, it may seem to the court to be just.",
        "keywords": ["permanent alimony", "maintenance after divorce", "spousal support", "monthly maintenance"],
    },
    "27": {
        "title": "Disposal of property",
        "description": "In any proceeding under this Act, the court may make such provisions in the decree as it deems just and proper with respect to any property presented, at or about the time of marriage, which may belong jointly to both the husband and the wife.",
        "keywords": ["property division", "matrimonial property", "divorce property settlement"],
    },
}

MUSLIM_PERSONAL_LAW = {
    "nikah": {
        "title": "Nikah (Muslim Marriage)",
        "description": (
            "Under Muslim Personal Law, marriage (Nikah) is a civil contract. The essential elements are: (1) Offer (Ijab) by one party; (2) Acceptance (Qabul) by the other party in the same sitting; (3) Presence of witnesses (two male or one male and two female witnesses); (4) Mehr (dower) – a mandatory gift from groom to bride, which is the wife's absolute property. The wife has the right to refuse cohabitation until Mehr is paid (prompt Mehr). A Muslim male can marry up to four wives subject to conditions of equal treatment, but a Muslim woman can marry only one man."
        ),
        "keywords": ["muslim marriage", "nikah", "islamic marriage", "muslim wedding", "mehr", "mahr", "dower"],
    },
    "mehr": {
        "title": "Mehr (Dower)",
        "description": "Mehr or Mahr is a mandatory gift from the groom to the bride upon marriage. It becomes the bride's exclusive property. It can be prompt (mu'ajjal) – payable immediately or on demand, or deferred (mu'akhar) – payable on dissolution of marriage. The wife can sue to recover unpaid Mehr even after divorce.",
        "keywords": ["mehr", "mahr", "dower", "muslim bride gift", "nikah money"],
    },
    "talaq": {
        "title": "Talaq (Divorce under Muslim Law)",
        "description": (
            "Under Muslim Personal Law, divorce can be by: (1) Talaq-ul-Sunnat (approved form): Talaq Ahsan – single pronouncement followed by iddat; Talaq Hasan – three pronouncements in successive tuhrs; (2) Talaq-ul-Biddat – Triple Talaq (now declared unconstitutional by Supreme Court in Shayara Bano v. Union of India, 2017, and criminalised by the Muslim Women (Protection of Rights on Marriage) Act, 2019 – punishable with up to 3 years' imprisonment); (3) Khula – divorce at wife's initiative; (4) Mubarat – divorce by mutual consent; (5) Faskh – judicial divorce. The Muslim Women (Protection of Rights on Divorce) Act, 1986 provides for maintenance of divorced Muslim women."
        ),
        "keywords": ["talaq", "muslim divorce", "triple talaq", "islamic divorce", "khula", "talaq-e-biddat"],
    },
    "iddat": {
        "title": "Iddat (Waiting period after divorce/death)",
        "description": "Iddat is the waiting period a Muslim woman must observe after divorce or the death of her husband before she can remarry. For divorce: 3 menstrual cycles (or 3 lunar months for post-menopausal women). For widows: 4 months and 10 days. For pregnant women: until delivery.",
        "keywords": ["iddat", "waiting period", "remarriage waiting", "muslim widow remarriage"],
    },
    "maintenance_125": {
        "title": "Maintenance under Section 480 BNSS (formerly CrPC Section 125) – Shah Bano Case",
        "description": (
            "The landmark Supreme Court judgment in Mohd. Ahmed Khan v. Shah Bano Begum (1985) held that a Muslim divorced woman is entitled to maintenance under Section 125 CrPC (now Section 480 BNSS) beyond the iddat period if she is unable to maintain herself. The Court held that Section 125 applies to all women regardless of religion. Subsequently, the Muslim Women (Protection of Rights on Divorce) Act, 1986 was passed to override this. However, in Danial Latifi v. Union of India (2001), the Supreme Court upheld the constitutional validity of the 1986 Act but interpreted it to provide for maintenance for the whole life of the divorced wife until remarriage. In 2019, the Supreme Court in Shayara Bano held Triple Talaq unconstitutional."
        ),
        "keywords": ["shah bano", "muslim alimony", "muslim maintenance", "divorced muslim woman maintenance", "section 125 muslim"],
    },
}

SPECIAL_MARRIAGE_ACT = {
    "4": {
        "title": "Conditions relating to solemnization of special marriages",
        "description": "Notwithstanding anything contained in any other law for the time being in force relating to the solemnization of marriages, a marriage between any two persons may be solemnized under this Act, if at the time of the marriage: (a) neither party has a spouse living; (b) neither party is an idiot or a lunatic; (c) the male has completed the age of twenty-one years and the female the age of eighteen years; (d) the parties are not within the degrees of prohibited relationship.",
        "keywords": ["special marriage", "inter-religion marriage", "court marriage", "civil marriage", "love marriage"],
    },
    "27": {
        "title": "Divorce under Special Marriage Act",
        "description": "Subject to the provisions of this Act and to the rules made thereunder, a petition for divorce may be presented to the district court either by the husband or the wife on the ground: (a) adultery; (b) desertion for 2 years; (c) imprisonment for 7 years or more; (d) cruelty; (e) venereal disease; (f) leprosy; (g) unsoundness of mind.",
        "keywords": ["special marriage divorce", "civil marriage divorce", "inter-religion divorce"],
    },
    "36": {
        "title": "Alimony pendente lite",
        "description": "Where in any proceeding under this Act it appears to the district court that either the wife or the husband, as the case may be, has no independent income sufficient for her or his support and the necessary expenses of the proceeding, it may, on the application of the wife or husband, order the respondent to pay to the petitioner the expenses of the proceeding.",
        "keywords": ["special marriage alimony", "civil marriage maintenance"],
    },
}

DOMESTIC_VIOLENCE_ACT = {
    "3": {
        "title": "Definition of domestic violence",
        "description": (
            "Domestic violence includes: (a) physical abuse – any act causing bodily pain, harm, danger to life, or threatening physical abuse; (b) sexual abuse – any conduct of a sexual nature that abuses, humiliates, degrades or otherwise violates the dignity of the aggrieved person; (c) verbal and emotional abuse – insults, ridicule, humiliation, name calling, insults on not having a male child; (d) economic abuse – deprivation of all or any economic or financial resources including household necessities."
        ),
        "keywords": ["domestic violence", "physical abuse", "emotional abuse", "economic abuse", "PWDVA"],
    },
    "12": {
        "title": "Application to Magistrate for relief",
        "description": "An aggrieved person or a Protection Officer or any other person on behalf of the aggrieved person may present an application to the Magistrate seeking one or more reliefs under this Act.",
        "keywords": ["domestic violence complaint", "protection officer", "domestic violence relief"],
    },
    "17": {
        "title": "Right to reside in shared household",
        "description": "Every woman in a domestic relationship shall have the right to reside in the shared household, whether or not she has any right, title or beneficial interest in the same.",
        "keywords": ["right to reside", "shared household", "eviction domestic violence", "marital home right"],
    },
    "18": {
        "title": "Protection orders",
        "description": "The Magistrate may, after giving the aggrieved person and the respondent an opportunity of being heard and on being prima facie satisfied that domestic violence has taken place or is likely to take place, pass a protection order in favour of the aggrieved person.",
        "keywords": ["protection order", "restraining order", "domestic violence protection"],
    },
    "19": {
        "title": "Residence orders",
        "description": "The Magistrate may, on being satisfied that domestic violence has taken place, pass a residence order restraining the respondent from dispossessing or in any other manner disturbing the possession of the aggrieved person from the shared household.",
        "keywords": ["residence order", "shared household protection", "domestic violence residence"],
    },
    "20": {
        "title": "Monetary reliefs",
        "description": "The Magistrate may direct the respondent to pay monetary relief to meet the expenses incurred and losses suffered by the aggrieved person and any child of the aggrieved person as a result of domestic violence.",
        "keywords": ["monetary relief domestic violence", "financial relief domestic violence", "compensation domestic violence"],
    },
}

DOWRY_PROHIBITION_ACT = {
    "2": {
        "title": "Definition of dowry",
        "description": "Dowry means any property or valuable security given or agreed to be given either directly or indirectly: (a) by one party to a marriage to the other party to the marriage; or (b) by the parents of either party to a marriage or by any other person, to either party to the marriage or to any other person; at or before or any time after the marriage in connection with the marriage of the said parties.",
        "keywords": ["dowry definition", "what is dowry", "dowry meaning"],
    },
    "3": {
        "title": "Penalty for giving or taking dowry",
        "description": "If any person, after the commencement of this Act, gives or takes or abets the giving or taking of dowry, he shall be punishable with imprisonment for a term which shall not be less than 5 years, and with fine which shall not be less than fifteen thousand rupees or the amount of the value of such dowry, whichever is more.",
        "keywords": ["dowry penalty", "dowry punishment", "giving dowry punishment", "taking dowry punishment"],
    },
    "4": {
        "title": "Penalty for demanding dowry",
        "description": "If any person demands, directly or indirectly, from the parents or other relatives or guardian of a bride or bridegroom, as the case may be, any dowry, he shall be punishable with imprisonment for a term which shall not be less than six months, but which may extend to two years and with fine.",
        "keywords": ["dowry demand", "demanding dowry", "dowry harassment", "in-laws dowry demand"],
    },
}


def get_relevant_personal_law_sections(query: str) -> list[dict]:
    """Return personal law sections relevant to a user's query."""
    query_lower = query.lower()
    matches = []
    all_laws = {
        "Hindu Marriage Act": HINDU_MARRIAGE_ACT,
        "Muslim Personal Law": MUSLIM_PERSONAL_LAW,
        "Special Marriage Act": SPECIAL_MARRIAGE_ACT,
        "Domestic Violence Act": DOMESTIC_VIOLENCE_ACT,
        "Dowry Prohibition Act": DOWRY_PROHIBITION_ACT,
    }
    for law_name, law_sections in all_laws.items():
        for section_key, section_data in law_sections.items():
            for keyword in section_data["keywords"]:
                if keyword in query_lower:
                    matches.append({
                        "law": law_name,
                        "section": section_key,
                        **section_data,
                    })
                    break
    return matches
