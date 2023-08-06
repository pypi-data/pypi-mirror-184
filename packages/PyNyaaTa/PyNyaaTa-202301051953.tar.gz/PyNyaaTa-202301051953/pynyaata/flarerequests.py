from io import BytesIO
from urllib import parse
from requests import Response, Session, post
from .config import CLOUDPROXY_ENDPOINT


class FlareRequests(Session):
    def request(self, method, url, params=None, data=None, **kwargs):
        if not CLOUDPROXY_ENDPOINT:
            return super().request(method, url, params, data, **kwargs)

        if params:
            url += "&" if len(url.split("?")) > 1 else "?"
            url = f"{url}{parse.urlencode(params)}"

        post_data = {
            "cmd": f"request.{method.lower()}",
            "url": url,
        }

        if data:
            post_data["postData"] = parse.urlencode(data)

        response = post(
            CLOUDPROXY_ENDPOINT,
            json=post_data,
        )

        solution = response.json()

        if "solution" in solution:
            encoding = None
            headers = solution["solution"]["headers"]
            if "content-type" in headers:
                content_type = headers["content-type"].split(";")
                if len(content_type) > 1:
                    charset = content_type[1].split("=")
                    if len(charset) > 1:
                        encoding = charset[1]

            resolved = Response()

            resolved.status_code = solution["solution"]["status"]
            resolved.headers = headers
            resolved.raw = BytesIO(solution["solution"]["response"].encode())
            resolved.url = url
            resolved.encoding = encoding
            resolved.reason = solution["status"]
            resolved.cookies = solution["solution"]["cookies"]

            return resolved
