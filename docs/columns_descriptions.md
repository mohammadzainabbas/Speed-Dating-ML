### Speed Dating - Column Descriptions

__Column__ | __Description__ | __Type__ 
--- | --- | --- 
`iid` | unique subject number, group(wave id gender) | `int`
`id` | subject number within wave | `float`
`gender` | tells the gender |	`0 = Female,  1 = Male`
`idg` | subject number within gender, group(id gender) | `int`
`condtn` | choice type | `1 = limited choice, 2 = extensive choice`
`wave` | dating wave. see more detail [here](#wave-dating) | `int`
`round` | number of people that met in wave | `int`
`position` | station number where met partner | `int`
`positin1` | station number where started | `float`
`order` | the number of date that night when met partner | `int`
`partner` | partner’s id number the night of event | `int`
`pid` | partner’s iid number | `float`
`match` | tells the match | `1 = yes, 0 = no`
`int_corr` | correlation between participant’s and partner’s ratings of interests in time 1 (first date) | `float`
`samerace` | participant and the partner were the same race | `1 = yes, 0 = no`
`age_o` | age of partner | `float`
`race_o` | race of partner | `float`
`pf_o_att` | partner’s stated preference at time 1 (attr1_1) - for attractiveness | `float`
`pf_o_sin` | partner’s stated preference at time 1 (sin1_1) - for sincerity | `float`
`pf_o_int` | partner’s stated preference at time 1 (int1_1) - for intelligence | `float`
`pf_o_fun` | partner’s stated preference at time 1 (fun1_1) - for fun | `float`
`pf_o_amb` | partner’s stated preference at time 1 (amb1_1) - for ambition | `float`
`pf_o_sha` | partner’s stated preference at time 1 (sha1_1) - for shared interests | `float`
`dec_o` | decision of partner the night of event | `int`
`attr_o` | rating by partner the night of the event, for attractiveness | `float`
`sinc_o` | rating by partner the night of the event, for sincerity | `float`
`intel_o` | rating by partner the night of the event, for intelligence | `float`
`fun_o` | rating by partner the night of the event, for fun | `float`
`amb_o` | rating by partner the night of the event, for ambition | `float`
`shar_o` | rating by partner the night of the event, for shared interests | `float`

---

### Survey data columns which were filled out by students that were interested in participating (before signup)

__Column__ | __Description__ | __Type__ 
--- | --- | --- 
`age` | age of the person | `float`
`field` | field of study | `str`
`field_cd` | encoding for `field` attribute | `1 = Law  , 2 = Math, 3 = Social Science, Psychologist , 4 = Medical Science, Pharmaceuticals, and Bio Tech , 5 = Engineering  , 6 = English/Creative Writing/ Journalism , 7 = History/Religion/Philosophy , 8 = Business/Econ/Finance , 9 = Education, Academia , 10 = Biological Sciences/Chemistry/Physics, 11 = Social Work, 12 = Undergrad/undecided , 13 = Political Science/International Affairs, 14 = Film, 15 = Fine Arts/Arts Administration, 16 = Languages, 17 = Architecture, 18 = Other`
`undergrd` | school attended for undergraduate degree | `str`
`mn_sat` | Median SAT score for the undergraduate institution where attended. Taken from Barron’s 25th Edition college profile book.  Proxy for intelligence. | `str`

tuition: 	Tuition listed for each response to undergrad in Barron’s 25th Edition 			college profile book.

race:
	Black/African American=1
	European/Caucasian-American=2
	Latino/Hispanic American=3
	Asian/Pacific Islander/Asian-American=4
	Native American=5
	Other=6

imprace:
How important is it to you (on a scale of 1-10) that a person you date be of the same racial/ethnic background?

imprelig:
 How important is it to you (on a scale of 1-10) that a person you date be of the same religious background?

 from:
Where are you from originally (before coming to Columbia)? 

zipcode:
What was the zip code of the area where you grew up? 

income:
Median household income based on zipcode using the Census Bureau website:
http://venus.census.gov/cdrom/lookup/CMD=LIST/DB=C90STF3B/LEV=ZIP 
When there is no income it means that they are either from abroad or did not enter their zip code.

goal:
What is your primary goal in participating in this event? 
	Seemed like a fun night out=1
	To meet new people=2
	To get a date=3
	Looking for a serious relationship=4
	To say I did it=5
	Other=6

date:
In general, how frequently do you go on dates? 
	Several times a week=1
	Twice a week=2
	Once a week=3
	Twice a month=4
	Once a month=5
	Several times a year=6
	Almost never=7

go out:
How often do you go out (not necessarily on dates)?
	Several times a week=1
	Twice a week=2
	Once a week=3
	Twice a month=4
	Once a month=5
	Several times a year=6
	Almost never=7

career:
What is your intended career?

career_c: career coded 
1= Lawyer 
2= Academic/Research 
3= Psychologist 
4= Doctor/Medicine 
5=Engineer 
6= Creative Arts/Entertainment 
7= Banking/Consulting/Finance/Marketing/Business/CEO/Entrepreneur/Admin 
8= Real Estate 
9= International/Humanitarian Affairs 
10= Undecided 
11=Social Work
12=Speech Pathology
13=Politics
14=Pro sports/Athletics
15=Other
16=Journalism
17=Architecture


12.  How interested are you in the following activities, on a scale of 1-10?
sports: Playing sports/ athletics
tvsports: Watching sports
excersice: Body building/exercising
dining: Dining out
museums: Museums/galleries
art: Art
hiking:  Hiking/camping
gaming: Gaming
clubbing: Dancing/clubbing
reading: Reading
tv: Watching TV
theater: Theater
movies: Movies
concerts: Going to concerts
music: Music
shopping: Shopping
yoga: Yoga/meditation

 exphappy:
Overall, on a scale of 1-10, how happy do you expect to be with the people you meet 
during the speed-dating event?

expnum: 
Out of the 20 people you will meet, how many do you expect will be interested in dating you? 

We want to know what you look for in the opposite sex. 
Waves 6-9: Please rate the importance of the following attributes in a potential date on a scale of 1-10 (1=not at all important, 10=extremely important):
Waves 1-5, 10-21: You have 100 points to distribute among the following attributes -- give more points to those attributes that are more important in a potential date, and fewer points to those attributes that are less important in a potential date.  Total points must equal 100.
 
attr1_1 
Attractive
sinc1_1
Sincere
intel1_1
Intelligent
fun1_1
Fun
amb1_1
Ambitious
shar1_1
Has shared interests/hobbies

Now we want to know what you think MOST of your fellow men/women look for in the opposite sex.
Waves 6-9: Please rate the importance of the following attributes on a scale of 1-10 (1=not at all important, 10=extremely important):
Waves 10-21 : You have 100 points to distribute among the following attributes -- give more points to those attributes that you think your fellow men/women find more important in a potential date and fewer points to those attributes that they find less important in a potential date.  Total points must equal 100.

attr4_1
Attractive
sinc4_1
Sincere
intel4_1
Intelligent
fun4_1
Fun
amb4_1
Ambitious
shar4_1
Shared Interests/Hobbies



What do you think the opposite sex looks for in a date?
Waves 6-9: Please rate the importance of the following attributes on a scale of 1-10 (1=not at all important, 10=extremely important):
 Waves 1-5 and 10-21: Please distribute 100 points among the following attributes -- give more points to those attributes that you think are more important to members of the opposite sex when they are deciding whether to date someone.  Total points must equal 100.

attr2_1 
Attractive
sinc2_1
Sincere
int2_1
Intelligent
fun2_1
Fun
amb2_1
Ambitious
shar2_1
Has shared interests/hobbies

How do you think you measure up?
Please rate your opinion of your own attributes, on a scale of 1-10 (be honest!):
attr3_1 
Attractive
sinc3_1
Sincere
int3_1
Intelligent
fun3_1
Fun
amb3_1
Ambitious

And finally, how do you think others perceive you? 
Please rate yourself how you think others would rate you on each of the following attributes, on a scale of 1-10 (1=awful, 10=great) 
attr5_1 
Attractive
sinc5_1
Sincere
int5_1
Intelligent
fun5_1
Fun
amb5_1
Ambitious
Scorecard:
[Filled out by subjects after each "date" during the event.]

SCORECARD
YOUR ID NUMBER: 
Circle “Yes” or “No” below the ID number of each person you meet to indicate whether or not you would like to see him or her again.  Rate their attributes on a scale of 1-10:  (1=awful, 10=great).  If you haven’t formed an opinion based on your conversation, fill in N/A, but please fill in all boxes.  This will be TOTALLY confidential and will NOT be shared with anyone.  Then, answer the remaining questions for each person you meet.
ID #:	1	2	3	4	5	6	7	8	9	10
dec										
Decision	1=yes
0=no	Y
n 	yes
no	yes
no	yes
no	yes
no	yes
no	yes
no	yes
no	yes
no
										
Attributes
(1=awful, 10=great)										
Attractive	attr									
Sincere	sinc									
Intelligent	intel									
Fun	fun									
Ambitious	amb									
Shared Interests/Hobbies	shar									
										
Overall, how much do you like this person?
(1=don't like at all, 10=like a lot)	like									
How probable do you think it is that this person will say 'yes' for you?
(1=not probable, 10=extremely probable)	prob									
Have you met this person before?	met
1=yes
2=no	 	yes
no	yes
no	yes
no	yes
no	yes
no	yes
no	yes
no	yes
no



ID #:	11	12	13	14	15	16	17	18	19	20
										
Decision	yes
no	yes
no 	yes
no	yes
no	yes
no	yes
no	yes
no	yes
no	yes
no	yes
no
										
Attributes
(1=awful, 10=great)										
Attractive										
Sincere										
Intelligent										
Fun										
Ambitious										
Shared Interests/Hobbies										
										
Overall, how much do you like this person?
(1=don't like at all, 10=like a lot)										
How probable do you think it is that this person will say 'yes' for you?
(1=not probable, 10=extremely probable)										
Have you met this person before?	yes
no	yes
no 	yes
no	yes
no	yes
no	yes
no	yes
no	yes
no	yes
no	yes
no



match_es:
How many matches do you estimate you will get (a match occurs when you and your partner both check “Yes” next to decision)?: ___________


Half way through meeting all potential dates during the night of the event on their scorecard:

Hold up!  Now that you are half way through your Speed Dates, we have a few questions for you…

We want to know what you look for in the opposite sex.
Please rate the importance of the following attributes in a potential date on a scale of 1-10: (1=not at all important, 10=extremely important).
attr1_s
Attractive______
sinc1_s
Sincere  ______
intel1_s
Intelligent _______
fun1_s
Fun _______
amb1_s
Ambitious  ________
shar1_s
Shared Interests/Hobbies  __________

Please rate your opinion of your own attributes, on a scale of 1-10 (1=awful, 10=great) --Be honest!
attr3_s
Attractive______
sinc3_s
Sincere  ______
intel3_s
Intelligent _______
fun3_s
Fun _______
amb3_s
Ambitious  ________



followup/Time2:
[Survey is filled out the day after participating in the event.  Subjects must have submitted this in order to be sent their matches.]
satis_2:
Overall, how satisfied were you with the people you met? (1=not at all satisfied, 10=extremely satisfied)

length:
Four minutes is:
	Too little=1
	Too much=2
	Just Right=3

numdat_2:
The number of Speed "Dates" you had was:	
	Too few=1
	Too many=2
	Just right=3

Now, think back to your yes/no decisions during the Speed Dating event.  Try to distribute the 100 points among these six attributes in the way that best reflects the actual importance of these attributes in your decisions. Give more points to those attributes that were more important in your decisions, and fewer points to those attributes that were less important in your decisions.  Total points must equal 100. 
attr7_2 
Attractive
sinc7_2
Sincere
intel7_2
Intelligent
fun7_2
Fun
amb7_2
Ambitious
shar7_2
Has shared interests/hobbies

We want to know what you look for in the opposite sex. 
Waves 1-5 and 10-21: You have 100 points to distribute among the following attributes -- give more points to those attributes that are more important in a potential date, and fewer points to those attributes that are less important in a potential date.  Total points must equal 100.
Waves 6-9: Please rate the importance of the following attributes in a potential date on a scale of 1-10 (1=not at all important, 10=extremely important): 
attr1_2 
Attractive
sinc1_2
Sincere
intel1_2
Intelligent
fun1_2
Fun
amb1_2
Ambitious
shar1_2
Has shared interests/hobbies

What do you think MOST of your fellow men/women look for in the opposite sex?
You have 100 points to distribute among the following attributes -- give more points to those attributes that you think your fellow men/women find more important in a potential date, and fewer points to those attributes that they find less important in a potential date.
Total points must equal 100.
attr4_2
Attractive
sinc4_2
Sincere
intel4_2
Intelligent
fun4_2
Fun
amb4_2
Ambitious
shar4_2
Shared Interests/Hobbies

What do you think the opposite sex looks for in a date?
Please distribute 100 points among the following attributes -- give more points to those attributes that you think are more important to members of the opposite sex when they are deciding whether to date someone.  Total points must equal 100.
attr2_2 
Attractive
sinc2_2
Sincere
intel2_2
Intelligent
fun2_2
Fun
amb2_2
Ambitious
shar2_2
Has shared interests/hobbies

How do you think you measure up?
Please rate your opinion of your own attributes, on a scale of 1-10 (1= awful and 10=great).  Be honest!
attr3_2 
Attractive
sinc3_2
Sincere
int3_2
Intelligent
fun3_2
Fun
amb3_2
Ambitious

And finally, how do you think others perceive you?
Please rate yourself how you think others would rate you on each of the following attributes, on a scale of 1-10 (1=awful, 10=great)
attr5_2 
Attractive
sinc5_2
Sincere
int5_2
Intelligent
fun5_2
Fun
amb5_2
Ambitious
	


followup2/ Time3:
[Subjects filled out 3-4 weeks after they had been sent their matches]

SINCE HURRYDATING…

1.  Of the matches that you received:
 you_call:
(a) How many have you contacted to set up a date?
them_cal:
(b) How many have contacted you?

date_3:
Have you been on a date with any of your matches?
	Yes=1
	No=2

If you have been on at least one date, please answer the following:
numdat_3: 
(a) How many of your matches have you been on a date with so far?
num_in_3
If yes, how many?

What do you look for in the opposite sex?
Please distribute 100 points among the following attributes -- give more to attributes that were more important in your decisions when Hurrydating, and less to attributes that were less important.  Total points must equal 100.
We want to know what you look for in the opposite sex. 
Please rate the importance of the following attributes in a potential date on a scale of 1-10 (1=not at all important, 10=extremely important):
attr1_3 
Attractive
sinc1_3
Sincere
intel1_3
Intelligent
fun1_3
Fun
amb1_3
Ambitious
shar1_3
Has shared interests/hobbies

Now, think back to your yes/no decisions during the night of the Speed Dating event.  Try to distribute the 100 points among these six attributes in the way that best reflects the actual importance of these attributes in your decisions. Give more points to those attributes that were more important in your decisions, and fewer points to those attributes that less less important in your decisions.  Total points must equal 100. 
attr7_3 
Attractive
sinc7_3
Sincere
intel7_3
Intelligent
fun7_3
Fun
amb7_3
Ambitious
shar7_3
Has shared interests/hobbies


Now we want to know what you think MOST of your fellow men/women look for in the opposite sex. 
Please rate the importance of the following attributes on a scale of 1-10 (1=not at all important, 10=extremely important):
attr4_3 
Attractive
sinc4_3
Sincere
intel4_3
Intelligent
fun4_3
Fun
amb4_3
Ambitious
shar4_3
Has shared interests/hobbies


What do you think the opposite sex looks for in a date? 
Please rate the importance of the following attributes on a scale of 1-10 (1=not at all important, 10=extremely important):
attr2_3 
Attractive
sinc2_3
Sincere
intel2_3
Intelligent
fun2_3
Fun
amb2_3
Ambitious
share2_3
Has shared interests/hobbies


Please rate your opinion of your own attributes, on a scale of 1-10 (1= awful and 10=great).  Be honest!
attr3 _3
Attractive
sinc3_3
Sincere
intel3_3
Intelligent
fun3_3
Fun
amb3_3
Ambitious

And finally, how do you think others perceive you?
Please rate yourself how you think others would rate you on each of the following attributes, on a scale of 1-10 (1=awful, 10=great)  
attr5_3 
Attractive
sinc5_3
Sincere
int5_3
Intelligent
fun5_3
Fun
amb5_3
Ambitious
	


---

<a id="wave-dating" />

wave:		
Wave #	Date	Preference Scale	Variations	# Males	# Females
1	October 16th ‘02	100 pt alloc.		10	10
2	October 23rd ‘02
	100 pt alloc.		16	19
3	November 12th ‘02	100 pt alloc.		10	9
4	November 12th ‘02	100 pt alloc.		18	18
5	November 20th, ‘02	100 pt alloc.	undergrads	10	10
6	March 26th ‘03	1-10 scale		5	5
7	March 26th ‘03  	1-10 scale		16	16
8	April 2nd ‘03  	1-10 scale		10	10
9	April 2nd ‘03  	1-10 scale		20	20
10	September 24th ‘03	100 pt alloc.		9	9
11	September 24th ‘03	100 pt alloc.		21	21
12	October 7th ‘03	100 pt alloc.	Budget: only allowed to yes yes to 50% of the people that met	14	15
13	October 8th ‘03	100 pt alloc.	Different M.C.	9	10
14	October 8th ‘03	100 pt alloc.	Different M.C.	18	20
15	February 24th ‘04	100 pt alloc.		19	18
16	February 25th ‘04	100 pt alloc.		8	6
17	February 25th ‘04	100 pt alloc.		14	10
18	April 6th ‘04	100 pt alloc.	brought a magazine	6	6
19	April 6th ‘04	100 pt alloc.	brought a book	15	16
20	April 7th ‘04	100 pt alloc.	brought a book	8	6
21	April 7th ‘04	100 pt alloc.	brought a magazine	22	22

---