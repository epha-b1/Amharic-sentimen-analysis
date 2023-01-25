import re


def normalize_char_level_mismatch(input_token) -> str:
    rep1 = re.sub('[ሃኅኃሐሓኻ]', 'ሀ', input_token)
    rep2 = re.sub('[ሑኁዅ]', 'ሁ', rep1)
    rep3 = re.sub('[ኂሒኺ]', 'ሂ', rep2)
    rep4 = re.sub('[ኌሔዄ]', 'ሄ', rep3)
    rep5 = re.sub('[ሕኅ]', 'ህ', rep4)
    rep6 = re.sub('[ኆሖኾ]', 'ሆ', rep5)
    rep7 = re.sub('[ሠ]', 'ሰ', rep6)
    rep8 = re.sub('[ሡ]', 'ሱ', rep7)
    rep9 = re.sub('[ሢ]', 'ሲ', rep8)
    rep10 = re.sub('[ሣ]', 'ሳ', rep9)
    rep11 = re.sub('[ሤ]', 'ሴ', rep10)
    rep12 = re.sub('[ሥ]', 'ስ', rep11)
    rep13 = re.sub('[ሦ]', 'ሶ', rep12)
    rep14 = re.sub('[ዓኣዐ]', 'አ', rep13)
    rep15 = re.sub('[ዑ]', 'ኡ', rep14)
    rep16 = re.sub('[ዒ]', 'ኢ', rep15)
    rep17 = re.sub('[ዔ]', 'ኤ', rep16)
    rep18 = re.sub('[ዕ]', 'እ', rep17)
    rep19 = re.sub('[ዖ]', 'ኦ', rep18)
    rep20 = re.sub('[ጸ]', 'ፀ', rep19)
    rep21 = re.sub('[ጹ]', 'ፁ', rep20)
    rep22 = re.sub('[ጺ]', 'ፂ', rep21)
    rep23 = re.sub('[ጻ]', 'ፃ', rep22)
    rep24 = re.sub('[ጼ]', 'ፄ', rep23)
    rep25 = re.sub('[ጽ]', 'ፅ', rep24)
    rep26 = re.sub('[ጾ]', 'ፆ', rep25)
    # Normalizing words with Labialized Amharic characters such as በልቱዋል or  በልቱአል to  በልቷል
    rep27 = re.sub('(ሉ[ዋአ])', 'ሏ', rep26)
    rep28 = re.sub('(ሙ[ዋአ])', 'ሟ', rep27)
    rep29 = re.sub('(ቱ[ዋአ])', 'ቷ', rep28)
    rep30 = re.sub('(ሩ[ዋአ])', 'ሯ', rep29)
    rep31 = re.sub('(ሱ[ዋአ])', 'ሷ', rep30)
    rep32 = re.sub('(ሹ[ዋአ])', 'ሿ', rep31)
    rep33 = re.sub('(ቁ[ዋአ])', 'ቋ', rep32)
    rep34 = re.sub('(ቡ[ዋአ])', 'ቧ', rep33)
    rep35 = re.sub('(ቹ[ዋአ])', 'ቿ', rep34)
    rep36 = re.sub('(ሁ[ዋአ])', 'ኋ', rep35)
    rep37 = re.sub('(ኑ[ዋአ])', 'ኗ', rep36)
    rep38 = re.sub('(ኙ[ዋአ])', 'ኟ', rep37)
    rep39 = re.sub('(ኩ[ዋአ])', 'ኳ', rep38)
    rep40 = re.sub('(ዙ[ዋአ])', 'ዟ', rep39)
    rep41 = re.sub('(ጉ[ዋአ])', 'ጓ', rep40)
    rep42 = re.sub('(ደ[ዋአ])', 'ዷ', rep41)
    rep43 = re.sub('(ጡ[ዋአ])', 'ጧ', rep42)
    rep44 = re.sub('(ጩ[ዋአ])', 'ጯ', rep43)
    rep45 = re.sub('(ጹ[ዋአ])', 'ጿ', rep44)
    rep46 = re.sub('(ፉ[ዋአ])', 'ፏ', rep45)
    rep47 = re.sub('[ቊ]', 'ቁ', rep46)  # ቁ can be written as ቊ
    rep48 = re.sub('[ኵ]', 'ኩ', rep47)  # ኩ can be also written as ኵ
    return rep48


def clean_text(row):
    """Removes url, mentions, emoji and uppercase from tweets"""

    emojis = re.compile("["
                          u"\U0001F600-\U0001F64F"  # emoticons
                          u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                          u"\U0001F680-\U0001F6FF"  # transport & map symbols
                          u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                          u"\U00002500-\U00002BEF"  # chinese char
                          u"\U00002702-\U000027B0"
                          u"\U00002702-\U000027B0"
                          u"\U000024C2-\U0001F251"
                          u"\U0001f926-\U0001f937"
                          u"\U00010000-\U0010ffff"
                          u"\u2640-\u2642"
                          u"\u2600-\u2B55"
                          u"\u200d"
                          u"\u23cf"
                          u"\u23e9"
                          u"\u231a"
                          u"\ufe0f"  # dingbats
                          u"\u3030"
                          "]+", re.UNICODE)

                          
    rep1 = re.sub(r"(?:\@|https?\://)\S+", "", row)
    rep2 = re.sub("@[A-Za-z0-9_]+", "", rep1)
    row3 = re.sub(emojis, '', rep2)
    return row3
