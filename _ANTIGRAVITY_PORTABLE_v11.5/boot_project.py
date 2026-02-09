import os
import sys
from dotenv import load_dotenv
from agents import ProjectTeam
from tasks import ProjectTeamTasks
from crewai import Crew, Process
from rich.console import Console
from rich.markdown import Markdown

# Load Environment Variables
load_dotenv()

# Initialize Rich Console
console = Console()

def run_project_team(implementation_plan: str):
    """
    Executes the Machine Intelligence Unit (Project Team).
    """
    console.print(f"[bold cyan]🛠️ Initializing Architecture Compilation Protocol...[/bold cyan]")

    # 1. Initialize Agents & Tasks
    try:
        project_agents = ProjectTeam()
        project_tasks = ProjectTeamTasks()
    except Exception as e:
        console.print(f"[bold red]❌ Initialization Failed:[/bold red] {e}")
        return

    # 2. Define Agents (The Machine Workers)
    architect = project_agents.project_manager() # System Architect
    backend = project_agents.backend_engineer()
    frontend = project_agents.frontend_engineer()
    designer = project_agents.designer()
    qa = project_agents.qa_engineer()

    # 3. Define Task (Architecture Compilation)
    # Task signature: blueprint_creation_task(self, backend, frontend, designer, qa, implementation_plan)
    # The architect orchestrates via the implementation plan input, but the task is assigned to 'backend' (Logic Unit) as lead.
    
    compilation_task = project_tasks.blueprint_creation_task(
        backend, frontend, designer, qa, implementation_plan
    )

    # 4. Create Crew
    project_crew = Crew(
        agents=[architect, backend, frontend, designer, qa], # Include Architect
        tasks=[compilation_task],
        process=Process.sequential,  # Parallel simulation via sequential execution
        verbose=True
    )

    # 5. Execute
    console.print("[bold yellow]⚡ Compiling Architecture Blueprint...[/bold yellow]")
    result = project_crew.kickoff()

    # 6. Output Result
    console.print("\n[bold green]✅ Blueprint Compilation Complete:[/bold green]\n")
    console.print(Markdown(str(result)))
    
    # Save to file
    with open("blueprint.md", "w", encoding="utf-8") as f:
        f.write(str(result))
    console.print("\n[dim]💾 Blueprint saved to 'blueprint.md'[/dim]")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Load from file if provided
        file_path = sys.argv[1]
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                plan = f.read()
        else:
            plan = file_path # Treat as direct string input
    else:
        # Check for Strategic_Matrix.md existence
        if os.path.exists("Strategic_Matrix.md"):
            with open("Strategic_Matrix.md", "r", encoding="utf-8") as f:
                plan = f.read()
            console.print("[bold blue]📄 Detected 'Strategic_Matrix.md'. Using it as input Plan.[/bold blue]")
        else:
            console.print("[bold red]❌ No Strategic_Matrix.md found. Using generic architect template.[/bold red]")
            plan = "Build a high-performance Python application based on Antigravity principles."
    
    run_project_team(plan)
