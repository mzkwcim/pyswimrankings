import requsts

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
        """Search for athletes"""
        raise NotImplementedError

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