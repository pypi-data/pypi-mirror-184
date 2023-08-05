from typing import Optional

from pip_fluigio.__fluig_services_base.interfaces.workflow_engine import (
    Attachments, Colleagues, Item)
from pip_fluigio.utils.commomns import convert_to_base64


class WorkflowProperties:
    @classmethod
    def set_colleagues(cls, colleagues: list[str]):

        list_colleagues = []
        for colleague in colleagues:
            list_colleagues.append(Colleagues(item=colleague))

        return list_colleagues

    @classmethod
    def set_items(cls, data: dict):
        list_items = []
        for key, value in data.items():
            list_items.append(Item(key=key, value=value))

        return list_items

    @classmethod
    def set_attachments(cls, file_name: str, file_size: str, file_content: bytearray):

        return Attachments(
            attach="true",
            editing="true",
            file_name=file_name,
            file_size=file_size,
            file_content=convert_to_base64(obj=file_content),
            principal="true",
        )
