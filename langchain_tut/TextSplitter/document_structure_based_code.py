from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

# Using normal length based text splitter will fail here.
text = r"""
function split(text):

    pieces = text.split(separator)

    chunks = []
    current_chunk = ""

    for piece in pieces:

        if length(current_chunk + piece) <= chunk_size:
            current_chunk += piece

        else:
            chunks.append(current_chunk)

            current_chunk = piece

    chunks.append(current_chunk)

    return chunks

function recursive_split(text):

    separators = [
        "\n\n",   # paragraph
        "\n",     # line
        " ",      # word
        ""        # character
    ]

    for separator in separators:

        pieces = split(text, separator)

        if pieces are small enough:
            return pieces

    return pieces
"""
# Document Structure Based text splitter is used to split document that don't just have plain texts but also some different texts strucutre.
# It includes code, markdown etc.
# NOTE: You can also build custom hierarchy to split text using "separators"
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=380, chunk_overlap=0
)

result = splitter.split_text(text)

print(type(result), len(result))

print(result[1])
