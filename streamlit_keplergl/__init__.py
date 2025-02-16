# Load kepler.gl with an empty map

import streamlit.components.v1 as components
from keplergl import KeplerGl


def keplergl_static(
    fig: KeplerGl, height: int = 400, scrolling=False
) -> components.html:
    """
    Renders `keplergl.KeplerGl` map figure in a Streamlit app. This method is
    a static Streamlit Component, meaning, no information is passed back from
    KeplerGL on browser interaction.

    Args:
        fig: `keplergl.KeplerGl` map figure.
        height: Height of result. If `height` is set on the keplergl.KeplerGl` object,
                that value supersedes the values set with the keyword arguments of this
                function.

    Example:
        ```python
            >>> map_1 = KeplerGl(height=400)
            >>> keplergl_static(map_1)
        ```
    """
    try:
        html = fig._repr_html_()
    except AttributeError:
        raise TypeError("fig argument has to be a keplergl map object of type keplergl.KeplerGl!")

    return components.html(
        html, height=(fig.height or height) + 10, scrolling=scrolling
    )
