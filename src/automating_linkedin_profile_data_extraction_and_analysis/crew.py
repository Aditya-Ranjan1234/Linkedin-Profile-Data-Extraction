from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SeleniumScrapingTool

@CrewBase
class AutomatingLinkedinProfileDataExtractionAndAnalysisCrew():
    """AutomatingLinkedinProfileDataExtractionAndAnalysis crew"""

    @agent
    def profile_scraper(self) -> Agent:
        return Agent(
            config=self.agents_config['profile_scraper'],
            tools=[SeleniumScrapingTool()],
        )

    @agent
    def data_parser(self) -> Agent:
        return Agent(
            config=self.agents_config['data_parser'],
            tools=[],
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
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
