#! D:\python21
import re
import string
import types

def addPronouns():
    # nominative pronouns
    myLanguage.dictionary.addWord(Pronoun("written=I;case=nominative;person=first;number=singular;capitalized=true"))
    myLanguage.dictionary.addWord(Pronoun("written=you;case=nominative;person=second;number=singular"))
    myLanguage.dictionary.addWord(Pronoun("written=he;case=nominative;person=third;number=singular;gender=masculine"))
    myLanguage.dictionary.addWord(Pronoun("written=she;case=nominative;person=third;number=singular;gender=feminine"))
    myLanguage.dictionary.addWord(Pronoun("written=it;case=nominative;person=third;number=singular;gender=neuter"))
    myLanguage.dictionary.addWord(Pronoun("written=we;case=nominative;person=first;number=plural"))
    myLanguage.dictionary.addWord(Pronoun("written=you;case=nominative;person=second;number=plural"))
    myLanguage.dictionary.addWord(Pronoun("written=they;case=nominative;person=third;number=plural"))
    # accusative pronouns
    myLanguage.dictionary.addWord(Pronoun("written=me;case=accusative;person=first;number=singular;capitalized=true"))
    myLanguage.dictionary.addWord(Pronoun("written=you;case=accusative;person=second;number=singular"))
    myLanguage.dictionary.addWord(Pronoun("written=him;case=accusative;person=third;number=singular;gender=masculine"))
    myLanguage.dictionary.addWord(Pronoun("written=her;case=accusative;person=third;number=singular;gender=feminine"))
    myLanguage.dictionary.addWord(Pronoun("written=it;case=accusative;person=third;number=singular;gender=neuter"))
    myLanguage.dictionary.addWord(Pronoun("written=us;case=accusative;person=first;number=plural"))
    myLanguage.dictionary.addWord(Pronoun("written=you;case=accusative;person=second;number=plural"))
    myLanguage.dictionary.addWord(Pronoun("written=them;case=accusative;person=third;number=plural"))
    # genitive pronouns
    myLanguage.dictionary.addWord(Pronoun("written=mine;case=genitive;person=first;number=singular;capitalized=true"))
    myLanguage.dictionary.addWord(Pronoun("written=your;case=genitive;person=second;number=singular"))
    myLanguage.dictionary.addWord(Pronoun("written=his;case=genitive;person=third;number=singular;gender=masculine"))
    myLanguage.dictionary.addWord(Pronoun("written=hers;case=genitive;person=third;number=singular;gender=feminine"))
    myLanguage.dictionary.addWord(Pronoun("written=its;case=genitive;person=third;number=singular;gender=neuter"))
    myLanguage.dictionary.addWord(Pronoun("written=ours;case=genitive;person=first;number=plural"))
    myLanguage.dictionary.addWord(Pronoun("written=yours;case=genitive;person=second;number=plural"))
    myLanguage.dictionary.addWord(Pronoun("written=theirs;case=genitive;person=third;number=plural"))

def addCommonNouns():
    myLanguage.dictionary.addWord(CommonNoun('stem=book;synset=tome'))
    myLanguage.dictionary.addWord(CommonNoun('stem=cat;synset=feline'))

def addIrregularNouns():    
    myLanguage.dictionary.addWord(IrregularNoun('stem=goose;is a=bird;color=white','plural=geese'))
    myLanguage.dictionary.addWord(IrregularNoun('stem=mouse;is a=rodent;color=[white,grey,brown]','plural=mice'))

def addProperNouns():
    myLanguage.dictionary.addWord(ProperNoun('written=Mary;gender=feminine'))
    myLanguage.dictionary.addWord(ProperNoun('written=John;gender=masculine'))
    myLanguage.dictionary.addWord(ProperNoun('written=Spot;gender=neuter'))


