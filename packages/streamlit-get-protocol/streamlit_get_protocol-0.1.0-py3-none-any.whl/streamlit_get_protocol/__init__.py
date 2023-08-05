from pathlib import Path
from typing import Optional

import streamlit as st
import streamlit.components.v1 as components

# Tell streamlit that there is a component called camera_input_live,
# and that the code to display that component is in the "frontend" folder
frontend_dir = (Path(__file__).parent / "frontend").absolute()
_component_func = components.declare_component(
    "get_protocol", path=str(frontend_dir)
)


def get_protocol(key: Optional[str] = None) -> Optional[str]:
    """
    Add a descriptive docstring
    """
    data: Optional[str] = _component_func(key=key)

    if data is None:
        return None
    return data


def main():
    st.write("## Example")
    protocol = get_protocol()
    if protocol is not None:
        st.write(protocol)

if __name__ == "__main__":
    main()
