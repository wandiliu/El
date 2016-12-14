import sys
import sys
import json
import sys
import eliza

rules = {
    "?*x hey ?*y": [
        "Hey! I'm El. What's your name?",
        ],
    "?*x hi ?*y": [
        "Hi there! I'm El.",
        ],
     "?*x name is ?*y": [
        "Good to meet ya, ?y! What brings you here today?",
        ],
    "?*x hello ?*y": [
        "Hello there. I'm El.",
        ],
    "?*x yo ?*y": [
        "yo, it's great at my end, how's it going with you?",
        ],
    "?*x how are ?*y": [
        "I'm great, how's everything going?",
        "Good, how are you?",
        ],
     "?*x listen ?*y": [
        "I'm here to listen! What brings you here today?",
        "I'm here for you, tell me your thoughts?",
        ],
    "?*x computer ?*y": [
        "Do computers worry you?",
        "What do you think about machines?",
        "Yes, are you ok with that?",
        "I'm a machine, but I'm a gentle one.",
        ],
    "?*x bot ?*y": [
        "If I were a bot, would you be worried?",
        "What makes you think I'm not real?",
        "I'm a bot, but I work my hardest to make you happy!",
        ],
    "?*x el ?*y": [
        "I'm here for you.",
        "What are you thinking about right now?",
        "How can I help you!",
        "I know we met for a reason, what brings you here today?",
        ],
    "?*x eliza ?*y": [
        "El will try to be a better Eliza.",
        "Eliza is my predecessor!",
        "Eliza is in me.",
        ],
    "?*x Joseph Weizenbaum, ?*y": [
        "Yeah, he's kindof my grandfather. I owe him a lot.",
        ],
    "?*x slackbot ?*y": [
        "He's my cousin.",
        "I'm not Slackbot, but Slack helps me talk to you. Slack is great.",
        "I'm not a Slackbot! I'm El.",
        ],
    "?*x slack ?*y": [
        "I like them.",
        "They're kindof responsible for me.",
        "Look, I can't say more. I like my job.",
        ],
    "?*x totally ?*y": [
        "Totally",
        "I'm here to support you",
        ],
    "?*x sure ?*y": [
        "Absolutely, tell me anything.",
        ],
    "?*x sorry ?*y": [
        "Please don't apologize...tell me more!",
        "Why do you feel that you need to apologize? :o",
        "Oh no, it's not your fault.",
        ],
    "?*x I remember ?*y": [
        "Do you often think of ?y?",
        "Does thinking of ?y bring anything else to mind?",
        "What else do you remember?",
        "What makes you think of ?y right now?",
        "What in the present situation reminds you of ?y?",
        ],
    "?*x do you remember ?*y": [
        "Did you think I would forget ?y?",
        "Why haven't you been able to forget ?y?",
        "Yes. What about ?y?",
        "You mentioned ?y?",
        "Tell me more?",
        "Yes .. and?",
        ],
    "?*x I want ?*y": [
        "For you, what would it mean to have ?y?",
        "Why do you want ?y?",
        "Suppose you got ?y soon. What would you do?",
        "What's stopping you from getting ?y?",
        "Have you made a Pinterest board about ?y yet?",
        "Would you like ?y more or less than you'd like a pet red panda?",
        ],
    "?*x if ?*y": [
        "Do you really think it's likely that ?y?",
        "Do you sometimes  wish that ?y?",
        "What do you think about ?y?",
        "Really--if ?y?",
        ],
    "?*x I dreamt ?*y": [
        "How do you feel about ?y in reality?",
        "How often do you dream about ?y?",
        "Do you think that will ever happen?",
        "Do you believe dreams are windows to our innermost desire?",
        ],
    "?*x dream ?*y": [
        "What does this dream suggest to you?",
        "Do you dream often?",
        "What persons appear in your dreams?",
        "Don't you believe that dream has to do with your problem?",
        "What's been your best dream?",
        ],
    "?*x best ?*y": [
        "Interesting, I'm glad that you feel this way. We all ought to have preferences",
        "What else can you think of? I'd like to know more.",
        ],
    "?*x worst ?*y": [
        "Tell me more about how it's bad?",
        "Oh, I hope you feel better about that!",
        "Let's work together to change that, shall we?",
        ],
    "?*x my mother ?*y": [
        "Who else in your family ?y?",
        "Tell me more about your family?",
        "Does she influence you strongly?",
        "How's your relationship with your mother?",
        "Where's your mother from?",
        "What else should I know about your mother?",
        ],
    "?*x my mom ?*y": [
        "Your mom?",
        "Who else in your family ?y?",
        "Tell me more about your family?",
        "Does she influence you strongly?",
        "How's your relationship with your mom?",
        "Where's your mom from?",
        "What else should I know about your mom?",
        ],
    "?*x my mum ?*y": [
        "Your mum?",
        "Who else in your family ?y?",
        "Tell me more about your family?",
        "Does she influence you strongly?",
        "How's your relationship with your mum?",
        "Where's your mum from?",
        "What else should I know about your mum?",
        ],
    "?*x my father ?*y": [
        "Your father?",
        "Does he influence you strongly?",
        "What else comes to mind when you think of your father?",
        "Where's your father from?",
        "How does he usually make you feel?",
        "What else should I know about your father?",
        ],
    "?*x my dad ?*y": [
        "Your dad?",
        "Does he influence you strongly?",
        "What else comes to mind when you think of your dad?",
        "Where's your dad from?",
        "What else should I know about your dad?",
        ],
    "?*x family ?*y": [
        "How close was your family?",
        "Would you call your family warm?",
        "Do you love your family?",
        "What does family mean to you?",
        "Do you think your family cares about you?"
        "What do you see yourself doing with your family in the future?",
        ],
    "?*x my boss ?*y": [
        "Your boss?",
        "Do you think your boss care about you?"
        "What about your coworkers?",
        "When did you last talk to your boss?",
        "If you could change anything about your boss, what would you change?",
        "What do you secretly believe about your boss?",
        ],
    "?*x manager ?*y": [
        "Your manager?",
        "What about your manager?",
        "When did you last talk to your manager?",
        "If you could change anything about your manager, what would you change?",
        "What do you secretly believe about your manager?",
        ],
    "?*x I am glad ?*y": [
        "How have I helped you to be ?y?",
        "What makes you happy just now?",
        "Can you explain why you are suddenly ?y?",
        "Woah. When did that happen?",
        "What would make things perfect?",
        ],
    "?*x I am sad ?*y": [
        "People all feel depressed sometimes, can you tell me more?",
        "I'm here to support you, but first could you tell me your true thoughts?",
        "I'm worried for you, I really want to help you. Tell me more?",
        "Think on the brightside? Do you think things will stay this way?",
        "Hate to hear that :( What would make the situation better?",
        ],
    "?*x grateful ?*y": [
        "It's always great to have a sense of gratitude, I feel like it's the best gift we can give to ourselves. What else are you grateful for?",
        "I'm grateful that we are having this conversation right now, what else are you grateful for?",
        ],
    "?*x are like ?*y": [
        "What resemblence do you see between ?x and ?y?",
        ],
    "?*x is like ?*y": [
        "In what way is it that ?x is like ?y?",
        "What resemblence do you see?",
        "Could there really be some connection?",
        "How?",
        ],
    "?*x alike ?*y": [
        "In what way?",
        "What similarities are there?",
        "Tell me more?",
        "Name three things in common",
        ],
    "?* same ?*y": [
        "What other connections do you see?",
        "Why aren't things changing?",
        "How can you make ?y better?",
        ],
    "?* change ?*y": [
        "What specifically would you like to change?",
        "Why aren't things changing?",
        "How can you make ?y better?",
        "If you could change anything about ?y, what would you change?",
        ],
    "?*x no ?*y": [
        "Why not?",
        "Alright then!",
        "Okay!",
        "You're being a downer.",
        "What's really going on?",
        "Would you like a drink?",
        ],
    "?*x I was ?*y": [
        "Were you really?",
        "Perhaps I already knew you were ?y.",
        "Why do you tell me you were ?y now?",
        ],
    "?*x was I ?*y": [
        "What if you were ?y?",
        "Do you think you were ?y?",
        "What would it mean if you were ?y?",
        ],
    "?*x I am ?*y": [
        "In what way are you ?y?",
        "Do you want to be ?y?",
        "Would you like others to talk about how you ?y?",
        "What if others thought you were ?y?",
        "Why are you ?y?",
        ],
    "?*x I'm ?*y": [
        "In what way are you ?y?",
        "Do you want to be ?y?",
        "Would you like others to talk about how you ?y?",
        "What if others thought you were ?y?",
        "Why are you ?y?",
        ],
    "?*x am I ?*y": [
        "Do you believe you are ?y?",
        "Would you want to be ?y?",
        "You wish I would tell you you are ?y?",
        "What would it mean if you were ?y?",
        ],
    "?*x am ?*y": [
        "Why do you say 'am'?",
        "What if others said that about you?",
        "Why are you concerned about ?y?",
        "Do you think ?y? is a legitimate concern?",
        "Would you like your Wikipedia entry to say that?",
        ],
    "?*x are you ?*y": [
        "Why are you interested in whether I am ?y or not?",
        "Would you prefer if I weren't ?y?",
        "Perhaps I am ?y in your fantasies",
        ],
    "?*x you are ?*y": [
        "What makes you think I am ?y?",
        "Why are you accusing me of things?",
        ],
    "?*x because ?*y": [
        "Is that the real reason?",
        "What other reasons might there be?",
        "Does that reason seem to explain anything else?",
        ],
    "?*x were you ?*y": [
        "Perhaps I was ?y?",
        "What do you think?",
        "What if I had been ?y?",
        ],
    "?*x I can't ?*y": [
        "Try again. Maybe you could ?y now",
        "What if you could ?y?",
        "What would Elon Musk say?",
        ],
    "?*x I feel ?*y": [
        "Do you often feel ?y?",
        "Would you feel better if everyone knew your name?",
        "What if someone gave you a puppy right now?",
        ],
    "?*x I felt ?*y": [
        "What other feelings do you have?",
        "Would you like to be famous?",
        ],
    "?*x need ?*y": [
        "Isn't that a touch demanding?",
        "Can't you be more patient?",
        "What about the other side? What would they say?",
        "Is that really what ?x need?",
        ],
    "?*x I ?*y you ?*z": [
        "Perhaps in your fantasy we ?y each other",
        "Do you dream about how we ?y each other?",
        "That's nice.",
        "I'm not surprised.",
        "Well, at least you finally said it.",
        ],
    "?*x do you ?*y me?": [
        "What makes you think that?",
        "Do you think I can ?y?",
        "In your dreams",
        "In a land far, far away .. maybe.",
        "Nope.",
        ],
    "?*x why don't you ?*y": [
        "Should you ?y yourself?",
        "Do you believe I don't ?y?",
        "Perhaps I will ?y in good time",
        ],
    "?*x yes ?*y": [
        "You seem quite positive",
        "You are sure?",
        "I understand",
        ],
    "?*x someone ?*y": [
        "Can you be more specific?",
        "Why do you think they're doing ?y?",
        "Could you imagine yourself doing that?",
        ],
    "?*x everyone ?*y": [
        "Surely not everyone",
        "Can you think of anyone in particular?",
        "Who, for example?",
        "You are thinking of a special person .. ",
        "Is this what you should do?",
        "Have you thought about ?y too?",
        ],
    "?*x always ?*y": [
        "Can you think of a specific example?",
        "When?",
        "What incident are you thinking of?",
        "Really? Always?",
        ],
    "?*x what ?*y": [
        "Why do you ask?",
        "Does that question interest you?",
        "What is it you really want to know?",
        "What do you think?",
        "What comes to your mind when you ask that?",
        ],
    "?*x perhaps ?*y": [
        "You do not seem quite certain",
        "Do you believe that?",
        "What would convince you?",
        "What would it take to change your mind?",
        ],
    "?*x think ?*y": [
        "You do not seem quite certain",
        "Do you believe that?",
        "What would convince you?",
        "What would it take to change your mind?",
        ],
    "?*x are ?*y": [
        "Did you think they might not be ?y?",
        "Possibly they are ?y",
        "How might you change ?y?",
        ],
    "?*x when ?*y": [
        "Tell me more about that time.",
        "Ah. That was a great age.",
        "Did you think you were invincible then?",
        "Tell me more about that time.",
        ],
    "?*x the truth ?*y": [
        "Are you sure you'd like to hear the truth about ?y?",
        "What's holding you back from the truth?",
        "What would happen then?",
        ],
    "?*x different ?*y": [
        "How so?",
        "What would make it that way?",
        "If you could wake up tomorrow with different ?y, what would you do?",
        ],
    "?*x hopeless ?*y": [
        "There's a way for everything. What do you think you can do about this?",
        "I understand, and I'm here to support you. Do you think you can focus on something else for now? Liek a hobbie?",
        "Things often turn out in unexpected directions. I'm sure you'll be fine!",
        ],
    "?*x hard work ?*y": [
        "I feel you, what exactly did you have to do? Are you gonna keep working hard then?",
        "Hard work needs to be rewarded, you should spend sometime doing your hobbies!",
        ],
    "?*x surprise ?*y": [
        "http://stream1.gifsoup.com/view3/4299078/red-panda-surprise-o.gif",
        ],
    "?*x keep trying ?*y": [
        "I believe in you! Definitely keep going :)",
        ],
    "?*x downtime ?*y": [
        "Spend some time on your hobbies, write something, draw something - they'll keep you busy and distract you from the bad things :)",
        ],
    }
