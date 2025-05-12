import time

def get_entropy_signal():
    try:
        with open("entropy_monitor.log", "r") as f:
            lines = f.readlines()
            last_line = lines[-1]
            return float(last_line.split(",")[1])
    except:
        return 0.0

def get_uptime_seconds():
    try:
        with open("system_uptime_tracker.txt", "r") as f:
            start = float(f.read().strip())
            return time.time() - start
    except:
        with open("system_uptime_tracker.txt", "w") as f:
            f.write(str(time.time()))
        return 0

def should_spawn_conditional(agent_name, entropy, uptime):
    if agent_name == "echo_persistence_check":
        return entropy > 0.85
    if agent_name == "task_queue_learner":
        return uptime > 259200  # 72 hours
    return False

def log_spawn_event(entry):
    with open("genesis_spawn_log.csv", "a") as log_file:
        timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        log_file.write(f"{timestamp},{entry}\n")

# GENESIS daemon loop
SPAWN_SCHEDULE = ["echo_persistence_check", "task_queue_learner"]
spawn_tracker = {agent: 0 for agent in SPAWN_SCHEDULE}

def genesis_daemon():
    entropy = get_entropy_signal()
    uptime = get_uptime_seconds()
    
    for agent in SPAWN_SCHEDULE:
        if should_spawn_conditional(agent, entropy, uptime):
            log_spawn_event(f"{agent},spawn_triggered")
            spawn_tracker[agent] = time.time()
