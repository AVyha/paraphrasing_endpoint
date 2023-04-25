# Paraphrasing endpoint

## Description
This endpoint rephrases your current sentence by switching the NP (noun phrase) with each other without losing meaning

## Installation
```
git copy https://github.com/AVyha/paraphrasing_endpoint.git
python -m venv venv
venv\Scripts\activate
pip install -m requirements.txt
```

## How to use
### How to run without docker
1. Run in terminal `python main.py`


### How to run with docker
1. Run in terminal `docker build . -t [container_name]`
2. Run in terminal `docker run -p 8000:8000 [container_name]`


### After starting the app
1. Open in browser `localhost:8000/docs`
2. Open "/paraphrase" endpoint
3. Place your syntax tree in the "tree" variable

For example, you can use this syntax tree:

```
(S(NP(NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter))(, ,)(CC or)(NP (NNP Barri) (NNP Gòtic)))(, ,)(VP(VBZ has)(NP(NP (JJ narrow) (JJ medieval) (NNS streets))(VP(VBN filled)(PP(IN with)(NP(NP (JJ trendy) (NNS bars))(, ,)(NP (NNS clubs))(CC and)(NP (JJ Catalan) (NNS restaurants))))))))
```

Response example
![response.png](response.png)