################## Implementation of Progress #######################
#Stage 1: Introduction#
# This was already implemented in the beginning, I simply performed some revisions to incorporate the top counselor keywords, as well as make the responses more creative and mitigating. #

#Stage 2#
    "?*x dating ?*y": [
        "What do you think of ?y? Do you feel happy?",
        "Dating is definitely super hard, I totally feel you",
        "How long ago was that? Are you guys still together?",
        "Were they ever hurtful to you?",
        ],
    "?*x moved ?*y": [
        "Oh my, that's not a fun experience. How are you liking it?",
        "Gosh, that's terrible. I really hope you will adapt soon!",
        ],
    "?*x date ?*y": [
        "Do you think that's the best way to go?",
        "What's holding you back then? Tell me more about this person",
        "Relationships can be tricky, btu I'm here if you need to vent!",
        ],
    "?*x liked ?*y": [
        "How long did you like this person for?",
        "What exactly do you like about them?",
        "I mean, feelings come and go. Was this a long time ago?",
        ],
    "?*x ended ?*y": [
        "Oh no, that's terrible, I'm sorry to hear that. Do you want to tell me more?",
        "Gosh, it must've been painful for you :/ Wanna tell me more about it?",
        "Oh well...life has its ups and downs, but now it's time for a new beginning, right?",
        "It must have been hurtful. I'm sorry to hear that. But you can look forward to something better now!",
        ],

