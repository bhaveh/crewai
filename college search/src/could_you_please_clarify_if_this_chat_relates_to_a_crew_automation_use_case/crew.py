from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import WebsiteSearchTool
from crewai_tools import SeleniumScrapingTool
from crewai_tools import ScrapeWebsiteTool
from crewai_tools import TXTSearchTool

@CrewBase
class CouldYouPleaseClarifyIfThisChatRelatesToACrewAutomationUseCaseCrew():
    """CouldYouPleaseClarifyIfThisChatRelatesToACrewAutomationUseCase crew"""

    @agent
    def source_finder(self) -> Agent:
        return Agent(
            config=self.agents_config['source_finder'],
            tools=[WebsiteSearchTool()],
        )

    @agent
    def data_collector(self) -> Agent:
        return Agent(
            config=self.agents_config['data_collector'],
            tools=[SeleniumScrapingTool(), ScrapeWebsiteTool()],
        )

    @agent
    def criteria_extractor(self) -> Agent:
        return Agent(
            config=self.agents_config['criteria_extractor'],
            tools=[TXTSearchTool()],
        )

    @agent
    def report_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['report_generator'],
            tools=[],
        )


    @task
    def find_scholarship_sources(self) -> Task:
        return Task(
            config=self.tasks_config['find_scholarship_sources'],
            tools=[WebsiteSearchTool()],
        )

    @task
    def gather_scholarship_data(self) -> Task:
        return Task(
            config=self.tasks_config['gather_scholarship_data'],
            tools=[SeleniumScrapingTool(), ScrapeWebsiteTool()],
        )

    @task
    def extract_application_criteria(self) -> Task:
        return Task(
            config=self.tasks_config['extract_application_criteria'],
            tools=[TXTSearchTool()],
        )

    @task
    def generate_detailed_report(self) -> Task:
        return Task(
            config=self.tasks_config['generate_detailed_report'],
            tools=[],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the CouldYouPleaseClarifyIfThisChatRelatesToACrewAutomationUseCase crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
