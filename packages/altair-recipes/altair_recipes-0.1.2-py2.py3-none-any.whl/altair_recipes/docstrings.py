"""Reusable docstrings elements."""
from inspect import getfullargspec

docstrings = dict(
    data="""data: Altair Data or pandas DataFrame or csv or json file URL
    The data from which the statistical graphics is being generated""",
    column="""column: str or other column selector
    The column containing the data to be used in the graphics""",
    x="""x: str or other columns selector
    The column containing the data associated with the horizontal dimension""",
    y="""y: str or other column selector
    The column containing the data associated with the vertical dimension""",
    columns="""columns: str or list thereof or other column selector
    The column or columns to be used in the graphics""",
    group_by="""group_by: str or other column selector
    The column to be used to group the data when in long form. When group_by is
    specified columns should point to a single column""",
    return_object="""altair.Chart_area
    The graphics object""",
    mark="""mark: dictionary
    Additional arguments to pass to the mark method of Chart""",
    encoding="""encoding: dictionary
    Additional arguments to the encode method of Chart""",
    properties="""properties: dictionary
    Additional arguments to the properties method of Chart""",
    returns="""altair.Chart
    The chart described in the summary""")


def make_docstring(func, summary, additional_params={}):
    """Make docstrings from simple reusable parts.

    Parameters
    ----------
    summary : str
        The docstring summary.
    additional_params : dict
        A list of parameter docstrings. If present in the .docstrings.Docstring
        enum, will be replaced by corresponding value (default meaning for that
        argument)


    Returns
    -------
    str
        A docstring. Assign to __doc__ of desired object.

    """
    docstrings_ = docstrings.copy()
    docstrings_.update(additional_params)
    params = list(map(lambda x: docstrings_[x], getfullargspec(func).args))
    returns = docstrings['returns']
    return "\n".join([summary + ".", "\nParameters\n---------"] + [
        ".\n".join(params),
        "\nReturns\n-------",
        returns,
    ]) + "."