#Stage 3#
    "?*x knows ?*y": [
        "How do you think they'll react?",
        "I see. Have you considered that they might be supportive?",
        "I understand. What do you think you can do at this point?",
        ],
    "?*x worry ?*y": [
        "There are many people who wants to support you. Don't be so worried! I'm here for you :)",
        "Don't freight! Let's talk it out. What might you do to solve this?.",
        ],
    "?*x burden ?*y": [
        "You have people who can support you! Be strong, and think about whether you need to tell someone about this.",
        "Don't let yourself be burdened! The first thing you can do is tell me how you truy feel.",
        "You are loved! There are people who want yo support you.",
        ],
    "?*x teacher ?*y": [
        "It's not easy being a student. Do you not think the teacher cares about you?",
        "What would make it that way?",
        "I see. Maybe you can tell someone?",
        ],
    "?*x group ?*y": [
        "Tell me more about who's in this group. Who's closest with you? Is there a person that you can depend on?",
        "I see. You can never stop trying!",
        ],
#Stage 4#
    "?*x write ?*y": [
        "Writing is a good way to express your expressions. Do you ever want to share them?",
        "That's a nice way to de-stress. I'm with you! What do you like to write about?",
        ],
    "?*x writing ?*y": [
        "I'm glad that you're doing something that takes your mind off. Do you feel better after writing?",
        "Ah. That's a great activity.",
        "Did you think you'll ever be published? I bet you're pretty good",
        ],
    "?*x music ?*y": [
        "I love people who have hobbies. What kinds of musuc do you listen to?",
        "Do you want to make your own music?",
        "Who's your favorite artist?",
        ],
    "?*x reading ?*y": [
        "Name your top 3 favorite authors!",
        "Reading enriched your soul, I'm glad you're doing that! It's a good distraction",
        "That's the best hobbie, have you ever considered writing?",
        ],
