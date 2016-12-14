###Key Linguistic Features:
As implemented in [El](el.py)

####Adaptability 
> "*successful counselors are more sensitive to the current trajecory of the conversation and react accordingly"*

This feature suggests that counselors often use similar language at the beginning of conversations, but pay attention to the flow and progress of their specific conversation by varying their language in the latter stages of the conversation to rememdy poor conversations. I will attempt to incorporate the factor of Adaptability through a combined implementation with the Progress feature, which will be mentioned below. This will rely on my intuition as a past counselor at 7Cups, and I will try to create a set of responses that tailor best to the given situation. 

However, because attention is not taken into perspective (a significant drawback to retrieval models), I will be unable to accurately predict the success of a conversation at any given point through the entire previous dialogue --  I can only attempt to capture the flow of the conversation through keywords at the most-current exchanges. The Adaptability feature suggests the importance of incorporating context in the situations crisis counseling. This further highlights the importance of implementing a more advanced model. 

####Clarification
> *"successful counselors clarify situations by writing more, reflect back to check understanding, and making their conversation partners more comfortable through affirmation"*

This feature, also known as "echoing", is one of the easier methods to imitate. It seeks to resolve ambiguity, which may negatively impact the success of a conversation. In situations where a texter is giving short, indirect, or muddled responses, it is shown that counselors with stronger/longer responses to resolve ambiguity achieve more successful conversations. Clarification is typical implemented through "check questions", which serve as checkpoints for the counselor to reinstall the understanding of the texter and to reassure the texter of an attentive audience. 

I will implement the clarification through the capturing of certain ambiguous keywords such as "sometimes" and "liked", then targeting them with longer responses that seek clarification and tries to reaffirm the audience of their expressions, while incorporating factors of Creativity mentioned below. In the capturing of short text, we can formulate check questions about generic responses in the model, but for free-form responses around a certain key phrase, we can only speculate its actual length. This will be taken into account in our latter model as well.

####Creativity
> *"successful counselors respond in a more creative way, not directly repeating the patients' words and not using generic, formatted responses"*

Ideally, counselor creativity can be best imitated through a seq2seq network that is capable of creating novel responses from a generic corpus. Unfortunately, this is another ideal that cannot be implemented by the primitive retrieval model. Given its nature, it can only generate an output from a fixed set of reponses. In this retrieval model, my solution is, given a keyword, to associate responses to it that do not use directly repeat the keyword but approach its issue through paraphrasing. I will also implement creativity intuitively, utilizing more verbal responses, as the SMS setting is more forgiving of institutional talk and allows for the blending of informality. 

####Progress
> *"successful counselors are quicker to get to know the core issue and faster to move on to collaboratively solving the problem"*

Again, this relies on the counselor's knowledge of the current "stage" of the conversation, which is heavily reliant on context. Because our model does not include an attention vector, the best way to incorporate existing knowledge into the model is to use the 5 stages and their respective texter-counselor "top keywords" discovered in the research of Althoff *et al*. These keywords are shown below:

![stage keywords](https://github.com/wandiliu/El/blob/master/plugins/el/Screen%20Shot%202016-12-13%20at%202.55.10%20PM.png)

For my retrieval model, I will associate the texter's top keywords with responses containing their respective counselor keywords. 

####Keywords
Successful counselors are able to direct the texter in a positive direction to encourage positive sentiments. This is to say that the pragmatic features in their responses will guide, induce, or provoke the texters and can be controlled to create a positive influence. Moreover, analysis demonstrates that counselors who are less influenced by the talk styles of their texters (in other words, have more stylistic independence), have more successful conversations and are able to influence the texters in their own choice of speech. This is rather easy to implement as the nature of the retrieval model insists on the fixed style of the prepared set of responses. 

I will focus on the use of mitigating words, linguistically known as "hedges". Hedges are words that lessen the impact of the associated word, and makes the statement approximate, rather than exact. Mitigation in a crisis counseling setting often soothes the patients and alleviates temporary stress and intensity during intervention points. I will incorporate hedges into most of my responses, with a concentration in latter-stage responses and responses associated with negative keywords. 
