#Mad_Libs_Generator
from random import randrange
noun = ('apple', 'fifth', 'scale', 'arithmetic', 'finger', 'seashore', 'badge', 'flock', 'sidewalk', 'smoke', 'battle', 'beast', 'stage', 'throne')
adjective =('abundant', 'faithful', 'kind', 'large', 'important', 'huge', 'orange', 'sticky', 'tall', 'vast', 'low')
verbs = ('talk', 'reach', 'bang', 'jump', 'lock', 'march', 'notice', 'pass', 'work', 'question', 'scatter', 'allow')
adverb = ('actually', 'angrily', 'keenly', 'positively', 'readily', 'highly', 'selfishly', 'viciously', 'immediately', 'clearly', 'briskly')
plural_nouh = ('cats', 'roofs', 'cities', 'boys', 'potatoes', 'analyses', 'rivers')
part_body = ('foot', 'head', 'nose', 'ear', 'hair', 'hand', 'shoulder')

story = (
	"Ye pretend to be a bloodthirsty " + noun[randrange(len(noun))] + " threatening everyone by waving yer " + adjective[randrange(len(adjective))] + 
	" sword in the air, but until ye learn to " + verbs[randrange(len(verbs))] + " like a pirate,ye'll never be " + adverb[randrange(len(adverb))] + 
	" accepted as an authentic " + noun[randrange(len(noun))] +
	", So here’s what ye do: Cleverly work into yer daily conversations " + adjective[randrange(len(adjective))] +
	" pirate phrases such Ahoy there " + plural_nouh[randrange(len(plural_nouh))] + ", Avast, ye " + plural_nouh[randrange(len(plural_nouh))] + "” and “Shiver me " + plural_nouh[randrange(len(plural_nouh))] +
	"” Remember to drop all yer gs when ye say such words as sailin’, spittin’, and fightin’. This will give ye a/an " + part_body[randrange(len(part_body))] + 
	" start to being recognized as a swashbucklin " + noun[randrange(len(noun))] +
	" Once ye have the lingo down pat, it helps to wear a three-cornered " + noun[randrange(len(noun))] + " on yer head, stash a/an " + noun[randrange(len(noun))] + 
	" in yer pants, and keep a/an " + noun[randrange(len(noun))] + " perched atop yer " + part_body[randrange(len(part_body))] + 
	" Aye now ye be a real pirate!"
	)
print(story)