def addVerbs():
    myLanguage.dictionary.addWord(Verb('stem=book;synset=reserve'))
    myLanguage.dictionary.addWord(Verb('stem=walk;synset=stroll'))

    myLanguage.dictionary.addWord(IrregularVerb("stem=arise","past=arose;past participle=arisen"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=awake","past=awoke;past participle=awoken"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=awake","past=awakened;past participle=awoken"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=bear","past=bore;past participle=born"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=bear","past=bore;past participle=borne"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=beat","past=beat;past participle=beaten"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=beat","past=beat;past participle=beat"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=become","past=became;past participle=become"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=befall","past=befell;past participle=befallen"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=begin","past=began;past participle=begun"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=behold","past=beheld;past participle=beheld"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=bend","past=bent;past participle=bent"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=bet","past=bet;past participle=bet"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=bet","past=betted;past participle=bet"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=bet","past=betted;past participle=betted"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=bid","past=bid;past participle=bid"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=bind","past=bound;past participle=bound"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=bite","past=bit;past participle=bitten"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=bleed","past=bled;past participle=bled"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=blow","past=blew;past participle=blown"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=break","past=broke;past participle=broken"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=breed","past=bred;past participle=bred"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=bring","past=brought;past participle=brought"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=broadcast","past=broadcast;past participle=broadcast"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=browbeat","past=browbeat;past participle=browbeat"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=build","past=built;past participle=built"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=burn","past=burnt;past participle=burnt"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=burn","past=burned;past participle=burnt"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=burn","past=burned;past participle=burned"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=burst","past=burst;past participle=burst"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=bust","past=busted;past participle=busted"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=bust","past=bust;past participle=busted"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=bust","past=bust;past participle=bust"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=buy","past=bought;past participle=bought"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=cast","past=cast;past participle=cast"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=catch","past=caught;past participle=caught"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=choose","past=chose;past participle=chosen"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=cling","past=clung;past participle=clung"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=come","past=came;past participle=come"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=cost","past=cost;past participle=cost"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=creep","past=crept;past participle=crept"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=cut","past=cut;past participle=cut"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=deal","past=dealt;past participle=dealt"))

    myLanguage.dictionary.addWord(IrregularVerb("stem=dig","past=dug;past participle=dug"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=dive","past=dived;past participle=dived"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=dive","past=dove;past participle=dived"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=do","past=did;past participle=done"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=draw","past=drew;past participle=drawn"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=dream","past=dreamt;past participle=dreamt"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=dream","past=dreamed;past participle=dreamt"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=dream","past=dreamed;past participle=dreamed"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=drink","past=drank;past participle=drunk"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=drive","past=drove;past participle=driven"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=dwell","past=dwelt;past participle=dwelt"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=dwell","past=dwelled;past participle=dwelt"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=dwell","past=dwelled;past participle=dwelled"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=eat","past=ate;past participle=eaten"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=fall","past=fell;past participle=fallen"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=feed","past=fed;past participle=fed"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=feel","past=felt;past participle=felt"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=fight","past=fought;past participle=fought"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=find","past=found;past participle=found"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=fit","past=fit;past participle=fit"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=fit","past=fit;past participle=fit"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=fit","past=fitted;past participle=fit"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=fit","past=fitted;past participle=fitted"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=flee","past=fled;past participle=fled"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=fling","past=flung;past participle=flung"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=fly","past=flew;past participle=flown"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=forbid","past=forbade;past participle=forbidden"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=forecast","past=forecast;past participle=forecast"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=forego","past=forewent;past participle=foregone"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=foresee","past=foresaw;past participle=foreseen"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=foretell","past=foretold;past participle=foretold"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=forget","past=forgot;past participle=forgotten"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=forgive","past=forgave;past participle=forgiven"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=forsake","past=forsook;past participle=forsaken"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=freeze","past=froze;past participle=frozen"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=get","past=got;past participle=gotten"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=get","past=got;past participle=got"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=give","past=gave;past participle=given"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=go","past=went;past participle=gone"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=grind","past=ground;past participle=ground"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=grow","past=grew;past participle=grown"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=hang","past=hung;past participle=hung"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=have","past=had;past participle=had"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=hear","past=heard;past participle=heard"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=hide","past=hid;past participle=hidden"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=hit","past=hit;past participle=hit"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=hold","past=held;past participle=held"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=hurt","past=hurt;past participle=hurt"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=input","past=input;past participle=input"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=inset","past=inset;past participle=inset"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=interbreed","past=interbred;past participle=interbred"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=interweave","past=interwove;past participle=interwoven"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=keep","past=kept;past participle=kept"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=kneel","past=knelt;past participle=knelt"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=kneel","past=kneeled;past participle=knelt"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=kneel","past=kneeled;past participle=kneeled"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=knit","past=knit;past participle=knit"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=knit","past=knitted;past participle=knit"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=knit","past=knitted;past participle=knitted"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=know","past=knew;past participle=known"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=lay","past=laid;past participle=laid"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=lead","past=led;past participle=led"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=lean","past=leaned;past participle=leaned"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=lean","past=leant;past participle=leaned"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=lean","past=leant;past participle=leant"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=leap","past=leapt;past participle=leapt"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=leap","past=leaped;past participle=leapt"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=leap","past=leaped;past participle=leaped"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=learn","past=learned;past participle=learned"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=learn","past=learnt;past participle=learned"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=learn","past=learnt;past participle=learnt"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=leave","past=left;past participle=left"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=lend","past=lent;past participle=lent"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=let","past=let;past participle=let"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=lie","past=lay;past participle=lain"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=light","past=lit;past participle=lit"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=light","past=lighted;past participle=lit"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=light","past=lighted;past participle=lighted"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=lose","past=lost;past participle=lost"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=make","past=made;past participle=made"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=mean","past=meant;past participle=meant"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=meet","past=met;past participle=met"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=mishear","past=misheard;past participle=misheard"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=mislay","past=mislaid;past participle=mislaid"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=mislead","past=misled;past participle=misled"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=misread","past=misread;past participle=misread"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=misspell","past=misspelled;past participle=misspelled"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=misspell","past=misspelt;past participle=misspelled"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=misspell","past=misspelt;past participle=misspelt"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=mistake","past=mistook;past participle=mistaken"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=misunderstand","past=misunderstood;past participle=misunderstood"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=mow","past=mowed;past participle=mowed"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=mow","past=mowed;past participle=mow"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=outbid","past=outbid;past participle=outbid"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=outdo","past=outdid;past participle=outdone"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=outgrow","past=outgrew;past participle=outgrown"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=outrun","past=outran;past participle=outrun"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=outsell","past=outsold;past participle=outsold"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=overcast","past=overcast;past participle=overcast"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=overcome","past=overcame;past participle=overcome"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=overdo","past=overdid;past participle=overdone"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=overdraw","past=overdrew;past participle=overdrawn"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=overeat","past=overate;past participle=overeaten"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=overhang","past=overhung;past participle=overhung"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=overhear","past=overheard;past participle=overheard"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=overlay","past=overlaid;past participle=overlaid"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=overlie","past=overlay;past participle=overlain"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=overpay","past=overpaid;past participle=overpaid"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=override","past=overrode;past participle=overridden"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=overrun","past=overran;past participle=overrun"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=oversee","past=oversaw;past participle=overseen"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=oversell","past=oversold;past participle=oversold"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=overshoot","past=overshot;past participle=overshot"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=oversleep","past=overslept;past participle=overslept"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=overtake","past=overtook;past participle=overtaken"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=overthrow","past=overthrew;past participle=overthrown"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=partake","past=partook;past participle=partaken"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=pay","past=paid;past participle=paid"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=plead","past=pled;past participle=pled"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=plead","past=pleaded;past participle=pled"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=plead","past=pleaded;past participle=pleaded"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=pre-set","past=pre-set;past participle=pre-set"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=proofread","past=proofread;past participle=proofread"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=prove","past=proved;past participle=proven"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=prove","past=proved;past participle=proved"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=put","past=put;past participle=put"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=quit","past=quit;past participle=quit"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=quit","past=quitted;past participle=quit"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=quit","past=quitted;past participle=quitted"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=read","past=read;past participle=read"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=rebind","past=rebound;past participle=rebound"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=rebuild","past=rebuilt;past participle=rebuilt"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=recast","past=recast;past participle=recast"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=redo","past=redid;past participle=redone"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=re-lay","past=re-laid;past participle=re-laid"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=remake","past=remade;past participle=remade"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=repay","past=repaid;past participle=repaid"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=rerun","past=reran;past participle=rerun"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=resell","past=resold;past participle=resold"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=reset","past=reset;past participle=reset"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=rethink","past=rethought;past participle=rethought"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=rewind","past=rewound;past participle=rewound"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=rewrite","past=rewrote;past participle=rewritten"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=rid","past=rid;past participle=rid"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=ride","past=rode;past participle=ridden"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=ring","past=rang;past participle=rung"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=rise","past=rose;past participle=risen"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=run","past=ran;past participle=run"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=say","past=said;past participle=said"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=see","past=saw;past participle=seen"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=seek","past=sought;past participle=sought"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=sell","past=sold;past participle=sold"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=send","past=sent;past participle=sent"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=set","past=set;past participle=set"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=sew","past=sewed;past participle=sewn"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=sew","past=sewed;past participle=sewed"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=shake","past=shook;past participle=shaken"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=shear","past=sheared;past participle=shorn"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=shear","past=sheared;past participle=sheared"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=shed","past=shed;past participle=shed"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=shine","past=shined;past participle=shined"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=shine","past=shone;past participle=shined"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=shine","past=shone;past participle=shone"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=shit","past=shit;past participle=shit"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=shit","past=shat;past participle=shit"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=shit","past=shat;past participle=shat"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=shoot","past=shot;past participle=shot"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=show","past=showed;past participle=shown"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=show","past=showed;past participle=showed"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=shrink","past=shrank;past participle=shrunk"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=shrink","past=shrunk;past participle=shrunk"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=shut","past=shut;past participle=shut"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=sing","past=sang;past participle=sung"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=sit","past=sat;past participle=sat"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=slay","past=slew;past participle=slain"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=sleep","past=slept;past participle=slept"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=slide","past=slid;past participle=slid"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=sling","past=slung;past participle=slung"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=slit","past=slit;past participle=slit"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=smell","past=smelled;past participle=smelled"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=smell","past=smelt;past participle=smelled"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=smell","past=smelt;past participle=smelt"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=speak","past=spoke;past participle=spoken"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=speed","past=sped;past participle=sped"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=speed","past=speeded;past participle=sped"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=speed","past=speeded;past participle=speeded"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=spell","past=spelled;past participle=spelled"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=spell","past=spelt;past participle=spelled"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=spell","past=spelt;past participle=spelt"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=spend","past=spent;past participle=spent"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=spin","past=spun;past participle=spun"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=spit","past=spit;past participle=spit"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=spit","past=spat;past participle=spit"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=spit","past=spat;past participle=spat"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=split","past=split;past participle=split"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=spoil","past=spoiled;past participle=spoiled"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=spoil","past=spoilt;past participle=spoiled"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=spoil","past=spoilt;past participle=spoilt"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=spoon-feed","past=spoon-fed;past participle=spoon-fed"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=spread","past=spread;past participle=spread"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=spring","past=sprang;past participle=sprung"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=spring","past=sprung;past participle=sprung"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=stand","past=stood;past participle=stood"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=steal","past=stole;past participle=stolen"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=stick","past=stuck;past participle=stuck"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=sting","past=stung;past participle=stung"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=stink","past=stank;past participle=stunk"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=stink","past=stunk;past participle=stunk"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=strew","past=strewed;past participle=strewn"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=strew","past=strewed;past participle=strewed"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=stride","past=strode;past participle=stridden"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=strive","past=strove;past participle=striven"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=strike","past=struck;past participle=stricken"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=strike","past=struck;past participle=struck"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=strike","past=struck;past participle=stricken"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=string","past=strung;past participle=strung"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=strive","past=strove;past participle=striven"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=strive","past=strived;past participle=striven"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=strive","past=strived;past participle=strived"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=swear","past=swore;past participle=sworn"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=sweep","past=swept;past participle=swept"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=swell","past=swelled;past participle=swollen"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=swell","past=swelled;past participle=swelled"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=swim","past=swam;past participle=swum"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=swing","past=swung;past participle=swung"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=take","past=took;past participle=taken"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=teach","past=taught;past participle=taught"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=tear","past=tore;past participle=torn"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=tell","past=told;past participle=told"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=think","past=thought;past participle=thought"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=throw","past=threw;past participle=thrown"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=thrust","past=thrust;past participle=thrust"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=tread","past=trod;past participle=trodden"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=tread","past=trod;past participle=trod"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=unbind","past=unbound;past participle=unbound"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=underlie","past=underlay;past participle=underlain"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=understand","past=understood;past participle=understood"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=undertake","past=undertook;past participle=undertaken"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=underwrite","past=underwrote;past participle=underwritten"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=undo","past=undid;past participle=undone"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=unwind","past=unwound;past participle=unwound"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=uphold","past=upheld;past participle=upheld"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=upset","past=upset;past participle=upset"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=wake","past=woke;past participle=woken"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=wake","past=waked;past participle=woken"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=wake","past=waked;past participle=waked"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=wear","past=wore;past participle=worn"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=weave","past=wove;past participle=woven"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=wed","past=wed;past participle=wed"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=wed","past=wedded;past participle=wed"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=wed","past=wedded;past participle=wedded"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=weep","past=wept;past participle=wept"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=wet","past=wet;past participle=wet"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=wet","past=wetted;past participle=wet"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=wet","past=wetted;past participle=wetted"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=win","past=won;past participle=won"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=wind","past=wound;past participle=wound"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=withdraw","past=withdrew;past participle=withdrawn"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=wring","past=wrung;past participle=wrung"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=write","past=wrote;past participle=written"))    

def addNumbers():
    myLanguage.dictionary.addWord(Number("stem=one;value=1"))
    myLanguage.dictionary.addWord(Number("stem=two;value=2"))
    myLanguage.dictionary.addWord(Number("stem=three;value=3"))
    myLanguage.dictionary.addWord(Number("stem=four;value=4"))
    myLanguage.dictionary.addWord(Number("stem=five;value=5"))
    myLanguage.dictionary.addWord(Number("stem=six;value=6"))
    myLanguage.dictionary.addWord(Number("stem=seven;value=7"))
    myLanguage.dictionary.addWord(Number("stem=eight;value=8"))
    myLanguage.dictionary.addWord(Number("stem=nine;value=9"))
    myLanguage.dictionary.addWord(Number("stem=ten;value=10"))

def addAdjectives():

    myLanguage.dictionary.addWord(Adjective('stem=tall;dimension=height;value=positive;opposite=short'))
    myLanguage.dictionary.addWord(Adjective('stem=short;dimension=height;value=negative;opposite=tall'))
    
    myLanguage.dictionary.addWord(Adjective('stem=big;dimension=size;value=positive;opposite=small;synset=large'))
    myLanguage.dictionary.addWord(Adjective('stem=small;dimension=size;value=negative;opposite=big;synset=little'))

    myLanguage.dictionary.addWord(Adjective('stem=happy;dimension=emotion;value=positive;opposite=sad'))
    myLanguage.dictionary.addWord(Adjective('stem=sad;dimension=emotion;value=negative;opposite=happy'))

    myLanguage.dictionary.addWord(Adjective('stem=fat;dimension=width;value=positive;opposite=thin'))
    myLanguage.dictionary.addWord(Adjective('stem=thin;dimension=width;value=negative;opposite=fat'))

    myLanguage.dictionary.addWord(Adjective('stem=smart;dimension=intelligence;value=positive;opposite=stupid'))
    myLanguage.dictionary.addWord(IrregularAdjective('stem=stupid;dimension=intelligence;value=negative;opposite=smart','comparative=stupider;superlative=stupidest'))
    
    myLanguage.dictionary.addWord(IrregularAdjective('stem=good;dimension=judgement;value=positive;opposite=bad','comparative=better;superlative=best'))
    myLanguage.dictionary.addWord(IrregularAdjective('stem=bad;dimension=judgement;value=negative;opposite=good','comparative=worse;superlative=worst'))   

Languages = {}

class Language:
    def __init__(self,name):
        dbg = 0
        if dbg: print "Creating a new instance of class Language"
        Languages[name] = self
        self.dictionary = Dictionary()

class Dictionary(object):
    def __init__(self):
        dbg = 0
        if dbg: print "Creating a new instance of class Dictionary"
        self.Words = {}
    def addWord(self,myWord):
        dbg = 0
        if dbg: print "-->Dictionary.addWord"
        avatars = myWord.Avatars
        for avatar in avatars:
            if self.Words.has_key(avatar):
                knownDefinitions = self.Words[avatar]
                if dbg: print "have seen written form before, knownDefinitions are:",knownDefinitions
                knownDefProps = []
                for aDef in knownDefinitions:
                    knownDefProps.append(aDef.Properties)
                    if dbg:
                        print "aDef.Properties =",aDef.Properties
                if myWord.Properties in knownDefProps:
                    if dbg: print "Have seen this definition before."
                else:
                    self.Words[avatar].append(myWord)
                    if dbg: print "Have not seen this definition before, so I'm adding it"
            else:
                self.Words[avatar] = [myWord]
                if dbg: print "adding a new word=",myWord.Properties
    def dump(self):
        for wordForm in self.Words.keys():
            print "\n--------------------"
            print wordForm
            for word in self.Words[wordForm]:
                word.printProperties()
    def printWordList(self):
        for wordForm in self.Words.keys():
            print wordForm
    
class Word:
    def __init__(self):
        dbg = 0
        if dbg: print "Creating a new instance of Word"
        self.Forms = {}
        self.Avatars = {}
        self.Properties = {}
    def addProperties(self,definition):
        dbg = 0
        if dbg: print "--> addProperties, definition=",definition
        if string.find(definition,";") > -1:
            for KVP in string.split(definition,";"):
                if string.find(KVP,"=") > -1:          
                    aKey,aVal = string.split(KVP,"=")
                    if dbg: print "aKey =",aKey,"aVal =",aVal
                    self.Properties[aKey] = [aVal]
                    if self.Forms.has_key(aKey):
                        if dbg: print "Over-riding form a"
                        self.Forms[aKey] = [aVal]
                else:
                    print "error"
        else:
            if string.find(definition,"=") > -1:              
                aKey,aVal = string.split(definition,"=")
                self.Properties[aKey] = [aVal]
                if self.Forms.has_key(aKey):
                    if dbg: print "Over-riding form b"
                    self.Forms[aKey] = [aVal]
            else:
                print "error"
        if dbg: print "<-- addProperties"
    def printProperties(self):

        #print type(self),repr(self)
        #print self.__class__,self.__dict__
        junk,myClassName = string.split(str(self.__class__),".")
        print "Part of speech:",myClassName
        if self.Properties.has_key('stem'):
            print "stem:",self.Properties['stem']
        else:
            if self.Properties.has_key('written'):
                print "written:",self.Properties['written']
        print self.__dict__

    def discoverAvatars(self):
        dbg = 0
        if dbg: print "--> discoverAvatars, self.Forms=",self.Forms
        for form in self.Forms.keys():      # e.g. self.Forms = {'plural':['books'],'singular':['book']}, so form = 'plural', then 'singular'
            if dbg: print "form is",form
            for word in self.Forms[form]:        # e.g. ['books']
                if self.Avatars.has_key(word):      # self.Avatars = {'books':['plural],'book':['singular']}
                    if form not in self.Avatars[word]:  
                        self.Avatars[word].append(form)
                        if dbg: print "found additional form",form
                else:
                    self.Avatars[word] = [form]
                    if dbg: print "self.Avatars =",self.Avatars
        if dbg: print "<-- discoverAvatars"

class Verb(Word):
    def __init__(self,definition):
        dbg = 0
        if dbg: print "Creating a new verb instance"
        Word.__init__(self)
        self.Properties['capitalized'] = ['false']
        self.addProperties(definition)
        stem = self.Properties['stem'][0]
        if stem[-1] == 'e':
            pstem = stem[:-1]
        else:
            pstem = stem

        lastLetter = stem[-1]
        doubleset = ['b','p','d','t','g','k','m','n']
        vowels = ['a','e','i','o','u']
        # if the word ends in e (sue-suer-suing)
        if lastLetter in vowels:
            if lastLetter == 'e':
                if not stem[-2] == 'e':
                    pstem = stem[:-1]
                    sstem = stem
                else:
                    pstem = stem
                    sstem = stem
            else:
                if lastLetter == 'o':
                    sstem = stem + 'e'
                    pstem = stem
                else:
                    pstem = stem
                    sstem = stem
        else:
            # if the adj ends in d,t,g (bid-bidder-bidding, run-runner-running) need to double
            if lastLetter in doubleset:
                # if the next to the last letter is a vowel
                if stem[-2] in vowels:
                    # and the letter before that is not a vowel, i.e., not bead - beadding
                    if not stem[-3] in vowels:
                        pstem = stem + lastLetter
                        sstem = stem
                    else: 
                        # but make one check for 'qu'
                        if stem[-3] == 'u' and stem[-4] == 'q':
                            pstem = stem + lastLetter
                            sstem = stem
                        else:
                            pstem = stem
                            sstem = stem
                else:
                    sstem = stem
                    pstem = stem
            else:
                pstem = stem
                sstem = stem
                    
        if dbg:print "stem is",pstem
        self.Forms = {
            'infinitive':['to ' + stem],
            'third person singular':[sstem + 's'],
            'other':[stem],
            'past':[pstem + 'ed'],
            'past participle':[pstem + 'ed'],
            'present participle':[pstem + 'ing']}
        ppKludge = self.Forms['present participle']
        ending = ppKludge[0]
        if dbg: print "+++",ending,"+++"
        if string.find(ending,"iing") > -1:
            ending = string.replace(ending,"iing","ying")
        self.Forms['present participle'] = [ending]

        self.discoverAvatars()
        if dbg:self.printProperties()

class IrregularVerb(Verb):
    def __init__(self,definition,exceptions):
        dbg = 0
        if dbg: print "Creating a new irregular verb instance"
        Verb.__init__(self,definition)
        self.addProperties(exceptions)
        self.Avatars = {}               #wipe out existing avatars
        self.discoverAvatars()
        if dbg:self.printProperties()

class Noun(Word):
    def __init__(self):
        dbg = 0
        if dbg: print "Creating a new instance of class Noun"
        Word.__init__(self)

class Pronoun(Noun):
    def __init__(self,definition):
        dbg = 0
        if dbg: print "Creating a new instance of class Pronoun"
        Noun.__init__(self)
        self.Properties['capitalized'] = ['false']
        self.addProperties(definition)
        self.Forms['written'] = [self.Properties['written'][0]]
        self.discoverAvatars()
        if dbg:self.printProperties()

class CommonNoun(Noun):
    def __init__(self,definition):
        dbg = 0
        if dbg: print "Creating instance of common noun, definition =",definition
        Noun.__init__(self)    
        self.Properties['capitalized'] = ['false']
        self.Properties['person'] = ['third']
        self.addProperties(definition)
        stem = self.Properties['stem'][0]
        self.Forms = {'singular':[stem],'plural':[stem + 's']}
        self.Properties['Forms'] = self.Forms
        self.discoverAvatars()
        if dbg:self.printProperties()
        
class IrregularNoun(CommonNoun):
    def __init__(self,definition,exceptions):
        dbg = 0
        if dbg: print "Creating instance of Irregular common noun, definition =",definition," exceptions=",exceptions
        CommonNoun.__init__(self,definition)
        self.addProperties(exceptions)
        self.Avatars = {}               #wipe out existing avatars
        self.discoverAvatars()
        if dbg:self.printProperties()

# ProperNoun('written=Mary;gender=feminine')        
class ProperNoun(Noun):
    def __init__(self,definition):
        dbg = 0
        if dbg: print "Creating a new instance of class ProperNoun,definition=",definition
        Noun.__init__(self)    
        self.Properties['capitalized'] = ['true']
        self.Properties['person'] = ['third']
        self.Properties['number'] = ['singular']
        self.addProperties(definition)
        self.Forms['written'] = [self.Properties['written'][0]]
        self.discoverAvatars()
        if dbg:self.printProperties()

class Number(Word):
    def __init__(self,definition):
        dbg = 0
        if dbg: print "Creating a new instance of class Number,definition=",definition
        Word.__init__(self)
        self.Properties['capitalized'] = ['false']
        self.addProperties(definition)
        self.value = int(self.Properties['value'][0])
        if self.value > 1:
            self.Properties['number'] = ['singular']
        else:
            self.Properties['number'] = ['plural']
        stem = self.Properties['stem'][0]
        self.Forms['written'] = [stem]
        self.discoverAvatars()
        if dbg:
            self.printProperties()

class Adjective(Word):
    def __init__(self,definition):
        dbg = 0
        if dbg: print "Creating a new instance of class Number,definition=",definition
        Word.__init__(self)
        self.Properties['capitalized'] = ['false']
        self.addProperties(definition)
        stem = self.Properties['stem'][0]
        lastLetter = stem[-1]
        doubleset = ['d','t','g','k','p','n']
        # if the adj ends in e (blue-bluer-bluest)
        if lastLetter == 'e':
            pstem = stem[:-1]
        else:
            # if the adj ends in d,t,g (sad-sadder-saddest, fat-fatter-fattest) need to double
            if lastLetter in doubleset:
                # if the next to last letter is not 'r'
                if not stem[-2] == 'r':                 
                    pstem = stem + lastLetter
                else:
                    pstem = stem
            else:
                # if the adj ends in y (flabby-flabbier-flabbiest)
                if lastLetter == 'y':
                    pstem = stem[:-1] + 'i'
                else:
                    pstem = stem

        self.Forms = {'base':[stem],'comparative':[pstem + 'er'],'superlative':[pstem + 'est']}
        self.discoverAvatars()
        if dbg:
            self.printProperties()

class IrregularAdjective(Adjective):            
    def __init__(self,definition,exceptions):
        dbg = 0
        if dbg: print "Creating instance of Irregular adjective, definition =",definition," exceptions=",exceptions
        Adjective.__init__(self,definition)
        self.addProperties(exceptions)
        self.Avatars = {}               #wipe out existing avatars
        self.discoverAvatars()
        if dbg:self.printProperties()
        
if __name__ == "__main__":
    import sys, time
    dbg = 1
    t1 = time.time()
    try:
    	infilename = sys.argv[1]
    	infile = open(infilename,"r")
    except IndexError:
       	sys.stderr.write("\nUsage: %s <in_filename.txt> (out_file.txt)\n\n" % sys.argv[0] )  
    try:
    	outfilename = sys.argv[2]
    	outfile = open(outfilename,"w")
    except IndexError:
        outfile = sys.stdout
    if dbg: print "---------------------------------"

    myLanguage = Language("English")
    addNumbers()
    #addVerbs()
    #addPronouns()
    #addCommonNouns()
    #addIrregularNouns()
    #addProperNouns()
    #addAdjectives()
    myLanguage.dictionary.addWord(Verb('stem=die;synset=expire'))
    myLanguage.dictionary.addWord(IrregularVerb("stem=overlie","past=overlay;past participle=overlain"))
    myLanguage.dictionary.addWord(IrregularVerb("stem=quit","past=quit;past participle=quit"))
    #myLanguage.dictionary.dump()
    #myLanguage.dictionary.printWordList()


    
