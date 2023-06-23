from pomegranate import *
Graduate = DiscreteDistribution({'graduated':0.9, 'not-graduated':0.1})
#graduated probability is 0.9
#offer from company 1 is 0.5 if graduated and 0.05 if not graduated
Offer1 = ConditionalProbabilityTable([
['graduated', 'positive', 0.5],
['graduated', 'negative', 0.5],
['not-graduated', 'positive', 0.05],
['not-graduated', 'negative', 0.95]], [Graduate])
#offer from company 2 is 0.75 if graduated and 0.25 if not graduated
Offer2 = ConditionalProbabilityTable([
['graduated', 'positive', 0.75],
['graduated', 'negative', 0.25],
['not-graduated', 'positive', 0.25],
['not-graduated', 'negative', 0.75]], [Graduate])
#make states
s_graduate = State(Graduate, 'graduated')
s_offer_1 = State(Offer1, 'offer_1')
s_offer_2 = State(Offer2, 'offer_2')
model = BayesianNetwork('graduation')
model.add_states(s_graduate, s_offer_1, s_offer_2)
model.add_transition(s_graduate, s_offer_1) #gradute -> offer1
model.add_transition(s_graduate, s_offer_2) #graduate -> offer2
model.bake() # finalize the topology of the model
# predict_proba(Given factors)
#Popquiz
print('Popquiz:')
print ('The number of nodes:', model.node_count())
print ('The number of elges:', model.edge_count())
#a P(offer 2 | graduated and not offer 1)
print (model.predict_proba({'graduated':'graduated', 'offer_1':'negative'})[2].parameters)
#b P(graduated | offer 1 and offer 2)
print (model.predict_proba({'offer_2':'positive', 'offer_1':'positive'})[0].parameters)
#c P(graduated | not offer 1 and offer 2)
print (model.predict_proba({'offer_2':'positive', 'offer_1':'negative'})[0].parameters)
#d P(graudated | not offer 1 and not offer 2)
print (model.predict_proba({'offer_2':'negative', 'offer_1':'negative'})[0].parameters)
#e P(offer 2 | offer 1)
print (model.predict_proba({'offer_1':'positive'})[2].parameters)
#example 3
Sunny = DiscreteDistribution({'sunny':0.7, 'not-sunny':0.3})
#sunny probability 0.7
Raise = DiscreteDistribution({'raise':0.01, 'not-raise':0.99})
#raise probability 0.01
#conditional probability table for happiness (taken from example 3)
#P(h|s,r) = 1, P(h|~s, r) = 0.9, P(h|s, ~r)=0.7, P(h|~s,~r)=0.1
#P(~h|s,r) = 0, P(~h|~s, r) = 0.1, P(~h|s, ~r)=0.3, P(~h|~s,~r)=0.9
Happy = ConditionalProbabilityTable([
['sunny', 'raise', 'positive', 1],
['not-sunny', 'raise', 'positive', 0.9],
['sunny', 'not-raise', 'positive', 0.7],
['not-sunny', 'not-raise', 'positive', 0.1],
['sunny', 'raise', 'negative', 0],
['not-sunny', 'raise', 'negative', 0.1],
['sunny', 'not-raise', 'negative', 0.3],
['not-sunny', 'not-raise', 'negative', 0.9]], [Sunny, Raise])
#make states
s_sunny = State(Sunny, 'sunny')
s_raise = State(Raise, 'raise')
s_happy = State(Happy, 'happy')
model = BayesianNetwork('Happiness')
model.add_states(s_sunny, s_raise, s_happy)
model.add_transition(s_sunny, s_happy) #sunny -> happiness
model.add_transition(s_raise, s_happy) #raise -> happiness (also)
model.bake() # finalize the topology of the model
print()
print("example 3:")
print ('The number of nodes:', model.node_count())
print ('The number of elges:', model.edge_count())
#a P(rainy | sunny)
print (model.predict_proba({'sunny':'sunny'})[1].parameters)
#b P(rainy | happy and sunny)
print (model.predict_proba({'sunny':'sunny', 'happy':'positive'})[1].parameters)
#c P(rainy | happy)
print (model.predict_proba({'happy':'positive'})[1].parameters)
#d P(rainy | happy and not sunny)
print (model.predict_proba({'sunny':'not-sunny', 'happy':'positive'})[1].parameters)