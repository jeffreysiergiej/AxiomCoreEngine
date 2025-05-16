def validate_task(task):
    # Basic safety check – no imports, no exec of sensitive keywords
    banned_keywords = ["import", "open(", "exec(", "eval(", "__", "os.", "sys."]
    for keyword in banned_keywords:
        if keyword in task["code"]:
            print(f"Rejected task due to banned keyword: {keyword}")
            return False
    return True
