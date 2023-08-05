# Cornell Conversational Analysis Toolkit
This toolkit contains tools to extract conversational features and analyze social phenomena in conversations.  Several large [conversational datasets](https://github.com/CornellNLP/Cornell-Conversational-Analysis-Toolkit#datasets) are included together with scripts exemplifying the use of the toolkit on these datasets.

The toolkit currently implements features for:

- [Linguistic coordination](https://github.com/CornellNLP/Cornell-Conversational-Analysis-Toolkit/blob/master/Coordination_README.md), a measure of linguistic influence (and relative power) between individuals or groups based on their use of function words (see the [Echoes of Power](https://www.cs.cornell.edu/~cristian/Echoes_of_power.html) paper). Example script [exploring the balance of power in the US Supreme Court](https://github.com/CornellNLP/Cornell-Conversational-Analysis-Toolkit/blob/master/examples/coordination/examples.ipynb).

- [Politeness strategies](https://github.com/CornellNLP/Cornell-Conversational-Analysis-Toolkit/blob/master/Politeness_README.md), a set of lexical and parse-based features correlating with politeness and impoliteness (see the [A computational approach to politeness](https://www.cs.cornell.edu/~cristian/Politeness.html) paper).  Example script for [understanding the (mis)use of politeness strategies in conversations gone awry on Wikipedia](https://github.com/CornellNLP/Cornell-Conversational-Analysis-Toolkit/blob/master/examples/conversationsGoneAwry/Conversations%20Gone%20Awry%20Prediction.ipynb).

- [Question typology](https://github.com/CornellNLP/Cornell-Conversational-Analysis-Toolkit/blob/master/QuestionTypology_README.md), an unsupervised method for extracting surface motifs that recur in questions, and for grouping them according to their latent rhetorical role (see the [Asking too much](http://www.cs.cornell.edu/~cristian/Asking_too_much.html) paper).  Example scripts for extracting common question types in the [UK parliament](https://github.com/CornellNLP/Cornell-Conversational-Analysis-Toolkit/blob/master/examples/questionTypology/parliament_question_typology.py), on [Wikipedia edit pages](https://github.com/CornellNLP/Cornell-Conversational-Analysis-Toolkit/blob/master/examples/questionTypology/wiki_question_typology.py), and in [sport interviews](https://github.com/CornellNLP/Cornell-Conversational-Analysis-Toolkit/blob/master/examples/questionTypology/tennis_question_typology.py).

- [Conversational prompts](https://github.com/CornellNLP/Cornell-Conversational-Analysis-Toolkit/blob/master/QuestionTypology_README.md), an unsupervised method for extracting types of conversational prompts (see the [Conversations gone awry](http://www.cs.cornell.edu/~cristian/Conversations_gone_awry.html) paper).  Example script for [understanding the use of conversational prompts in conversations gone awry on Wikipedia](https://github.com/CornellNLP/Cornell-Conversational-Analysis-Toolkit/blob/master/examples/conversationsGoneAwry/Conversations%20Gone%20Awry%20Prediction.ipynb).

- Coming soon: Basic message and turn features, currently available here [Constructive conversations](https://github.com/CornellNLP/Cornell-Conversational-Analysis-Toolkit/tree/constructive/cornellversation/constructive)

## Datasets
These datasets are included for ready use with the toolkit:

- [Conversations Gone Awry Corpus](https://github.com/CornellNLP/Cornell-Conversational-Analysis-Toolkit/datasets/conversations-gone-awry-corpus/awry.README.v1.00.txt): a collection of conversations from Wikipedia talk pages that derail into personal attacks (1,270 conversations, 6,963 comments)

- [Tennis Corpus](http://www.cs.cornell.edu/~liye/tennis_README.txt): transcripts for tennis singles post-match press conferences for major tournaments between 2007 to 2015 (6467 post-match press conferences)

- [Wikipedia Talk Pages Corpus](http://www.cs.cornell.edu/~cristian/Echoes_of_power_files/wikipedia.talkpages.README.v1.01.txt): collection of conversations from Wikipedia editors' talk pages

- [Supreme Court Corpus](http://www.cs.cornell.edu/~cristian/Echoes_of_power_files/supreme.README.v1.01.txt): collection of conversations from the U.S. Supreme Court Oral Arguments

- [Parliament Corpus](http://www.cs.cornell.edu/~cristian/Asking_too_much_files/paper-questions.pdf): parliamentary question periods from May 1979 to December 2016 (216,894 question-answer pairs)

## Usage

### Installation
This toolkit requires Python 3.

1. Download the toolkit: `pip3 install convokit`
2. Download Spacy's English model: `python3 -m spacy download en`

Alternatively, visit our [Github Page](https://github.com/CornellNLP/Cornell-Conversational-Analysis-Toolkit) to install from source.

### Use

Use `import convokit` to import it into your project.

Detailed installation and usage examples are provided on the specific pages dedicated to each function of this toolkit.

## Documentation
Documentation is hosted [here](http://zissou.infosci.cornell.edu/socialkit/documentation/).

The documentation is built with [Sphinx](http://www.sphinx-doc.org/en/1.5.1/) (`pip3 install sphinx`). To build it yourself, navigate to `doc/` and run `make html`. 

## Acknowledgements

Andrew Wang ([azw7@cornell.edu](mailto:azw7@cornell.edu))  wrote the Coordination code and the respective example script, wrote the helper functions and designed the structure of the toolkit.

Ishaan Jhaveri ([iaj8@cornell.edu](mailto:iaj8@cornell.edu)) refactored the Question Typology code and wrote the respective example scripts.

Jonathan Chang ([jpc362@cornell.edu](mailto:jpc362@cornell.edu)) wrote the example script for Conversations Gone Awry.
