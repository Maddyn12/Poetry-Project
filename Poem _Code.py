import random

from textblob import TextBlob
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

with open("/content/drive/MyDrive/College /Creative Coding/THE ATTRACTION OF LEVITATION BY H. G. PAINE.txt") as f:
  bird_text = f.read()

bird_blob = TextBlob(bird_text)

poem_text = """
"Oh, dear!" said little Johnny Frost,
"Sleds are such different things!
When down the hill you swiftly coast
You'd think that they had wings;

"But when uphill you slowly climb,
And have to drag your sled,
It feels so heavy that you'd think
'Twas really made of lead.

"And all because an Englishman,
Sir Isaac Newton named,
Invented gravitation, and
Became unduly famed;

"While if he had reversed his law,
So folks uphill could coast,
It seems to me he would have had
A better claim to boast.

"Then coasting would all pleasure be;
To slide up would be slick!
And dragging sleds downhill would be
An awful easy trick!"
"""

poem_blob = TextBlob(poem_text)

poem_blob.tags

cordination_conjuntion = []
cardinal_digit = []
determiner = []
existential = []
foriegn_word = []
prep_subcon = []
adjective = []
comp_adjective = []
supp_adjective = []
list_marker = []
modal = []
singular_noun = ['cat', 'sock', 'ship', 'hero', 'monkey', 'baby', 'match']
plural_noun = []
proper_noun_singular = []
proper_noun_plural = []
predeterminer = []
possesive_ending = []
personal_prounoun = []
possessive_pronoun = []
adverb = []
comp_adverb = []
supp_adverb = []
particle = []
to = []
interjection = []
verb = ['run','fall','act',	'answer',	'approve',	'arrange','break','build','buy','coach','color','cough','create','complete',
'cry',	'dance','describe',	'draw','drink','eat','enter','exit','imitate','invent','jump',
'laugh','lie','listen','paint','plan','play','read','replace','run','scream','see','shop',
'shout','sing','skip','sleep','sneeze','solve','study','teach','touch','turn','walk','win',
'write','whistle','yank','zip']
past_tense_verb = []
present_part_verb = []
past_part_verb = []
sing_present_verb = []
thirdperson_singular_present_verb = []
wh_determiner = []
wh_pronoun = []
wh_possesive_pronoun = []
wh_adverb = []
punctuation = ['.','?','!']

for word,pos in bird_blob.tags:
  if(pos == 'CC'):
    cordination_conjuntion.append(word)

  if(pos == 'CD'):
    cardinal_digit.append(word)
  
  if(pos == 'DT'):
    determiner.append(word)

  if(pos == 'EX'):
    existential.append(word)

  if(pos == 'FW'):
    foriegn_word.append(word)

  if(pos == 'IN'):
    prep_subcon.append(word)

  if(pos == 'JJ'):
    adjective.append(word)

  if(pos == 'JJR'):
    comp_adjective.append(word)

  if(pos == 'JJS'):
    supp_adjective.append(word)

  if(pos == 'LS'):
    list_marker.append(word)

  if(pos == 'MD'):
    modal.append(word)

  if(pos == 'NN'):
    singular_noun.append(word)

  if(pos == 'NNS'):
    plural_noun.append(word)

  if(pos == 'NNP'):
    proper_noun_singular.append(word)

  if(pos == 'NNPS'):
    proper_noun_plural.append(word)

  if(pos == 'PDT'):
    predeterminer.append(word)

  if(pos == 'POS'):
    possesive_ending.append(word)

  if(pos == 'PRP'):
    personal_prounoun.append(word)

  if(pos == 'PRP$'):
    possessive_pronoun.append(word)

  if(pos == 'RB'):
    adverb.append(word)

  if(pos == 'RBR'):
    comp_adverb.append(word)

  if(pos == 'RBS'):
    supp_adverb.append(word)

  if(pos == 'RP'):
    particle.append(word)

  if(pos == 'TO'):
    to.append(word)

  if(pos == 'UH'):
    interjection.append(word)

  if(pos == 'VB'):
    verb.append(word)

  if(pos == 'VBD'):
    past_tense_verb.append(word)

  if(pos == 'VBG'):
    present_part_verb.append(word)

  if(pos == 'VBN'):
    past_part_verb.append(word)

  if(pos == 'VBP'):
    sing_present_verb.append(word)

  if(pos == 'VBZ'):
    thirdperson_singular_present_verb.append(word)

  if(pos == 'WDT'):
    wh_determiner.append(word)

  if(pos == 'WP'):
    wh_pronoun.append(word)

  if(pos == 'WP$'):
    wh_possesive_pronoun.append(word)

  if(pos == 'WRB'):
    wh_adverb.append(word)

  if(pos == 'PUNKT'):
    punctuation.append(word)

random.choice(proper_noun_singular)

print('"Oh, dear' + random.choice(punctuation) + " said " + random.choice(adjective) + ' Johnny Frost,')
print('"Sleds are such different things'+ random.choice(punctuation))
print('When down the ' + random.choice(singular_noun) + ' you swiftly coast')
print("You'd think that they had wings;")
print('')
print('"But when uphill you ' + random.choice(adverb) +  ' climb,')
print('And have to drag your sled,')
print("It feels so " + random.choice(adjective) +  " that you'd think")
print("'Twas really made of lead"+ random.choice(punctuation))
print('')
print('"And all because an ' + random.choice(proper_noun_singular) + ',')
print('Sir Isaac Newton named,')
print('Invented gravitation, and')
print('Became unduly ' + random.choice(past_tense_verb) + ';')
print('')
print('"While if he had reversed his law,')
print('So folks uphill could ' + random.choice(verb) + ',')
print('It seems to me he would have had')
print('A better claim to ' + random.choice(verb) + '.')
print('')
print('"Then coasting would all ' + random.choice(singular_noun) + ' be;')
print('To slide up would be slick'+ random.choice(punctuation))
print('And dragging sleds ' + random.choice(singular_noun) + ' would be')
print('An awful easy trick'+ random.choice(punctuation)+'"' )
