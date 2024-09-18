# Extractive Summarization Tool

This repository contains code for an extractive summarization tool that generates concise summaries by selecting the most important sentences from a given text. The summarization technique used is extractive summarization, which focuses on identifying and extracting relevant sentences without generating new content.

## Key Characteristics

- **TF-IDF Scoring**: The tool uses Term Frequency-Inverse Document Frequency (TF-IDF) to score sentences. TF-IDF measures the importance of a word in a document relative to other documents, helping to identify sentences that are most relevant for inclusion in the summary.
- **Sentence Selection**: The tool selects the top-scoring sentences based on their TF-IDF scores. You can adjust the number of sentences included in the summary using the `N` parameter.
- **No New Text Generation**: The summary consists entirely of existing sentences from the original text, without any modifications or additions.

## Advantages

- **Simplicity**: The extractive approach is straightforward and does not require complex language generation models.
- **Preserves Original Meaning**: The summary is derived directly from the original text, ensuring accurate conveyance of key points and information.
- **Efficiency**: Extractive summarization can be computationally efficient compared to more complex abstractive summarization techniques.

## Limitations

- **May Not Capture Overall Meaning**: The approach may occasionally miss the underlying theme or coherence of the original text.
- **Limited Creativity**: Since it does not generate new text, it cannot provide insights or interpretations beyond what is explicitly stated in the original text.
