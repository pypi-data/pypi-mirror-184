from typing import Tuple

from mercuryclient.types.okyc_verification.enums import RequestTypes


class OkycVerificationMixin:
    """
    Mixin for verifying Okyc
    """

    def request_verify_okyc(
        self,
        request_type: RequestTypes,
        provider: str,
        profile: str,
        **kwargs,
    ) -> str:
        api = "api/v1/okyc_verification/"

        try:
            RequestTypes(request_type)
        except ValueError:
            raise Exception(f"{request_type} is not a valid request_type")

        data = {
            "provider": provider,
            "profile": profile,
            "request_type": request_type,
        }

        if request_type == RequestTypes.OTP_VERIFY.value:
            otp = kwargs.get("otp")
            request_id = kwargs.get("request_id")
            if not otp:
                raise Exception("otp is required to verify Okyc Otp")
            elif not request_id:
                raise Exception("request_id is required to verify Okyc Otp")
            else:
                data["otp"] = otp
                data["request_id"] = request_id

        if request_type == RequestTypes.OTP_REQUEST.value:
            if not kwargs.get("id_number"):
                raise Exception("id_number is required to generate Okyc Otp")
            data["id_number"] = kwargs.get("id_number")

        request_id, r = self._post_json_http_request(
            api, data=data, send_request_id=True, add_bearer_token=True
        )

        if r.status_code == 201:
            return request_id

        try:
            response_json = r.json()
        except Exception:
            response_json = {}
        raise Exception(
            "Error while sending Okyc verification request. Status: {}, Response is {}".format(
                r.status_code, response_json
            )
        )

    def get_verify_okyc_result(self, request_id: str) -> Tuple[str, dict]:
        api = "api/v1/okyc_verification/"

        request_id, r = self._get_json_http_request(
            api,
            headers={"X-Mercury-Request-Id": request_id},
            send_request_id=False,
            add_bearer_token=True,
        )

        if r.status_code == 200:
            result = r.json()
            return request_id, result

        try:
            response_json = r.json()
        except Exception:
            response_json = {}
        raise Exception(
            "Error getting Okyc Verification result. Status: {}, Response is {}".format(
                r.status_code, response_json
            )
        )
