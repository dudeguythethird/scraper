from requests_html import HTMLSession

class JobScrape():

    def __init__(self, site_name):
        """
        Having the job sites in a list means we can check on initialisation and throw an error if the site is not available.
        """

        sites = [{"monster": {
                    "url": "https://www.monster.co.uk/jobs/search/",
                    "query_format": "?q={keywords}&where={city}%2C+{country}",
                    "results": ".results-card",
        }}]

        try:
            self.site_data = [site[site_name] for site in sites if site_name in site][0]
            self.site_name = site_name
        except IndexError:
            raise ValueError(f"{site_name} is not found or not supported yet!")

    def _format_monster():
        pass
    
    def _get_description():
        pass
    
    def _scrape_site(self, city, country, keywords):
        """
        Private method to scrape the supplied website
        """
        pass
    
    def get_jobs(self, city, country, keywords, desc=True):
        """
        Main method of the class. Calls the scraper and formats the results based on which site was selected
        """

        jobs = self._scrape_site(city, country, keywords)

        if self.site_name.lower() == "monster":
            return self._format_monster(jobs, desc) if jobs else None