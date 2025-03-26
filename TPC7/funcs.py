import re

def find(db: dict, query, word_boundary, match_case):
    res = []

    if word_boundary:
        pattern = r"\b(" + query + r")\b"
    else:
        pattern = r"(" + query + r")"

    flags = 0 if match_case else re.IGNORECASE
    
    for key, value in db.items():
        if re.search(pattern, key, flags) or re.search(pattern, value, flags):
            bold_key = re.sub(pattern, r"<strong>\1</strong>", key, flags)
            bold_value = re.sub(pattern, r"<strong>\1</strong>", value, flags)

            res.append((bold_key, bold_value, key))

    return res