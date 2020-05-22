import os
import requests as r
from requests.auth import HTTPBasicAuth


class TeamCityCompleter:

    IGNORE_LIST = ["webUrl", "versionMinor", "versionMajor", "version", "startTime", "internalId", "currentTime", "buildNumber", "buildDate"]

    def __init__(self, url, username, password):
        self.url = url
        self.auth = HTTPBasicAuth(username, password)
        self._headers = {"accept": "application/json"}
        self._cache = {}

    def __call__(self, ctx, args, incomplete):
        if not args:
            return self._first_completer(ctx, args, incomplete)
        if len(args) == 1:
            if args[0] == "projects":
                return self._projects_completer(ctx, args, incomplete)

    def _first_completer(self, ctx, args, incomplete):
        return [k for k in self._get("/app/rest/server").keys() if incomplete in k and k not in self.IGNORE_LIST]

    def _projects_completer(self, ctx, args, incomplete):
        return [
            (v["name"], v.get("description", "No description"))
            for v in self._get("/app/rest/projects")["project"]
            if incomplete in v["name"]
        ]

    def _get(self, path) -> dict:
        return self._cache.get(
            path,
            r.get(
                f"{self.url}{path}",
                headers=self._headers,
                auth=self.auth
            ).json()
        )
