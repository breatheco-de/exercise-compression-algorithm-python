# Compression Algorithm

<p align="center">
    <img height="300" src="https://github.com/breatheco-de/exercise-compression-algorithm-python/blob/master/preview.png?raw=true" />
</p>

Lets create a compression algorithm 🤯
It sounds hard but it's something achievable for almost anyone.

## 📝 Instructions

Create an algorithm that given a string, replaces its words matching the **`symbols` dictionary keys** and replaces them with their respective values on the same dictionary.

```
symbols = {
    "implementation": "🤯",
    "practicality": '🤩',
    "better": '😅',
    "Although": "🥺"
}
```

For example:

`Although, this is a great implementation of time` should become `🥺, this is a great 🤯 of time`

## Running the project

Download/clone the project and type the folloding in the command line:

```bash
python3 app.py
```

You should get a response similar to this:
```bash
✅No data lost.
document.txt has 824 size, compressed.txt has 768 size, compression of 7% in 0.0003972053527832031 seconds 
```

## 🎯 Metrics

1. Compression power: Ratio is defined as the ratio between the uncompressed size and compressed size.
2. No Data lost: If we compress and decompress document.txt the result should be the original string of content.

## 🍩🍬🍭 Feeling confident?

By adding more words to the `symbols` dict you can achieve more compression power.  

Try to re-do the algorithm to achieve a compression power above 15% with no data lost without just adding more words.
