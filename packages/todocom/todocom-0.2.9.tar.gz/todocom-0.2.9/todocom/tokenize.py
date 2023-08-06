import re
from todocom.comments import Token
from todocom.utils import specs


def tokenize(code, file, **kwargs):
    """
    Followed instructions in 're' module documentation and
    modified the code to include TODO regex.

    Types of TODOs:
        1. single_line      ---> should work with most files
        2. multiline        ---> specifically designed for python docstrings
        3. urgent           ---> should work with most files
        4. urgent_multiline ---> specifically designed for python docstrings
        5. soon             ---> should work with most files
        6. soon_multiline   ---> specifically designed for python docstrings
        ** newline          ---> required for counting rows!
    """

    if kwargs["urgent"]:
        tok_regex = specs("urgent")

    elif kwargs["soon"]:
        tok_regex = specs("soon")

    elif kwargs["assigned"]:
        tok_regex = specs("assign", assigned = kwargs["assigned"])

    else:
        tok_regex = specs()

    assign_to, et_index = None, -1
    line_num = 1
    multi_line_num = None
    end_last_token = -1

    # iteration over tokens found in code
    for mo in re.finditer(tok_regex, code):

        # Ensure last token was multi-line
        if multi_line_num:

            # Must add the number of rows in the comment
            # Or else the next tokens will be shifted!
            line_num += multi_line_num
            multi_line_num = None

        # Type of token (TODO) found
        kind = mo.lastgroup

        # Ensure comment is an actual TODO
        if kind != "newline":

            # Store TODO comment
            value = mo.group()

            # Clean comment and find its starting index
            value = re.sub("\n", " ", value.strip())
            value = re.sub(" +", " ", value.strip())

            index = re.search(":", value).span()[0]

            if kind == "assign":
                et_index = re.search("@", value).span()[0]

            multi_line_num = 1

            # Ensure ":" was found
            if index:
                index = re.search(":", value).span()[0]

            # Ensure TODO is multiline
            if 'multiline' in kind:

                # Calculate number of lines to add
                multi_line_num = len(re.findall("\n", mo.group())) + 1

                # Store the comment without the trailing double quotes (""")
                value = value[index + 1: -3].strip()

            else:
                if kind != "assign":
                    assign_to = None
                else:
                    assign_to = value[et_index + 1: index].strip()

                # Comment is single line --> store it all
                value = value[index + 1:].strip()

            # Store the last char in the token
            # Required to prevent "\n" from being considered twice
            end_last_token = mo.end()

            yield Token(kind, file, value, line_num, assign_to)

        # Ensure token is a newline
        if kind == 'newline':

            # Ensure newline is not used twice
            if mo.start() != end_last_token:
                line_num += 1
            else:
                end_last_token = -1
