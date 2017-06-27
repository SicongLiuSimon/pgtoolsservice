# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import pgsqltoolsservice.utils as utils
from pgsqltoolsservice.workspace.contracts import Range


class TextEdit:
    """
    A textual edit applicable to a text document.
    """
    @classmethod
    def from_data(cls, text_range: Range, new_text: str):
        obj = cls()
        obj.range = text_range
        obj.new_text = new_text
        return obj

    @classmethod
    def from_dict(cls, dictionary: dict):
        return utils.serialization.convert_from_dict(cls, dictionary, range=Range)

    def __init__(self):
        self.range: Range = None
        self.new_text: str = None
