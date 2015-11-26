import sys
sys.path.append('../')

from feature_computation.Sentence import ReadSentencesFromTextFileSimple

A = ['place-on-map',
     'move',
     'change-harvest-loc',
     'change-harvest-tool',
     'harvest',
     'harvest-loose-tool',
     'get-harvest-wood',
     'get-harvest-stone',
     'get-harvest-coal',
     'get-harvest-ironore',
     'get-harvest-seeds',
     'get-harvest-wheat',
     'get-harvest-sandstone',
     'get-harvest-sand',
     'get-harvest-clay',
     'get-harvest-bone',
     'get-harvest-brown-mushroom',
     'get-harvest-red-mushroom',
     'get-harvest-sugarcane',
     'get-harvest-string',
     'get-harvest-egg',
     'get-harvest-fish',
     'get-harvest-wool',
     'get-harvest-milk',
     'grow-tallgrass',
     'make-farmland',
     'grow-wheatgrass',
     'place',
     'craft-wood-plank',
     'craft-wood-stick',
     'craft-torch',
     'craft-furnace',
     'craft-wood-pickaxe',
     'craft-wood-axe',
     'craft-wood-shovel',
     'craft-wood-hoe',
     'craft-sandstone',
     'craft-clayblock',
     'craft-brick',
     'make-sugar',
     'make-paper',
     'make-wool',
     'craft-bed',
     'craft-chest',
     'craft-wood-door',
     'craft-iron-door',
     'craft-ladder',
     'craft-fence',
     'craft-stone-brick',
     'craft-ironbar',
     'craft-glasspane',
     'make-bread',
     'craft-shears',
     'craft-bowl',
     'craft-bucket',
     'craft-fishingrod',
     'craft-bonemeal',
     'craft-wood-stairs',
     'craft-stone-stairs',
     'craft-brick-stairs',
     'craft-stonebrick-stairs',
     'make-mushroomstew-1',
     'make-mushroomstew-2',
     'furnace-cook-fish',
     'furnace-fire-brick',
     'furnace-make-charcoal',
     'furnace-smelt-iron',
     'furnace-make-glass']


T = ['ironbar',
     'seeds',
     'brown-mushroom',
     'sand',
     'bone',
     'fish',
     'bucket',
     'wood-pickaxe',
     'sugar',
     'string',
     'egg',
     'plank',
     'clay',
     'iron',
     'wood-axe',
     'coal',
     'bed',
     'glasspane',
     'brick',
     'wood-stairs',
     'iron-door',
     'shears',
     'bread',
     'paper',
     'ladder',
     'wood-shovel',
     'cookedfish',
     'wood-door',
     'glass',
     'stick',
     'claybrick',
     'cut-sugarcane',
     'sandstone',
     'chest',
     'stonebrick-stairs',
     'fishingrod',
     'stonebrick',
     'fornace-fuel',
     'red-mushroom',
     'furnace',
     'wheat',
     'ironore',
     'stone-stairs',
     'wool',
     'hand',
     'wood',
     'bowl',
     'milk',
     'brick-stairs',
     'torch',
     'mushroomstew',
     'stone',
     'bonemeal',
     'fence',
     'wood-hoe',
     'clayblock']

P = ['player-at',
     'thing-at-map',
     'placed-thing-at-map',
     'resource-at-craft',
     'craft-empty',
     'connect',
     'crafting']


def question_t(question):
    t = question
    return []


def question_pt(question):
    question.split(" ")
    p = question[0]
    t = question[1]
    return []


def question_rpc(question_type, question):
    if question_type == 1:
        return question_t(question)
    elif question_type == 2:
        return question_pt(question)

if __name__ == '__main__':
    sSentenceFile = '../../data/minecraft_text.raw'
    lSentences = ReadSentencesFromTextFileSimple(sSentenceFile)
    print [sentence.lWords for sentence in lSentences]