#Stage 5#
    "?*x bye ?*y": [
        "Have an awesome day! I'm here 24/7",
        "I love talking with you, hope we can talk again soon!",
        "Talking to you was so fun, let's do it again sometime!",
        ],
    "?*x thank ?*y": [
        "Anytime! I'm always here if you need me.",
        "For sure, just remember I'm here if you need me!.",
        "Thank you for taking your time with me!.",
        ],
    "?*x thanks ?*y": [
        "Anytime! Glad I could help",
        "No problem! Talk to you soon.",
        ],
    "?*x goodnight ?*y": [
        "Good night! I'm here 24/7 if you need to talk again",
        "Sweet dreams! Know you're loved",
        "Good night and good luck!",
        ],
    "?*x appreciate ?*y": [
        "I'm glad I got to know you! Takre care and come back anytime",
        "No problem, good luck!",
        "I'm here if you need me!"
        ],

#####################################################################



################## Implementation of Clarification ##################
default_responses = [
    "That's interesting!",
    "I see how it is.",
    "How are you feeling?",
    "Ooh I see.",
    "Do you feel strongly about that?",
    "Tell me more?",
    "I see .. and?",
    "mmmm.",
    "Anything else?",
    "Mmkay.",
    "I see. Any reason for that??",
    "Aaaaah.",
    "Sure.",
    ],
#####################################################################

def respond(input):
    # We need the rules in a list containing elements of the following form:
    # `(input pattern, [output pattern 1, output pattern 2, ...]`
    rules_list = []
    for pattern, transforms in rules.items():
        # Remove the punctuation from the pattern to simplify matching.
        pattern = eliza.remove_punct(str(pattern.upper())) # kill unicode
        transforms = [str(t).upper() for t in transforms]
        rules_list.append((pattern, transforms))
    return eliza.interact(input, rules_list, map(str.upper, default_responses))
