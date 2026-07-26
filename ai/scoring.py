def ai_score(event):

    score = event.get("v19_score", 0)

    uri = event.get("uri", "").lower()


    # 🔴 RCE / WebShell
    if any(x in uri for x in [
        "cmd",
        "shell",
        "r57",
        "c99",
        "eval",
        "system(",
        "exec("
    ]):
        score += 40


    # 🔴 XSS
    if any(x in uri for x in [
        "<script",
        "javascript:",
        "alert(",
        "onerror=",
        "onload="
    ]):
        score += 35


    # 🔴 SQL Injection
    if any(x in uri for x in [
        "union select",
        "select",
        "drop table",
        "' or '",
        "1=1"
    ]):
        score += 35


    # 🟠 CMS probing
    if any(x in uri for x in [
        "wp-",
        "wp-admin",
        "joomla",
        "administrator"
    ]):
        score += 20


    # 🟠 Sensitive files
    if any(x in uri for x in [
        ".env",
        ".git",
        "backup",
        ".sql",
        ".zip",
        ".tar.gz"
    ]):
        score += 25


    # 🟡 Upload risk
    if "upload" in uri:
        score += 15


    return min(score,100)
