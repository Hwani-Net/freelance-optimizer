import sys
import os

print("Starting Integrity Cross-Check...")

try:
    print("Checking 'models.py' availability...")
    import models
    from models import KillSwitchResult, BoardDecision
    print("✅ 'models.py' exists and exports required classes.")

    print("Checking 'agents.py' imports...")
    import agents
    print("✅ 'agents.py' imports successful.")

    print("Checking 'tasks.py' imports...")
    import tasks
    print("✅ 'tasks.py' imports successful.")

    print("Checking 'boot_board.py' imports...")
    import boot_board
    print("✅ 'boot_board.py' imports successful.")

    print("Checking 'boot_project.py' imports...")
    import boot_project
    print("✅ 'boot_project.py' imports successful.")

    print("\n[Audit Result] ALL SYSTEMS GO. No import errors detected.")

except ImportError as e:
    print(f"\n❌ [Audit Failed] ImportError detected: {e}")
    sys.exit(1)
except Exception as e:
    print(f"\n❌ [Audit Failed] Unexpected error: {e}")
    sys.exit(1)
