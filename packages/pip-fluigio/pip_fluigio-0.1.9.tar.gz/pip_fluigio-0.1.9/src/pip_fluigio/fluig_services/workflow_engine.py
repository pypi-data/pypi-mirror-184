from typing import List, Optional

from pip_fluigio.__fluig_services_base.interfaces.workflow_engine import (
    Attachments, Colleagues, Item)
from pip_fluigio.__fluig_services_base.workflow_engine import \
    WorkflowEngineProvider
from pip_fluigio.fluig_services.infraestruture.server import ClientFluig
from pip_fluigio.utils.logger import Logger


class WorflowEngine(WorkflowEngineProvider):
    def __init__(self, wsdl_url: str, client: Optional[ClientFluig] = None):
        self._client = client or ClientFluig(wsdl_url=wsdl_url)
        self._logger = Logger()

    def save_and_send_task(
        self,
        *,
        company_id: str,
        user_name: str,
        password: str,
        attachments: List[Attachments],
        colleague_ids: List[Colleagues],
        items: list[Item],
        choosed_state: int,
        comments: str,
        user_id: str,
        complete_task: str,
        process_instance_id: str,
        appoitments: str,
        manager_mode: str,
        thread_sequence: str,
    ) -> None:

        try:
            self._logger.attribute.info(f"Start request save and send task")

            response = self._client.soap_intance.service.saveAndSendTaskClassic(
                user_name,
                password,
                company_id,
                process_instance_id,
                choosed_state,
                [colleague for colleague in colleague_ids],
                comments,
                user_id,
                complete_task,
                [attachment for attachment in attachments],
                [item for item in items],
                appoitments,
                manager_mode,
                thread_sequence,
            )

            return response

        except Exception as error:
            self._logger.attribute.error(error)

        return
