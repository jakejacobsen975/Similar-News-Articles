# Similar-News-Articles

This project calculates the similarity between news articles from various sources using the Jaccard similarity equation. The articles are processed in phases, with each phase performing specific tasks to extract, process, and compare the content.

## Project Structure

- `phase_1/`: Contains scripts for the first phase of processing the articles.
  - `run.sh`: Runs the preprocessing and categorization of articles into different news sources.
  - `part-00000`: Output file containing processed articles in the format `url:::content`.

- `phase_2/`: Contains scripts for the second phase of comparing article contents.
  - `run.sh`: Runs the Jaccard similarity computation for all the articles of a respective news source.
  - `part-00000`: Output file with calculated similarity scores.

## How It Works

1. **Phase 1 (Article Processing)**: 
   - The first script processes the articles, categorizing them by their news source (e.g., KSL, CNBC, The Verge) and stores the content in a key value pairs.

2. **Phase 2 (Jaccard Similarity Calculation)**:
   - The second script computes the Jaccard similarity between pairs of articles using sets of content from each source.

3. **Final Output**:
   - The results are stored in `part-00000` file in the `/phase_2/jaccard/` directory, showing the similarity score between the articles from different sources.

## Requirements

- Python 3.x
- Hadoop (for running scripts in a distributed environment)
- Necessary Python libraries:
  - `sys`
  - `json`
  - `itertools`
  - `logging`

## Running the Project

To run the entire project, download Hadoop and find its location then replace the lines in `phase_1/run.sh` and `phase_2/run.sh` that look like this `hadoop jar /home/jake/hadoop-3.4.0/share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar \`

then to run everything run the command in the main directory 
```./run.sh```

