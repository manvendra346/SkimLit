# SkimLit
Many research papers have an abstract which gives us a basic understanding of what the research paper is about. But it does not define what part of the abstract relates to what part of the paper is objective, result, methods, or conclusions.

 This problem can be solved by using skimlit which can divide and label the text of the abstract with appropriate labels about what part of the paper this text belongs to.
 
This project replicates  the model which powers the PubMed 200k paper to classify different sequences in PubMed medical abstracts (which can help researchers read through medical abstracts faster) by Frank Dernoncourt, Ji Young Lee and is trained on over 200k medical research paper abstracts and can successfully label the part of abstracts to get an easy understanding of the whole paper.

This model is trained on more than 200k medical abstracts and can separate the abstract into these 5 different classes ['BACKGROUND', 'CONCLUSIONS', 'METHODS', 'OBJECTIVE', 'RESULTS'] with 90% accuracy, which makes the reading of the abstract easier.

The model shown in Python notebook is only trained on 20k which was a test model but the model used in the app is the full model trained on 200k abstracts.
