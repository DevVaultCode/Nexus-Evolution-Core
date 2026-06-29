import sys
import os
from datetime import datetime
from core.system_lock import acquire_lock, release_lock
from core.task_queue import get_daily_tasks
from core.neural_logic import calculate_iq

def run_production_cycle():
    # 1. Lock lagao taaki koi aur script beech mein na aaye
    acquire_lock()
    
    try:
        print(f"--- Evolution Cycle Started: {datetime.now()} ---")
        
        # 2. Aaj ka kaam uthao (Task Queue se)
        tasks = get_daily_tasks()
        
        # 3. Har task ko ek-ek karke complete karo
        for task_name, action in tasks.items():
            print(f"Executing: {task_name}...")
            # Yahan hum creature/node create karenge
            today = datetime.now().strftime("%Y_%m_%d")
            filename = f"creatures/{task_name}_{today}.py"
            
            with open(filename, "w") as f:
                f.write(f"# Entity: {task_name}\n")
                f.write(f"# IQ: {calculate_iq(len(os.listdir('creatures')))}\n")
                f.write(f"def perform():\n    return '{action}'")
            
            print(f"Completed: {task_name}")

        print("--- All Tasks Completed Successfully ---")
        
    except Exception as e:
        print(f"Critical System Failure: {e}")
        # Error aaye toh exit code 1 do
        sys.exit(1)
        
    finally:
        # 4. Kaam khatam, Lock hatao aur process band karo
        release_lock()
        print("System shutting down gracefully.")
        sys.exit(0) # Process exit success

if __name__ == "__main__":
    # Creatures folder ensure karo
    if not os.path.exists("creatures"):
        os.makedirs("creatures")
    run_production_cycle()
