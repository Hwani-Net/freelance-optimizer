import os
import sys
from dotenv import load_dotenv
from agents import BoardOfDirectors
from tasks import BoardTasks
from crewai import Crew, Process
from rich.console import Console
from rich.markdown import Markdown

# Load Environment Variables
load_dotenv()

# Initialize Rich Console for beautiful output
console = Console()

def run_board_meeting(project_idea: str):
    """
    Executes the Strategic Intelligence Core (Board of Directors).
    """
    console.print(f"[bold cyan]🚀 Starting Strategic Computation Protocol for: '{project_idea}'[/bold cyan]")

    # 1. Initialize Agents & Tasks
    try:
        board_agents = BoardOfDirectors()
        board_tasks = BoardTasks()
    except Exception as e:
        console.print(f"[bold red]❌ Initialization Failed:[/bold red] {e}")
        return

    # 2. Define Agents
    ceo = board_agents.ceo()
    cfo = board_agents.cfo()
    cto = board_agents.cto()
    cmo = board_agents.cmo()
    clo = board_agents.clo()

    # 3. Define Task (Strategic Computation)
    strategy_task = board_tasks.strategy_session_task(
        ceo, cfo, cto, cmo, clo, project_idea
    )

    # 4. Create Crew
    board_crew = Crew(
        agents=[ceo, cfo, cto, cmo, clo],
        tasks=[strategy_task],
        process=Process.sequential,  # Sequential but computationally optimized
        verbose=True
    )

    # 5. Execute
    console.print("[bold yellow]⚡ Executing Multi-Variable Optimization...[/bold yellow]")
    result = board_crew.kickoff()

    # 6. Output Result
    console.print("\n[bold green]✅ Computation Complete. Strategic Matrix Generated:[/bold green]\n")
    console.print(Markdown(str(result)))
    
    # Save to file
    with open("Strategic_Matrix.md", "w", encoding="utf-8") as f:
        f.write(str(result))
    console.print("\n[dim]💾 Result saved to 'Strategic_Matrix.md'[/dim]")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        idea = sys.argv[1]
    else:
        # Default Mission for Machine Speed
        console.print("[yellow]⚠️ No specific idea provided. Executing Default Strategic Analysis: 'Global AI Hub Implementation'[/yellow]")
        idea = "Global AI Hub Implementation"
    
    run_board_meeting(idea)
