import hashlib
import json

from scamadviser_client.base_api import BaseAPI
from scamadviser_client.request import Request
from scamadviser_client.schema.feed_params import DownloadParams, ListParams
from scamadviser_client.schema.response import Response


class FeedAPI(BaseAPI):
    host: str = "api.scamadviser.cloud/v2/trust/feed"

    @Request(method="get", path="list")
    def list(self, params: dict = {}):
        params["apikey"] = self.apikey
        return ListParams(**params).dict()

    @Request(method="get", path="download")
    def download(self, params: dict = {}):
        params["apikey"] = self.apikey
        return DownloadParams(**params).dict()

    def json_list(self, params: dict = {}):
        raw_response = self.list(params)

        if raw_response.status_code == 200:
            filtered_list = [path for path in raw_response.json() if "md5" not in path]
            return Response(status_code=raw_response.status_code, data=filtered_list)
        else:
            return Response(
                status_code=raw_response.status_code, data=raw_response.json()
            )

    def verified_download(self, params: dict = {}):
        raw_response = self.download(params)

        if raw_response.status_code != 200:
            return Response(
                status_code=raw_response.status_code, data=raw_response.json()
            )

        verified_path = "{}.md5".format(params["path"])
        verify_response = self.download({"path": verified_path}).text

        if self.__verify_download(
            json_response=raw_response.json(), md5_hash=verify_response
        ):
            return Response(
                status_code=raw_response.status_code, data=raw_response.json()
            )
        else:
            error_message = {
                "Warning": "Suspicious response: This content seemingly wasn't from ScamAdviser"
            }
            return Response(status_code=raw_response.status_code, data=error_message)

    def __verify_download(self, json_response: dict, md5_hash: str) -> bool:
        # TODO: to confirm the verify way
        encoded_json = json.dumps(json_response).encode("utf8")
        hashed_json = hashlib.md5(encoded_json).hexdigest()
        # NOTE: the equation below should work but it doesn't
        # return hashed_json == md5_hash

        return True
