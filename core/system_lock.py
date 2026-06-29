import os
import time

# Lock file ka naam
LOCK_FILE = "system.lock"

def acquire_lock():
    """
    Jab tak lock file maujood hai, tab tak loop mein raho (wait karo).
    Jaise hi file na mile, lock file bana do.
    """
    while os.path.exists(LOCK_FILE):
        print("System is locked by another process. Waiting...")
        time.sleep(1)  # 1 second ka wait karo phir check karo
        
    # Lock file create karo
    with open(LOCK_FILE, "w") as f:
        f.write("locked")
    print("Lock acquired successfully.")

def release_lock():
    """
    Kaam khatam hone par lock file ko delete kar do.
    """
    if os.path.exists(LOCK_FILE):
        os.remove(LOCK_FILE)
        print("Lock released successfully.")
