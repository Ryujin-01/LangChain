from langchain_text_splitters import MarkdownHeaderTextSplitter

# Using normal length based text splitter will fail here.
text = r"""
# The Ocean

The ocean covers a large portion of Earth's surface and contains an incredible variety of life.

## Ocean Zones

The ocean is divided into several zones based on depth and the amount of sunlight that reaches them.

### Sunlight Zone

The sunlight zone is the uppermost layer of the ocean. Sunlight allows algae and other organisms to perform photosynthesis.

Many fish, sea turtles, dolphins, and other marine animals live in this region.

### Twilight Zone

The twilight zone lies below the sunlight zone. Only a small amount of sunlight reaches this region.

Animals living here often have adaptations such as large eyes and bioluminescence.

### Midnight Zone

The midnight zone receives essentially no sunlight. Temperatures are low and the pressure is extremely high.

Many organisms in this zone rely on organic material falling from the layers above.

## Marine Ecosystems

The ocean contains many different ecosystems, each supporting unique communities of organisms.

### Coral Reefs

Coral reefs are among the most diverse ecosystems on Earth.

They provide shelter and food for thousands of marine species. However, coral reefs are vulnerable to rising ocean temperatures and pollution.

### Deep Sea

The deep sea contains organisms that have evolved to survive without sunlight.

Some species produce their own light through a process called bioluminescence.

"""

# You can also split markdowns using the "from_language" function, but this one is more accurate.

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)

result = splitter.split_text(text)

print(type(result), len(result))

print(result)
