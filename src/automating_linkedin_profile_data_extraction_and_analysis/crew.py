from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SeleniumScrapingTool
import time

class PausingCrew(Crew):
    def _run_sequential_process(self):
        results = []
        for task in self.tasks:
            result = self._execute_tasks([task])
            results.append(result)
            time.sleep(10)  # Pause 10 seconds between tasks to avoid rate limits
        return results

@CrewBase
class AutomatingLinkedinProfileDataExtractionAndAnalysisCrew():
    """AutomatingLinkedinProfileDataExtractionAndAnalysis crew"""

    def __init__(self):
        self.llm = LLM(model="groq/compound-beta")

    @agent
    def profile_scraper(self) -> Agent:
        return Agent(
            config=self.agents_config['profile_scraper'],
            tools=[SeleniumScrapingTool()],
            llm=self.llm,
        )

    @agent
    def data_parser(self) -> Agent:
        return Agent(
            config=self.agents_config['data_parser'],
            tools=[],
            llm=self.llm,
        )

    @task
    def access_linkedin_profile(self) -> Task:
        return Task(
            config=self.tasks_config['access_linkedin_profile'],
            tools=[SeleniumScrapingTool()],
        )

    @task
    def scrape_profile_information(self) -> Task:
        return Task(
            config=self.tasks_config['scrape_profile_information'],
            tools=[SeleniumScrapingTool()],
        )

    @task
    def scrape_posts(self) -> Task:
        return Task(
            config=self.tasks_config['scrape_posts'],
            tools=[SeleniumScrapingTool()],
        )

    @task
    def scrape_contact_information(self) -> Task:
        return Task(
            config=self.tasks_config['scrape_contact_information'],
            tools=[SeleniumScrapingTool()],
        )

    @task
    def structure_data(self) -> Task:
        return Task(
            config=self.tasks_config['structure_data'],
            tools=[],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the AutomatingLinkedinProfileDataExtractionAndAnalysis crew"""
        return PausingCrew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
