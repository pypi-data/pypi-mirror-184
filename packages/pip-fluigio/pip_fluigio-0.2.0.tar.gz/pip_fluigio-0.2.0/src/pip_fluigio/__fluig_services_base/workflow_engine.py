from abc import ABC


class WorkflowEngineProvider(ABC):
    def __init__(self):
        pass

    def save_and_send_task(self) -> None:

        """
        Decriptions: Abstrat method move task and save attachments with fluig service WSDL

        Returns:

        Args:
            company_id: str
            username: str
            password: str
            attachments: List of ItemAttachments
            colleague_id: List of Colleagues
            items: List of Item
            choosed_state: Optional[int]
            comments: Optional[str]
            user_id: Optional[str]
            complete_task Optional[str]
            process_instance_id: int
            appoitments: Optional[str]
            manager_mode: Optional[str]
            thread_sequence: Optional[str]

        Raises:

        """

        return
