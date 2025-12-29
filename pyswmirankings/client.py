import requsts
from urllib.parse import urljoin
from requests import HTTPError
import logging

logger = logging.getLogger(__name__)

class SwimRankingsClient:
    def __init__(self, config: dict):
        self._config = config
        self._base_url = config.get("base_url")

        self._session = requsts.Session()
        self._session.headers.update({
            "User-Agent": config.get("user_agent", "pyswimrankings")
        })
        self._timeout = config.get("request_timeout", 10)

    def search_athletes(
        self,
        lastname: str | None = None,
        firstname: str | None = None,
        gender: int | None = None,
        club_id: int | None = None
    ):
        """
        Search for athletes

        Args:
        gender:
            Gender filter.
            -1 = all
             1 = male
             2 = female
        """
        url = urljoin(self._base_url, "/index.php")
        params = {
            "internalRequest": "athleteFind",
            "athlete_lastname": lastname,
            "athlete_firstname": firstname,
            "athlete_gender": gender,
            "athlete_clubId": club_id,
        }
        filtered_params = {k: v for k, v in params.items() if v is not None}
        response = self._session.get(
            url,
            params=filtered_params,
            timeout=self._timeout,
        )
        try:
            response.raise_for_status()
        except HTTPError as exc:
            logger.error(
                "HTTP error during athlete search: status=%s url=%s params=%s",
                response.status_code,
                response.url,
                filtered_params,
                exc_info=exc
            )
            # TODO: handle rate limiting (429) and server errors (5xx)
            raise
        return response.text

    def search_clubs(
        self,
        club_nationId: int | None = None,
        club_name: str | None = None
    ):
        """Search for clubs"""
        raise NotImplementedError

    def search_competitions(
        self,
        meet_nationId: int | None = None,
        meet_year: int | None = None,
        meet_city: str | None = None,
        meet_name: str | None = None
    ):
        """Search for competitions"""
        raise NotImplementedError