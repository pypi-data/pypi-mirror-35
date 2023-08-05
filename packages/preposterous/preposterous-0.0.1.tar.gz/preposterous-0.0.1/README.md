# Pre/Posterous
Estimate the impact of an intervention, with simplicity and humility

##Installation

You can install with `pip install preposterous`

If you want to install from source, then clone this repository and run `python setup.py install` from the project root.

**Pre/Posterous is under active development** and the current release can be considered a 'proof of concept'. 
The largest restriction is that it only imports data from the [Reporter app](http://www.reporter-app.com/), 
which is my current default recommendation for anyone who is trying to track something.

## Use cases
### Quantified Self data
The primary use case is for quantified self, where you have periodic measurements of the target metric (weight, categorical sleep quality, ect) and potential interventions (medications, diet shifts, ect). This library can organize these into 'natural experiments' that point the way towards a causal relationship

*Warning* Python is pretty great, but nothing can replace a well powered [Double Blind Randomized Controlled Trial](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3196997/) for establishing causality. That said, many (most?) situations do not lend themselves to RCTs, and yet we're still forced to make decisions. That's where tools like this, used with an appreciation for non-binary modes of belief, can be helpful.

## Example
```
import preposterous.preposterous as ppl
pdf = ppl.PrePostDF()
pdf.add_outcome(filename='data/sample_reporter_output.csv')
pdf.add_intervention(filename='data/sample_reporter_output.csv')
print(pdf.basic_info())
pdf.generate_confusion_matrix(intervention='Exercise')
```
