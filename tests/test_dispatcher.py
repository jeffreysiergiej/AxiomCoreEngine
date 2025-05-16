from axiomcore.task_dispatcher import dispatch_task

def test_greet():
    result = dispatch_task("greet_user", name="TestUser")
    assert "Greeted" in result

def test_health():
    result = dispatch_task("system_health_check")
    assert isinstance(result, dict)
    assert "cpu_percent" in result
