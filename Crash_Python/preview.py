#import wordcloud
#import numpy as np
#from matplotlib import pyplot as plt
#from IPython.display import display
#import fileupload
#import io
#import sys

text = """The Project Gutenberg EBook of Pride and Prejudice, a play, by
Mary Keith Medbery Mackaye

This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it away or
re-use it under the terms of the Project Gutenberg License included
with this eBook or online at www.gutenberg.org


Title: Pride and Prejudice, a play

Author: Mary Keith Medbery Mackaye

Release Date: September 15, 2011 [EBook #37431]

Language: English


*** START OF THIS PROJECT GUTENBERG EBOOK PRIDE AND PREJUDICE, A PLAY ***




Produced by Chuck Greif and the Online Distributed
Proofreading Team at http://www.pgdp.net (This book was
produced from scanned images of public domain material
from the Internet Archive.)








_PRIDE AND PREJUDICE_

_A PLAY_

[Illustration: "_Mr. Darcy, I have never desired your good opinion, and
you have certainly bestowed it most unwillingly._"]




_PRIDE AND PREJUDICE_

_A PLAY_

_FOUNDED ON JANE AUSTEN'S
NOVEL_

_BY_

_MRS. STEELE MACKAYE_

[Illustration: colophon]

_NEW YORK_
_DUFFIELD AND COMPANY_
_1906_


                 COPYRIGHT, 1906, BY DUFFIELD & COMPANY.

                        Published September, 1906.

                                  ------

                         SPECIAL COPYRIGHT NOTICE.

     This play is fully protected by copyright, all requirements of the
     law having been complied with. Performances may be given only with
     the written permission of Duffield & Company, agents for Mrs.
     Steele Mackaye, owner of the acting rights.

     Extract from the law relating to copyright:

     "SEC. 4996. Any person publicly performing or representing any
     dramatic or musical composition for which a copyright has been
     obtained, without the consent of the proprietor of said dramatic or
     musical composition or his heirs or assigns, shall be liable for
     damages therefor, such damages in all cases to be assessed at such
     sum not less than one hundred dollars for the first and fifty
     dollars for every subsequent performance as to the Court shall
     appear just. If the unlawful performance and representation be
     wilful and not for profit, such person or persons shall be guilty
     of a misdemeanor, and upon conviction be imprisoned for a period
     not exceeding one year."




PERSONS OF THE PLAY


     MR. DARCY--(OF PEMBERLEY, DERBYSHIRE). "_Possessed of a fine tall
     person, handsome features, noble mien, and ... ten thousand a year
     ... clever ... haughty, reserved and fastidious; his manners,
     though well-bred, were not inviting. 'Some people call him proud,'
     said Mrs. Reynolds, the housekeeper at Pemberley, 'but I am sure I
     never saw anything of it.... He is the best landlord and the best
     master that ever lived.'_"

     MR. BINGLEY--(OF NETHERFIELD, HERTFORDSHIRE, DARCY'S FRIEND).
     "_Just what a young man ought to be; sensible and good-humoured,
     lively ... such happy manners! So much ease, with such perfect good
     breeding.... Also handsome, which a young man ought likewise to be
     if he possibly can._"

     COLONEL FITZWILLIAM--(COUSIN TO DARCY). "_About thirty, not
     handsome, but in person and address most truly the gentleman._"

     MR. BENNET--(OF LONGBOURN). "_An odd mixture of quick parts,
     sarcastic humour, reserve and caprice. He was fond of the country
     and of books, and from these tastes had arisen his principal
     enjoyments._"

     MR. COLLINS--(A COUSIN OF MR. BENNET, AND NEXT IN THE ENTAIL OF
     LONGBOURN ESTATE.) "_A tall, heavy-looking young man of
     five-and-twenty. His air was grave and stately, and his manners
     very formal. His veneration for his patroness, Lady Catherine de
     Bourg, mingling with a very good opinion of himself and of his
     authority as a clergyman ... made him altogether a mixture of pride
     and obsequiousness, self-importance and humility._"

     SIR WILLIAM LUCAS--(AN INTIMATE FRIEND AND NEIGHBOUR OF THE
     BENNETS). "_Formerly in trade in Meryton ... he had risen to the
     honour of knighthood by an address to the King during his
     mayoralty. The distinction had ... given him a disgust to his
     business, and, ... quitting it, he had removed ... to Lucas Lodge,
     where he could think with pleasure of his own importance, and ...
     occupy himself solely in being civil to all the world._"

     COLONEL FORSTER--(THE COLONEL OF THE REGIMENT STATIONED AT
     MERYTON).

     MR. WICKHAM--(AN OFFICER IN THE REGIMENT). "_Endowed with all the
     best parts of beauty--a fine countenance, a good figure, and a very
     pleasing address. As false and deceitful as he is insinuating._"

     MR. DENNY--(ANOTHER OFFICER IN THE REGIMENT).

     HARRIS--(THE BUTLER AT LONGBOURN).

     MRS. BENNET--(THE WIFE OF MR. BENNET). "_A woman of mean
     understanding, little information, and uncertain temper. When she
     was discontented she fancied herself nervous. The business of her
     life was to get her daughters married; its solace was visiting and
     news._"

     JANE--(ELDEST DAUGHTER OF MR. AND MRS. BENNET). "_She united with
     great strength of feeling a composure of temper and a uniform
     cheerfulness of manner. Her mild and steady candour always pleaded
     allowances, and urged the possibility of mistakes._"

     ELIZABETH--(THEIR SECOND DAUGHTER). "_Although not so handsome as
     Jane, her face was rendered uncommonly intelligent by the beautiful
     expression of her dark eyes. She had a lively, playful disposition,
     which delighted in anything ridiculous, with more quickness of
     observation and less pliancy of temper than her sister. There was a
     mixture of sweetness and archness in her manner which made it
     difficult for her to affront anybody._"

     LYDIA--(THEIR YOUNGEST DAUGHTER). "_A stout, well-grown girl of
     fifteen, with a fine complexion and a good-humoured countenance--a
     favourite with her mother, whose affection had brought her into
     public at an early age._"

     LADY LUCAS--(THE WIFE OF SIR WILLIAM). "_Not too clever to be a
     valuable neighbour to Mrs. Bennet._"

     CHARLOTTE LUCAS--(DAUGHTER OF SIR WILLIAM AND LADY LUCAS). "_A
     sensible, intelligent young woman, about twenty-seven, ...
     Elizabeth's intimate friend._"

     MISS BINGLEY--(SISTER OF MR. BINGLEY). "_A very fine lady ... but
     proud and conceited._"

     LADY CATHERINE DE BOURG--(AUNT OF DARCY AND PATRONESS OF MR.
     COLLINS). "_A tall, large woman, with strongly marked features,
     which might once have been handsome. Her air was not
     conciliating.... Whatever she said, was spoken in so authoritative
     a tone as marked her self-importance._"

     HILL--(THE HOUSEKEEPER AT LONGBOURN).

     MARTHA--(THE MAID AT MR. COLLINS'S PARSONAGE).




ACT I

THE DRAWING-ROOM AT LONGBOURN

ACT II

THE ORANGERY AT NETHERFIELD

ONE MONTH LATER

ACT III

MR. COLLINS'S PARSONAGE AT HUNSFORD

THREE MONTHS LATER

ACT IV

THE SHRUBBERY AT LONGBOURN

ONE WEEK LATER

PLACE: ENGLAND TIME: 1796

     "In the novels of the last hundred years there are vast numbers of
     young ladies with whom it might be a pleasure to fall in love,--but
     to live with and to marry, I do not know that any of them can come
     into competition with _Elizabeth Bennet_."--GEORGE SAINTSBURY.
     Preface to the Peacock Edition of "Pride and Prejudice."




ACT I




PRIDE AND PREJUDICE

A PLAY




ACT I


_The drawing-room at Longbourn. At the back, wide glass doors open upon
a terrace which overlooks an English landscape. It is winter, and coals
are burning in the fireplace. On each side of the glass doors are
rounded recesses with windows. On one side of the room a door opens into
the library. On the other side is a door to the hall--the chief entrance
of the house. The room is handsomely furnished in eighteenth century
style._ MR. _and_ MRS. BENNET _are discovered sitting on either side of
the table._ MRS. BENNET _is knitting--_MR. BENNET _reading._


MRS. BENNET.

[_After a slight pause and laying down her knitting._]

My dear Mr. Bennet, did not you hear me? Did you know that Netherfield
Park is let at last?


MR. BENNET.

[_Continues reading and does not answer._]


MRS. BENNET.

[_Impatiently._] Do not you want to know who has taken it?


MR. BENNET.

[_Ceases reading and looks up at her with an amused smile._] You want to
tell me, and I have no objection to hearing it.


MRS. BENNET.

[_With animation._] Why, my dear, you must know Lady Lucas says that
Netherfield is taken by a young man of large fortune from the North of
England. His name is Bingley, and he is _single_, my dear. Think of
that, Mr. Bennet! A single man of large fortune; four or five thousand
pounds a year. What a fine thing for our girls!


MR. BENNET.

How so? How can it affect them?


MRS. BENNET.

My dear Mr. Bennet, how can you be so tiresome! You must know that I am
thinking of his marrying one of them.


MR. BENNET.

Is that his design in settling here?


MRS. BENNET.

Design!--Nonsense! How can you talk so? But it is very likely that he
will fall in love with one of them, and therefore you must visit him as
soon as you can. Consider your daughters, Mr. Bennet! Only think what an
establishment it would be for one of them! Sir William and Lady Lucas
are determined to go merely on that account. Indeed you must go, for it
will be impossible for us to visit him if _you_ do not.


MR. BENNET.

[_Who has risen during this last speech and now stands with his back to
the fire, facing_ MRS. BENNET.] You are overscrupulous, surely. I dare
say Mr. Bingley will be very glad to see you, and I will send a few
lines to assure him of my hearty consent to his marrying whichever he
chooses of the girls--though I must throw in a good word for my little
Lizzy.


MRS. BENNET.

[_Sharply._] I desire you will do no such thing! Lizzy is not a bit
better than the others. She is not half as handsome as Jane, nor as
good-humoured as Lydia. But you are always giving her the preference.


MR. BENNET.

Not unless she deserves it, my dear. But in this particular instance my
poor little Lizzy is the only one who is unprovided for. Lydia and the
others belong in the schoolroom, and you tell me that Mr. Collins has
already spoken for Jane.


MRS. BENNET.

Oh, that odious Mr. Collins! I wish he had never come here. I wish I
might never hear his name again!


MR. BENNET.

Mr. Collins odious! You surprise me! I thought that he had won your full
approval.


MRS. BENNET.

[_Fretfully._] Oh, well, since he had to be your cousin, and since you
_will_ not do anything about the entail, I suppose it will be a mercy if
he does marry Jane. [_Half crying._] But I do think, Mr. Bennet, it is
the hardest thing in the world that we have no son of our own, so that
your property has to be entailed away from your own wife and children,
so if you should die, we may all be turned out of the house whenever
this Mr. Collins pleases. [_In bewailing tone._] He certainly does seem
to have all the luck in the world. Here he has just got this good living
from that grand Lady Catherine de Bourg.


MR. BENNET.

But, my dear, that will soon be _your_ luck, as well. You forget that
your daughter is to profit by it.


MRS. BENNET.

Well, perhaps. I don't know about _that_, but, [_With renewed
excitement._] I _do_ know that it is too monstrous that after you are
gone I shall be forced to make way for this man and live to see him
master in this house!


MR. BENNET.

My dear, do not give way to such gloomy thoughts. Let us hope for better
things. Let us flatter ourselves that I may be the survivor.


MRS. BENNET.

[_This is not very consoling to_ MRS. BENNET; _and therefore, instead of
making answer, she goes on as before._] If it was not for the entail I
should not mind it.


MR. BENNET.

What should not you mind?


MRS. BENNET.

I should not mind anything at all.


MR. BENNET.

Let us be thankful that you are preserved from a state of such
insensibility. But it certainly is a most iniquitous affair, and nothing
can clear Mr. Collins from the guilt of inheriting Longbourn. However,
you know he is doing his best to mend matters. He has not only
handsomely apologised for his fault, but he has now assured us of his
readiness to make every possible amends by marrying one of the girls.
Surely, my dear, you must acknowledge that this plan is excessively
generous on his part.


MRS. BENNET.

[_Dolefully._] Well, I suppose it might be worse.


MR. BENNET.

[_Cheerfully._] Decidedly worse. With Jane so well settled, and a single
man like Mr. Bingley in prospect, I think you should be quite cheerful.


MRS. BENNET.

[_Excited once more._] Mr. Bingley! We shall never know Mr. Bingley. Oh,
Mr. Bennet, you take delight in vexing me. You have no compassion on my
poor nerves.


MR. BENNET.

You mistake, my dear. I have a high respect for your nerves. They are my
old friends. I have heard you mention them with consideration these
twenty years at least.


MRS. BENNET.

Ah! You do not know what I suffer.


LYDIA.

[_Bursting into the room, followed by_ JANE.] Oh, that horrid practice!
[_Looking back at_ JANE.] Jane does so keep me at it. [_Throwing herself
into a chair._] La, I'm tired to death.


JANE.

[_Who sees that her mother is half crying, goes and stands behind her
chair, puts her hand affectionately on her shoulder, and bends over
her._] Does your head ache, mamma?


MRS. BENNET.

Of course my head aches. Your father is so teasing. I cannot persuade
him to call on Mr. Bingley at Netherfield, so I suppose we shall never
know him.


JANE.

[_Smiling._] But you forget, mamma, that we shall meet him at the
assemblies, and Lady Lucas has promised to introduce him.


MRS. BENNET.

I do not believe Lady Lucas will do any such thing. She has daughters of
her own. She is a selfish, hypocritical woman, and I have no opinion of
her.


MR. BENNET.

No more have I, and I am glad to find that you do not depend on her
serving you.


MRS. BENNET.

I may have to depend on her after all, Mr. Bennet, since you will do
nothing to help me. [_Fretfully to_ LYDIA, _who has been yawning and
coughing._] Don't keep coughing, Lydia, for Heaven's sake! Have a little
compassion on my nerves.

[LYDIA _pouts and looks unutterable things._]


MR. BENNET.

Lydia has no discretion in her coughs. She times them ill.


LYDIA.

I do not cough for my own amusement, papa. Jane, when is your next ball?


JANE.

To-morrow fortnight.


MRS. BENNET.

[_Starting excitedly._] Ay, so it is--and Lady Lucas does not come back
till the day before. So you see it will be impossible for her to
introduce Mr. Bingley, for she will not know him herself.


MR. BENNET.

Then, my dear, you may have the advantage of your friend, and _you_ can
introduce Mr. Bingley to _her_.


MRS. BENNET.

Impossible, Mr. Bennet, when I am not acquainted with him myself. How
can you be so teasing?


MR. BENNET.

I honour your circumspection. A fortnight's acquaintance is certainly
very little. But if _we_ do not venture, somebody else will, and if
_you_ decline the office _I_ will take it upon myself.


MRS. BENNET.

[_As the two girls stare at their father._] Oh, nonsense--nonsense! I am
sick of Mr. Bingley!


MR. BENNET.

I am sorry to hear that; but why did not you tell me so before? If I had
known as much a week ago, I certainly should not have called upon him.


MRS. BENNET.

[_Springing from her chair and throwing her arms about_ MR. BENNET'S
_neck._] What! You have really called upon him? Oh, how good in you, my
dear Mr. Bennet!


MR. BENNET.

It is very unlucky; but as I have actually paid the visit--and as he
will very likely return it at any time, and bring his friend, Mr. Darcy,
with him--we cannot now avoid the acquaintance of Mr. Bingley and his
party.


MRS. BENNET.

Oh, my dear Mr. Bennet, I was sure you loved your girls too well to
neglect such an acquaintance. [MR. BENNET _deftly takes her hands from
his shoulders. She stands looking fondly at him._] Well, how pleased I
am! And it was such a good joke that you should have already paid Mr.
Bingley a visit and never said a word about it.


MR. BENNET.

Yes. Yes. Well, I must go to the library. [_He goes to the door, but
stops for a moment._] Now, Lydia, you can cough as much as you choose.
[_He goes out._]


MRS. BENNET.

[_Looking after_ MR. BENNET.] What an excellent father you have, girls!
[_Turns to the girls._] I do not know how you will ever make him amends
for his kindness, or me either, for that matter. At our time of life it
is not so pleasant to be making new acquaintances every day. But for
your sakes we would do anything. [_Looking about her._] Where is Lizzy?
Lydia, my love, where is your sister?


LYDIA.

Oh, she is out walking with Charlotte Lucas and that dismal Mr. Collins.


MRS. BENNET.

Lizzy--out walking with Mr. Collins? Why didn't _you_ go, Jane?


JANE.

I had to practise with Lydia.


LYDIA.

I'm sure I would have excused you. But what is Mr. Collins here for,
mamma? I am sure I caught Mr. Wickham and Colonel Forster laughing at
him the day we went to Meryton. Why does papa have a cousin like that?


MRS. BENNET.

He really cannot help it. It is the entail, my love--[_Mysteriously._]
But I hope that all you girls will be very civil to him, Jane
especially.


JANE.

I--mamma?


MRS. BENNET.

[_Embarrassed._] Yes--my love.--You see----

[_She is interrupted by the sound of laughter outside, and_ ELIZABETH'S
_voice._]


ELIZABETH.

Very well, Mr. Collins.

[MRS. BENNET _makes a sudden awed gesture of silence to the girls, who
fail to understand._ ELIZABETH _enters by the glass doors. She is
dressed in winter walking costume: a large hat,--fur-trimmed pelerine,
and a large muff. She stops in the doorway and looks at_ MRS. BENNET,
_half puzzled and smiling._]


ELIZABETH.

Well, what is it, mamma? What is the matter?


MRS. BENNET.

Nothing. Hush! What have you done with Mr. Collins?


ELIZABETH.

[_Laughing._] Oh, Mr. Collins is safe! He has gone round to the
library.


MRS. BENNET.

[_With a sigh of relief._] How providential!


ELIZABETH.

[_Looking back._] But I have brought someone else with me.

[MR. WICKHAM _and_ CHARLOTTE LUCAS _come in gaily._]


ALL.

[_Exclaiming._] Oh, Mr. Wickham!


WICKHAM.

[_To_ MRS. BENNET.] How do you do, Mrs. Bennet? This is indeed a
pleasure. [_Going over to_ JANE.] Miss Bennet, I am _so_ glad to see
you. [_Reproachfully._] You were not with our party! [_To_ LYDIA.] Why
do you never come to Meryton, Miss Lydia? Mr. Denny is quite downcast.


LYDIA.

[_Pouting._] La, Mr. Denny!


WICKHAM.

And many others beside him, Miss Lydia.

[LYDIA _giggles._ WICKHAM _returns to_ MRS. BENNET.]


MRS. BENNET.

Well, 'tis an age since we saw you, Mr. Wickham. What _have_ you been
doing?


WICKHAM.

Colonel Forster keeps me so busy that I have no time for enjoyment.


ELIZABETH.

Yes, Mr. Wickham bears all the marks of an harassed and overworked man.


WICKHAM.

[_Bowing to_ ELIZABETH.] Thank you, Miss Elizabeth. You have given me
the very terms I needed. [_To_ MRS. BENNET.] You see before you, Mrs.
Bennet, an harassed and overworked man. Miss Elizabeth will bear witness
that I was on my way to a business appointment when I yielded to
temptation and went off for a walk with her and Miss Lucas and their
irreproachable escort.


ELIZABETH.

And Miss Elizabeth will also testify that you yielded with the celerity
and ease of long practice.


WICKHAM.

[_Laughing; to_ ELIZABETH.] But in this case who was the tempter?


ELIZABETH.

Oh, I will admit that Mr. Collins was partially responsible.

[_All laugh._]


MRS. BENNET.

Come, Lizzy, you have been talking to Mr. Wickham all the morning. Now,
let some of the rest of us have a chance. [_Turning to_ WICKHAM.] You
must stay to dinner, Mr. Wickham.


WICKHAM.

I wish I might. That is indeed a temptation. But you know Miss Elizabeth
has just reminded me of my duty.


MRS. BENNET.

Oh, nobody ever minds Lizzy!


WICKHAM.

Truly, I cannot to-day, Mrs. Bennet. It is too bad, but I am to meet
Colonel Forster [_Smiling at_ ELIZABETH] on important _business_ at the
Drake Farm.


MRS. BENNET.

Well, I am very sorry.


WICKHAM.

[_Hesitatingly._] I might perhaps bring Colonel Forster in for a few
moments on the way back--that is, if we return this way.


ALL.

Oh, yes, do.


MRS. BENNET.

Yes, indeed. Tell Colonel Forster we should be delighted to see him.


WICKHAM.

Thank you, I will. But now I really must be gone. [_Bowing brightly to_
JANE _and_ LYDIA.] Good morning.

[_To_ CHARLOTTE LUCAS.] Good morning, Miss Lucas. You must let me hear
more about those clever plans of yours. I am vastly interested in them.
[_To_ ELIZABETH.] Good morning, Miss Elizabeth. [_Laughing._] You must
try to temper your justice with mercy the next time I join you in a
walk. [_Pausing, he looks at_ MRS. BENNET, _who is standing between her
daughters._] Do you know, Mrs. Bennet, that you always remind me of one
of my old schoolboy phrases. _Filiæ pulchræ!--Mater pulchrior!_
Good-bye.

[_He runs off laughing. He has only gone a few steps when_ LYDIA, _who
has been standing close to the door, runs out and calls to him._]


LYDIA.

Oh, Mr. Wickham!

[WICKHAM _turns and_ LYDIA _runs up to him and whispers something in his
ear._ WICKHAM _laughs, then shakes his finger at her, still laughing,
and goes off._ LYDIA _stops outside and watches him._]


JANE.

Really, mamma, I think you should speak to Lydia. She is too forward.


MRS. BENNET.

Nonsense! You are jealous.


JANE.

Jealous! Of Lydia?


MRS. BENNET.

Well, she is no more forward than any of you. All you girls are crazy
about Mr. Wickham. [_Indulgently._] But I can't wonder at it. He
certainly is a most engaging young man. What were those French words he
said to me as he went out, Lizzy?


ELIZABETH.

They were Latin, dear. He paid a very charming compliment to our pretty
mamma. He said--The daughters are lovely, but the mother is lovelier.
You know papa always says that you are handsomer than any of us.


MRS. BENNET.

My dear Lizzy, I certainly have had my share of beauty, but I don't
pretend to be anything extraordinary now. [MR. COLLINS _enters._] Oh,
Mr. Collins, there you are.


MR. COLLINS.

[_Bowing profoundly._] I do not find Mr. Bennet in the library, Madam.
Do you know where he is?


MRS. BENNET.

Why, really, Mr. Collins, I can't imagine. Did you enjoy your walk?


MR. COLLINS.

Most assuredly, Madam. The beauties of nature, not only in the
landscape, but also [_Bowing to_ ELIZABETH _and_ CHARLOTTE LUCAS.] in
the blooming countenances of my fair companions, made our expedition a
peculiarly enjoyable one.


MRS. BENNET.

Well, I am very glad of it, I am sure. [_To_ JANE _and_ LYDIA.] Girls,
we haven't told Lizzy and Charlotte the news.


ELIZABETH.

What news, mamma?


MRS. BENNET.

[_Looking at_ CHARLOTTE _with an ill-concealed triumph_.] Oh, nothing of
consequence, Lizzy, only your father has just told us that we may expect
a visit at any time from our new neighbour, Mr. Bingley, and that friend
of his who is stopping with him.


ELIZABETH.

Oh, Mr. Bingley! That will be entertaining. [_Suddenly with mischief she
turns to_ MR. COLLINS, _who all through this latter conversation has
been staring at_ JANE _with solemn persistence_.] Do not you think so,
Mr. Collins?


MR. COLLINS.

[_Starting from his absorption._] Eh? What? [_Pompously again._] Excuse
me, Miss Elizabeth, on what subject did you ask my opinion?


ELIZABETH.

I asked you if you didn't think it was a very pleasant thing to meet new
neighbours.


MR. COLLINS.

Most assuredly, Miss Elizabeth, if those neighbours are possessed of
those qualifications which redound to their own credit, and to the
edification of their friends. Otherwise, as a clergyman, I must hesitate
in my approval. [_To_ MRS. BENNET.] You realise, I am sure, Madam, the
caution which should ever be exercised where my amiable young cousins
are concerned.


ELIZABETH.

Yes, mamma, you really should be cautious.


MRS. BENNET.

Nonsense! Why, my dear Mr. Collins, we have found out all about them.
Mr. Bingley and Mr. Darcy are connected with some of the most
respectable families in England.


MR. COLLINS.

[_In amazement._] Mr. Darcy? Mr. Fitzgerald Darcy! My dear Madam, can it
be possible that you are to be honoured by a visit from him? Respectable
indeed! Why, he is the nephew of my noble patroness, Lady Catherine de
Bourg. It is true that I have never yet had the honour of meeting
him--but he frequently visits his aunt, and she has promised to bring
him on some occasion to inspect my humble abode. I am surprised,
indeed, by this civility on his part. [_Anxiously._] I only fear there
may be some mistake, for Mr. Darcy has the reputation of possessing a
very natural pride of birth; but if your information is indeed to be
relied upon, I think Lady Catherine would consent to my approval of this
visit, provided my fair cousins will keep in mind the proper attitude of
respectful humility which should be assumed toward a person of his
superior station.


ELIZABETH.

We will promise you, Mr. Collins, never for one instant to forget either
Mr. Darcy's exalted position or our own insignificance.


MR. COLLINS.

[_Looking at her with admiration._] With that assurance, Miss Elizabeth,
I think even Lady Catherine would be satisfied. So I need no longer
withhold my sanction.


ELIZABETH.

[_Curtsying._] We thank you, sir.


MR. COLLINS.

This is the very attitude of mind I could desire. [_To_ MRS. BENNET.] I
think, with your permission, I will now retire again to the library.
[_Going over smilingly to_ JANE.] There was a volume of Fordyce's
sermons that you may remember I was reading to you in this room
yesterday. I do not find it in the library. Do you know where it is?
[_Looking about him._]


JANE.

I haven't seen it, Mr. Collins. I will try to find it for you. [_She
starts as if to go out of the room._]


MRS. BENNET.

[_Wishing to leave them together._] No--no, Lydia will find it. Lydia,
my love, go see if you can find the sermons for Mr. Collins.

[LYDIA, _with a grimace, rises slowly from her chair_.]


CHARLOTTE LUCAS.

Oh, Mrs. Bennet, I am quite sure that I saw the book in the hall. I will
go fetch it.


MRS. BENNET.

[_Sharply._] On no account, Charlotte. Lydia will find the book. Lizzy,
go and get the mud off your shoes.


MR. COLLINS.

Oh, I will not trouble any of you ladies.


MRS. BENNET.

It is no trouble, Mr. Collins. Charlotte, if you will come with me, I
have a parcel I should like to send your mother.


MR. COLLINS.

But I assure you, Madam----

     [_As they go out_, MRS. BENNET--_looking daggers at_
     CHARLOTTE--_tries to keep_ MR. COLLINS _with_ JANE.]

MRS. BENNET.

Lydia will find your book, Mr. Collins.


MR. COLLINS.

On no account, Madam----

     [_With awkward gallantry_ MR. COLLINS _ushers out the
     ladies_--LYDIA _rebellious_, CHARLOTTE _somewhat offended_.]

ELIZABETH.

[_With an amused smile, having watched the party vanish, turns to_ JANE
_and speaks to her in mock-heroic fashion_.] Miss Bennet! Do you realise
the honour which is so soon to fall upon our humble home, and our
gratefully humble selves?


JANE.

[_Smiling._] Oh, Lizzy!


ELIZABETH.

Do you really grasp in its full significance the fact that we may soon
be honoured by a visit from Mr. Bingley of Netherfield and Mr.
Fitzgerald Darcy, nephew of the Lady Catherine de Bourg?


JANE.

Oh, Lizzy, Mr. Collins is a little pompous, but he seems a very
well-meaning young man--indeed, sometimes quite agreeable.


ELIZABETH.

[_Looking quizzically, but affectionately, at her sister._] No one can
be anything but agreeable in the mind of our dear Jane. This time,
however, I quite agree with you, I am as delighted as papa with Mr.
Collins. I can see that his mixture of servility and importance promises
well.


JANE.

And I think Mr. Bingley and Mr. Darcy promise well. If the half of what
our neighbours say is true, Mr. Bingley will give us all sorts of
gaieties. [_Slyly._] Who knows? We may find him as entertaining as Mr.
Wickham.


ELIZABETH.

As Mr. Wickham? Then, dear Jane, we shall be rich indeed. [_Counting on
her fingers._] For hospitality--Mr. Bingley; for conversation--Mr.
Wickham; for grandeur--Mr. Darcy, and the agreeable Mr. Collins!


JANE.

Oh, Lizzy! Can not you let the poor man alone?


ELIZABETH.

With all my heart. I will gladly let him alone. You shall have him all
to yourself. [_Mischievously._] If only Mr. Collins knew your good
opinion of him! But he is too modest to find it out for himself.


JANE.

[_Playfully pulling_ ELIZABETH'S _ear_.] You are a tease!


HARRIS.

[_Entering._] The two gentlemen from Netherfield have just brought their
horses into the paddock, Madam.


JANE.

Show them in, Harris, and speak to Mrs. Bennet at once.

[HARRIS _bows and goes out_.]


JANE.

They have come soon, Lizzy. Really this is very civil in them.


ELIZABETH.

Uncommonly civil. Come with me, Jane. I must make myself tidy. Mud and
dirty petticoats for Mr. Darcy!--Oh, that would never do.

     [_They run off, laughing. There is a short pause. Then_ MR. BINGLEY
     _and_ MR. DARCY _enter. The latter is very quiet, with an air of
     scornful hauteur_. BINGLEY, _on the contrary, has a gracious and
     animated manner_. HARRIS _ushers them in, much impressed_.]

BINGLEY.

[_To_ HARRIS.] You will announce us to Mr. Bennet and the ladies.

[HARRIS _goes out_.]

Do you know, Darcy, I believe that was George Wickham we saw just now,
going toward the Drake Farm.


DARCY.

[_Quietly._] I think there is no doubt of it.


BINGLEY.

But what is he doing here?


DARCY.

[_With assumed indifference._] Probably it is his regiment which is
stationed at Meryton.


BINGLEY.

[_Excitedly._] No, Darcy! You don't mean it! Why, confound it, if I had
had any notion of that--I ... I....


DARCY.

[_Contemptuously._] I don't think we need mind Wickham.


BINGLEY.

But I do mind! To think that I should bring you into the neighbourhood
of that rascal----

DARCY.

He must live somewhere, I suppose.


BINGLEY.

Yes, unfortunately. But, Darcy, you are a puzzle to me.--You are,
indeed! How can you speak with any charity of a man who for years abused
the patience and generous kindness of your father, and who so lately has
attempted against your family the most dastardly action that----

DARCY.

[_Interrupting him with hauteur._] We have already said too much of
George Wickham. I prefer not to discuss him further.

     [BINGLEY _turns away hurt and embarrassed_. DARCY _seeing the
     effect of his words and manner, goes to him kindly, and speaks to
     him in a changed voice_.]

Bingley, I entirely understand your indignation. Indeed, I share it so
fully that I dare not trust myself to think of the man's villainy. It is
better that I say nothing of him, even to you.


BINGLEY.

[_Moved._] I am sure, I beg your pardon, Darcy.


DARCY.

It is rather for me to ask yours.

     [_There follows an awkward pause, which BINGLEY at length breaks by
     speaking in a tone of forced gaiety_.]

BINGLEY.

Pretty place, this.


DARCY.

[_With a shrug._] Very small.


BINGLEY.

What has the size to do with it? I think we are in luck to have such
charming neighbours. You know we saw two of the young ladies going
through the lane the other day. Why, Darcy, one of them is the most
beautiful creature I ever beheld--and the other--the one with the dark
eyes--she is uncommonly pretty. Don't you think so?


DARCY.

She is tolerable, but fine eyes cannot change family connections.


BINGLEY.

[_Quickly._] What do you mean?


DARCY.

I think I have heard you say that their uncle is an attorney in
Meryton.


BINGLEY.

[_Shortly._] Yes.


DARCY.

And that they have another in London who lives somewhere near Cheapside.


BINGLEY.

[_With irritation._] If they had uncles enough to fill all Cheapside, it
wouldn't make them one jot less handsome.


DARCY.

But it must materially lessen their chances of marrying men of any
consideration in the world.


BINGLEY.

Of marrying? You go fast, Darcy.


DARCY.

Perhaps. But I am in no humour to give consequence to young ladies. I am
here to please you, Bingley--and--[_He smiles meaningly._] knowing your
disposition, I think it is just as well that I came.

     [BINGLEY _is about to reply when the door opens and_ MRS. BENNET
     _enters, followed by_ JANE _and_ ELIZABETH. _The two young men
     make ceremonious bows._ MRS. BENNET _curtsies and then advances
     with delighted fussiness_.]


MRS. BENNET.

Good morning, gentlemen. I am so sorry that Mr. Bennet has gone for his
walk.

     [_As she looks a little puzzled from one to the other_, BINGLEY
     _advances_.]

BINGLEY.

Good morning, Mrs. Bennet. I am Mr. Bingley, your new neighbour at
Netherfield. This is my friend, Mr. Darcy, of Pendleton, Derbyshire.
[_All bow and curtsy._] Mr. Bennet has been so kind as to call upon us,
and we are most happy to have the honour of waiting upon the ladies of
his family.


MRS. BENNET.

We are delighted to see you, I am sure! Mr. Bingley--Mr.
Darcy--[_Indicating_ JANE]--my eldest daughter, Miss Bennet.
[_Indicating_ ELIZABETH]--Miss Elizabeth Bennet.

[_The girls make low curtsies--the gentlemen bow._]

Will not you be seated, gentlemen? [_The guests and ladies seat
themselves._] I am sure you must like Netherfield, Mr. Bingley. I do not
know a place in the country that is equal to Netherfield. You will not
think of quitting it in a hurry, I hope, though you have but a short
lease.


BINGLEY.

Whatever I do is done in a hurry, Mrs. Bennet, and therefore if I should
resolve to quit Netherfield I should probably be off in five minutes. At
present, however, [_looking intently at_ JANE] I consider myself as
quite fixed here.


JANE.

It is very pleasant to have Netherfield open once more, although you
must both miss London. There is so much gaiety in London.


DARCY.

Yes, in a country neighbourhood you move in a confined and unvarying
society.

[MRS. BENNET _looks vexed at this speech_.]


ELIZABETH.

But people themselves alter so much that there is something new to be
observed in them forever.

[DARCY _turns and looks at_ ELIZABETH _with surprise and interest_.]


BINGLEY.

Then you are a student of character, Miss Elizabeth. It must be an
amusing study.


MRS. BENNET.

Yes, Lizzy always likes to watch people. [_Looking at_ DARCY.] And there
are plenty of people about, even if you do live in the country. The
country is a vast deal pleasanter than London, is not it, Mr. Bingley?


BINGLEY.

When I am in the country I never wish to leave it, and when I am in town
it is pretty much the same. They have each their advantages and I am
equally happy in either.


MRS. BENNET.

Ay--that is because _you_ have the right disposition. [_Looking at_
DARCY.] But that gentleman seemed to think the country was nothing at
all.


ELIZABETH.

[_Quickly._] Indeed, mamma, you are mistaken. You quite mistook Mr.
Darcy. He only meant that there is not such a variety of people to be
met with in the country as in town, which you must acknowledge to be
true.


MRS. BENNET.

Certainly, my dear, nobody said there was--but as to not meeting with
many people in this neighbourhood, I believe there are few
neighbourhoods larger. I know we dine with four-and-twenty families.

     [_As all become embarrassed at this speech_, BINGLEY _comes to the
     rescue_.]

BINGLEY.

Yes, there are many fine estates hereabout. Can you see Sir William
Lucas' place from the garden? I am not quite sure I have placed it.


MRS. BENNET.

Oh, yes, there is a fine view of the chimneys from the terrace. Sir
William is our nearest neighbour. Such an agreeable man--so genteel, and
so easy---- [_Rising, she goes toward the glass doors._] Come, Jane, we
must show Mr. Bingley Sir William's chimneys.

     [MRS. BENNET, BINGLEY, _and_ JANE _go out upon the terrace_.]

ELIZABETH.

[_Smiling mischievously._] Would not you also like to see the chimneys,
Mr. Darcy?


DARCY.

Thank you. Like yourself, I prefer people to places.


ELIZABETH.

Did I say that?


DARCY.

Not precisely. But I have drawn that conclusion.


ELIZABETH.

[_Gathering her sewing materials, begins to embroider._] Well, I can
laugh at people better than places, and I dearly love a laugh.


DARCY.

Isn't that rather a dangerous trait, Miss Bennet? The wisest and the
best of men may be rendered ridiculous by a person whose first object in
life is a joke.


ELIZABETH.

Certainly. But I hope I never ridicule what is wise or good. Whims and
inconsistencies do divert me, I own, and I laugh at them whenever I can.
[_Mischievously._] But these, I suppose, are precisely what you are
without.


DARCY.

Perhaps that is not possible for anyone. But it has been the study of my
life to avoid those weaknesses which often expose a strong understanding
to ridicule.


ELIZABETH.

And in your list of weaknesses do you include such faults as vanity and
pride, for instance?


DARCY.

Yes, vanity is a weakness, indeed, but _pride_, where there is a real
superiority of mind--pride will be always under good regulation.


ELIZABETH.

I am perfectly convinced, Mr. Darcy, that you have no defect.


DARCY.

I have made no such pretension, Miss Bennet. I have faults enough. My
temper I dare not vouch for. I cannot forget the follies and vices of
others against myself. My good opinion once lost is lost forever.


ELIZABETH.

That is a failing, indeed. Implacable resentment _is_ a shade in a
character. But you have chosen your fault well. I really cannot laugh at
it. You are safe from me.


DARCY.

There is, I believe, in every disposition a tendency to some particular
evil--a natural defect which not even the best education can overcome.


ELIZABETH.

And your defect is a propensity to hate everybody.


DARCY.

[_Smiling._] And yours to wilfully misunderstand them.

     [_Voices are heard outside._ ELIZABETH _applies herself to her
     embroidery_. BINGLEY, JANE, _and_ MRS. BENNET _return from the
     terrace_.]

BINGLEY.

The surrounding country is really charming, Mrs. Bennet.


MRS. BENNET.

_We_ think so. But you must give us a ball at Netherfield, Mr. Bingley,
and then you will see that some of the people who live here are worth
knowing.


ELIZABETH.

[_Distressed._] Oh, mamma!


JANE.

Mamma!


BINGLEY.

Certainly, Mrs. Bennet. I had already decided upon it. I told Mr. Darcy
only yesterday that as soon as my sister, Miss Bingley, arrived, and
Nicholas could make white soup enough, I should send out my cards. Did
not I, Darcy?


DARCY.

[_Very stiffly._] I believe you did.


MRS. BENNET.

Well, that is vastly good in you, Mr. Bingley; and then, perhaps, your
friend may change his mind about the country. [_To_ DARCY.] You didn't
come to admire Sir William's chimneys, Mr. Darcy.


DARCY.

I was admiring your daughter's work, Madam.


MRS. BENNET.

Oh, you should see Jane's work. Lizzy is all for books, like her father.
She is a great reader and has no pleasure in anything else. Jane, show
your embroidered parrot to Mr. Bingley.


JANE.

I do not think Mr. Bingley would be interested, ma'am.


BINGLEY.

[_Eagerly._] Oh, indeed, I should, Miss Bennet; I am very much
interested in parrots.--Pray show it to me.


MRS. BENNET.

Yes, and the new hand-screen. I will find it for you.

     [_All three withdraw, leaving_ ELIZABETH _and_ DARCY _together_.]

DARCY.

And so you are a great reader and take no pleasure in anything else?


ELIZABETH.

Mamma does not understand. I deserve neither such praise nor such
censure. I am _not_ a great reader, and I have pleasure in many things.


DARCY.

So I should have thought.


BINGLEY.

[_Looking at the screen which he holds in his hand._]

It is amazing to me how young ladies can have patience to be so very
accomplished as they are; to think how you all paint tables and cover
screens and net purses. It is quite wonderful.


ELIZABETH.

Do you agree with your friend, Mr. Darcy?


DARCY.

His list of the common extent of accomplishments has too much truth. But
I cannot boast of knowing more than half a dozen young ladies in the
whole range of my acquaintance that are really accomplished.


ELIZABETH.

Then you must comprehend a great deal in your idea of an accomplished
woman.


DARCY.

Perhaps. To deserve the word, a woman must have a thorough knowledge of
music, singing, drawing, dancing, and the modern languages. She must
also possess a certain something in her air and manner of walking--the
tone of her voice--her address and expression, and to all this she must
yet add something more substantial--[_With a little bow to_ ELIZABETH.]
in the improvement of her mind by extensive reading.


ELIZABETH.

[_Laughing._] I am no longer surprised at your knowing only six
accomplished women! I rather wonder at your knowing any.


HARRIS.

[_Enters and announces._] Colonel Forster and Mr. Wickham.

[_The gentlemen enter, smiling._]


WICKHAM.

Here I am again, Mrs. Bennet. I found that Colonel Forster had a message
for the young ladies.


MRS. BENNET.

I am delighted to see you. You are just in time to meet our new
neighbours. [_Introducing the gentlemen._] Colonel Forster, Mr.
Wickham--Mr. Bingley, Mr. Darcy.

     [_As the gentlemen enter_, MR. DARCY _has his back turned to them
     in conversation with_ ELIZABETH. _At the sound of_ WICKHAM'S _voice
     he starts and turns so that he faces the latter just in time for
     the introduction. At sight of_ DARCY, WICKHAM _starts and is
     greatly confused_. DARCY _stiffens and scarcely nods when_ WICKHAM
     _is introduced. The whole situation is so marked that everyone
     looks on with an astonishment to which_ MRS. BENNET _gives audible
     expression_.]

MRS. BENNET.

Well, well! If ever there was a proud, stiff man----

JANE.

[_In a dismayed whisper._] Mamma!


BINGLEY.

[_Looking distressed, speaks hurriedly._] Oh, Mrs. Bennet, I'm sorry
that we cannot wait for Mr. Bennet. We--we--were on the way to meet my
steward--and we are already late for the appointment.


MRS. BENNET.

[_Effusively._] I am very sorry you must go, Mr. Bingley. But I hope you
will come again. We must engage you soon for dinner.


BINGLEY.

[_In an absent and worried way._] It will be a pleasure.

[_Then with bows, the party moves toward the door._]


MRS. BENNET.

[_Bustling._] Your best way to the paddock is by the terrace.

     [_The gentlemen have almost reached the glass doors when_ MR.
     COLLINS _comes in excitedly, putting himself directly in the way
     of_ BINGLEY _and_ DARCY.]

MR. COLLINS.

My dear Miss Elizabeth, I have this moment found out by a singular
accident that there is now in this room a near relation of my patroness
Lady Catherine de Bourg. Will you present me?

     [_He looks enquiringly from one to the other of the young men._]

ELIZABETH.

Mr. Bingley, allow me to present my cousin, Mr. Collins--Mr. Darcy--Mr.
Collins.


MR. COLLINS.

[_Taking almost no notice of_ MR. BINGLEY, _he greets_ MR. DARCY _with
servile effusion_.] My dear sir--I trust you will pardon me for not
having paid my respects before. My total ignorance of your presence here
must plead my apology. [_Looking severely about him at the ladies._] I
was not informed of it. Is there any message, sir, which I could take
from you to my honoured patroness--your aunt, or to your fair
cousin--Miss de Bourg?


DARCY.

[_Stiffly._] Thank you, I will not trouble you so far.


MR. COLLINS.

It would be no trouble--but an honour and a privilege.


DARCY.

[_Disgusted, turns from him to_ BINGLEY.] We are already very late,
Bingley.


BINGLEY.

Yes,--we have no time to lose.

     [DARCY _and_ BINGLEY _give passing bows and go out by the glass
     doors_. MR. COLLINS _keeps by_ DARCY'S _side and, as they pass out
     of sight, is seen still talking to him, to his evident annoyance.
     All the time that the party is bidding good-bye to_ BINGLEY _and_
     DARCY, WICKHAM _has been moodily standing by the fireplace_.
     ELIZABETH _has evidently been concerned about him, for throughout
     the foregoing interview with_ MR. COLLINS, _she has looked at_
     WICKHAM _from time to time_.]

HILL.

[_Enters at the door leading to the hall._] May I speak to you, Madam?


MRS. BENNET.

Yes, Hill, yes. [_To the gentlemen._] Excuse me for a moment. I will
return directly. [MRS. BENNET _and_ HILL _go out_.]


COLONEL FORSTER.

Oh, Miss Bennet, Miss Elizabeth! Your aunt, Mrs. Phillips, has sent word
by me that her card-party is to be on Wednesday. She hopes you will
surely be there.


ELIZABETH.

[_In a pre-occupied way, looking towards_ WICKHAM.] Oh, yes, we shall
go.


COLONEL FORSTER.

[_As he passes the piano, and looking at some music which is on the
rack._] Ah! Here is the song you have promised to sing to me. Pray sing
it now, Miss Elizabeth.


ELIZABETH.

Really, Colonel Forster, you must excuse me for to-day. Jane will play
for you, instead.


JANE.

Indeed, I cannot, Lizzy.


ELIZABETH.

[_Looking meaningly at her._] _Please_, Jane.


COLONEL FORSTER.

Oh, do, I beg--Miss Bennet.

     [_All through the following interview between_ ELIZABETH _and_
     WICKHAM, _the tinkle of the instrument is heard. During their
     conversation_ JANE'S _back is_ _turned--also_ COLONEL FORSTER'S _as
     he looks over her music--so that_ ELIZABETH _and_ WICKHAM _are
     practically alone_. ELIZABETH _returns to her embroidery. There is
     an awkward pause for a moment._ WICKHAM _finally breaks it_.]

WICKHAM.

How long has Mr. Darcy been in Hertfordshire, Miss Elizabeth?


ELIZABETH.

Only for a very short time, I believe. He comes from Derbyshire, I
understand, and has a very large property there.


WICKHAM.

Yes, his estate is a noble one. A clear ten thousand per annum. I am
well informed on this head---- [_Hesitates._] I have been connected with
Mr. Darcy's family in a particular manner since my infancy.


ELIZABETH.

[_Surprised._] Indeed?


WICKHAM.

You may well be surprised, Miss Elizabeth, at this assertion after
seeing the very cold manner of our meeting just now. [_After a pause._]
Are you much acquainted with Mr. Darcy?


ELIZABETH.

No. Though I have heard of him, I met him for the first time to-day, but
even on this short acquaintance I should take him to be an ill-tempered
man.


WICKHAM.

[_As if he had come to a sudden decision._] Miss Elizabeth, you have
been a witness of Mr. Darcy's treatment of me to-day, and therefore I
feel that I must, for my own justification, acquaint you with the facts
of my past connection with him.


ELIZABETH.

I shall respect your confidence, Mr. Wickham.


WICKHAM.

I am sure of it. [_After a short pause._] Mr. Darcy and I were born in
the same parish. My own father, who, to be frank, was steward of the
Darcy estates, gave up everything to serve the interests of the Darcy
family. Mr. Darcy's father was excessively attached to me:--indeed, I
was his godson. He meant to provide for me amply, and thought he had
done so. I was destined for the church and Mr. Darcy's father left to me
a most valuable living. But the present Mr. Darcy chose to ignore his
father's will and gave the living to another man. This closed for me the
career for which I was most fitted and left me with almost no means of
support.


ELIZABETH.

Good heavens! But how could that be? Why did not you seek legal redress?


WICKHAM.

There was an informality in the terms of the will which gave me no hope
from the law. Mr. Darcy's father had relied implicitly upon the honour
of his son.


ELIZABETH.

But--this is quite shocking. Mr. Darcy deserves to be publicly
disgraced!


WICKHAM.

Sometime or other he will be, but not by me. Till I can forget his
father, I can never defy or expose him.


ELIZABETH.

This feeling does you honour. But what can have induced Mr. Darcy to
behave so cruelly?


WICKHAM.

I must attribute it in some measure to his jealousy. His father's
uncommon attachment to me irritated him, but the fact is, Miss
Elizabeth, as you can see, we are very different men, and he hates me.


ELIZABETH.

His disposition must be dreadful.


WICKHAM.

I will not trust myself on that subject.


ELIZABETH.

To treat in such a manner the godson--the friend--the favourite of his
father! How abominable!


WICKHAM.

And yet, Miss Elizabeth, we must try to be just to him. Mr. Darcy has
many good qualities. He can be both liberal and generous. He has also a
brother's affection and pride which makes him a careful guardian of his
sister.


ELIZABETH.

Oh, he has a sister?


WICKHAM.

Yes. You will hear him cried up as the most attentive and best of
brothers. Oh, Mr. Darcy can please when he chooses. Among those who are
his equals he is a very different man from what he is to the less
prosperous.


ELIZABETH.

Contemptible!


COLONEL FORSTER.

[_Interrupting._] Wickham!


WICKHAM.

[_Starting._] Yes, Colonel Forster.


COLONEL FORSTER.

I fear we must be going.


WICKHAM.

[_Hurriedly to Elizabeth._] Thank you for listening to me. It is hard to
be misjudged.


ELIZABETH.

Thank you for your confidence. It is well to know the truth.


COLONEL FORSTER.

Well, Miss Elizabeth, I hope we shall see you all at your aunt's on
Wednesday. Good morning. [_To_ JANE.] Good morning, Miss Bennet. Thank
you for the music. Please present my respects to Mrs. Bennet. I am sorry
that we cannot wait longer.


WICKHAM.

[_Effusively._] Yes, Miss Bennet, be sure to give your mother my best
regards. Good morning--[_All bow and curtsy. As he is leaving he speaks
aside._] Oh, Miss Elizabeth, may I entreat----

ELIZABETH.

You may depend upon my sympathy.


WICKHAM.

[_Looking at her with an understanding smile._] I am most grateful.

     [_The gentlemen go out of the door._ JANE _and_ ELIZABETH _go into
     the recess and look from the window. There is a short pause._]

MRS. BENNET.

[_Enters, flurried, and looks about her._] Well, have they gone?

     [MR. COLLINS _enters through the glass doors at the center. He
     sees_ MRS. BENNET.]

MR. COLLINS.

Oh, Madam, I am just returned from attending on Mr. Darcy. Such a
privilege! He was most condescending. I was able to tell him that Lady
Catherine was very well on Saturday sennight. He is very like Lady
Catherine. I am sure you must have been impressed by his distinguished
manners.


MRS. BENNET.

Well, really, Mr. Collins!

     [_A titter is heard from the recess where the girls are seated, and
     then_ JANE'S _voice_.]

JANE.

Oh, Lizzy, hush!


MR. COLLINS.

[_Hearing this, turns and discovers the two girls. Then he speaks to_
MRS. BENNET _with lowered voice, as if an idea had just come to him_.]
This meeting is most opportune. Will you kindly step this way for a
moment? [_He draws_ MRS. BENNET _aside_.] May I hope, Madam, for your
interest with your fair daughter Jane, in the matter on which we were
speaking yesterday? I would solicit the honour of a private audience
with her this morning.


MRS. BENNET.

Certainly, Mr. Collins. [_Hesitating._] But there have been some changes
since then. Some things have happened--I think it is right you should
know, that--that Jane is very likely to be soon engaged.
[_Encouragingly._] But there is Elizabeth. I cannot take it upon myself
to say--I cannot possibly answer--but I do not know of any prepossession
in her case, and I am sure she can have no objection to listen to you.

[MRS. BENNET _goes to the fire and stirs it_.]


MR. COLLINS.

[_As soon as she has finished._] Then Miss Elizabeth let it be, Madam. I
was struck by her attitude of respectful awe when I mentioned the Lady
Catherine de Bourg. Such modesty and humility of mind cannot but
recommend her to my patroness.


MRS. BENNET.

[_Looking rather astonished at this last speech, but recovering
herself._] Yes, my daughter Elizabeth knows what is proper. She will be
very happy to listen to you. Shall I call her now?


MR. COLLINS.

I think, Madam, there should be no further loss of time, as my leave of
absence extends only to the coming Saturday.


MRS. BENNET.

Very well--[_She goes to the recess where the two girls are talking
together._] Jane, I want you upstairs. Lizzy, Mr. Collins has something
he wishes to say to you.


ELIZABETH.

[_Suspicious and dismayed._] Dear ma'am, Mr. Collins must excuse me. I
was just going away myself.


MRS. BENNET.

Now, no nonsense, Lizzy! I desire you will stay. Mr. Collins has
something _very_ particular to say to you. [_As_ ELIZABETH _tries to
escape_.] Lizzy, I insist upon your staying and hearing Mr. Collins.
Come, Jane--[MRS. BENNET _and_ JANE _go out_.]


MR. COLLINS.

[_Approaching_ ELIZABETH, _who does not move from the place where her
mother left her_.] Believe me, my dear Miss Elizabeth, your modesty so
far from doing you any disservice rather adds to your other perfections.
But allow me to assure you that I have your respected mother's
permission for this address. [_He escorts_ ELIZABETH _with clumsy
gallantry to the sofa, then brings a chair and seats himself opposite to
her_. ELIZABETH _has recovered herself sufficiently to begin to enjoy
the humour of the situation_.] My fair cousin, you must have at least
surmised that I am about to ask you to become the companion of my life.
And perhaps I had better begin by stating my reasons for this decision
before I am run away with by my feelings on this subject. [ELIZABETH _is
so overcome with laughter at this idea that she can hardly speak, or
keep a decent countenance_.]


ELIZABETH.

Oh, I beg, Mr. Collins----

MR. COLLINS.

One moment. My reasons for marrying are, first,--that I think it a right
thing for every clergyman to set the example of matrimony to his parish;
second, I am convinced it will add very greatly to my happiness; third,
it is the particular advice of that very noble lady whom I have the
honour of calling patroness.


ELIZABETH.

[_With more command of her voice._] Believe me, Mr. Collins----

MR. COLLINS.

Excuse me--one moment. It remains only to be told why my views were
directed to Longbourn instead of to my own neighbourhood. The fact is
that, being as I am to inherit this estate after the death of your
father (who, however, may live many years longer), I could not satisfy
myself without resolving to choose a wife from among his daughters, that
the loss to them might be as little as possible, when the melancholy
event took place. This has been my motive, my fair cousin, and I flatter
myself it will not sink me in your esteem.


ELIZABETH.

Mr. Collins,--I----

MR. COLLINS.

[_Rising and approaching nearer to_ ELIZABETH.] Still one moment more!
And now nothing remains for me but to assure you, in the most animated
language, of the violence of my affection. To fortune I am perfectly
indifferent, and you may assure yourself that no ungenerous reproach on
that score shall ever pass my lips when we are married.


ELIZABETH.

[_Rising in her turn._] You are too hasty, sir! You forget that I have
made no answer. Accept my thanks for the compliment you are paying me. I
am very sensible of the honour of your proposals, but it is impossible
for me to do otherwise than decline them.


MR. COLLINS.

[_With another formal wave of the hand._] I am not unmindful of the fact
that sometimes a young lady's refusal is repeated a second or even a
third time. I am, therefore, by no means discouraged by what you have
just said, and I shall hope to lead you to the altar ere long.


ELIZABETH.

Upon my word, sir, your hope is rather an extraordinary one after my
declaration! You must pay me the compliment of believing what I say. I
wish you very happy, and very rich, and, by refusing your hand, do all
in my power to prevent your being otherwise. This matter may be
considered, therefore, as definitely settled.

     [_She is about to leave the room when_ MR. COLLINS _detains her_.]

MR. COLLINS.

One moment. When I do myself the honour of speaking to you next on this
subject, I shall hope to receive a more favourable answer.


ELIZABETH.

[_Becoming angry._] Really, Mr. Collins, you puzzle me exceedingly. I
know not how to express my refusal in such a way as may convince you of
its being one.


MR. COLLINS.

You must give me leave to flatter myself, my dear cousin, that your
refusals of my address are merely words, of course. I shall choose to
attribute them to your wish of increasing my love by suspense, according
to the usual practice of elegant females.


ELIZABETH.

[_Very decidedly._] Please do not consider me now as an 'elegant
female'; I would rather be paid the compliment of being believed
sincere. To accept your proposal is absolutely impossible. Can I speak
plainer?


MR. COLLINS.

[_With awkward gallantry._] You are uniformly charming; but I am
persuaded that when my proposals are sanctioned by both your parents
they will not fail of being acceptable. Meanwhile I may perhaps best
serve my cause by leaving you to consider the matter by yourself for a
while.

     [_He bows and withdraws to the door._ ELIZABETH _with a gesture as
     if she gave the whole matter up in despair, and yet half amused,
     goes to the fireplace. Just as_ MR. COLLINS _reaches the door_ MRS.
     BENNET _opens it_.]

MRS. BENNET.

Well, Mr. Collins, are we to congratulate each other? [_Looking
doubtfully at_ ELIZABETH.] Has all gone as you could wish?


MR. COLLINS.

I have every reason to be satisfied, Madam. My cousin has indeed
steadily refused this, my first offer, and with considerable warmth, but
this refusal would naturally flow from her bashful modesty. With your
influence behind me, I have no doubt of my ultimate success.


MRS. BENNET.

Yes, you may depend upon me, Mr. Collins. I will speak to Lizzy myself
directly. She is a very headstrong, foolish girl and does not know her
own interest. But I will make her know it.


MR. COLLINS.

[_Alarmed._] Pardon me, Madam, but if she is really headstrong and
foolish, I know not whether she would altogether be a very desirable
wife to a man in my situation. If, therefore, Miss Elizabeth persists in
rejecting my suit, perhaps it were better not to force her into
accepting me.


MRS. BENNET.

[_Alarmed in her turn._] Sir, you quite misunderstand me. Lizzy is only
headstrong in such matters as these. In everything else she is as
good-natured a girl as ever lived. Let me see her alone for a moment.
That will be the best.


MR. COLLINS.

But Madam--I----

MRS. BENNET.

[_Almost forcing_ MR. COLLINS _out of the room_.] Oh, I shall very soon
settle it with her, I am sure. [MR. COLLINS _goes out_. MRS. BENNET
_goes quickly to_ ELIZABETH.] Lizzy, what is the meaning of all this?
Have you refused Mr. Collins?


ELIZABETH.

Yes, mamma, but please listen----

MRS. BENNET.

[_Angrily._] No, I will not listen. I tell you what, Miss Lizzy, if you
take it into your head to go on refusing every offer of marriage in this
way, you will never get a husband at all. I am going at once to the
library and speak to your father. You will listen _to him_ perhaps.

     [MRS. BENNET _starts to go when she sees_ MR. BENNET _outside
     passing the glass doors. He is just returning from his walk and
     carries a book under his arm_.]

MRS. BENNET.

Oh, there he is now! [_She runs to the door, and opens it._] Oh, Mr.
Bennet--Mr. Bennet! [MR. BENNET _turns_. MRS. BENNET _runs out, takes
him by the arm, and tries to pull him into the room by main force_. MR.
BENNET, _puzzled, submits_.]


MRS. BENNET.

[_While she draws_ MR. BENNET _into the room_.] Oh, Mr. Bennet, you are
wanted immediately. We are all in an uproar. You must come and make
Lizzy marry Mr. Collins, for she vows she will not have him, and, if you
do not make haste, Mr. Collins will change his mind and not have _her_.


MR. BENNET.

I have not the pleasure of understanding you. Of what are you talking?


MRS. BENNET.

Of Mr. Collins and Lizzy! Lizzy declares she will not have Mr. Collins,
and Mr. Collins begins to say he will not have Lizzy.


MR. BENNET.

Lizzy? I thought it was Jane.


MRS. BENNET.

No--no--It's Lizzy now!


MR. BENNET.

Ah! And what am I to do on the occasion? It seems a hopeless business.


MRS. BENNET.

Speak to Lizzy. There she is. [_Pointing to_ ELIZABETH _at the
fireplace_.] Tell her that you insist upon her marrying him.


MR. BENNET.

[_Turning to_ ELIZABETH.] Come here, child. [ELIZABETH _goes to her
father_.] This is an affair of importance. I understand that Mr. Collins
has made you an offer of marriage. Is this true?


ELIZABETH.

Yes--papa--it--is.


MR. BENNET.

Very well--and this offer of marriage you have refused.


ELIZABETH.

I have, sir.


MR. BENNET.

We now come to the point. Your mother insists upon your accepting him.
Is it not so, Mrs. Bennet?


MRS. BENNET.

Yes, or I will never see her again!


MR. BENNET.

An unhappy alternative is before you, Elizabeth. From this day, you must
be a stranger to one of your parents. Your mother will never see you
again, if you do _not_ marry Mr. Collins; and _I_ will never see you
again if you _do_.




ACT II


     _The Conservatory or Orangery at Netherfield. On one side, an
     archway, approached by two or three steps and hung with curtains,
     separates the Orangery from the ball-room. On the opposite side is
     a smaller archway with curtains, which are looped back, giving a
     glimpse of the drawing-room beyond. There is another door on the
     right._ BINGLEY _is discovered directing two_ FOOTMEN, _who are
     putting a bench in place_. DARCY _stands watching him_.


BINGLEY.

A little more to the right, Martin. That will do. Push those lights
farther back--behind the trees. Yes, that is better. [_Looking about
him._] I think that is all. You may go. [_The men leave the room._]
Well, Darcy, do you approve of the arrangements? Have you anything to
suggest? Any criticisms?


DARCY.

I have no criticisms for the arrangements.


BINGLEY.

[_Laughing._] But you have for the _ball_. Yes, I know--still I was
really obliged to keep my promise.


DARCY.

I am glad to find that a promise is with you an obligation.


BINGLEY.

Oh, come, Darcy! I understand. Set your mind at rest. I am going to
London with you, although I must say I do not see the necessity for it.
I think you are exaggerating the effect of any small attentions of mine
toward Miss Bennet. However, we will cling together, and fly a common
danger.


DARCY.

[_Coldly._] Common danger?


BINGLEY.

[_Smiling._] Yes, common danger! I, too, have eyes. Where will you match
the wit and vivacity of Miss Elizabeth Bennet?


DARCY.

[_Quietly._] She is indeed charming, and I admit that were it not for
the inferiority of her connections, I might be in some danger. [_Very
coolly and confidently._] But they form, for me, an insurmountable
barrier against any possible peril.


BINGLEY.

Love laughs at bars, Darcy! [DARCY _looks annoyed_.] No,--I won't! It
really is not fair, since it is my fault. You would never have been put
to this test if you hadn't been so good as to stay on here with me after
that----

[_Stopping suddenly, and with an entire change from his former bantering
tone, he says in a hesitating manner._] Darcy, do you really think you
should be silent about Wickham?


DARCY.

[_Haughtily._] Decidedly! I do not choose to lay my private affairs
before the world.


BINGLEY.

But the fellow is sailing under false colours. You do not know what the
result may be. I really must speak of this again, Darcy, even at the
risk of offending you. [DARCY _makes an impatient gesture_.] I am truly
concerned at the foothold this rascal has already gained in the Bennet
family. What he has failed to accomplish once he may succeed in again.
These young ladies have no brother to defend them.


DARCY.

Neither have they the wealth to excite Wickham's cupidity. At any rate I
do not wish to be the one to enlighten the neighbourhood. Besides, I
understand that he has left Meryton.


BINGLEY.

Even so--I---- [_He is interrupted by_ MISS BINGLEY, _who enters gaily
from the drawing-room_.]


MISS BINGLEY.

Ah! Here you are! [_To_ DARCY.] Will you be so kind? [_She holds out
her arm for him to clasp her bracelet._] Your sister Georgiana should be
here, Mr. Darcy. [_To her brother._] Charles, you should have insisted
on her coming.


BINGLEY.

I am not in the habit of insisting with Darcy.


MISS BINGLEY.

[_Laughingly._] Very true. [_To_ DARCY, _who has at length succeeded in
fastening the bracelet_.] Thank you. [_Looking about her._] It is vastly
pretty, Charles, but I am much mistaken if there are not some among us
to whom a ball will be rather a punishment than a pleasure.


BINGLEY.

[_Laughing._] If you mean Darcy, he may go to bed, if he pleases, before
it begins.


MISS BINGLEY.

But, Charles, it would certainly be more rational if conversation
instead of dancing were made the order of the day.


BINGLEY.

Much more rational, my dear Caroline, but it would not be near so much
like a ball.


MARTIN, THE FOOTMAN.

[_Entering, to_ BINGLEY.] Several of the carriages have arrived, sir,
and the guests will soon be entering the ball-room.


BINGLEY.

[_To the_ FOOTMAN.] Very well. [_To_ MISS BINGLEY.] Come Caroline, we
must be at our post. We will leave Darcy to make up his mind whether he
will join us later.

     [BINGLEY _and his sister disappear through the archway leading to
     the ball-room_. DARCY _does not follow them, but walks thoughtfully
     up and down the room. The sound of a voice is heard announcing_.]

THE VOICE.

Mrs. Long--the Miss Longs. [_A pause._] Colonel Forster and Mr. Denny.
[_A pause._] Mr. and Mrs. Goulding. [_A pause._] Mrs. Bennet--the Miss
Bennets. [DARCY _stops in his walk and goes toward the ball-room
archway--then he walks once more up and down_.] Mrs. King--Miss King.
[DARCY _again moves toward the ball-room; he lifts the curtain,
hesitates--looks in--then disappears_.] Sir William and Lady Lucas--Miss
Lucas--Mr. Robinson.

     [_The music now begins, the stage is left empty. After a short
     pause_, ELIZABETH _and_ CHARLOTTE _appear between the curtains of
     the ball-room archway_.]

CHARLOTTE.

[_Peeps in--then enters._] Isn't this pretty! Come in here for a moment,
Eliza. I want to tell you something.


ELIZABETH.

[_Following her._] Why _did_ I promise to dance with Mr. Darcy just now!
Why did not I have more presence of mind!

     [_They sit on the bench together while they talk; the guests, at
     the back, pass to and from the drawing-room and ball-room, and the
     sound of music is heard faintly._]

CHARLOTTE.

I dare say you will find him very agreeable.


ELIZABETH.

Heaven forbid! That would be the greatest misfortune of all. To find a
man agreeable whom one is determined to hate! Do not wish me such an
evil.


CHARLOTTE.

I wouldn't be a simpleton, Eliza. You are angry because Wickham is not
here, but I wouldn't allow my fancy for him to make me unpleasant in the
eyes of a man of ten times his consequence.


ELIZABETH.

My _fancy_ for Wickham, as you choose to call it, is simply my sympathy
for a most ill-used man: also the relief of meeting with good manners
and a good understanding after the insufferable pride of Mr. Darcy, and
the stupid pomposity of that _dreadful_ Mr. Collins! [CHARLOTTE
_starts_.] Oh, my dear Charlotte, I have never thanked you half enough
for helping us to endure that man. It was so good-natured in you to
sacrifice yourself by listening to those interminable speeches of
his.--I am more obliged to you than I can express. But oh, what a relief
it is to know that he is really gone!


CHARLOTTE.

[_Who has listened to all this tirade in increasing embarrassment._] Oh,
don't! Don't, Eliza! You are making it so terribly hard for me.
But,--but I must tell you.--I am engaged to Mr. Collins!

     [ELIZABETH _is stupefied with surprise and looks at_ CHARLOTTE _for
     a moment in silent and incredulous amazement. Then with difficulty
     she speaks._]

ELIZABETH.

Engaged! Engaged to--to Mr. Collins! Oh, my dear
Charlotte--_impossible_! [_Hopefully._] You are joking!


CHARLOTTE.

[_With spirit._] No, indeed, Eliza, I am in most serious earnest. Why
should you be so surprised? Do you think it incredible that Mr. Collins
should be able to procure _any_ woman's good opinion, because he was not
so happy as to succeed with you?


ELIZABETH.

[_Confused._] Oh, no--no--of course not. And,--and you must forgive all
I have just said. I couldn't possibly have imagined----

CHARLOTTE.

[_More sweetly._] No, Eliza, indeed you could not. [_She puts her hand
on_ ELIZABETH'S _shoulder_.] And we shall be friends still?


ELIZABETH.

Why, of course, of course, dear Charlotte. It was only the--the
surprise. You know how fond I am of you. You know I wish you all
imaginable happiness.


CHARLOTTE.

Yes, I am sure of it. You must be surprised--very much surprised, so
lately as Mr. Collins was wishing to marry you. But, dear Eliza, when
you have had time to think it all over, I hope you will be satisfied
with what I have done. I am not romantic. I ask only a comfortable home,
and, considering Mr. Collins' situation in life, I am convinced that my
chance of happiness with him is as fair as most people can boast on
entering the marriage state.


ELIZABETH.

[_In an absent manner._] Undoubtedly.


CHARLOTTE.

[_Looking at Elizabeth affectionately and wistfully._] And you will come
to visit me sometimes? I could not bear to lose you, Eliza!


ELIZABETH.

[_Looking up, and patting_ CHARLOTTE'S _hand_.] Surely, Charlotte!
[_Smiling._] We are to be cousins, you know.


CHARLOTTE.

[_Cheerfully._] Why, so we are!

[COLONEL FORSTER _comes from the ball-room_. LYDIA _and_ DENNY _enter
from the drawing-room_.]


COLONEL FORSTER.

[_Hurriedly going to_ CHARLOTTE.] I am to have the honour of this reel,
I believe, Miss Lucas.


CHARLOTTE.

Oh yes, Colonel Forster.

     [_She goes out with_ FORSTER, _leaving_ ELIZABETH _alone, still
     seated_. LYDIA _and_ DENNY _approach_ ELIZABETH.]

LYDIA.

I think we are being treated abominably ill, Lizzy! It seems that Mr.
Wickham has gone off on business somewhere, so he will not be here at
all. [LYDIA _looks off toward the ball-room_.]


DENNY.

[_Aside to_ ELIZABETH _significantly_.] I do not imagine his business
would have called him away just now if he had not wished to avoid a
certain gentleman.


LYDIA.

[_Suddenly._] Why, Mr. Denny--I do believe the reel is half over--I
dearly love a reel! We shall miss it, altogether. Come! [_She drags_
DENNY _off_.]


ELIZABETH.

[_Alone._] Well! Well! The world is surely upside down. Charlotte
and--Collins! _What_ a match!


DARCY.

[_Approaching from the ball-room._] Do not you feel a great inclination,
Miss Bennet, to seize such an opportunity of dancing a reel?

[ELIZABETH _makes no answer_.]

Do not you enjoy the reel, Miss Bennet?


ELIZABETH.

[_Looking up._] Oh, I heard you before, but I could not immediately
determine what to say in reply. You wanted me, I know, to say--"Yes,"
that you might have the pleasure of despising my taste; but I always
delight in overthrowing that kind of scheme. I have therefore made up my
mind to tell you that I do not want to dance a reel at all; and now
despise me, if you dare!


DARCY.

[_Smiling._] I do not dare.

     [MISS BINGLEY _enters from the ball-room with an officer. They talk
     together._]

COLONEL FORSTER.

[_Entering from the ball-room, and looking about him, sees_ ELIZABETH
_and comes to her_.] May I have the honour, Miss Bennet?


ELIZABETH.

I do not dance the reel, Colonel Forster.


COLONEL FORSTER.

Oh, the reel is over. This is our dance.


ELIZABETH.

Oh!

     [_She goes off with_ COLONEL FORSTER. DARCY _remains where_
     ELIZABETH _leaves him and watches her till she disappears into the
     ball-room. The officer bows and leaves_ MISS BINGLEY.]

MISS BINGLEY.

[_Approaching_ DARCY.] I can guess the subject of your reverie.


DARCY.

I should imagine not.


MISS BINGLEY.

You are considering how insufferable it would be to pass many evenings
in such society. Indeed, I am quite of your opinion. I was never more
annoyed. The insipidity and yet the noise;--the nothingness and yet the
self-importance of all these people! What would I give to hear your
strictures on them!


DARCY.

Your conjecture is totally wrong. I assure you, my mind was more
agreeably engaged. I was meditating on the very great pleasure which a
pair of fine eyes in the face of a pretty woman can bestow.


MISS BINGLEY.

[_Looking at him very meaningly and sweetly, speaks with coquetry._]
Indeed! And will not you tell me what lady has the credit of inspiring
such reflections?


DARCY.

[_With great intrepidity._] Miss Elizabeth Bennet.


MISS BINGLEY.

[_Taken aback._] Miss Elizabeth Bennet! I am all astonishment! How long
has she been such a favourite? Pray when am I to wish you joy?


DARCY.

That is exactly the question which I expected you to ask. A lady's
imagination is very rapid: it jumps from admiration to love, from love
to matrimony in a moment. I knew you would be wishing me joy.


MISS BINGLEY.

Nay, if you are so serious about it I shall consider the matter as
absolutely settled. You will have a charming mother-in-law! Of course
she will always be at Pemberley with you. Perhaps you might give her a
few hints as to the advantage of holding her tongue.


DARCY.

Thank you. Have you anything else to propose for my domestic felicity?


MISS BINGLEY.

Oh, yes! Let the portrait of your uncle, the attorney, be placed next to
your great uncle, the Judge. They are in the same profession, you know,
only in different lines. As for your Elizabeth's picture, you must not
attempt to have it taken, for what painter could do justice to those
beautiful eyes!


DARCY.

It would not be easy, indeed, to catch their expression; but their
colour and shape, and the eyelashes, so remarkably fine, might be
copied.


MISS BINGLEY.

[_Sarcastically._] Oh, I fear not--[ELIZABETH _and_ COLONEL FORSTER,
_with others, enter from the ball-room_--MRS. BENNET _with_ LADY LUCAS
_from the drawing-room_.] Here comes the fair one--[_Seeing_ MRS.
BENNET.]--and mamma-in-law as well. I will not intrude on the family
party.

     [_She goes off laughing and mingles with the guests._ COLONEL
     FORSTER _bows and leaves_ ELIZABETH _with her mother_. BINGLEY
     _enters with_ JANE _from the drawing-room_. _He sees_ DARCY, _who
     is standing where_ MISS BINGLEY _left him, and comes to him_.

BINGLEY.

I thought this next dance was the one you liked so much, Darcy. Let me
find you a partner.


DARCY.

[_Starting, as if from a reverie._.] So it is. Thank you--I have a
partner.

     [_He goes to_ ELIZABETH, _bows, and they go into the ball-room
     together_. MRS. BENNET _and_ MRS. LONG _follow them_.]

BINGLEY.

[_Looking after_ DARCY _with a smile, turns to_ JANE.] You must be
tired, Miss Bennet. I propose that we sit quietly through this dance. Do
you agree?


JANE.

Yes, indeed. [_She sits on the bench._] It will be very pleasant.
[_Looking about her._] How very prettily you have arranged all the
rooms, Mr. Bingley.


BINGLEY.

I am so glad you think so. I feared they were rather inconvenient for so
large a party.


JANE.

Oh, I find them delightful!


BINGLEY.

You are always charitable, Miss Bennet. It seems to me you always manage
to see the best side of everything. I never knew you to say an ill word
about a person or a place.


JANE.

[_Smiling._] Oh, I fear that is not quite exact. I only try to see
things in their best light, perhaps.


BINGLEY.

That is just it. The rest of us rarely try to see things in that way. So
you see I have proved my case. You are too amiable.


JANE.

Not for to-night, Mr. Bingley. Everybody is of one mind to-night. There
is but one point of view--you are giving nothing but pleasure.


BINGLEY.

[_Soberly._] I wish it were so--but---- [_With impulsive earnestness._]
Dear Miss Bennet, I wish to tell you--I must tell you----

     [_He is interrupted by the people coming in again from the dance._
     DARCY _and_ ELIZABETH _enter with_ SIR WILLIAM LUCAS _and others_.
     BINGLEY _and_ JANE _rise from their seats and walk slowly toward
     the back of the room_. DARCY _escorts_ ELIZABETH _to a seat and
     stands by her. They are both silent for a moment._]

ELIZABETH.

It is your turn to say something now, Mr. Darcy. I talked about the
dance, and you ought to make some kind of remark on the size of the
rooms, or the number of couples.


DARCY.

[_Smiling._] I assure you I will say whatever you wish.


ELIZABETH.

Very well, that reply will do for the present. Perhaps by and by I may
observe that private balls are much pleasanter than public ones.


DARCY.

Do you talk by rule then?


ELIZABETH.

Sometimes. One must speak a little, you know,--and yet for the advantage
of some, conversation ought to be so arranged that they may have the
trouble of saying as little as possible.


DARCY.

Are you consulting your own feelings in the present case, or do you
imagine that you are gratifying mine?


ELIZABETH.

[_Archly._] Both, for I have always seen a great similarity in the turn
of our minds; we are each of an unsocial, taciturn disposition,
unwilling to speak, unless we expect to say something that will amaze
the whole room and be handed down to posterity with all the _éclat_ of a
proverb.


DARCY.

This is no very striking resemblance of your own character, I am sure.
How near it may be to mine, I cannot pretend to say. You think it a
faithful portrait, undoubtedly.


ELIZABETH.

I shall not decide on my own performance. [_There is a short silence;
then, as if with an effort_, ELIZABETH _speaks_.] I am surprised not to
see Mr. Wickham here to-night. I find that he is a great favourite with
the officers. He has made many friends among them.


DARCY.

[_With great hauteur._] Mr. Wickham is blessed with such happy manners
as may insure his _making_ friends; whether he may be equally capable of
_retaining_ them is less certain.


ELIZABETH.

[_Excitedly._] He has been so unlucky as to lose your friendship, and in
a manner which he is likely to suffer from all his life.

[_They are both silent._]


SIR WILLIAM LUCAS.

[_Coming up to them all urbanity and smiles._] What a charming amusement
for young people this dancing is, Mr. Darcy! I consider it as one of the
first refinements of polished societies.


DARCY.

Certainly, sir, and it has the advantage also of being in vogue amongst
the less polished societies of the world: every savage can dance.


SIR WILLIAM.

[_Smiling._] Do you often dance at St. James?


DARCY.

Never, sir.


SIR WILLIAM.

You have a house in town, I conclude.

[MR. DARCY _bows, but does not speak_.]


SIR WILLIAM.

I had once some thoughts of fixing in town myself: but I did not feel
quite certain that the air of London would agree with Lady Lucas.

     [MR. DARCY _bows in silence again_--ELIZABETH _is amused_.]

SIR WILLIAM.

But I must not further interrupt you, sir! I only wish to tell you once
more how highly gratified I have been by your superior dancing; allow me
also to say that your fair partner does not disgrace you. It is a great
pleasure to see you together. I must hope to--to have this pleasure
often repeated, especially when a certain desirable event, my dear Miss
Eliza, [_Glancing at_ BINGLEY _and_ JANE, _who are talking earnestly
together at the back of the scene_.] shall take place. What
congratulations will then flow in: but let me not interrupt you--you
will not thank me, Mr. Darcy, for detaining you from the bewitching
converse of that young lady, whose bright eyes are also upbraiding me!


DARCY.

[_Murmurs to himself._] So! [_Looking earnestly at_ BINGLEY _and_ JANE,
_he seems much impressed by what_ SIR WILLIAM _has said_. ELIZABETH
_notices this. Recovering himself_, DARCY _turns to her again_.] Sir
William's interruption has made me forget what we were talking of.


ELIZABETH.

I do not think we were speaking at all. Sir William could not have
interrupted any two people who had less to say for themselves. We have
tried two or three subjects already without success, and what we are to
talk of next, I cannot imagine.


DARCY.

[_Smiling._] What think you of books?


ELIZABETH.

Books? Oh no: I am sure we never read the same, or not with the same
feelings.


DARCY.

I am sorry you think so, but if that be the case, there can at least be
no want of subject. We may compare our different opinions of them.


ELIZABETH.

No, I cannot talk of books at a ball--my head is always full of
something else.


DARCY.

The present always occupies you in such scenes, does it?


ELIZABETH.

[_In an absent manner._] Yes, always. [_Suddenly._] I remember hearing
you once say, Mr. Darcy, that you hardly ever forgave; that your
resentment once created was unappeasable. You are very cautious, I
suppose, as to its being created?


DARCY.

[_Firmly._] I am.


ELIZABETH.

And never allow yourself to be blinded by prejudice?


DARCY.

I hope not.


ELIZABETH.

It is particularly incumbent on those who never change their opinion, to
be secure of judging properly at first.


DARCY.

May I ask to what these questions lead?


ELIZABETH.

Merely to the illustration of your character. I am trying to make it
out.


DARCY.

And what is your success?


ELIZABETH.

[_Shaking her head._] I do not get on at all. I hear such different
accounts of you as puzzle me exceedingly.


DARCY.

[_Gravely._] I can readily believe that reports may vary greatly with
respect to me; and I could wish, Miss Bennet, that you were not to
sketch my character at the present moment, as there is reason to fear
that the performance would reflect no credit on either.


ELIZABETH.

But if I do not take your likeness now I may never have another
opportunity.


DARCY.

[_Very stiffly._] I would by no means suspend any pleasure of yours.

[MISS BINGLEY _enters from the ball-room. She comes directly to_ DARCY
_and_ ELIZABETH.]


MISS BINGLEY.

Oh, Mr. Darcy--would you be so good as to go to Charles? He wishes very
much to consult with you about some of the table arrangements. You will
find him in the dining-parlour. [_With exaggerated politeness to_
ELIZABETH.] That is, if Miss Bennet will permit you.


ELIZABETH.

[_Carelessly._] Oh, certainly.

[DARCY _bows and goes out_.]


MISS BINGLEY.

[_To_ ELIZABETH, _after a moment's silence_.] So, Miss Bennet, I hear
that you are quite delighted with George Wickham. He must have told you
all a pretty tale. As to Mr. Darcy's using him ill, it is perfectly
false. I do not know the particulars, but I do know that George Wickham
has treated Mr. Darcy in a most infamous manner. His coming into the
county at all is a most insolent thing. I feel very strongly on this
point, Miss Bennet, as Mr. Darcy's interests are so intimately
associated with our own. [_She watches_ ELIZABETH.] We hope Miss
Georgiana Darcy may some day be my sister. My brother admires her
greatly.


ELIZABETH.

[_With indifference._] Ah!


MISS BINGLEY.

Yes, and therefore we resent these falsehoods and this presumption on
the part of George Wickham. But, really, considering his descent, we
could not expect much better. He has evidently forgotten to tell you
that he is the son of old Wickham, steward to the late Mr. Darcy.


ELIZABETH.

[_Angrily._] His guilt and his descent appear by your account to be the
same. I have heard you accuse him of nothing worse than of being the son
of Mr. Darcy's steward, and of _that_, I can assure you, he informed me
himself.


MISS BINGLEY.

[_With a sneer._] Oh! I beg your pardon. Excuse my interference; it was
kindly meant.

[_She goes out._]


ELIZABETH.

Insolent girl! You are much mistaken if you expect to influence me by
such a paltry attack at this. I see nothing in it but your own wilful
ignorance and the malice of Mr. Darcy.

     [FOOTMEN _now come in with small tables, which they place about the
     stage_. BINGLEY _comes in and directs them_. DARCY _follows him_.]

BINGLEY.

[To ELIZABETH, JANE, _his sister, and others who have entered_.] I
thought it would be pleasant to have some of the tables here. [_To_
JANE.] We must have places together.

     [_With some bustle, all seat themselves. At the table on one side
     are seated_ DARCY, ELIZABETH, BINGLEY _and_ JANE: _A little behind
     them are_ MISS BINGLEY _with_ COLONEL FORSTER, CHARLOTTE LUCAS
     _with an officer. At the table on the opposite side is_ MRS. BENNET
     _with_ SIR WILLIAM _and_ LADY LUCAS. _Behind them are more tables
     at which other guests are seated._]

LYDIA.

[_Entering with_ DENNY, _much excited, goes to_ MRS. BENNET.] Mamma,
have you heard the news? Mr. Denny has just told me that the regiment is
to leave Meryton, and go to Brighton! Good heavens! What is to become of
us, mamma?


MRS. BENNET.

[_Sympathetically._] Are they really going? Well, my love, it _is_ too
bad! I know how you feel. I am sure I cried for two days together when
Colonel Millar's regiment went away, five-and-twenty years ago. I
thought I should have broken my heart.


LYDIA.

I am sure I shall break mine. [_Coaxingly._] Mamma, might we not _all_
go to Brighton?


MRS. BENNET.

Oh, if we only could! But I fear your father will not hear of it.


LYDIA.

Oh, papa is so disagreeable! I am sure a little sea-bathing would set me
up forever! Wouldn't it, Mr. Denny?


DENNY.

Surely, Miss Lydia. Oh, you must manage it in some way.

     [_They move off and take their places at one of the tables._]

MRS. BENNET.

[_Looking after them._] Well, Lady Lucas, it is hard for a lively young
girl like my Lydia to be cooped up in a place where there is so little
going on. However, [_Looking at_ BINGLEY _and_ JANE.] we are not likely
to have it so very dull in the future. [_In a loud whisper to_ LADY
LUCAS.] You know what I mean--[_Nudging her and laughing._] Jane and
Bingley!


LADY LUCAS.

Ah! Indeed!


MRS. BENNET.

[_With importance and in a still louder tone._] Oh, yes! It's quite
settled. Such a charming young man--and Netherfield only three miles
from Longbourn! And Jane's marrying will be a fine thing for my other
girls. They will be sure to meet other rich men who will fall in love
with them.


ELIZABETH.

[_Who has heard the beginning of this conversation, makes a pretext to
go to arrange her mother's scarf and says in low tones._] Oh, mamma! Be
careful, I beg. Mr. Darcy can hear you!


MRS. BENNET.

What is Mr. Darcy to me, pray, that I should be afraid of him? I am sure
we owe him no such particular civility as to be obliged to say nothing
_he_ may not like to hear!


ELIZABETH.

[_In distress._] For heaven's sake, Madam, speak lower! What advantage
can it be to you to offend Mr. Darcy? You will never recommend yourself
to his friend by so doing.


MRS. BENNET.

That is enough, Lizzy! I think I can take care of myself. I never knew
before that it was a crime to speak to one's friends about what
everybody can see plainly enough, who has eyes in his head. [_Turning
to_ SIR WILLIAM.] Did _you_, Sir William?


SIR WILLIAM.

[_Smiling._] Our friends usually have very sharp eyes for what is going
on, Mrs. Bennet! [_Significantly._] I have, indeed, sometimes expected
that _you_ would observe what has been going on in our own household of
late.


MRS. BENNET.

[_Sharply._] Going on? What _has_ been going on, Sir William?


SIR WILLIAM.

[_With an important air._] It is only this, Mrs. Bennet, that Lady Lucas
and myself have to ask your congratulations on our very great
satisfaction in the recent engagement of our daughter, Charlotte.


MRS. BENNET.

Charlotte! Engaged! Why, who in the world is going to marry _her_?

     [SIR WILLIAM _draws himself up with offended dignity_; LADY LUCAS
     _bridles_.]

SIR WILLIAM.

The gentleman whom my daughter has honoured with her hand is your
husband's cousin--Mr. Collins!


MRS. BENNET.

[_Rising in rage and amazement._] Mr. Collins! Marry your Charlotte?
Good Lord, Sir William, how can you tell such a story! Do not you know
that Mr. Collins is going to marry my Lizzy--or--or one of my other
girls!


LADY LUCAS.

Well, really, Mrs. Bennet!


SIR WILLIAM.

[_Offended._] What I have told you is quite true, nevertheless, Mrs.
Bennet. The whole matter was settled before Mr. Collins returned to
Hunsford. I am sorry we are not to receive your good wishes.


ELIZABETH.

[_Hastily._] Oh, but you _are_, Sir William! Charlotte has already told
me all about her engagement, and we shall be most happy to welcome her
as a cousin.


SIR WILLIAM.

[_Mollified and with gallantry._] Thank you, Miss Elizabeth! I am sure
other congratulations will shortly be in order.

     [_He glances significantly at_ DARCY; ELIZABETH _draws herself up_.
     SIR WILLIAM, _smiling, makes a little bow and then turns to the
     table, where he and_ LADY LUCAS _busy themselves with their
     supper_.]

MRS. BENNET.

[_To_ ELIZABETH.] So Charlotte has told you, has she? I don't believe a
word of it!


ELIZABETH.

Oh, mamma!


MRS. BENNET.

I am sure Mr. Collins has been taken in. Well, I trust they will never
be happy together, and I hope the match will be broken off.


ELIZABETH.

[_Imploringly._] Mamma!


MRS. BENNET.

[_Turning on_ ELIZABETH _in a rage_.] And _you_ are the cause of the
whole mischief, Lizzy! I think I have been barbarously used by you all!

     [_While this conversation has been going on, the other guests have
     been taking their supper._ COLONEL FORSTER _now rises with a glass
     of wine in his hand_.]

COLONEL FORSTER.

Ladies and gentlemen---- [_The buzz of conversation ceases._] Ladies and
gentlemen, I should like to propose the health of Mr. Bingley.


ALL.

Mr. Bingley!


COLONEL FORSTER.

[_Raising his glass._] To Mr. Bingley--may the pleasure which he has
given us all to-night be but a foretaste of the future happiness which
he will both _receive_ and _give_ in this community.


ALL.

Mr. Bingley--Colonel Forster!--Mr. Bingley!

[_All drink as_ BINGLEY _bows_.]


SIR WILLIAM.

[_Rising._] And may _I_ be allowed to still farther express the
sentiments of this community, by proposing another toast in which I am
sure you will all join me with enthusiasm? [_Raising his glass._] To the
Master of Netherfield! May he retain that title from his present
fortunate youth, to his future green and honoured old age!


ALL.

[_Drinking._] Mr. Bingley! Sir William! Mr. Bingley!


BINGLEY.

[_Rising._] Ladies and gentlemen! Friends!


ALL.

Hear! Hear!


BINGLEY.

I--I really cannot tell you how much I am touched by the very kind
words of Colonel Forster and Sir William! And--and I only wish that I
deserved them.


ALL.

Indeed, you do!


BINGLEY.

[_Embarrassed and looking toward_ DARCY, _who with folded arms, is
staring at the ceiling_.] No, I do not. I--I did not like to speak of
such a painful thing on an occasion like this, and so I have told no one
of the fact that I am about to--to leave Netherfield.


ALL.

Leave Netherfield! Oh! Oh!


BINGLEY.

[_Still more ill at ease._] Yes.--It is a very sudden decision, but--but
important interests have made it necessary for me to--[_Lamely._] to
leave Netherfield.


SIR WILLIAM.

But only for a time, Mr. Bingley! Let us hope it will only be a--a
_temporary_ separation.


MRS. BENNET.

Why, surely, Mr. Bingley, you will be back again very soon.


BINGLEY.

[_In a dogged manner._] No--no. I am afraid my returning at all is
extremely uncertain. In fact, I--I expect to leave Netherfield
_permanently_.

     [_Great consternation._ JANE _looks down_. ELIZABETH _looks at_
     DARCY. MISS BINGLEY _has a triumphant smile_.]

COLONEL FORSTER.

[_Incredulously._] Oh, my dear Mr. Bingley!


SIR WILLIAM.

[_Solemnly._] This is, indeed, a calamity.


MRS. BENNET.

[_To_ ELIZABETH.] Good Lord, Lizzy, poor Jane! What----

ELIZABETH.

Oh, hush, mamma!


BINGLEY.

[_Looks again at_ DARCY, _who remains perfectly calm through all this
commotion. This time the sight of him seems to make_ BINGLEY _somewhat
angry, and he pulls himself together and speaks in a firmer tone and in
a more cheerful manner_.] But, my friends, nobody knows what may happen.
We shall undoubtedly all meet again sometime, and meanwhile, you must
not let what I have said spoil your pleasure. [_The music is now heard
again in the ball-room._] There is the music. We must have another dance
together.

     [_There is a general movement among the guests. Those at the back
     of the room begin to go into the ball-room._]

BINGLEY.

[_To_ JANE, COLONEL FORSTER, _and others near him_.] Let us make up a
set here; I think there will be room.


COLONEL FORSTER.

Capital idea!

[_The_ FOOTMEN _remove the tables_.]


MISS BINGLEY.

Oh, yes, capital! [_With meaning, to_ DARCY.] Do not you think so, Mr.
Darcy?

[DARCY _bows stiffly, without speaking_.]


COLONEL FORSTER.

Miss Bingley, may I have the pleasure?

     [_She bows, looks daggers at_ DARCY, _and takes her place in the
     dance_.]

BINGLEY.

[_To_ JANE.] Miss Bennet, will you grant me the happiness? [DARCY _gives
him a look which_ ELIZABETH _sees_.] The--the _final_ happiness of my
stay at Netherfield.


JANE.

[_Curtsies, a tremor in her voice._] Thank you.

     [_They begin to form a set with_ MISS BINGLEY _and_ COLONEL
     FORSTER, LYDIA _and_ DENNY.]

DARCY.

[_Crossing to_ ELIZABETH.] May I have the honour, Miss Elizabeth?


ELIZABETH.

[_Looking at him with frank hauteur._] Thank you, Mr. Darcy, I am
indisposed.

     [DARCY _bows, reddens, and crosses to the other side of the room.
     The music begins. Amid embarrassed astonishment_, SIR WILLIAM _and_
     CHARLOTTE LUCAS _fill the quadrille set. As the dance commences_,
     ELIZABETH _and_ DARCY, _standing at either side of the dancers,
     exchange a glance of the keenest pride and prejudice_.]




ACT III


     _The parlour of_ MR. COLLINS'S _parsonage at Hunsford. At the back
     of the room is an open door. This door leads directly into the
     garden, beyond which is seen, through an opening in the trees of
     the park opposite, "the prospect of Rosings"--the residence of_
     LADY CATHERINE DE BOURG--"_a handsome, modern building on rising
     ground." A wide cottage window, also at the back of the room, gives
     a plain view of the passers-by. On either side of the parlour is a
     door, leading to other parts of the house._ ELIZABETH _is
     discovered standing at the open door and looking up at some one
     outside who is evidently climbing the trellis_.

A VOICE (_outside._)

Is this the cluster you wish, Miss Bennet?


ELIZABETH.

[_Mischievously._] No, Colonel Fitzwilliam. Those are buds; the ones
higher still. There--by the eaves.

     [ELIZABETH _laughingly watches_ COLONEL FITZWILLIAM _until he
     appears with a cluster of half opened roses, which he presents to
     her with a gallant air_.]

ELIZABETH.

[_Taking the roses and putting them in her girdle._]

Thank you.


COLONEL FITZWILLIAM.

May not I have _one_, as my reward, Miss Bennet?


ELIZABETH.

Is not accomplishment its own reward?


COLONEL FITZWILLIAM.

And is not the power to be generous the highest reward that can be given
to any accomplishment?


ELIZABETH.

Oh, surely! And so _you_ would have to be generous and get me some more
roses: then we should each of us have to invent new speeches, and so we
should never be done till we were ready to print a phrase book. However,
you have certainly won your rose. [_She gives it to him._]


COLONEL FITZWILLIAM.

Thank you! That phrase-book is a capital idea, Miss Bennet. Nothing
could please me better than just such an occupation. It would really be
a charity, for Darcy is such a dull fellow these days that I really
don't know what to do with myself.


ELIZABETH.

But we should hardly have the time for such a project. You say that you
and Mr. Darcy are to leave Lady Catherine on Saturday.


COLONEL FITZWILLIAM.

Yes, if Darcy doesn't put it off again. He has already paid our aunt a
much longer visit than ever before. I am at his disposal, you know. He
arranges the business just as he pleases.


ELIZABETH.

I do not know anybody who seems more to enjoy the power of doing what he
pleases than Mr. Darcy.


COLONEL FITZWILLIAM.

He likes to have his own way very well, but so do we all. It is only
that he has better means of having it than many others. [_Looking at his
watch._] I suppose I ought to go and look for him now. I expected to
find him here, [_With a meaning smile._] as not unfrequently happens.
But since he is not, he probably expects me to meet him at the
Crossroads.


ELIZABETH.

I imagine your cousin brought you down with him chiefly for the sake of
having somebody at his disposal. I wonder he does not marry to secure a
lasting convenience of that kind. But perhaps his sister does as well
for the present,--and, as she is under his sole care, he may do what he
likes with her.


COLONEL FITZWILLIAM.

No--that is an advantage which he must share with me. I am joined with
him in the guardianship of Miss Darcy.


ELIZABETH.

Are you, indeed? And pray what sort of a guardian do you make? Does your
charge give you much trouble? Young ladies of her age are sometimes a
little difficult to manage. And, if she has the true Darcy spirit, she
may like to have her own way.

     [COLONEL FITZWILLIAM _looks at_ ELIZABETH _very suspiciously as she
     makes this last remark_.]

COLONEL FITZWILLIAM.

Why--what?--Why do you suppose Miss Darcy is likely to give us any
uneasiness, Miss Bennet?


ELIZABETH.

[_Carelessly._] Oh, nothing at all! You need not be frightened! I never
heard any harm of her; she is a great favourite with a lady of my
acquaintance--Miss Bingley. I think I have heard you say that you knew
Miss Bingley.


COLONEL FITZWILLIAM.

I know her a little. Her brother is a pleasant, gentlemanlike man. He is
a great friend of Darcy's.


ELIZABETH.

Oh, yes. Mr. Darcy is uncommonly kind to Mr. Bingley and takes a
prodigious deal of care of him.


COLONEL FITZWILLIAM.

Care of him? Yes, I really believe Darcy does take care of him. From
something he has told me, I have reason to think Bingley very much
indebted to him. [_Stopping._] But I ought to beg his pardon, for I have
no right to suppose that Bingley was the person meant.


ELIZABETH.

[_Curiously, and with ill-concealed anxiety._] What is it you mean?


COLONEL FITZWILLIAM.

It is a circumstance which, of course, Darcy could not wish to be
generally known, because if it were to get round to the lady's family it
would be an unpleasant thing.


ELIZABETH.

You may depend upon my not mentioning it.


COLONEL FITZWILLIAM.

And, remember, that I haven't much reason for supposing it to be
Bingley. What he told me was merely this: that he congratulated himself
on having lately saved a friend from the inconveniences of a most
imprudent marriage, but without names or any other particulars, and I
only suspected it to be Bingley from believing him to be the kind of
young man to get into a scrape of that sort.


ELIZABETH.

[_Trying to suppress her feeling._] Did Mr. Darcy give you his reasons
for this interference?


COLONEL FITZWILLIAM.

I understood that there were some very strong objections against the
lady.


ELIZABETH.

Indeed! [_Trying to speak calmly._] And what arts did he use to separate
them?


COLONEL FITZWILLIAM.

[_Smiling._] He did not talk to me of his own arts. He only told _me_,
what I have now told _you_.


ELIZABETH.

Why was your cousin to be the judge?


COLONEL FITZWILLIAM.

You are rather disposed to call his interference officious?


ELIZABETH.

[_Growing excited._] I do not see what right Mr. Darcy had to decide on
the propriety of his friend's inclination; why, upon his _own_ judgment
alone, Mr. Darcy was to determine in what manner his friend was to be
happy. [_Recovering herself._] But as we know none of the particulars,
it is not fair to condemn him. It is not to be supposed that there was
much affection in the case.


COLONEL FITZWILLIAM.

That is not an unnatural surmise, and I believe Darcy told me that he
did not think that the lady, at least, was very deeply concerned in the
matter. However, to lessen the affection on either side is to lessen the
honour of my cousin's triumph very sadly.


ELIZABETH.

Your cousin's triumph----

[_Greatly excited, she is about to continue, when_ CHARLOTTE'S _voice is
heard outside_.]


CHARLOTTE.

Yes, Mr. Darcy, I think I saw Colonel Fitzwilliam go up the garden path
a few moments ago. [_Protesting._] Oh, no, Mr. Darcy, you are too kind!
Really----

DARCY.

[_Outside._] Pray, allow me.

     [CHARLOTTE _enters, accompanied by_ DARCY, _who is carrying a
     basket of eggs. She wears a garden hat and gloves._]

CHARLOTTE.

Ah, here he is. Good morning, Colonel Fitzwilliam. [_To_ DARCY.] Pray
let me have the basket now, Mr. Darcy. [DARCY _gives_ CHARLOTTE _the
basket, and then turns to_ ELIZABETH.]


DARCY.

Good morning, Miss Bennet. [ELIZABETH _returns_ DARCY'S _greeting with a
self-consciousness which does not escape his notice, but the motive of
which he mistakes_. DARCY _gives a quick glance from_ ELIZABETH _to_
COLONEL FITZWILLIAM, _as he turns to speak to the latter_.] Ah,
Fitzwilliam, I thought I might find you here.


COLONEL FITZWILLIAM.

[_Lightly._] Yes, I have been so fortunate as to secure some of Mrs.
Collins's early roses for Miss Bennet.


CHARLOTTE.

[_In surprise._] Really! Have they already opened?


ELIZABETH.

[_Who has by this time recovered her self-possession._] A very few of
them. But Colonel Fitzwilliam was obliged to climb very near to the sun
to get me these. [_She looks admiringly upon the flowers as she
speaks._]


COLONEL FITZWILLIAM.

[_Showing the rose which_ ELIZABETH _has given him_.]

And you see I have my reward.


DARCY.

[_Smiling faintly._] Colonel Fitzwilliam might not have won his prize so
easily, Miss Bennet, had there been others in the field.


ELIZABETH.

Ah, no, Mr. Darcy, I cannot lessen Colonel Fitzwilliam's achievement by
admitting any such possibility.


COLONEL FITZWILLIAM.

[_Gallantly._] Thank you, Miss Bennet!

     [DARCY _turns away with an unconscious look of chagrin_.]

CHARLOTTE.

Well, surely, my roses will have to bloom their prettiest this season in
return for all the attention they have received. [_To the young men._]
Will not you be seated, gentlemen?


DARCY.

[_Tartly._] Thanks, no, Mrs. Collins; I merely stopped for Colonel
Fitzwilliam; but perhaps his rose-gathering has caused him to abandon
our project of taking a walk together this morning.


COLONEL FITZWILLIAM.

By no means, Darcy, that pleasure has only been deferred.


DARCY.

Very good then. We will go at once, if Mrs. Collins and Miss Bennet will
pardon me this hasty call.


CHARLOTTE.

Certainly, Mr. Darcy! [ELIZABETH _also, absent-mindedly, murmurs her
assent, for which_ DARCY _lingers with vague uneasiness before departing
with_ FITZWILLIAM. CHARLOTTE _looks at_ ELIZABETH _curiously, then calls
to the little maid, who enters_.]


CHARLOTTE.

Martha--take these eggs to the pantry. Do not disturb them.


MARTHA.

Very well, ma'am.

[_She curtsies and goes out._]


CHARLOTTE.

[_Taking off her hat and gloves._] Now, Eliza, we must get to our work
and have a comfortable chat. You have been here nearly two weeks and we
really haven't had a good talk yet.


ELIZABETH.

[_Getting out her embroidery._] Yes, you promised me a quiet visit,
Charlotte. But I find you are more lively here than we are at Longbourn.

[_The two ladies sit at the table with their embroidery._]


CHARLOTTE.

But how could I have anticipated the arrival here of two very attentive
young gentlemen? [_Smiling at_ ELIZABETH.] It is really quite a
surprising coincidence, or else Mr. Darcy has timed his visit to his
aunt very cleverly. As to these daily visits to the parsonage--you may
be sure I do not take to myself the credit of them. Neither of these
young gentlemen would ever come so often to see me. I have to thank you,
Eliza, for this civility.


ELIZABETH.

[_With a little temper._] You may thank a lack of occupation on their
part. You know very well my opinion of Mr. Darcy!


CHARLOTTE.

Yes. You have often expressed it. I wish I were as well informed of Mr.
Darcy's opinion of Eliza.


ELIZABETH.

When you know the one, you know the other. They are identical.


CHARLOTTE.

Well, perhaps under the circumstances, that is the most satisfactory
condition of things. And do we hold the same opinion of Colonel
Fitzwilliam?


ELIZABETH.

[_Tossing her head._] Oh, Colonel Fitzwilliam!


CHARLOTTE.

[_Looking at_ ELIZABETH _sharply, and after a short silence_.] And so
Jane is once more at home after her visit in London, and Lydia has gone
to Brighton after all. How did she ever manage to persuade your father?


ELIZABETH.

Oh, Lydia was so determined upon it that she and mamma gave my father no
peace till they had teased him to consent. But I am very sorry. Lydia is
too foolish, too ignorant and wilful to be trusted away from home. I
only hope that no harm will come of it.


CHARLOTTE.

And is Mr. Wickham still with the regiment?


ELIZABETH.

Yes, he went with it to Brighton.


CHARLOTTE.

I hear that he is thinking of marrying Miss King, since she has just
received a legacy of ten thousand pounds. I should be sorry to think
that our friend was mercenary.


ELIZABETH.

A man in distressed circumstances has not time for all those elegant
decorums which other people may observe. If Miss King does not object to
it, why should we?


CHARLOTTE.

_Her_ not objecting does not justify--him.


ELIZABETH.

[_Emphatically._] Well, have it as you choose. _He_ shall be mercenary,
and _she_ shall be foolish! Mr. Wickham's worst fault, after all, is his
power of being agreeable. Thank heaven, we both of us know some men who
haven't one agreeable quality. Stupid men are the only ones worth
knowing!


CHARLOTTE.

[_Smiling._] Well, well, Eliza! That speech savours a little
of--disappointment.


ELIZABETH.

Oh, yes--anything you please!


CHARLOTTE.

[_Changing the subject._] And you say that Jane is not in her usual
spirits?


ELIZABETH.

[_Shortly._] Yes.


CHARLOTTE.

And she is looking poorly?


ELIZABETH.

[_Still more shortly._] Yes--very!


CHARLOTTE.

Did she see much of the Bingleys in London?


ELIZABETH.

[_Bursting out hotly._] She saw nothing of them. Oh, Charlotte, I have
just had all my suspicions verified.


CHARLOTTE.

Your suspicions?


ELIZABETH.

Yes, there has been an arrangement in all this. Mr. Bingley has been
kept away from Jane by---- [_Stops suddenly._]


CHARLOTTE.

[_Looks up curiously, then speaks quickly._] Don't imagine any such
nonsense, Eliza. A young man like Mr. Bingley so easily falls in love
with a pretty girl for a few weeks--and, when accident separates them,
so easily forgets her, that this sort of inconstancy is very frequent.


ELIZABETH.

We do not suffer from accident, Charlotte. A young man of independent
fortune does not suddenly decide of his own free will to think no more
of a girl with whom he was violently in love.


CHARLOTTE.

But were they so violently in love?


ELIZABETH.

Yes--I never saw a more promising inclination. Why, Mr. Bingley would
talk to no one else--would look at no one else. Is not general
incivility the very essence of love?


CHARLOTTE.

[_Smiling._] It is usually a good test. But if Jane did not return his
affection---- It really did not seem to me that there was anything
_violent_ in Jane's attitude. I could never see that she showed any
extreme affection for Bingley.


ELIZABETH.

[_Hotly._] Well, I know that Jane was very much in love with him, and
that she showed her affection as much as her nature would allow. If
Bingley didn't see it he must have been a simpleton. No--the real
trouble was that Jane didn't see him often enough, perhaps, to make her
understand his character.


CHARLOTTE.

Oh, if Jane were married to Bingley to-morrow, I should think she had as
good a chance of happiness as if she were studying him for a
twelve-month. It is far better to know as little as possible of the
person with whom you are to pass your life.


ELIZABETH.

[_Demurely._] In some cases that is undoubtedly true.


MR. COLLINS.

[_Appears at the garden door. He wears a wide-brimmed hat and carries a
hoe--also a large basket. He looks in._] Ah! A very charming domestic
picture! [_Taking a bunch of radishes from the basket, he speaks to_
CHARLOTTE.] My dear, I have found some fine early radishes. I thought it
would be a graceful attention on your part to send some of these to Miss
de Bourg. [_He sits upon the chair near the doorway._]


CHARLOTTE.

I fear the apothecary might object.


MR. COLLINS.

True--they might not be suitable, but [_Looking at them proudly._] they
are very fine radishes. [_To_ ELIZABETH.] Miss Elizabeth, I am very
successful in my gardening. I consider the work I do in my garden to be
one of my most respectable pleasures. Lady Catherine is always ready to
encourage me in it, and my dear Charlotte is ever willing that I should
leave her side for the sake of this healthful exercise. [_Looking at the
radishes again._] It is, indeed, a pity that Miss de Bourg is not well
enough to enjoy them. My dear Charlotte has doubtless told you, Miss
Elizabeth, of the alliance which is in prospect between Miss de Bourg
and Mr. Darcy. This extreme delicacy of constitution would seem to be
the only bar to their happiness.


ELIZABETH.

Yes, Charlotte has told me that Miss de Bourg is sickly. She will make
Mr. Darcy a very proper wife.

     [CHARLOTTE _looks anxiously at_ MR. COLLINS _as_ ELIZABETH _says
     this, but he is gazing out of the door and does not seem to notice
     the remark_.]

MR. COLLINS.

I hope you are pleased with Kent, Miss Elizabeth.


ELIZABETH.

Very much, Mr. Collins.


MR. COLLINS.

I do not think the kingdom can boast a grander scene than the one now
spread before our eyes: [_Pointing._] This garden--that park with
Rosings in the distance. Do not you think my dear Charlotte is most
fortunately placed, Miss Elizabeth?


ELIZABETH.

Most fortunately, Mr. Collins.


MR. COLLINS.

And when you have seen Lady Catherine, you will be more deeply
impressed, I am sure. We can hardly expect her to call upon you. This
illness of Miss de Bourg would prevent it, and in any case it would be
an act of extreme condescension on her part; but I am quite confident
that you will receive an invitation to drink tea of a Sunday evening
with her, after Mr. Darcy and his cousin are gone, of course. And--we
may later have an invitation to dinner--although I would not for the
world arouse in you false hopes which may be shattered.


MARTHA.

[_Enters in great excitement._] Oh, Mrs. Collins! Lady Catherine's
carriage is turning into the lane and _she_ is in it!


MR. COLLINS.

[_Rising in great excitement_.] Lady Catherine--at this hour! What
amazing condescension! [_He turns in a helpless manner to_ CHARLOTTE.]
But, my dear, I am quite unprepared. My habiliments--I would not be
wanting in respect.--What shall I do?


CHARLOTTE.

[_Hurriedly putting up her work and giving her hat and gloves to the
maid._] Go make yourself ready, Mr. Collins. We will do the same.
[CHARLOTTE _pushes_ MR. COLLINS _gently toward the door_.]


MR. COLLINS.

[_Protesting._] Yes--yes! But this implement----

[_He holds out the hoe._]


CHARLOTTE.

Give it to Martha!

     [MR. COLLINS _hastily gives the hoe to the maid and then goes out.
     He instantly returns, however, and again appeals in distressed
     tones to his wife_.]

MR. COLLINS.

[_Holding out the basket._] And these radishes, my dear?


CHARLOTTE.

Martha, take the radishes from Mr. Collins.


MARTHA.

Yes, ma'am.

     [_The maid tries to hold at once--basket, hoe, hat, and gloves, as
     she stands in a corner, open-mouthed._]

MR. COLLINS.

[_Again emerging from the door._] Do not make yourself uneasy about your
own apparel, Miss Elizabeth; Lady Catherine is far from requiring that
elegance in us which becomes herself and daughter--I----

CHARLOTTE.

[_Impatiently._] Oh, do go, Mr. Collins! Lady Catherine will be here in
an instant!

[_She shuts the door on_ MR. COLLINS.]


ELIZABETH.

[_Greatly amused at all this excitement._] Are you going to make any
change in your dress, Charlotte? Do you wish me to do so?


CHARLOTTE.

Well, Eliza, if you wouldn't mind, I should like you to put on your
sprigged muslin. In spite of what Mr. Collins says, I know it would
please him. I have no time to change. Is my cap straight? Oh, here she
is. [_To the maid, who stands staring, with her arms full._] Why,
Martha! Are you still there? Go! Go! [_She bustles the maid out of one
door, then runs to the other, calling her husband._] Mr. Collins! Mr.
Collins!

     [_She then rushes into the garden, followed immediately by_ MR.
     COLLINS _in the same state of excitement_. ELIZABETH, _as she looks
     after them, is convulsed with laughter_.]

ELIZABETH.

So, at last--her high and only mightiness! No tremors, Elizabeth! Now is
the time for all your courage. [_She runs laughing out of the room._]

     [_Sounds of voices are heard, and_ LADY CATHERINE _appears escorted
     up the path by_ CHARLOTTE _and_ COLLINS.]

LADY CATHERINE.

[_As she reaches the door._] You keep too many hens, Mrs. Collins. There
is just a certain number which are profitable--beyond that there is
waste. [LADY CATHERINE _sits on the sofa_.] A clergyman's wife should
set an example of thrift. You should have asked my advice.


MR. COLLINS.

Mrs. Collins will in the future regulate her poultry-yard according to
your directions, Lady Catherine, if you will be so condescending as to
give them.


CHARLOTTE.

Yes, thank you, Lady Catherine.


MR. COLLINS.

Will your Ladyship not take some refreshment?


CHARLOTTE.

Oh, yes--let me fetch you a cup of tea?


LADY CATHERINE.

No, no--I wish nothing. [_To_ MR. COLLINS.] But you may go, Mr. Collins,
and see if Jones is walking the horses up and down. I do not trust
Jones.


MR. COLLINS.

With great pleasure, your Ladyship. [MR. COLLINS _goes out_.]


LADY CATHERINE.

[_To_ CHARLOTTE.] I thought you had a visitor, Mrs. Collins.


CHARLOTTE.

Yes, your Ladyship--I have. It is my friend, Miss Elizabeth Bennet. She
is a cousin of Mr. Collins and a neighbour of ours in Hertfordshire.


LADY CATHERINE.

I have heard about her. Fitzwilliam says she is a very genteel, pretty
kind of girl.


CHARLOTTE.

[_Pleased._] Indeed she is, Lady Catherine.


LADY CATHERINE.

Well, where is she?


CHARLOTTE.

She has gone to make a little change in her dress, before presenting
herself to your Ladyship.


LADY CATHERINE.

Oh! very proper--very proper!


CHARLOTTE.

I am delighted to hear that Miss de Bourg is better, Lady Catherine.


LADY CATHERINE.

Yes, thank you. She is very greatly improved. [_After a slight pause,
with impatience_.] Well, Miss Bennet takes her time!


CHARLOTTE.

[_Anxiously._] I am sure she will be here in a moment. [ELIZABETH
_enters_.] Oh, here she is. [_Presenting_ ELIZABETH.] Lady Catherine,
Miss Elizabeth Bennet. [ELIZABETH _curtsies_.]


LADY CATHERINE.

[_Without leaving her seat, looks_ ELIZABETH _over from head to foot_.]
Oh, how do you do, Miss Bennet. You are younger than I thought!


ELIZABETH.

[_Smiling._] Indeed?


LADY CATHERINE.

You know my nephew, Mr. Darcy?


ELIZABETH.

Yes, I met him in Hertfordshire.


LADY CATHERINE.

Humph! And you know Colonel Fitzwilliam?


ELIZABETH.

I have only met Colonel Fitzwilliam since coming here.


LADY CATHERINE.

Humph! Has your governess left you?


ELIZABETH.

[_Half laughs._] My sisters and I have never had a governess, Madam.


LADY CATHERINE.

No governess! I never heard of such a thing! Your mother must have been
quite a slave to your education.


ELIZABETH.

[_Smiling._] I assure you she was not, Lady Catherine.


LADY CATHERINE.

Then who taught you? Without a governess you must have been neglected.


ELIZABETH.

Such of us as wished to learn, never wanted the means, Madam.


LADY CATHERINE.

Well, if I had known your mother, I should have advised her most
strenuously to engage a governess. I should have seen to it myself.
[_To_ CHARLOTTE.] Go on with your work, Mrs. Collins. A clergyman's wife
should set an example of industry. [_Looking at_ CHARLOTTE'S _embroidery
with disapproval_.] I will send you some more of the parish petticoats
to hem, Mrs. Collins. [_To_ ELIZABETH.] Go on with your work, Miss
Bennet. Young ladies should never be idle. [_Both_ ELIZABETH _and_
CHARLOTTE _go on with their embroidery. Looking hard at_ ELIZABETH.]
Pray what is your age, Miss Bennet?


ELIZABETH.

I am not one and twenty.


LADY CATHERINE.

You have sisters, have not you?


ELIZABETH.

Yes, Madam.


LADY CATHERINE.

Are any of them out?


ELIZABETH.

All, Madam.


LADY CATHERINE.

What! All out at once? Very odd! Out before the oldest is married!


ELIZABETH.

Really, Madam, I think it would be very hard on the younger sisters not
to have their share of society because the eldest one does not happen to
be married. That would hardly be likely to promote sisterly affection,
or delicacy of mind.


LADY CATHERINE.

Upon my word, you give your opinion very decidedly for so young a
person! Your sisters may be married before you. You must not be too
ambitious. A good many young girls have lost their chances through being
too ambitious. [_Looking at a large picture on the wall and then
pointing to it._] Mrs. Collins, I suppose you have shown Miss Bennet
this print of Pemberley--Mr. Darcy's place?


CHARLOTTE.

Yes, Lady Catherine.


LADY CATHERINE.

[_Complacently._] Pemberley is one of the finest places in England. My
daughter Anne is very fond of it, which is fortunate, since she will
probably spend the most of her life there.


CHARLOTTE.

Most fortunate, your Ladyship.


LADY CATHERINE.

[_To_ ELIZABETH.] You see my nephews here often, Miss Bennet?


ELIZABETH.

[_Mischievously._] Yes, _very_ often, Lady Catherine.


LADY CATHERINE.

Humph! Well, idle young gentlemen often make very foolish use of their
time. My daughter, Miss de Bourg, is unfortunately not able to accompany
Mr. Darcy in his walks as often as both of them could desire.


MR. COLLINS.

[_Entering._] I think your Ladyship's mind may be quite at rest about
the horses. Jones seems to have them well in hand.


LADY CATHERINE.

Oh, I am glad you have come back, Mr. Collins. I am going to ask you and
Mrs. Collins to go and see the new cottages with me. I shall take you in
the carriage. [_To_ CHARLOTTE.] You had better put on a plain bonnet,
Mrs. Collins.


CHARLOTTE.

By all means, your Ladyship. [_She goes out._]


LADY CATHERINE.

Are you quite ready to go, Mr. Collins?


MR. COLLINS.

Oh--assuredly, your Ladyship--quite!


LADY CATHERINE.

[_To_ ELIZABETH.] Miss Bennet, I should advise you to write to your
family while we are gone. [CHARLOTTE _returns in her bonnet and mantle_.
LADY CATHERINE _looks her over_.] Yes, that will do very well!


CHARLOTTE.

[_To_ ELIZABETH.] We shall not be gone very long, Eliza.


LADY CATHERINE.

I am not sure of that, Mrs. Collins, but I have provided an occupation
for Miss Bennet during our absence. Good morning, Miss Bennet. I may ask
you later for dinner.


ELIZABETH.

[_Curtsying._] Good morning, Madam. [_All go out_, MR. COLLINS _showing
servile attentions to_ LADY CATHERINE. ELIZABETH _watches them from the
door_.] Really! I might have spared myself some of the mortifications I
have felt for the shortcomings of my own family. The contrast is not
such a violent one after all. [_Looking at the writing desk._] However,
Lady Catherine can give good advice. I really ought to write to my poor,
dear Jane.

     [_She seats herself at the writing table--gets out her paper, etc.
     and begins her letter when the door-bell sounds._ ELIZABETH _starts
     and is putting away the writing materials, when the maid ushers in_
     MR. DARCY, _who seems much excited_.]

DARCY.

I am here again, Miss Bennet. I saw Mr. and Mrs. Collins drive away
with my aunt. I have something which I _must_ say to you. [_He walks
excitedly up and down for a moment, while_ ELIZABETH _watches him in
amazed silence. Then he suddenly goes up to her and begins to speak in
an agitated manner._] Miss Bennet--in vain have I struggled! It will not
do! My feelings will not be repressed! You must allow me to tell you how
ardently I admire and love you!


ELIZABETH.

[_Is perfectly astounded. She stares, colours, doubts, and is silent._]


DARCY.

[_Taking her silence for encouragement._] Miss Bennet, I can well
understand your own astonishment at this declaration, for I am amazed at
myself! My feeling for you has taken possession of me against my will,
my reason, and almost against my character!


ELIZABETH.

[_Starting in indignation._] Sir!


DARCY.

Oh, understand me, I beg of you! For yourself alone my admiration is
only too natural. I share it with everyone who has the happiness of
knowing you. But--pardon me--for it pains me to offend you--the defects
of your nearest relations, the total lack of propriety so frequently
betrayed by your family, has so opposed my judgment to my inclination,
that it has required the utmost force of passion on my part to put them
aside. But, my dear Miss Bennet, your triumph is complete. Your own
loveliness stands out the fairer in its contrast to your surroundings,
and I now hope that the strength of my love may have its reward in your
acceptance of my hand.


ELIZABETH.

[_Who has gone through all sorts of emotions during this speech, speaks,
in a constrained manner as if trying to control herself._] Mr. Darcy--in
such cases as this, it is, I believe, the established mode to express a
sense of obligation for the sentiments avowed, however unequally they
may be returned. If I could feel gratitude I would now thank you. But I
cannot. I have never desired your good opinion, and _you_ have certainly
bestowed it most unwillingly.


DARCY.

[_Leaning against the mantel-piece, hears her words with no less
resentment than surprise. After a little he speaks in a voice of forced
calmness._] And that is all the reply which I am to have the honour of
expecting? I might perhaps wish to be informed why, with so little
endeavour at civility, I am thus rejected. But it is of small
importance.


ELIZABETH.

I might as well inquire why, with so evident a design of insulting me,
you chose to tell me that you liked me against your will, your reason,
and even against your character! Was not this some excuse for
incivility, if I was uncivil?


DARCY.

I very clearly explained that the objections which appealed to my reason
applied entirely to your _family_, and in no respect to yourself.


ELIZABETH.

I am a part of my family, Mr. Darcy; and allow me to say that, since I
have had the opportunity of comparing my relations with your own, the
contrast is not so marked as I had been led to suppose. [DARCY
_starts_.] But--aside from all questions of either feeling or family--do
you think any consideration would tempt me to accept the man who has
been the means of ruining, perhaps forever, the happiness of a most
beloved sister, and involving her in misery of the acutest kind? [DARCY
_looks at her with a smile of incredulity._.] Can you deny that you have
done this?


DARCY.

I have no wish of denying that I did everything in my power to separate
my friend from your sister. I did not, indeed, anticipate that I should
involve either of them in "misery" of any kind. On your sister's side,
at least, I was never able to discover any symptoms of peculiar regard
for Mr. Bingley. While, for every reason, I must rejoice in my success
with my friend; toward him I have been kinder than toward myself.


ELIZABETH.

[_With disdain._] Your arrogance in calmly deciding the extent of other
people's sentiments does not surprise me. It is of a piece with your
whole nature! But your interference in my sister's concerns is not all.
Long before it had taken place, my opinion of you was decided. Your
character was unfolded in the recital which I received months ago from
Mr. Wickham. [DARCY _starts excitedly_.] What can you have to say on
this subject? In what imaginary act of friendship can you here defend
yourself?


DARCY.

[_In a tone of suppressed excitement, in marked contrast to his previous
self-assured manner._] You take an eager interest in that gentleman.


ELIZABETH.

Who that knows what his misfortunes have been can help feeling an
interest in him?


DARCY.

[_Contemptuously._] His misfortunes! Yes, his misfortunes have been
great indeed!


ELIZABETH.

[_With energy._] And of your infliction! You have reduced him to his
present state of poverty--comparative poverty; you have withheld the
advantages which you must know to have been designed for him. You have
done all this, and yet you can treat the mention of his misfortunes
with contempt and ridicule!


DARCY.

[_Walking up and down the room with quick steps._] And this is your
opinion of me? This is the estimation in which you hold me! I thank you
for explaining it so fully. [_Stopping and looking at her._] Perhaps if
I were to divulge the truth regarding Mr. Wickham, I might give _you_ as
great a surprise as you have given _me_. [_After a slight pause._] I do
not care to go into particulars, but in justice to myself, I must tell
you that the man whom you consider a martyr is a profligate with the
most vicious propensities. A man who should never have entered your
home, for his presence there is a constant source of danger.


ELIZABETH.

[_In indignation._] Mr. Darcy!


DARCY.

[_With dignity._] I am ready to give you the full proofs of all I have
said, Miss Bennet, whenever you may so desire, although I would gladly
forget all the miserable circumstances myself, and no obligation less
than the present should induce me to unfold them to any human being.


ELIZABETH.

[_Coldly._] Your judgment in the matter of my sister's happiness has
given me a gauge by which I can measure your fairness to a man who has
been so unfortunate as to offend you. My faith in Mr. Wickham is
unshaken.


DARCY.

[_Looking at_ ELIZABETH _in indignation and by a great effort governing
himself_.] I shall take what you have said, Miss Bennet, as a reflection
on my _judgment_ alone; otherwise, my veracity would be at stake, and
this, I am sure, you did not intend. Indeed I understand your whole
position perfectly. I have erred in the manner of my declaration. Your
bitter accusations might have been suppressed, had I concealed my
struggles. It is my own fault. I have wounded your pride. I should have
flattered you into the belief that I was impelled by inclination, by
reason, by reflection, by everything! But disguise of every sort is my
abhorrence. Could you expect me to rejoice in the inferiority of your
connections?


ELIZABETH.

[_Angrily._] And do you expect _me_ to rejoice in your proposal that I
ally myself to the conceit and impertinence of _yours_? No, Mr. Darcy!
The manner of your declaration has affected me only in one way:--it has
spared me the concern which I might otherwise have felt in refusing you,
had you behaved in a more _gentlemanlike_ way. [DARCY _starts_.] You
could not, however, have made me the offer of your hand in any possible
way that would have tempted me to accept it. [DARCY _looks at her with
an expression of mortified amazement_.] I had not known you a month,
before I felt that you were the last man in the world whom I could ever
be prevailed upon to marry.


DARCY.

You have said quite enough, Madam! I perfectly comprehend your feelings
and have now only to be ashamed of what my own have been. Forgive me for
having taken up so much of your time, and accept my best wishes for your
health and happiness. [DARCY _hastily leaves the room_.]


ELIZABETH.

[_Sinking into a chair, then getting up and walking excitedly about the
room._] To insult my family! To think I was ready to fall on my knees,
in gratitude for his condescension! To calmly dispose of Jane's
happiness! [_Stopping in her walk and with a half-amused smile._] And
yet really to be in love with me in spite of every obstacle. [_Throwing
herself again into the chair, half laughing, half crying._] Oh, Jane,
Jane! I wish you were here!


MARTHA.

[_Enters with a letter._] Here is a letter, Miss. The express has just
brought it.


ELIZABETH.

A letter? For me?


MAID.

Yes, Miss--[_She gives_ ELIZABETH _the letter; curtsies and goes out_.]


ELIZABETH.

[_Looking at the letter._] Why, it is from Jane! What can be the matter?
[_She opens the letter hurriedly and reads._] "Dearest Lizzy--I have bad
news for you, and it cannot be delayed. An express came to us last night
from Colonel Forster. He told us that Lydia had run away from Brighton
with one of his officers:--to own the truth--with Wickham!"

ELIZABETH.

Oh! Wickham! [_Going on with the letter._] "He first thought they had
gone to Scotland, but, oh, Lizzy, it is far worse than that! We now know
that Wickham never intended to go there, or to marry Lydia at all!"

ELIZABETH.

Oh! [_Reading again._] "Colonel Forster has been here to-day. He says
Wickham is not a man to be trusted! He has left Brighton terribly in
debt, and his record is bad in every way. Oh, Lizzy, our distress is
very great! My father is going to London with Colonel Forster instantly
to try to discover the fugitives. It is hard to ask you to shorten your
visit, but we are in such distress that----" [_Darting from her seat._]
Oh where--where is the express? I must write. No--I must go. Oh, Lydia
and Wickham! I must go at once! I must send someone for a carriage.
[_She rushes to the garden door calling._] Martha, Martha! The express!
[_Suddenly she calls again._] Oh, Colonel Fitzwilliam, is that you?


COLONEL FITZWILLIAM.

[_Appearing in the garden._] What is the matter, Miss Bennet?


ELIZABETH.

[_Wildly._] Oh, Colonel Fitzwilliam--the express--or can you get me a
carriage? I have bad news from home. I must return at once and Mr.
Collins is away. Will you be so kind? [_She falls, half-fainting, upon a
chair near the door._]


COLONEL FITZWILLIAM.

[_With concern._] Certainly, my dear Miss Bennet--of course--but----
[_Calling off._] Darcy, don't wait for me. I can't join you now. Miss
Bennet is in distress.


DARCY.

[_Entering._] Miss Bennet? Good God! What is the matter?


COLONEL FITZWILLIAM.

Miss Bennet has just had bad news from home. She wishes to return, and
desires a carriage.


DARCY.

[_In a decided tone._] Do you go for the carriage, Fitzwilliam. Get one
from the stables. [FITZWILLIAM _hesitates_.]


DARCY.

Go. I will remain with Miss Bennet.

[FITZWILLIAM _goes out_.]


DARCY.

[_To_ ELIZABETH _very gently_.] Shall I call the maid, Miss Bennet? A
glass of wine? Shall I get it for you? You are very ill.


ELIZABETH.

[_Hardly able to speak._] No, I thank you: there is nothing the matter
with me. I am quite well. I am only distressed by some dreadful news
which I have just received from Longbourn. [_She bursts into tears._]


DARCY.

[_Helplessly._] I am sorry, very indeed!


ELIZABETH.

[_After a short silence._] I have just had a letter from Jane with such
_dreadful_ news! It cannot be concealed from anyone.


DARCY.

I am grieved, Miss Bennet. Grieved indeed!


ELIZABETH.

Oh, Mr. Darcy, you were right. If I had only believed you! You, and
others! But I could not believe it. [_She sobs._]


DARCY.

[_Greatly moved._] What is it, my dear Miss Bennet? What has happened?


ELIZABETH.

[_Wildly._] Oh, I cannot tell it, and yet everyone must know! My sister
Lydia--has--has eloped--has thrown herself into the power of--of _Mr.
Wickham_! She has no money, nothing that can tempt him to--she is lost
forever! [_She sobs again._]


DARCY.

Good God, Miss Bennet! Your sister and Wickham! Oh, this is _my_ fault.
I should have realised this danger--I should have spoken. My own
wretched experience with this man should have been told.


ELIZABETH.

[_Wonderingly._] Your experience!


DARCY.

Yes--I--you remember. I hinted it to you--to-day. But I should long ago
have spoken boldly.


ELIZABETH.

What do you mean?


DARCY.

Mr. Wickham attempted this same plan with my own sister--two years ago.
She was an ignorant, innocent, trusting girl of fifteen. Happily, his
villainy was discovered and prevented. But oh, I should have told you!
Had his character been known, this could not have happened.


ELIZABETH.

You tried to tell me, Mr. Darcy. Everybody has tried to warn me. But I
could not believe it, and now--it is too late, too late!


DARCY.

Let us hope not. Is what you have told me certain--absolutely certain?


ELIZABETH.

Oh, yes. They left Brighton together on Sunday night. They are certainly
not gone to Scotland.


DARCY.

And what has been done, or attempted, to recover your sister?


ELIZABETH.

My father has gone to London. He will beg my uncle Gardiner's
assistance. But nothing can be done! I know very well that nothing _can_
be done. How is such a man to be worked on? How are they ever to be
discovered? I have not the smallest hope. It is all horrible!


DARCY.

Miss Bennet, I have made a wretched mistake in all this. Would to Heaven
that anything could be said or done on my part that might make you
reparation, or offer consolation to such distress!

     [ELIZABETH _sinks sobbing into a chair while_ DARCY _walks up and
     down in deep thought. In a moment a carriage is heard outside--then
     voices._]

DARCY.

[_Looking out._] Mr. and Mrs. Collins are returning. What would you wish
me to do?


ELIZABETH.

Oh, I do not know! I do not know!


DARCY.

[_Returning to_ ELIZABETH, _speaks quickly and in deep concern_.] You
really wish to return home at once?


ELIZABETH.

[_Rising from her chair._] Oh, yes, yes--at once. [_Reaching her hand to
him appealingly._] Take me home, Mr. Darcy! Take me home!

     [_At this instant_ MR. AND MRS. COLLINS _appear at the garden door,
     and, transfixed with astonishment, stand gazing at_ DARCY _and_
     ELIZABETH.]




ACT IV


     _The Lawn and Shrubbery at Longbourn._ MRS. BENNET _is seated in a
     garden chair with pillows at her back. She has an umbrella over her
     head. Near her stands a table on which are bottles, dishes, etc.
     She wears a big cap, and is gowned in a widely-flowing, flowered
     chamber-robe, over which is fastened a shawl; across her knees is a
     lap-robe. Her entire get-up is grotesque and laughable. About her
     hover the housekeeper_, HILL _and_ JANE.

JANE.

Dear mamma, do try and take some of this nice gruel. You will be ill if
you do not eat something.


HILL.

Yes, do, I beg of you, Madam. Now that you are once more in the air, if
you will only take some food you will feel much better.


MRS. BENNET.

[_Fretfully._] How can I feel better? I must be ill. It is all very well
for the rest of you, now that this disgrace has been brought upon
me--but if I had been able to carry my point--if I could have gone to
Brighton with all my family, this would never have happened. But poor
dear Lydia had nobody to take care of her. Oh, that villainous Wickham!
I am sure there was some great neglect or other somewhere, for Lydia is
not the kind of girl to run away with a man. But no one would listen to
me. I was overruled, as I always am. Poor Lydia! Poor dear child!


JANE.

[_Soothingly._] Oh, mamma, try to be calm.


HILL.

Yes, Madam, this excitement is so bad for you.


MRS. BENNET.

How can I help being excited? You have no feelings. Here is Mr. Bennet
gone away, and I know he will fight that abominable Wickham and be
killed. And then what is to become of us all? The Collinses will turn us
out before Mr. Bennet is cold in his grave.


JANE.

Oh, mamma, do not have such terrific ideas.


MRS. BENNET.

[_Weeping._] If my brother Gardiner is not kind to me, I do not know
what we shall do.


JANE.

Yes, yes. My Uncle Gardiner is very kind. He is doing everything in his
power for us. He is helping my father now in London, you know. I hope
he will find Lydia, and perhaps he may be able to arrange a marriage
after all. You must not give up so, dear mamma.


HILL.

No indeed, Madam. You must not indeed.


MRS. BENNET.

[_Brightening._] Yes, Jane, that is true. My brother may be able to see
that they are married. Write to him at once, Jane. Tell him to find them
out wherever they may be, and if they are not married already, make them
marry. Oh, I do think that Wickham is the wickedest young man in the
world to so deceive my poor innocent Lydia. But, Jane, go and write my
brother and tell him that Lydia need not wait for wedding clothes--don't
let her even give directions till she has seen me, for she doesn't know
which are the best warehouses. And oh, Jane, tell my brother to keep
your father from fighting that hateful Wickham. Tell him what a dreadful
state I am in.


JANE.

Yes, mamma. [_She is about to go._]


MRS. BENNET.

Where are you going?


JANE.

Why, to write the letter, mamma.


MRS. BENNET.

[_Fretfully._] Oh, not just this minute. Don't leave me alone. Where is
Lizzy?


JANE.

She has gone down the road to meet the post. She hopes to bring you good
news.


MRS. BENNET.

[_Lamenting._] She had better stay here and be of some help. She has
only just got home and now she leaves me. But nobody thinks of me.
Nobody knows what I suffer. I am frightened out of my wits. I have such
tremblings and flutterings all over me--such spasms in my side--and
pains in my head, and such beatings at my heart. Oh, I can get no rest
by night or by day! [_To_ HILL.] You might try and do something, Hill.
Where is my soothing draught?


HILL.

[_Looking._] Here, Madam. No, I must have left it in your room. I will
run fetch it. [_She goes out quickly._]


JANE.

[_Who has been looking off toward the driveway during part of this
tirade._] Oh, mamma--mamma! Lizzy's running up the drive. She is
smiling! She has some good news, I am sure.


MRS. BENNET.

Take care, Jane. You are exciting me. Oh, my poor nerves.

     [ELIZABETH _enters, breathless. She has a letter in her hand._]

ELIZABETH.

Oh, good news--good news, Jane!--mamma! They are married!


JANE.

Oh, Lizzy--Lizzy!


MRS. BENNET.

You are sure, Lizzy? Don't excite me. You are sure?


ELIZABETH.

[_Half laughing and half crying._] Oh, yes, 'tis certain. My dear Aunt
Gardiner has written me all about it. They are really married! Oh, how
good my uncle is! [_She kisses the letter._]


MRS. BENNET.

Oh, Jane--Oh, Lizzy! My dear, dear Lydia! She is really married! I shall
see her again! Oh, my good, kind brother! But how did it happen, Lizzy?


JANE.

Yes, tell us all about it. Let me read it. [_She reaches for the
letter._]


ELIZABETH.

[_Keeping the letter._] No, I will tell you. Well, my father and my
uncle succeeded in finding Lydia. My aunt does not tell me just how it
was done.


MRS. BENNET.

[_Triumphantly._] And your father found that they were married after
all. I told him----

ELIZABETH.

No, mamma. They were not married, and they had no idea of being--but my
father and uncle insisted upon it. They took Lydia away at once to my
aunt's house and from there, they were married only yesterday at St.
Clement's Church.


MRS. BENNET.

St. Clement's--fine!


ELIZABETH.

My dear good uncle has arranged to have all Mr. Wickham's debts paid and
my father is to settle an allowance on Lydia.


JANE.

But where are they? What are they going to do?


ELIZABETH.

My father is coming home at once. He may be here at any moment. At first
he would not consent to let Lydia and Wickham come to us, but my aunt
and uncle urged it--and my father knew how anxious mamma would be--and
so _they_ are coming here too.


JANE.

At once?


ELIZABETH.

Yes, directly, to-day.


MRS. BENNET.

Oh, my dear Lydia! How I long to see her, and to see my dear Wickham
too. But the clothes, the wedding clothes! I must write to my Sister
Gardiner about them directly.

[_She tries to get out of the chair._]


JANE.

Oh, mamma, there is plenty of time for that.


MRS. BENNET.

Well, perhaps so. My dear, dear Lydia! How merry we shall all be
together! I am so happy! Lydia married. She is Mrs. Wickham. How well it
sounds. My dear Jane, I must see about the clothes. We will settle with
your father about the money later. Oh, I am in such a flutter! Here
comes Hill. [HILL _enters with the bottle_.] My dear Hill, have you
heard the news? Miss Lydia is married and is coming home directly.


HILL.

Indeed!


MRS. BENNET.

Yes, you shall all have a bowl of punch, to make merry for her wedding,
and I am going into the house to write about the clothes. [_To_ JANE,
_who is going with her_.] No, Jane, you stay where you are. I know what
I am about. Come, Hill. Think of it--Mrs. Wickham!

     [_She goes out leaning on_ HILL'S _arm, leaving_ JANE and ELIZABETH
     together.]

JANE.

Oh, Lizzy, how relieved and happy we should be. Is not it wonderful?
[_Anxiously._] Are you sure it is true? Have you told us all?


ELIZABETH.

Yes, Jane, it is true. They are really married. And for this we are to
be thankful. In spite of Lydia's folly and Wickham's wretched character,
we are to rejoice. How strange it is! Heigh-ho!


JANE.

[_Putting out her hand for the letter which_ ELIZABETH _still carries_.]
May not I read the letter, Lizzy?


ELIZABETH.

No, not now, dear. My aunt has some queer notions in her head. Later
perhaps. [_After a pause._] I am very sorry now that in my agitation I
told Mr. Darcy about this wretched affair. Now that it has come out so
well, he need never have known anything about it, and it would have
saved me a great deal of mortification.


JANE.

But how would you ever have explained things to Charlotte and Mr.
Collins without his help? Mr. Darcy made everything so smooth and
plausible for your sudden departure.


ELIZABETH.

Yes, that is true.


JANE.

Really, Lizzy, I think I shall have to take up the cudgels in Mr.
Darcy's defence. His kindness to you has quite won my heart, and his
amazing proposal was certainly a most flattering compliment. Why can you
see no good in Mr. Darcy, Lizzy? You were always so full of excuses for
Wickham, though it is true his open and delightful manners deceived us
all.


ELIZABETH.

Yes, there certainly was some great mismanagement in the education of
those two young men. One has all the goodness and the other all the
appearance of it.


JANE.

I never thought Mr. Darcy so deficient in the appearance of it as you
did, and he certainly could hardly have had the friends he has if he did
not possess some good qualities. [_Shyly._] Lizzy, have you heard that
Mr. Bingley is back in Netherfield?


ELIZABETH.

[_Astonished._] Oh, Jane, no. When did he come? Have you seen him?


JANE.

No; I hardly expect to see him.


ELIZABETH.

[_Brightly._] Yes, you will, if he has returned. [_Suddenly clapping her
hands._] Oh, I understand. [_Kissing her._] My darling Jane, you are
going to be very happy!


JANE.

Lizzy dear--don't, don't. That is all over now, and besides I don't want
to be happy unless you can be, too.


ELIZABETH.

Oh, forty Mr. Bingleys wouldn't make me happy. Till I have your
disposition, I never can have happiness. No, no, let me shift for
myself. Perhaps if I have very good luck I may meet with another Mr.
Collins in time.


HARRIS.

[_Entering._] Mr. Bennet has returned, Madam, and is looking for you.


JANE.

Papa returned!


ELIZABETH.

Where is he, Harris? [_Looking off._] There he comes! Papa!

     [_They run to meet_ MR. BENNET, _and, bringing him in, seat him in
     a garden chair, one on either side of him_.]

ELIZABETH.

Papa, tell us all about it quickly--quickly.


JANE.

Are they really married, papa?


MR. BENNET.

Yes, that misfortune is well settled on them. They are married fast
enough.


ELIZABETH.

And where are they? When will they be here?


MR. BENNET.

I should say they would be here directly. I didn't care to travel with
them, but they are not far behind--only just far enough to keep out of
the dust of my post chaise.


ELIZABETH.

Dear papa--how you must have suffered!


MR. BENNET.

Say nothing of that--who should suffer but myself? It has been my own
doing, and I ought to feel it.


ELIZABETH.

You must not be too severe upon yourself.


MR. BENNET.

You may well warn me against such an evil. No, Lizzy, let me once in my
life feel how much I have been to blame. The impression will pass away
soon enough.


ELIZABETH.

But, papa, how did you persuade them to marry?


MR. BENNET.

I didn't persuade them; I haven't the means. It is all your uncle's
doing. He has managed to buy Wickham for us.


JANE.

Oh, dear good uncle!


MR. BENNET.

[_Looks at_ JANE _quizzically_.] But there are two things that I want
very much to know--one is how much money your uncle has laid down to
bring it about, and the other, how I am ever to pay him.


JANE.

But my uncle did not do it all?


ELIZABETH.

No, papa. My Aunt Gardiner has written me that you are to give Lydia an
allowance.


MR. BENNET.

Yes, one hundred a year. Do you think that any man in his proper senses
would marry Lydia on so slight a temptation as one hundred a year?


ELIZABETH.

That is very true, though it had not occurred to me before. Oh, it must
be my uncle's doings. Generous man! I am afraid he has distressed
himself. A small sum could not do all this.


MR. BENNET.

No, Wickham's a fool if he takes Lydia with a farthing less than ten
thousand pounds. I should be sorry to think so ill of him in the very
beginning of our relationship.


ELIZABETH.

Ten thousand pounds! Heaven forbid! How is one-half such a sum to be
repaid?


MR. BENNET.

That is what I should like to know.


ELIZABETH.

Well, my uncle's kindness can never be requited. If such goodness as his
does not make Lydia miserable, then she will never deserve to be happy.

[_Laughter and voices are heard outside._]


ELIZABETH.

Surely I hear voices. [_Looking off._] Why, they have come. See
papa--Jane--there are Lydia and Wickham.


MR. BENNET.

Yes, here they are. I will go to the library. I can receive their
congratulations later. You know I am prodigiously fond of Wickham,
Lizzy. I defy even Sir William Lucas himself to produce a more valuable
son-in-law.

[_He goes out._]


JANE.

I must run and tell mamma.

     [_She is just starting when_ WICKHAM _and_ LYDIA _enter. They are
     in travelling dress and are followed by servants bringing all sorts
     of bandboxes, wraps and parcels. They come in with the utmost
     unconcern and no shadow of shame._]

LYDIA.

Well, Jane, well, Lizzy, here we are!


WICKHAM.

[_Smiling and unabashed._] My sister, Jane--My sister Elizabeth.

     [_He kisses their hands._ JANE _and_ ELIZABETH _are confused and
     blushing. Neither_ WICKHAM _nor_ LYDIA _is in the least
     discomposed_.]

LYDIA.

[_Looking about._] Good gracious! Here I am again! I am sure I had no
idea of being married when I went away, though I thought it would be
very good fun if I was. Why don't you take the boxes in, Harris?
Wickham, have you seen my pink-flowered bandbox? [_Looking over the
parcels._] No, it isn't here. Oh, my dear Wickham, do go fetch it--you
know 'tis the box with the white satin hat you bought me. I wouldn't
lose it for the world. Go, go!


WICKHAM.

Certainly, my dear. [_To the girls._] You see how eagerly I embrace my
new opportunities!

[_He runs out, laughing._]


LYDIA.

[_To_ ELIZABETH _and_ JANE.] Oh, girls, I am dying to give you an
account of my wedding.


ELIZABETH.

I think there cannot be too little said on that subject.


LYDIA.

La, you are so strange. But Jane wants to hear, I know. Anyway, I want
to tell you. Well, there was such a fuss! My aunt was preaching and
talking away to me all the time I was dressing, just as if she was
reading a sermon. I didn't hear one word in ten of it all. I was
thinking of my dear Wickham. I longed to know whether he would be
married in his blue coat. Well, we got to church, and then my uncle gave
me a fright after we got there, because he was so late, and he was going
to give me away, you know. But then, if he hadn't come, Mr. Darcy might
have done as well.


JANE AND ELIZABETH.

Mr. Darcy!


LYDIA.

Oh, yes, Darcy was there. He came along with Wickham. [_Suddenly
stopping._] But gracious me! I quite forgot. I ought not to have said a
word about it. I promised them as faithfully--what will Wickham say? It
was to be such a secret.


JANE.

If it was to be a secret, Lydia, say not another word on the subject. We
shall ask you no questions.

[ELIZABETH _looks most anxious, but says nothing_.]


LYDIA.

Thank you--for if you did, I should certainly tell you all, and then
Wickham would be angry. [_She sees_ MRS. BENNET, _who enters in great
excitement from the house_.] Oh, there is mamma.

     [_They rush into each other's arms._ WICKHAM _returns at about the
     same time_.]

MRS. BENNET.

Oh, my dear, dear Lydia! [_To_ WICKHAM _with affectionate warmth_.] My
dear Wickham!

[_They also embrace._]


LYDIA.

Oh, mamma! Aren't you glad to see us? [WICKHAM _turns and talks to_ JANE
_and_ ELIZABETH.] Do all the people hereabouts know that I am married? I
was afraid they might not, and so I let my hand just rest on the
window-frame outside the carriage, so that everybody could see my
wedding ring; and then I bowed and smiled like everything.


MRS. BENNET.

You may be sure, my dear, that everybody will rejoice with us in our
good luck. [_Sighing._] Your marriage is a great compensation to me
after all my disappointment about Jane and Lizzy. I do not blame Jane,
for she would have got Mr. Bingley if she could. But Lizzy! Oh, Lydia,
it is very hard to think she might now have been Mrs. Collins! But how
about your clothes?


LYDIA.

Oh, I have a lot already. You may be sure I would not forget _them_.


MRS. BENNET.

[_Alarmed._] But you didn't know the best warehouses! Well, never mind,
we will see to that later. Now you must all come in and have dinner.
You must be famished. Come, girls. Come, my dear Wickham.

     [_They all go toward the house. At the door_ LYDIA _pushes_ JANE
     _back_.]

LYDIA.

Ah, Jane, I take your place now. I go first because I am a married
woman.

     [_They all go into the house. After a pause_, HARRIS'S _voice is
     heard outside_.]

HARRIS.

Will not you come into the house, Madam?


LADY CATHERINE.

[_Entering, followed by_ HARRIS.] No, I prefer to remain here. Tell Miss
Elizabeth Bennet that a lady wishes to see her at once. Remember, I
cannot be kept waiting.


HARRIS.

Yes, Madam. [_He bows and goes out._]


LADY CATHERINE.

[_Looks about her with a sniff, then deliberately seats herself in the
big garden chair with the umbrella over it. She mutters to herself from
time to time and taps her foot impatiently._] Insufferable impudence!
Conceited little minx! She shall have a piece of my mind.

[ELIZABETH _comes to her from the house_.]


LADY CATHERINE.

[_Without moving._] Miss Bennet, you can be at no loss to understand the
reason of my journey hither. Your own heart--your own conscience must
tell you why I come.


ELIZABETH.

[_In unaffected astonishment._] Indeed, you are mistaken, Madam. I am
not at all able to account for the honour of seeing you here.


LADY CATHERINE.

Miss Bennet, you ought to know that I am not to be trifled with. I have
just been told that you--that Miss Elizabeth Bennet would in all
likelihood be soon married to my nephew, Mr. Darcy. Though I know it to
be a scandalous falsehood, I instantly resolved on setting off for this
place that I might make my sentiments known to you.


ELIZABETH.

[_With astonishment and disdain._] If you believed it impossible to be
true, I wonder you took the trouble of coming so far. What could your
Ladyship propose by it?


LADY CATHERINE.

At once to insist upon having such a report universally contradicted.


ELIZABETH.

[_Coolly._] Your coming to Longbourn to see me and my family, will be
rather a confirmation of it, if indeed such a report is in existence.


LADY CATHERINE.

If! Do you then pretend to be ignorant of it? Do you not know that such
a report is spread about?


ELIZABETH.

I never heard that it was.


LADY CATHERINE.

And can you likewise declare that there is no foundation for it?


ELIZABETH.

Your Ladyship may ask questions which I shall not choose to answer.


LADY CATHERINE.

This is not to be borne. Miss Bennet, I insist upon being satisfied. Has
he--has my nephew made you an offer of marriage?


ELIZABETH.

Your Ladyship has declared it to be impossible.


LADY CATHERINE.

It ought to be so. But your arts and allurements may have made him
forget what he owes to himself and to all his family. You may have drawn
him in.


ELIZABETH.

If I have, I shall be the last person to confess it.


LADY CATHERINE.

Miss Bennet, do you know who I am? I have not been accustomed to such
language as this. I am Mr. Darcy's own aunt, and am entitled to know all
his dearest concerns.


ELIZABETH.

But you are not entitled to know _mine_.


LADY CATHERINE.

Let me be rightly understood. This match can never take place. No,
never. Mr. Darcy is engaged to my daughter. Now what have you got to
say?


ELIZABETH.

Only this--that if it is so, you can have no reason to suppose Mr. Darcy
will make an offer to me.


LADY CATHERINE.

[_Hesitating._] The engagement between them is of a peculiar kind. While
in their cradles, my sister and I planned their union. Do you pay no
regard to the wishes of his friends? Do not you see that honour,
decorum--nay, interest, forbid you marrying my nephew? Yes _interest_,
Miss Bennet. For you will be slighted and despised by everyone connected
with him!


ELIZABETH.

These are heavy misfortunes. But the wife of Mr. Darcy must have such
extraordinary sources of happiness that she could have no cause to
repine.


LADY CATHERINE.

[_In a rage._] Obstinate, headstrong girl! Tell me once for all--are you
engaged to my nephew?


ELIZABETH.

[_Hesitates, then firmly._] I am not.


LADY CATHERINE.

[_Relieved._] And will you promise me never to enter into such an
engagement?


ELIZABETH.

I will make no promise of the kind.


LADY CATHERINE.

Miss Bennet, I am shocked and astonished. I shall not go away until you
have given me the assurance I require.


ELIZABETH.

And I certainly never shall give it. I must beg, therefore, to be
importuned no further on the subject.


LADY CATHERINE.

[_In a fury, but trying to speak calmly._] Not so hasty, if you please.
I had hoped to spare you this last humiliation--but your insolence
forbids it. I am no stranger to the particulars of your sister's
infamous elopement. I know all! The young man's marrying her was a
patched-up business at the expense of _my nephew_. [ELIZABETH _starts
violently_.] Oh, you needn't start, Miss! Nobody knows about the whole
affair better than you. But I don't wonder you blush to find yourself
discovered. You used your arts well. My nephew must have spent full five
or six thousand pounds to save your family from disgrace. I should think
that such generosity might appeal a little to your gratitude and your
sense of decency.


ELIZABETH.

[_Amazed._] Oh, Madam,--I----

LADY CATHERINE.

It is quite useless to protest. I have my facts from the best authority.
Heaven knows Darcy has reason enough to keep away from Wickham's
flirtations and entanglements, but [_stopping herself._] that is a
family affair. However, _you_ have managed to get him mixed up in them
again to the extent of five thousand pounds. But that is not
enough,--you want to make this shameless girl my nephew's _sister_, and
the son of his father's steward his brother. Heaven and Earth! Are the
shades of Pemberley to be thus polluted?


ELIZABETH.

[_Speaking with great effort._] Madam, you have insulted me in every
possible manner. I must beg to return to the house. This is beyond
endurance.


LADY CATHERINE.

Selfish girl! You are then resolved to have him?


ELIZABETH.

Lady Catherine, I have nothing further to say.


LADY CATHERINE.

[_Rising from her chair._] Very well. I shall now know how to act. Do
not imagine your ambition will be gratified. Depend upon it, I shall
carry my point. [_Going._] I take no leave of you, Miss Bennet. You
deserve no such attention. You will see what it is to rouse my
displeasure.

[LADY CATHERINE _goes out_.]


ELIZABETH.

[_Sinking upon the garden seat, overwhelmed._] Can it be possible? Do we
owe all this to Darcy? Oh, it is intolerable! [_She puts her hands over
her face in an abandonment of grief._]


JANE.

[_Is heard outside calling._] Lizzy! Lizzy! [_She enters, and on seeing
her sister rushes to her._] Lizzy dear! What is it? Is there any new
trouble?


ELIZABETH.

[_Throwing her arms about her sister._] Oh, Jane, Jane! Yes, there is
no end of trouble. Lady Catherine has been here.


JANE.

[_Astounded._] Lady Catherine!


ELIZABETH.

Yes, yes, and--she says--that--oh, Jane----

JANE.

[_Distressed._] _Tell_ me, Lizzy!


ELIZABETH.

She says it was Darcy who paid all the money to Wickham--it was Darcy
saved us--and--and she says I persuaded him. _I_ ensnared him, and--and
she has insulted me.


JANE.

My dear, dear Lizzy. There _must_ be some mistake. It was my good uncle
who----

ELIZABETH.

[_A little calmer._] No--no, Jane, it must be true. I can put things
together now. My aunt's hints in the letter--you know I did not want to
show it you. Then what Lydia let fall, and her fear of Wickham's anger.


JANE.

[_Soothingly._] Well, dear, even so, Mr. Darcy's _motive_ is clear
enough--and that should give you no pain.


ELIZABETH.

You are mistaken. I know his motive. He feels that he is responsible
because he was silent about Wickham's true character. He told me that
all this would never have happened, had he done his duty. And now, he
will despise us. He will never wish to see us again as long as he lives!

[_She walks up and down in great excitement._]


HARRIS.

[_Entering; to_ JANE.] The young gentlemen from Netherfield, Madam. I
told them they would find you here.


ELIZABETH.

Oh, Jane, I _cannot_ see them.

     [_She tries to run away, but before she can escape_ BINGLEY
     _enters, all smiles, followed by_ DARCY, _who looks very much
     troubled and excited. They are both in riding dress_; DARCY
     _carries a whip_.]

BINGLEY.

[_Shaking hands._] Miss Bennet, I am so happy to see you again. Miss
Elizabeth, it is good indeed to be back once more at Longbourn.

[_He takes_ JANE _to a garden seat_.]


DARCY.

[_Embarrassed._] Miss Bennet, believe me, I should not have followed my
friend. I only expected to ride with him to the Lodge, but--but I met
my aunt coming away from here, and from something she said, I feared,--I
imagined she might have offended--distressed you.

[ELIZABETH _does not reply_.]


BINGLEY.

[_Gaily._] Miss Bennet is going to show me the Hermitage. We shall be
back directly.

[JANE _and_ BINGLEY _go out_.]


DARCY.

[_Looking anxiously at_ ELIZABETH, _who remains silent_.] Forgive my
intrusion. I will go.

[_He starts to go away._]


ELIZABETH.

[_Recovering herself._] No--stay, Mr. Darcy. Excuse my own incivility.
Your aunt's visit has excited me. I shall be myself in a moment. [DARCY
_stands by, miserable. At length she speaks in a calmer tone._] Mr.
Darcy, your aunt has told me of our overwhelming obligation to you. You
must let me thank you for your unexampled kindness to my poor sister.


DARCY.

[_Exploding and banging his whip against his knees._]

Damn!--Oh, I beg your pardon, Miss Bennet. I _beg_ your pardon. What
right has my aunt to meddle in my affairs? How _dare_ she give you such
distress?


ELIZABETH.

It is far better that we know the truth, Mr. Darcy. For my part, I can
never express to you our obligation.


DARCY.

Oh, Miss Bennet--I beg of you! The obligation was entirely my own. I
only did what was my decent, plain duty. [_Faltering._] You remember--I
told you--if I had spoken, this would never have happened.


ELIZABETH.

Yes, I remember. But you exaggerated your responsibility. I--we--of
course my father will see you about your loan to us. I would not have
Lady Catherine think----

DARCY.

[_Furious again._] Oh, I will settle matters with Lady Catherine! Have
no fears on that score, Miss Bennet. _She_ shall be set right, I assure
you.


ELIZABETH.

Thank you. And for all your trouble--your kindness--my family can never
repay you.


DARCY.

Your family owes me nothing. If I had any thought beyond my duty, it was
a thought of--you. [ELIZABETH _turns away_.] Oh, pardon me. Perhaps, I
ought not to say all this--but I owe you a great deal, Miss
Bennet--more than you can know; and I want you to understand me better.
I really am not the pretentious prig I must have seemed to you. I wish
you could forgive my abominable pride.


ELIZABETH.

[_Looking at him with a half smile._] I will, on one condition.


DARCY.

Name it.


ELIZABETH.

That you forget my unwarrantable prejudice.


DARCY.

Oh, Miss Bennet! [_He goes impetuously forward--then restraining
himself, smiles and looks down at her._] I really think, after all, I
shall have to be grateful to my aunt. She has done us an enormous
service.


ELIZABETH.

[_Smiling still more._] Well, Lady Catherine loves to be useful!

     [_At the back of the scene_ BINGLEY _and_ JANE, _absorbed in each
     other, pass by, hand in hand_. ELIZABETH _looks at them, then turns
     to_ DARCY.]

ELIZABETH.

[_Archly._] Is _that_ by your permission?


DARCY.

[_Ruefully._] Yes, I told you I had been kinder to my friend than to
myself.

     [ELIZABETH, _silent, still looks after_ BINGLEY _and_ JANE.]

DARCY.

[_Continues in a discouraged tone._] Well, I deserve it. It is my own
fault. My selfish conceit has wounded you past help. Every sentiment of
your nature has felt it--seen it.


ELIZABETH.

[_Demurely._] But _one_ sentiment they say is _blind_.


DARCY.

[_Stunned._] Miss Bennet! [ELIZABETH _looks up at him. He rushes toward
her._] Dearest, loveliest Elizabeth!

[_He holds her in his arms._]


CURTAIN.





End of the Project Gutenberg EBook of Pride and Prejudice, a play, by
Mary Keith Medbery Mackaye

*** END OF THIS PROJECT GUTENBERG EBOOK PRIDE AND PREJUDICE, A PLAY ***

***** This file should be named 37431-8.txt or 37431-8.zip *****
This and all associated files of various formats will be found in:
        http://www.gutenberg.org/3/7/4/3/37431/

Produced by Chuck Greif and the Online Distributed
Proofreading Team at http://www.pgdp.net (This book was
produced from scanned images of public domain material
from the Internet Archive.)


Updated editions will replace the previous one--the old editions
will be renamed.

Creating the works from public domain print editions means that no
one owns a United States copyright in these works, so the Foundation
(and you!) can copy and distribute it in the United States without
permission and without paying copyright royalties.  Special rules,
set forth in the General Terms of Use part of this license, apply to
copying and distributing Project Gutenberg-tm electronic works to
protect the PROJECT GUTENBERG-tm concept and trademark.  Project
Gutenberg is a registered trademark, and may not be used if you
charge for the eBooks, unless you receive specific permission.  If you
do not charge anything for copies of this eBook, complying with the
rules is very easy.  You may use this eBook for nearly any purpose
such as creation of derivative works, reports, performances and
research.  They may be modified and printed and given away--you may do
practically ANYTHING with public domain eBooks.  Redistribution is
subject to the trademark license, especially commercial
redistribution.



*** START: FULL LICENSE ***

THE FULL PROJECT GUTENBERG LICENSE
PLEASE READ THIS BEFORE YOU DISTRIBUTE OR USE THIS WORK

To protect the Project Gutenberg-tm mission of promoting the free
distribution of electronic works, by using or distributing this work
(or any other work associated in any way with the phrase "Project
Gutenberg"), you agree to comply with all the terms of the Full Project
Gutenberg-tm License (available with this file or online at
http://gutenberg.org/license).


Section 1.  General Terms of Use and Redistributing Project Gutenberg-tm
electronic works

1.A.  By reading or using any part of this Project Gutenberg-tm
electronic work, you indicate that you have read, understand, agree to
and accept all the terms of this license and intellectual property
(trademark/copyright) agreement.  If you do not agree to abide by all
the terms of this agreement, you must cease using and return or destroy
all copies of Project Gutenberg-tm electronic works in your possession.
If you paid a fee for obtaining a copy of or access to a Project
Gutenberg-tm electronic work and you do not agree to be bound by the
terms of this agreement, you may obtain a refund from the person or
entity to whom you paid the fee as set forth in paragraph 1.E.8.

1.B.  "Project Gutenberg" is a registered trademark.  It may only be
used on or associated in any way with an electronic work by people who
agree to be bound by the terms of this agreement.  There are a few
things that you can do with most Project Gutenberg-tm electronic works
even without complying with the full terms of this agreement.  See
paragraph 1.C below.  There are a lot of things you can do with Project
Gutenberg-tm electronic works if you follow the terms of this agreement
and help preserve free future access to Project Gutenberg-tm electronic
works.  See paragraph 1.E below.

1.C.  The Project Gutenberg Literary Archive Foundation ("the Foundation"
or PGLAF), owns a compilation copyright in the collection of Project
Gutenberg-tm electronic works.  Nearly all the individual works in the
collection are in the public domain in the United States.  If an
individual work is in the public domain in the United States and you are
located in the United States, we do not claim a right to prevent you from
copying, distributing, performing, displaying or creating derivative
works based on the work as long as all references to Project Gutenberg
are removed.  Of course, we hope that you will support the Project
Gutenberg-tm mission of promoting free access to electronic works by
freely sharing Project Gutenberg-tm works in compliance with the terms of
this agreement for keeping the Project Gutenberg-tm name associated with
the work.  You can easily comply with the terms of this agreement by
keeping this work in the same format with its attached full Project
Gutenberg-tm License when you share it without charge with others.

1.D.  The copyright laws of the place where you are located also govern
what you can do with this work.  Copyright laws in most countries are in
a constant state of change.  If you are outside the United States, check
the laws of your country in addition to the terms of this agreement
before downloading, copying, displaying, performing, distributing or
creating derivative works based on this work or any other Project
Gutenberg-tm work.  The Foundation makes no representations concerning
the copyright status of any work in any country outside the United
States.

1.E.  Unless you have removed all references to Project Gutenberg:

1.E.1.  The following sentence, with active links to, or other immediate
access to, the full Project Gutenberg-tm License must appear prominently
whenever any copy of a Project Gutenberg-tm work (any work on which the
phrase "Project Gutenberg" appears, or with which the phrase "Project
Gutenberg" is associated) is accessed, displayed, performed, viewed,
copied or distributed:

This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it away or
re-use it under the terms of the Project Gutenberg License included
with this eBook or online at www.gutenberg.org

1.E.2.  If an individual Project Gutenberg-tm electronic work is derived
from the public domain (does not contain a notice indicating that it is
posted with permission of the copyright holder), the work can be copied
and distributed to anyone in the United States without paying any fees
or charges.  If you are redistributing or providing access to a work
with the phrase "Project Gutenberg" associated with or appearing on the
work, you must comply either with the requirements of paragraphs 1.E.1
through 1.E.7 or obtain permission for the use of the work and the
Project Gutenberg-tm trademark as set forth in paragraphs 1.E.8 or
1.E.9.

1.E.3.  If an individual Project Gutenberg-tm electronic work is posted
with the permission of the copyright holder, your use and distribution
must comply with both paragraphs 1.E.1 through 1.E.7 and any additional
terms imposed by the copyright holder.  Additional terms will be linked
to the Project Gutenberg-tm License for all works posted with the
permission of the copyright holder found at the beginning of this work.

1.E.4.  Do not unlink or detach or remove the full Project Gutenberg-tm
License terms from this work, or any files containing a part of this
work or any other work associated with Project Gutenberg-tm.

1.E.5.  Do not copy, display, perform, distribute or redistribute this
electronic work, or any part of this electronic work, without
prominently displaying the sentence set forth in paragraph 1.E.1 with
active links or immediate access to the full terms of the Project
Gutenberg-tm License.

1.E.6.  You may convert to and distribute this work in any binary,
compressed, marked up, nonproprietary or proprietary form, including any
word processing or hypertext form.  However, if you provide access to or
distribute copies of a Project Gutenberg-tm work in a format other than
"Plain Vanilla ASCII" or other format used in the official version
posted on the official Project Gutenberg-tm web site (www.gutenberg.org),
you must, at no additional cost, fee or expense to the user, provide a
copy, a means of exporting a copy, or a means of obtaining a copy upon
request, of the work in its original "Plain Vanilla ASCII" or other
form.  Any alternate format must include the full Project Gutenberg-tm
License as specified in paragraph 1.E.1.

1.E.7.  Do not charge a fee for access to, viewing, displaying,
performing, copying or distributing any Project Gutenberg-tm works
unless you comply with paragraph 1.E.8 or 1.E.9.

1.E.8.  You may charge a reasonable fee for copies of or providing
access to or distributing Project Gutenberg-tm electronic works provided
that

- You pay a royalty fee of 20% of the gross profits you derive from
     the use of Project Gutenberg-tm works calculated using the method
     you already use to calculate your applicable taxes.  The fee is
     owed to the owner of the Project Gutenberg-tm trademark, but he
     has agreed to donate royalties under this paragraph to the
     Project Gutenberg Literary Archive Foundation.  Royalty payments
     must be paid within 60 days following each date on which you
     prepare (or are legally required to prepare) your periodic tax
     returns.  Royalty payments should be clearly marked as such and
     sent to the Project Gutenberg Literary Archive Foundation at the
     address specified in Section 4, "Information about donations to
     the Project Gutenberg Literary Archive Foundation."

- You provide a full refund of any money paid by a user who notifies
     you in writing (or by e-mail) within 30 days of receipt that s/he
     does not agree to the terms of the full Project Gutenberg-tm
     License.  You must require such a user to return or
     destroy all copies of the works possessed in a physical medium
     and discontinue all use of and all access to other copies of
     Project Gutenberg-tm works.

- You provide, in accordance with paragraph 1.F.3, a full refund of any
     money paid for a work or a replacement copy, if a defect in the
     electronic work is discovered and reported to you within 90 days
     of receipt of the work.

- You comply with all other terms of this agreement for free
     distribution of Project Gutenberg-tm works.

1.E.9.  If you wish to charge a fee or distribute a Project Gutenberg-tm
electronic work or group of works on different terms than are set
forth in this agreement, you must obtain permission in writing from
both the Project Gutenberg Literary Archive Foundation and Michael
Hart, the owner of the Project Gutenberg-tm trademark.  Contact the
Foundation as set forth in Section 3 below.

1.F.

1.F.1.  Project Gutenberg volunteers and employees expend considerable
effort to identify, do copyright research on, transcribe and proofread
public domain works in creating the Project Gutenberg-tm
collection.  Despite these efforts, Project Gutenberg-tm electronic
works, and the medium on which they may be stored, may contain
"Defects," such as, but not limited to, incomplete, inaccurate or
corrupt data, transcription errors, a copyright or other intellectual
property infringement, a defective or damaged disk or other medium, a
computer virus, or computer codes that damage or cannot be read by
your equipment.

1.F.2.  LIMITED WARRANTY, DISCLAIMER OF DAMAGES - Except for the "Right
of Replacement or Refund" described in paragraph 1.F.3, the Project
Gutenberg Literary Archive Foundation, the owner of the Project
Gutenberg-tm trademark, and any other party distributing a Project
Gutenberg-tm electronic work under this agreement, disclaim all
liability to you for damages, costs and expenses, including legal
fees.  YOU AGREE THAT YOU HAVE NO REMEDIES FOR NEGLIGENCE, STRICT
LIABILITY, BREACH OF WARRANTY OR BREACH OF CONTRACT EXCEPT THOSE
PROVIDED IN PARAGRAPH F3.  YOU AGREE THAT THE FOUNDATION, THE
TRADEMARK OWNER, AND ANY DISTRIBUTOR UNDER THIS AGREEMENT WILL NOT BE
LIABLE TO YOU FOR ACTUAL, DIRECT, INDIRECT, CONSEQUENTIAL, PUNITIVE OR
INCIDENTAL DAMAGES EVEN IF YOU GIVE NOTICE OF THE POSSIBILITY OF SUCH
DAMAGE.

1.F.3.  LIMITED RIGHT OF REPLACEMENT OR REFUND - If you discover a
defect in this electronic work within 90 days of receiving it, you can
receive a refund of the money (if any) you paid for it by sending a
written explanation to the person you received the work from.  If you
received the work on a physical medium, you must return the medium with
your written explanation.  The person or entity that provided you with
the defective work may elect to provide a replacement copy in lieu of a
refund.  If you received the work electronically, the person or entity
providing it to you may choose to give you a second opportunity to
receive the work electronically in lieu of a refund.  If the second copy
is also defective, you may demand a refund in writing without further
opportunities to fix the problem.

1.F.4.  Except for the limited right of replacement or refund set forth
in paragraph 1.F.3, this work is provided to you 'AS-IS' WITH NO OTHER
WARRANTIES OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
WARRANTIES OF MERCHANTIBILITY OR FITNESS FOR ANY PURPOSE.

1.F.5.  Some states do not allow disclaimers of certain implied
warranties or the exclusion or limitation of certain types of damages.
If any disclaimer or limitation set forth in this agreement violates the
law of the state applicable to this agreement, the agreement shall be
interpreted to make the maximum disclaimer or limitation permitted by
the applicable state law.  The invalidity or unenforceability of any
provision of this agreement shall not void the remaining provisions.

1.F.6.  INDEMNITY - You agree to indemnify and hold the Foundation, the
trademark owner, any agent or employee of the Foundation, anyone
providing copies of Project Gutenberg-tm electronic works in accordance
with this agreement, and any volunteers associated with the production,
promotion and distribution of Project Gutenberg-tm electronic works,
harmless from all liability, costs and expenses, including legal fees,
that arise directly or indirectly from any of the following which you do
or cause to occur: (a) distribution of this or any Project Gutenberg-tm
work, (b) alteration, modification, or additions or deletions to any
Project Gutenberg-tm work, and (c) any Defect you cause.


Section  2.  Information about the Mission of Project Gutenberg-tm

Project Gutenberg-tm is synonymous with the free distribution of
electronic works in formats readable by the widest variety of computers
including obsolete, old, middle-aged and new computers.  It exists
because of the efforts of hundreds of volunteers and donations from
people in all walks of life.

Volunteers and financial support to provide volunteers with the
assistance they need, are critical to reaching Project Gutenberg-tm's
goals and ensuring that the Project Gutenberg-tm collection will
remain freely available for generations to come.  In 2001, the Project
Gutenberg Literary Archive Foundation was created to provide a secure
and permanent future for Project Gutenberg-tm and future generations.
To learn more about the Project Gutenberg Literary Archive Foundation
and how your efforts and donations can help, see Sections 3 and 4
and the Foundation web page at http://www.pglaf.org.


Section 3.  Information about the Project Gutenberg Literary Archive
Foundation

The Project Gutenberg Literary Archive Foundation is a non profit
501(c)(3) educational corporation organized under the laws of the
state of Mississippi and granted tax exempt status by the Internal
Revenue Service.  The Foundation's EIN or federal tax identification
number is 64-6221541.  Its 501(c)(3) letter is posted at
http://pglaf.org/fundraising.  Contributions to the Project Gutenberg
Literary Archive Foundation are tax deductible to the full extent
permitted by U.S. federal laws and your state's laws.

The Foundation's principal office is located at 4557 Melan Dr. S.
Fairbanks, AK, 99712., but its volunteers and employees are scattered
throughout numerous locations.  Its business office is located at
809 North 1500 West, Salt Lake City, UT 84116, (801) 596-1887, email
business@pglaf.org.  Email contact links and up to date contact
information can be found at the Foundation's web site and official
page at http://pglaf.org

For additional contact information:
     Dr. Gregory B. Newby
     Chief Executive and Director
     gbnewby@pglaf.org


Section 4.  Information about Donations to the Project Gutenberg
Literary Archive Foundation

Project Gutenberg-tm depends upon and cannot survive without wide
spread public support and donations to carry out its mission of
increasing the number of public domain and licensed works that can be
freely distributed in machine readable form accessible by the widest
array of equipment including outdated equipment.  Many small donations
($1 to $5,000) are particularly important to maintaining tax exempt
status with the IRS.

The Foundation is committed to complying with the laws regulating
charities and charitable donations in all 50 states of the United
States.  Compliance requirements are not uniform and it takes a
considerable effort, much paperwork and many fees to meet and keep up
with these requirements.  We do not solicit donations in locations
where we have not received written confirmation of compliance.  To
SEND DONATIONS or determine the status of compliance for any
particular state visit http://pglaf.org

While we cannot and do not solicit contributions from states where we
have not met the solicitation requirements, we know of no prohibition
against accepting unsolicited donations from donors in such states who
approach us with offers to donate.

International donations are gratefully accepted, but we cannot make
any statements concerning tax treatment of donations received from
outside the United States.  U.S. laws alone swamp our small staff.

Please check the Project Gutenberg Web pages for current donation
methods and addresses.  Donations are accepted in a number of other
ways including checks, online payments and credit card donations.
To donate, please visit: http://pglaf.org/donate


Section 5.  General Information About Project Gutenberg-tm electronic
works.

Professor Michael S. Hart is the originator of the Project Gutenberg-tm
concept of a library of electronic works that could be freely shared
with anyone.  For thirty years, he produced and distributed Project
Gutenberg-tm eBooks with only a loose network of volunteer support.


Project Gutenberg-tm eBooks are often created from several printed
editions, all of which are confirmed as Public Domain in the U.S.
unless a copyright notice is included.  Thus, we do not necessarily
keep eBooks in compliance with any particular paper edition.


Most people start at our Web site which has the main PG search facility:

     http://www.gutenberg.org

This Web site includes information about Project Gutenberg-tm,
including how to make donations to the Project Gutenberg Literary
Archive Foundation, how to help produce our new eBooks, and how to
subscribe to our email newsletter to hear about new eBooks."""

def check_punctuaction(text):
    text2 = ""
    for ch in text:
        if ch.isalpha() or ch == " " or ch == "\n":
            text2 += ch.lower()
    return text2

def create_dic(text, uninteresting_words):
    text = text.split()
    text_dic = {}
    for word in text:
        if word not in uninteresting_words:
            if word not in text_dic:
                text_dic[word] = 1
            else:
                text_dic[word] += 1
    return text_dic

def unique_words(text):
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    text = check_punctuaction(text)
    dictionary_unique_words = create_dic(text,uninteresting_words)
    return dictionary_unique_words

if __name__ == '__main__':
        print(unique_words(text))
