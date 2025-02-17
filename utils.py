from typing import Union, Dict, List

JSONType = Union[Dict[str, "JSONType"], List["JSONType"], str, int, float, bool, None]
